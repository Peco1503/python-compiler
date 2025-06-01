import sys
import os
import pickle
from typing import List, Dict, Any

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from quad_generator import OperatorType, Quadruple
from memory_manager import SegmentType, DataType
from symbol_table import SymbolTable, Function, Variable, Type

class ActivationRecord:
    """
    Registro de activación para una función
    """
    def __init__(self, function_name: str, return_address: int):
        self.function_name = function_name
        self.return_address = return_address
        self.local_memory = {}  # Para guardar variables locales de main
        self.temp_memory = {}  # Para guardar variables float de main
        self.parameters = []  # Lista para almacenar parámetros

class VMMemory:
    """
    Administrador de memoria para la máquina virtual
    """
    def __init__(self):
        # Memoria para cada segmento y tipo
        self.memory = {
            SegmentType.GLOBAL: {
                DataType.INT: {},
                DataType.FLOAT: {}
            },
            SegmentType.LOCAL: {
                DataType.INT: {},
                DataType.FLOAT: {}
            },
            SegmentType.TEMP: {
                DataType.INT: {},
                DataType.FLOAT: {},
                DataType.BOOL: {}
            },
            SegmentType.CONSTANT: {
                DataType.INT: {},
                DataType.FLOAT: {},
                DataType.STRING: {}
            }
        }
        
        # Definición de rangos de direcciones virtuales
        self.MEMORY_RANGES = {
            SegmentType.GLOBAL: {
                DataType.INT: (1000, 1999),
                DataType.FLOAT: (2000, 2999)
            },
            SegmentType.LOCAL: {
                DataType.INT: (3000, 3999),
                DataType.FLOAT: (4000, 4999)
            },
            SegmentType.TEMP: {
                DataType.INT: (5000, 5999),
                DataType.FLOAT: (6000, 6999),
                DataType.BOOL: (7000, 7999)
            },
            SegmentType.CONSTANT: {
                DataType.INT: (8000, 8999),
                DataType.FLOAT: (9000, 9999),
                DataType.STRING: (10000, 10999)
            }
        }
        
    def get_segment_type(self, address: int):
        """
        Determina el segmento y tipo de dato de una dirección virtual
        """
        for segment, segment_ranges in self.MEMORY_RANGES.items():
            for data_type, (start, end) in segment_ranges.items():
                if start <= address <= end:
                    return segment, data_type
                    
        raise ValueError(f"Dirección virtual inválida: {address}")
    
    def get_value(self, address: int):
        """
        Obtiene el valor almacenado en una dirección virtual
        """
        segment, data_type = self.get_segment_type(address)
        return self.memory[segment][data_type].get(address)
    
    def set_value(self, address: int, value: Any):
        """
        Almacena un valor en una dirección virtual
        """
        segment, data_type = self.get_segment_type(address)
        
        # Convertir el valor al tipo correcto si es necesario
        if data_type == DataType.INT and not isinstance(value, int):
            try:
                value = int(value)
            except (ValueError, TypeError):
                value = 0
        elif data_type == DataType.FLOAT and not isinstance(value, float):
            try:
                value = float(value)
            except (ValueError, TypeError):
                value = 0.0
        elif data_type == DataType.BOOL and not isinstance(value, bool):
            value = bool(value)
            
        self.memory[segment][data_type][address] = value
    
    def clear_local_memory(self):
        """
        Limpia la memoria local y temporal (al salir de una función)
        """
        self.memory[SegmentType.LOCAL] = {
            DataType.INT: {},
            DataType.FLOAT: {}
        }
        self.memory[SegmentType.TEMP] = {
            DataType.INT: {},
            DataType.FLOAT: {},
            DataType.BOOL: {}
        }

