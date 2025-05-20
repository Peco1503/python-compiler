from enum import Enum
from typing import List, Dict, Any, Tuple, Optional, Union
from semantic_cube import get_result_type, INT, FLOAT, ERROR
from symbol_table import Type, Variable, Function, SymbolTable
from memory_manager import MemoryManager, SegmentType, DataType

# ---------- Definición de las Estructuras de Datos ----------
class OperatorType(Enum):
    # Operadores Aritméticos
    PLUS = '+'
    MINUS = '-'
    MULT = '*'
    DIV = '/'

    # Operadores Relacionales
    LT = '<'
    GT = '>'
    LE = '<='
    GE = '>='
    EQ = '=='
    NE = '!='

    # Operador de Asignación
    ASSIGN = '='

    # Operadores de Salto
    GOTO = 'goto'
    GOTOF = 'gotof'
    GOTOT = 'gotot'

    # Operadores de I/O
    PRINT = 'print'

    # Operadores de Funciones
    ERA = 'era'
    PARAM = 'param'
    GOSUB = 'gosub'
    ENDFUNC = 'endfunc'

    def __str__(self):
        return self.value

class Quadruple:
    """Representa un cuádruplo en el código intermedio"""
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
    
    def __str__(self):
        return f"({self.operator}, {self.left_operand}, {self.right_operand}, {self.result})"
    

