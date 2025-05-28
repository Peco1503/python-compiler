#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Máquina virtual para el lenguaje BabyDuck

Este módulo implementa una máquina virtual capaz de ejecutar
los cuádruplos generados por el compilador BabyDuck.
"""

import sys
import os
from enum import Enum
from typing import List, Dict, Any, Tuple, Optional

# Importar módulos necesarios (asegurarse que estén en el PYTHONPATH)
from memory_manager import SegmentType, DataType
from quad_generator import OperatorType, Quadruple
from symbol_table import SymbolTable, Function, Variable, Type

class MemorySnapshot:
    """Guarda una copia de la memoria local y temporal"""
    
    def __init__(self, memory):
        # Crear copias profundas de la memoria local y temporal
        self.local_memory = {
            DataType.INT: memory[SegmentType.LOCAL][DataType.INT].copy(),
            DataType.FLOAT: memory[SegmentType.LOCAL][DataType.FLOAT].copy()
        }
        self.temp_memory = {
            DataType.INT: memory[SegmentType.TEMP][DataType.INT].copy(),
            DataType.FLOAT: memory[SegmentType.TEMP][DataType.FLOAT].copy(),
            DataType.BOOL: memory[SegmentType.TEMP][DataType.BOOL].copy()
        }
    
    def restore(self, memory):
        """Restaura la memoria desde este snapshot"""
        memory[SegmentType.LOCAL][DataType.INT] = self.local_memory[DataType.INT].copy()
        memory[SegmentType.LOCAL][DataType.FLOAT] = self.local_memory[DataType.FLOAT].copy()
        memory[SegmentType.TEMP][DataType.INT] = self.temp_memory[DataType.INT].copy()
        memory[SegmentType.TEMP][DataType.FLOAT] = self.temp_memory[DataType.FLOAT].copy()
        memory[SegmentType.TEMP][DataType.BOOL] = self.temp_memory[DataType.BOOL].copy()

class ActivationRecord:
    """
    Registro de activación para una función
    
    Almacena el contexto de ejecución de una función, incluyendo
    la dirección de retorno, los parámetros y el snapshot de memoria.
    """
    def __init__(self, function_name: str, return_address: int, memory_snapshot=None):
        self.function_name = function_name
        self.return_address = return_address
        self.parameters = []  # Lista para almacenar los parámetros pasados a la función
        self.memory_snapshot = memory_snapshot
        
    def __str__(self):
        return f"ActivationRecord(function={self.function_name}, return_addr={self.return_address}, params={len(self.parameters)})"

class VMMemory:
    """
    Administrador de memoria para la máquina virtual
    
    Maneja el almacenamiento y acceso a los valores en memoria virtual
    según las direcciones asignadas durante la compilación.
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
        
        # Definición de rangos de direcciones virtuales (debe coincidir con memory_manager.py)
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
        
    def get_segment_type(self, address: int) -> Tuple[SegmentType, DataType]:
        """
        Determina el segmento y tipo de dato de una dirección virtual
        
        Args:
            address: Dirección virtual a verificar
            
        Returns:
            Tuple[SegmentType, DataType]: Segmento y tipo de dato correspondientes
            
        Raises:
            ValueError: Si la dirección no pertenece a ningún segmento
        """
        for segment, segment_ranges in self.MEMORY_RANGES.items():
            for data_type, (start, end) in segment_ranges.items():
                if start <= address <= end:
                    return segment, data_type
                    
        raise ValueError(f"Dirección virtual inválida: {address}")
    
    def get_value(self, address: int) -> Any:
        """
        Obtiene el valor almacenado en una dirección virtual
        
        Args:
            address: Dirección virtual a consultar
            
        Returns:
            Any: Valor almacenado o None si no hay valor
        """
        segment, data_type = self.get_segment_type(address)
        return self.memory[segment][data_type].get(address)
    
    def set_value(self, address: int, value: Any) -> None:
        """
        Almacena un valor en una dirección virtual
        
        Args:
            address: Dirección virtual donde almacenar
            value: Valor a almacenar
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
        
    def print_memory_state(self, detailed=False):
        """
        Imprime el estado actual de la memoria (para depuración)
        
        Args:
            detailed: Si es True, muestra todos los valores; si es False, solo un resumen
        """
        print("\n=== ESTADO DE LA MEMORIA ===")
        
        for segment, segment_data in self.memory.items():
            print(f"\n== Segmento: {segment.name} ==")
            
            for data_type, values in segment_data.items():
                count = len(values)
                if count == 0:
                    continue
                    
                print(f"  {data_type.name}: {count} valores")
                
                if detailed and count > 0:
                    print(f"    {'Dirección':<10} {'Valor':<15}")
                    print(f"    {'-'*10} {'-'*15}")
                    
                    for address, value in sorted(values.items()):
                        print(f"    {address:<10} {str(value):<15}")

class VMError(Exception):
    """Excepción para errores en tiempo de ejecución de la máquina virtual"""
    pass

class VirtualMachine:
    """
    Máquina virtual para ejecutar cuádruplos de BabyDuck
    
    Interpreta y ejecuta los cuádruplos generados por el compilador,
    administra la memoria y maneja las llamadas a funciones.
    """
    def __init__(self, quadruples: List[Quadruple], constant_map: Dict[Any, int], symbol_table: SymbolTable, debug_mode=False):
        self.quadruples = quadruples
        self.memory = VMMemory()
        self.instruction_pointer = 0
        self.constant_map = constant_map
        self.symbol_table = symbol_table
        self.call_stack = []  # Pila para almacenar activation records
        self.current_era = None  # ERA actual en preparación
        self.debug_mode = debug_mode  # Modo de depuración
        
        # Cargar constantes en memoria
        self.load_constants(constant_map)
    
    def load_constants(self, constant_map: Dict[Any, int]):
        """
        Carga las constantes en la memoria de la máquina virtual
        
        Args:
            constant_map: Diccionario que mapea valores constantes a direcciones virtuales
        """
        for value, address in constant_map.items():
            self.memory.set_value(address, value)
    
    def execute(self):
        """
        Ejecuta los cuádruplos desde el inicio hasta el final o error
        """
        # Inicializar contador de instrucciones
        self.instruction_pointer = 0
        
        # Ciclo principal de ejecución
        while 0 <= self.instruction_pointer < len(self.quadruples):
            # Obtener cuádruplo actual
            quad = self.quadruples[self.instruction_pointer]
            
            # Para debug: imprimir el cuádruplo actual
            if self.debug_mode:
                print(f"\n[IP={self.instruction_pointer}] Ejecutando: {quad}")
                if self.call_stack:
                    print(f"Call stack: {[ar.function_name for ar in self.call_stack]}")
            
            # Ejecutar la operación correspondiente
            try:
                self.execute_quadruple(quad)
            except VMError as e:
                print(f"\nError en tiempo de ejecución (cuádruplo {self.instruction_pointer}): {str(e)}")
                if self.debug_mode:
                    self.memory.print_memory_state()
                return False
            except Exception as e:
                print(f"\nError inesperado (cuádruplo {self.instruction_pointer}): {str(e)}")
                if self.debug_mode:
                    import traceback
                    traceback.print_exc()
                return False
            
            # Avanzar al siguiente cuádruplo (a menos que sea un salto)
            self.instruction_pointer += 1
            
        if self.debug_mode:
            print("\n=== Ejecución finalizada ===")
            self.memory.print_memory_state()
            
        return True
    
    def execute_quadruple(self, quad: Quadruple):
        """
        Ejecuta un cuádruplo específico
        
        Args:
            quad: Cuádruplo a ejecutar
            
        Raises:
            VMError: Si ocurre un error durante la ejecución
        """
        operator = quad.operator
        
        # Operaciones aritméticas y relacionales
        if operator in [OperatorType.PLUS, OperatorType.MINUS, OperatorType.MULT, OperatorType.DIV,
                       OperatorType.LT, OperatorType.GT, OperatorType.LE, OperatorType.GE, 
                       OperatorType.EQ, OperatorType.NE]:
            # Obtener valores de los operandos
            left_value = self.memory.get_value(quad.left_operand)
            right_value = self.memory.get_value(quad.right_operand)
            
            # Verificar que los valores no sean None
            if left_value is None:
                raise VMError(f"Valor no inicializado en dirección {quad.left_operand}")
            if right_value is None:
                raise VMError(f"Valor no inicializado en dirección {quad.right_operand}")
            
            # Ejecutar la operación
            if operator == OperatorType.PLUS:
                result = left_value + right_value
            elif operator == OperatorType.MINUS:
                result = left_value - right_value
            elif operator == OperatorType.MULT:
                result = left_value * right_value
            elif operator == OperatorType.DIV:
                if right_value == 0:
                    raise VMError("División por cero")
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
            
            if self.debug_mode:
                print(f"  {left_value} {operator.value} {right_value} = {result}")
            
        # Operador de asignación
        elif operator == OperatorType.ASSIGN:
            value = self.memory.get_value(quad.left_operand)
            if value is None:
                raise VMError(f"Valor no inicializado en dirección {quad.left_operand}")
            self.memory.set_value(quad.result, value)
            
            if self.debug_mode:
                print(f"  Asignación: {quad.result} = {value}")
            
        # Operadores de salto
        elif operator == OperatorType.GOTO:
            if self.debug_mode:
                print(f"  Salto incondicional a {quad.result}")
            self.instruction_pointer = quad.result - 1  # -1 porque se incrementará después
            
        elif operator == OperatorType.GOTOF:
            condition = self.memory.get_value(quad.left_operand)
            if condition is None:
                raise VMError(f"Condición no inicializada en dirección {quad.left_operand}")
                
            if self.debug_mode:
                print(f"  Salto condicional: si {condition} es falso, ir a {quad.result}")
                
            if not condition:
                self.instruction_pointer = quad.result - 1  # -1 porque se incrementará después
                
        # Operador de impresión
        elif operator == OperatorType.PRINT:
            value = self.memory.get_value(quad.left_operand)
            
            if self.debug_mode:
                print(f"  Imprimiendo valor en dirección {quad.left_operand}: {value}")
            
            # Manejo especial para strings con comillas
            if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            
            print(value, end="")
            
        # Operadores de funciones
        elif operator == OperatorType.ERA:
            # Preparar nuevo activation record
            function_name = quad.left_operand
            
            if self.debug_mode:
                print(f"  Preparando ERA para función '{function_name}'")
                
            if function_name not in self.symbol_table.functions:
                raise VMError(f"Función '{function_name}' no encontrada")
                
            self.current_era = ActivationRecord(function_name, 0)  # El return_address se establecerá en GOSUB
            
        elif operator == OperatorType.PARAM:
            # Verificar que hay un ERA en proceso
            if not self.current_era:
                raise VMError("PARAM sin ERA previo")
                
            # Obtener valor del argumento
            value = self.memory.get_value(quad.left_operand)
            if value is None:
                raise VMError(f"Parámetro no inicializado en dirección {quad.left_operand}")
                
            # Obtener número de parámetro (format: "paramX")
            param_number = int(quad.result.replace("param", ""))
            
            if self.debug_mode:
                print(f"  Parámetro {param_number}: valor {value}")
                
            # Almacenar para su uso posterior
            self.current_era.parameters.append((param_number, value))
            
        elif operator == OperatorType.GOSUB:
            # Verificar que hay un ERA en proceso
            if not self.current_era:
                raise VMError("GOSUB sin ERA previo")
            
            memory_snapshot = MemorySnapshot(self.memory.memory)
                
            # Establecer dirección de retorno
            self.current_era.return_address = self.instruction_pointer + 1
            self.current_era.memory_snapshot = memory_snapshot
            
            # Obtener función del directorio
            function_name = quad.left_operand
            if function_name not in self.symbol_table.functions:
                raise VMError(f"Función '{function_name}' no encontrada")
            
            function = self.symbol_table.functions[function_name]
            
            if self.debug_mode:
                print(f"  Llamando a función '{function_name}', return={self.current_era.return_address}")
                print(f"  Parámetros: {self.current_era.parameters}")
            
            # Guardar el contexto actual
            self.call_stack.append(self.current_era)
            
            # Verificar número correcto de parámetros
            if len(self.current_era.parameters) != len(function.params):
                raise VMError(f"Número incorrecto de parámetros para función '{function_name}': "
                              f"esperaba {len(function.params)}, recibió {len(self.current_era.parameters)}")
            
            # Limpiar memoria local antes de establecer nuevos valores
            self.memory.clear_local_memory()
            
            # Preparar memoria local y copiar parámetros
            for param_idx, (param_num, value) in enumerate(sorted(self.current_era.parameters)):
                if param_idx >= len(function.params):
                    raise VMError(f"Demasiados parámetros para función '{function_name}'")
                
                param = function.params[param_idx]
                param_address = param.address
                
                if self.debug_mode:
                    print(f"  Copiando parámetro {param_num} a dirección {param_address}")
                    
                self.memory.set_value(param_address, value)
            
            # Reiniciar ERA actual
            self.current_era = None
            
            # Saltar a la función
            self.instruction_pointer = quad.result - 1  # -1 porque se incrementará después
            
        elif operator == OperatorType.ENDFUNC:
            # Restaurar contexto anterior
            if not self.call_stack:
                if self.debug_mode:
                    print("[INFO] Finalizando programa (ENDFUNC de main)")
                return 
                
            # Obtener activation record
            ar = self.call_stack.pop()
            
            if self.debug_mode:
                print(f"  Fin de función '{ar.function_name}', retornando a {ar.return_address}")

            if ar.memory_snapshot:
                ar.memory_snapshot.restore(self.memory.memory)
            else:
                # Si no hay snapshot, solo limpiar la memoria
                self.memory.clear_local_memory()
            
            # Restaurar dirección de retorno
            self.instruction_pointer = ar.return_address - 1  # -1 porque se incrementará después
        
        else:
            # Operador no reconocido
            raise VMError(f"Operador no implementado: {operator}")