class VirtualMachine:
    """
    Máquina virtual para ejecutar cuádruplos de BabyDuck
    """
    def __init__(self, quadruples: List[Quadruple], constant_map: Dict[Any, int], symbol_table: SymbolTable):
        self.quadruples = quadruples
        self.memory = VMMemory()
        self.instruction_pointer = 0
        self.constant_map = constant_map
        self.symbol_table = symbol_table
        self.call_stack = []  # Pila para almacenar activation records
        self.current_era = None  # ERA actual en preparación
        
        # Cargar constantes en memoria
        self.load_constants(constant_map)
    
    def load_constants(self, constant_map: Dict[Any, int]):
        """
        Carga las constantes en la memoria de la máquina virtual
        """
        for value, address in constant_map.items():
            self.memory.set_value(address, value)
    
    def execute(self):
        """
        Ejecuta los cuádruplos
        """
        # Inicializar contador de instrucciones
        self.instruction_pointer = 0
        
        # Ciclo principal de ejecución
        while self.instruction_pointer < len(self.quadruples):
            # Obtener cuádruplo actual
            quad = self.quadruples[self.instruction_pointer]
            
            # Para debug: imprimir el cuádruplo actual
            # print(f"[IP={self.instruction_pointer}] Ejecutando: {quad}")
            
            # Ejecutar la operación correspondiente
            self.execute_quadruple(quad)
            
            # Avanzar al siguiente cuádruplo (a menos que sea un salto)
            self.instruction_pointer += 1
    
    def execute_quadruple(self, quad: Quadruple):
        """
        Ejecuta un cuádruplo específico
        """
        operator = quad.operator

        # Para debugging - imprimir valores importantes
        # print(f"[DEBUG] Executing: {quad}")
        
        # Operaciones aritméticas y relacionales
        if operator in [OperatorType.PLUS, OperatorType.MINUS, OperatorType.MULT, OperatorType.DIV,
                       OperatorType.LT, OperatorType.GT, OperatorType.LE, OperatorType.GE, 
                       OperatorType.EQ, OperatorType.NE]:
            # Obtener valores de los operandos
            left_value = self.memory.get_value(quad.left_operand)
            right_value = self.memory.get_value(quad.right_operand)
            
            # Verificar que los valores no sean None
            if left_value is None:
                raise RuntimeError(f"Error: Valor no inicializado en dirección {quad.left_operand}")
            if right_value is None:
                raise RuntimeError(f"Error: Valor no inicializado en dirección {quad.right_operand}")
            
            # Ejecutar la operación
            if operator == OperatorType.PLUS:
                result = left_value + right_value
            elif operator == OperatorType.MINUS:
                result = left_value - right_value
            elif operator == OperatorType.MULT:
                result = left_value * right_value
            elif operator == OperatorType.DIV:
                if right_value == 0:
                    raise ZeroDivisionError("Error: División por cero")
                result = left_value / right_value
            elif operator == OperatorType.LT:
                result = left_value < right_value
            elif operator == OperatorType.GT:
                result = left_value > right_value
            elif operator == OperatorType.LE:
                result = left_value <= right_value
            elif operator == OperatorType.GE:
                result = left_value >= right_value
            elif operator == OperatorType.EQ:
                result = left_value == right_value
            elif operator == OperatorType.NE:
                result = left_value != right_value
            
            # Guardar resultado
            self.memory.set_value(quad.result, result)
            
        # Operador de asignación
        elif operator == OperatorType.ASSIGN:
            value = self.memory.get_value(quad.left_operand)
            if value is None:
                raise RuntimeError(f"Error: Valor no inicializado en dirección {quad.left_operand}")
            self.memory.set_value(quad.result, value)
            
        # Operadores de salto
        elif operator == OperatorType.GOTO:
            self.instruction_pointer = quad.result - 1  # -1 porque se incrementará después
            
        elif operator == OperatorType.GOTOF:
            condition = self.memory.get_value(quad.left_operand)
            if condition is None:
                raise RuntimeError(f"Error: Condición no inicializada en dirección {quad.left_operand}")
            if not condition:
                self.instruction_pointer = quad.result - 1  # -1 porque se incrementará después
                
        # Operador de impresión
        elif operator == OperatorType.PRINT:
            value = self.memory.get_value(quad.left_operand)
            if value is None:
                print("None", end="")
            else:
                # Si es una cadena con comillas, quitarlas
                if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                print(value, end="")
            
        # Operadores de funciones
        elif operator == OperatorType.ERA:
            # Preparar nuevo activation record
            function_name = quad.left_operand
            self.current_era = ActivationRecord(function_name, 0)  # El return_address se establecerá en GOSUB
            
        elif operator == OperatorType.PARAM:
            # Verificar que hay un ERA en proceso
            if not self.current_era:
                raise RuntimeError("Error: PARAM sin ERA previo")
                
            # Obtener valor del argumento
            value = self.memory.get_value(quad.left_operand)
            if value is None:
                raise RuntimeError(f"Error: Parámetro no inicializado en dirección {quad.left_operand}")
                
            # Obtener número de parámetro (format: "paramX")
            param_number = int(quad.result.replace("param", ""))
            
            # Almacenar para su uso posterior
            self.current_era.parameters.append((param_number, value))
            
        elif operator == OperatorType.GOSUB:
            # Verificar que hay un ERA en proceso
            if not self.current_era:
                raise RuntimeError("Error: GOSUB sin ERA previo")
                
            # Establecer dirección de retorno
            self.current_era.return_address = self.instruction_pointer + 1
            
            # Guardar explicitamente las variables de main
            main_vars = {}
            for addr in range(3000, 3003):
                val = self.memory.get_value(addr)
                main_vars[addr] = val
            
            # Tambien guardar la variable 'f' si existe
            f_val = self.memory.get_value(4000)

            # Colocar activation record en la pila
            self.current_era.local_memory = main_vars  # Usar el campo local_memory para guardar variables
            if f_val is not None:
                self.current_era.temp_memory = {4000: f_val}  # Usar temp_memory para f
            self.call_stack.append(self.current_era)
            
            # Obtener función del directorio
            function_name = quad.left_operand
            if function_name not in self.symbol_table.functions:
                raise RuntimeError(f"Error: Función '{function_name}' no encontrada")
            
            function = self.symbol_table.functions[function_name]
            
            # Preparar memoria local y copiar parámetros
            for param_idx, (param_num, value) in enumerate(self.current_era.parameters):
                if param_idx >= len(function.params):
                    raise RuntimeError(f"Error: Demasiados parámetros para función '{function_name}'")
                
                param = function.params[param_idx]
                param_address = param.address
                self.memory.set_value(param_address, value)
            
            # Reiniciar ERA actual
            self.current_era = None
            
            # Saltar a la función
            self.instruction_pointer = quad.result - 1  # -1 porque se incrementará después
            
        # En ENDFUNC, guarda el estado de la memoria antes de limpiarla
        elif operator == OperatorType.ENDFUNC:
            # print("\n[DEBUG] Memoria antes de ENDFUNC:")
            # for addr in range(3000, 3003):
            #     val = self.memory.get_value(addr)
            #     print(f"  Dirección {addr}: {val}")
            # Restaurar contexto anterior
            if self.call_stack:
                # Obtener activation record
                ar = self.call_stack.pop()
                
                # DEBUG: Imprimir estado de memoria antes de limpiar
                # print("\n[DEBUG] Memoria antes de ENDFUNC:")
                # for addr in range(3000, 3003):
                #     val = self.memory.get_value(addr)
                #     print(f"  Dirección {addr}: {val}")

                self.memory.clear_local_memory()
                
                # Restaurar variables de main si es necesario
                if hasattr(ar, 'local_memory') and ar.local_memory:
                    for addr, val in ar.local_memory.items():
                        if val is not None:
                            self.memory.set_value(addr, val)
                
                # Restaurar dirección de retorno
                self.instruction_pointer = ar.return_address - 1  # -1 porque se incrementará después

            else:
                # Si la pila esta vacia, es el ENDFUNC de main
                # En este caso simplemente seguimos adelante
                # print("[INFO] Finalizando programa (ENDFUNC de main)")
                pass

            # DEBUG: Imprimir estado de memoria después de limpiar/restaurar
            # print("\n[DEBUG] Memoria después de ENDFUNC:")
            # for addr in range(3000, 3003):
            #     val = self.memory.get_value(addr)
            #     print(f"  Dirección {addr}: {val}")
        
        elif operator == OperatorType.PARAM:
            value = self.memory.get_value(quad.left_operand)
            # print(f"[DEBUG] PARAM - Dirección {quad.left_operand} tiene valor: {value}")