class QuadrupleGenerator:
    def __init__(self):
        # Pilas
        self.operand_stack = []  # Ahora contendrá direcciones virtuales
        self.type_stack = []
        self.operator_stack = []
        self.jump_stack = []

        # Fila de cuádruplos
        self.quadruples = []

        # Contador de temporales
        self.temp_counter = 1

        # Contador de cuádruplos (usado para saltos)
        self.quad_counter = 0
        
        # Administrador de memoria
        self.memory_manager = MemoryManager()
        
        # Mapa para rastrear las direcciones virtuales de las variables
        self.var_address_map = {}
        
        # Función actual que se está procesando
        self.current_function = "global"

    # ---------- Métodos para Manejo de Memoria Virtual ----------
    def set_var_address(self, var_name: str, address: int):
        """
        Asocia una variable con su dirección virtual
        
        Args:
            var_name: Nombre de la variable
            address: Dirección virtual asignada
        """
        # Agregamos la función actual como prefijo para manejar el ámbito
        key = f"{self.current_function}.{var_name}" if var_name != "global" else var_name
        self.var_address_map[key] = address

    def get_var_address(self, var_name: str) -> Optional[int]:
        """
        Obtiene la dirección virtual de una variable
        
        Args:
            var_name: Nombre de la variable
            
        Returns:
            Optional[int]: Dirección virtual o None si no existe
        """
        # Primero buscamos en el ámbito local
        local_key = f"{self.current_function}.{var_name}"
        if local_key in self.var_address_map:
            return self.var_address_map[local_key]
        
        # Si no está en el ámbito local, buscamos en el global
        global_key = f"global.{var_name}"
        if global_key in self.var_address_map:
            return self.var_address_map[global_key]
        
        return None

    def set_current_function(self, function_name: str):
        """
        Establece la función actual y reinicia los contadores locales y temporales
        
        Args:
            function_name: Nombre de la función
        """
        self.current_function = function_name
        if function_name != "global":
            # Al cambiar de función, reiniciamos los contadores locales y temporales
            self.memory_manager.reset_local_counters()
    
    def get_constant_address(self, value: Any) -> int:
        """
        Obtiene la dirección virtual para una constante
        
        Args:
            value: Valor de la constante
            
        Returns:
            int: Dirección virtual asignada
        """
        try:
            # Si es una cadena que representa un número, convertirla
            if isinstance(value, str):
                if value.isdigit():
                    value = int(value)
                elif '.' in value and all(part.isdigit() for part in value.split('.', 1)):
                    value = float(value)
            
            return self.memory_manager.get_constant_address(value)
        except (ValueError, TypeError) as e:
            # Si no es una constante válida, verificar si es una variable
            address = self.get_var_address(value)
            if address is not None:
                return address
            raise ValueError(f"No se pudo obtener dirección para '{value}': {str(e)}")

    def get_temp_address(self, data_type: Type) -> int:
        """
        Obtiene una dirección temporal para el tipo especificado
        
        Args:
            data_type: Tipo de dato (Type.INT, Type.FLOAT, etc.)
            
        Returns:
            int: Dirección virtual temporal asignada
        """
        # Mapear el tipo de Type a DataType
        if data_type == Type.INT:
            memory_type = DataType.INT
        elif data_type == Type.FLOAT:
            memory_type = DataType.FLOAT
        elif data_type == Type.VOID:
            # Para operaciones relacionales, usamos temporales booleanos
            memory_type = DataType.BOOL
        else:
            memory_type = DataType.ERROR
            
        # Obtener dirección temporal
        return self.memory_manager.get_address(SegmentType.TEMP, memory_type)

    # ---------- Métodos para Generación de Cuádruplos ----------
    def add_quadruple(self, operator, left_operand, right_operand, result) -> int:
        """
        Añade un cuádruplo a la fila y devuelve su índice
        
        Args:
            operator: Operador del cuádruplo
            left_operand: Operando izquierdo (dirección virtual)
            right_operand: Operando derecho (dirección virtual)
            result: Resultado (dirección virtual o dirección de salto)
        
        Returns:
            int: Índice del cuádruplo generado
        """
        quad = Quadruple(operator, left_operand, right_operand, result)
        self.quadruples.append(quad)
        index = self.quad_counter
        self.quad_counter += 1
        return index
    
    def fill_quadruple(self, index: int, result):
        """
        Completa un cuádruplo con dirección de salto pendiente
        
        Args:
            index: Índice del cuádruplo a completar
            result: Valor para el campo de resultado (usualmente dirección de salto)
        """
        if 0 <= index < len(self.quadruples):
            self.quadruples[index].result = result
    
    # ---------- Métodos para Operaciones Aritméticas y Relacionales ----------
    def process_arithmetic_expression(self, operator_types: List[OperatorType]):
        """
        Procesa operadores aritméticos de la pila que tienen mayor o igual precedencia
        
        Args:
            operator_types: Lista de operadores a procesar
        """
        if self.operator_stack and self.operator_stack[-1] in operator_types:
            # Hay un operador de mayor o igual precedencia
            operator = self.operator_stack.pop()
            
            # Obtener operandos y tipos
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            
            # Verificar compatibilidad de tipos
            result_type_value = get_result_type(left_type.value, right_type.value, operator.value)
            if result_type_value == ERROR:
                raise ValueError(f"Error de tipos: Operación incompatible {left_type.name} {operator.value} {right_type.name}")
            
            # Mapear el valor resultante a un tipo Type
            if result_type_value == INT:
                result_type = Type.INT
            else:  # FLOAT
                result_type = Type.FLOAT
            
            # Generar dirección temporal para el resultado
            result_address = self.get_temp_address(result_type)
            
            # Añadir cuádruplo
            self.add_quadruple(operator, left_operand, right_operand, result_address)
            
            # Añadir resultado a las pilas
            self.operand_stack.append(result_address)
            self.type_stack.append(result_type)
    
    def process_relational_expression(self):
        """
        Procesa una operación relacional
        
        Las operaciones relacionales producen valores booleanos (representados como enteros 0 o 1)
        """
        if self.operator_stack and self.operator_stack[-1] in [OperatorType.LT, OperatorType.GT, 
                                                            OperatorType.LE, OperatorType.GE,
                                                            OperatorType.EQ, OperatorType.NE]:
            # Operador relacional
            operator = self.operator_stack.pop()
            
            # Obtener operandos y tipos
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            
            # Verificar compatibilidad de tipos
            result_type_value = get_result_type(left_type.value, right_type.value, operator.value)
            if result_type_value == ERROR:
                raise ValueError(f"Error de tipos: Operación incompatible {left_type.name} {operator.value} {right_type.name}")
            
            # Las operaciones relacionales devuelven un valor "booleano" (internamente un entero)
            # Usamos Type.VOID como marcador para valores booleanos en este contexto
            result_type = Type.VOID
            
            # Generar dirección temporal para el resultado booleano
            result_address = self.get_temp_address(result_type)
            
            # Añadir cuádruplo
            self.add_quadruple(operator, left_operand, right_operand, result_address)
            
            # Añadir resultado a las pilas
            self.operand_stack.append(result_address)
            self.type_stack.append(result_type)

    # ---------- Métodos para Estatutos Lineales (Asignación, Print) ----------
    def process_assignment(self):
        """
        Procesa una operación de asignación
        
        Asigna el valor de una expresión a una variable
        """
        if self.operator_stack and self.operator_stack[-1] == OperatorType.ASSIGN:
            # Operador de asignación
            operator = self.operator_stack.pop()
            
            # Obtener expresión (lado derecho) y variable (lado izquierdo)
            expression = self.operand_stack.pop()
            expr_type = self.type_stack.pop()
            variable = self.operand_stack.pop()
            var_type = self.type_stack.pop()
            
            # Verificar compatibilidad de tipos
            result_type = get_result_type(var_type.value, expr_type.value, operator.value)
            if result_type == ERROR:
                raise ValueError(f"Error de tipos: No se puede asignar {expr_type.name} a {var_type.name}")
            
            # Añadir cuádruplo
            self.add_quadruple(operator, expression, None, variable)

    def process_print(self, elements: List[Tuple[int, Type]]):
        """
        Genera cuádruplos para una instrucción print
        
        Args:
            elements: Lista de tuplas (dirección_virtual, tipo) para imprimir
        """
        for element_address, element_type in elements:
            self.add_quadruple(OperatorType.PRINT, element_address, None, None)
    
    # ---------- Soporte de Estructuras de Control ----------
    def generate_gotof(self, condition_address: int) -> int:
        """
        Genera un GOTOF para una condición y devuelve su índice
        
        Args:
            condition_address: Dirección virtual de la condición
            
        Returns:
            int: Índice del cuádruplo GOTOF generado
        """
        index = self.add_quadruple(OperatorType.GOTOF, condition_address, None, None)
        return index

    def generate_goto(self) -> int:
        """
        Genera un GOTO incondicional y devuelve su índice
        
        Returns:
            int: Índice del cuádruplo GOTO generado
        """
        index = self.add_quadruple(OperatorType.GOTO, None, None, None)
        return index
    
    # ---------- Métodos para Soporte de Funciones ----------
    def generate_era(self, function_name: str) -> int:
        """
        Genera un cuádruplo ERA para la llamada a función
        
        Args:
            function_name: Nombre de la función
            
        Returns:
            int: Índice del cuádruplo ERA generado
        """
        index = self.add_quadruple(OperatorType.ERA, function_name, None, None)
        return index
    
    def generate_param(self, argument_address: int, param_number: int) -> int:
        """
        Genera un cuádruplo PARAM para un parámetro de función
        
        Args:
            argument_address: Dirección virtual del argumento
            param_number: Número del parámetro
            
        Returns:
            int: Índice del cuádruplo PARAM generado
        """
        index = self.add_quadruple(OperatorType.PARAM, argument_address, None, f"param{param_number}")
        return index
    
    def generate_gosub(self, function_name: str, function_address: int) -> int:
        """
        Genera un cuádruplo GOSUB para llamar a una función
        
        Args:
            function_name: Nombre de la función
            function_address: Dirección de inicio de la función
            
        Returns:
            int: Índice del cuádruplo GOSUB generado
        """
        index = self.add_quadruple(OperatorType.GOSUB, function_name, None, function_address)
        return index
    
    def generate_endfunc(self) -> int:
        """
        Genera un cuádruplo ENDFUNC para marcar el fin de una función
        
        Returns:
            int: Índice del cuádruplo ENDFUNC generado
        """
        index = self.add_quadruple(OperatorType.ENDFUNC, None, None, None)
        return index