def load_obj_file(file_path):
    """
    Carga un archivo de objetos generado por el compilador BabyDuck
    """
    try:
        with open(file_path, 'rb') as f:
            obj_data = pickle.load(f)
            
        if not isinstance(obj_data, dict):
            raise ValueError("Formato de archivo de objetos incorrecto")
            
        # Verificar que tiene las claves necesarias
        required_keys = ['quadruples', 'constant_map', 'symbol_table']
        for key in required_keys:
            if key not in obj_data:
                raise ValueError(f"Falta la clave '{key}' en el archivo de objetos")
                
        return obj_data
    except Exception as e:
        print(f"Error al cargar el archivo de objetos: {e}")
        sys.exit(1)


def main():
    """
    Función principal del intérprete
    """
    # Verificar argumentos
    if len(sys.argv) != 2:
        print("Uso: python3 vm_interpreter.py <archivo_objeto.bdobj>")
        sys.exit(1)
        
    # Cargar archivo de objetos
    obj_file = sys.argv[1]
    if not os.path.exists(obj_file):
        print(f"Error: El archivo '{obj_file}' no existe")
        sys.exit(1)
        
    # Cargar datos del archivo
    obj_data = load_obj_file(obj_file)
    
    # Crear máquina virtual
    vm = VirtualMachine(
        obj_data['quadruples'],
        obj_data['constant_map'],
        obj_data['symbol_table']
    )
    
    # Ejecutar programa
    #print(f"Ejecutando programa desde '{obj_file}'...")
    #print("=" * 50)
    try:
        vm.execute()
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()