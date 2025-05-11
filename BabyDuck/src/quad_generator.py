from enum import Enum
from typing import List, Dict, Any, Tuple, Optional
from semantic_cube import get_result_type, INT, FLOAT, ERROR
from symbol_table import Type, Variable, Function, SymbolTable

# ---------- Definicion de las Estructuras de Datos ----------
class OperatorType(Enum):
    # Operadadores Aritmeticos

    PLUS = '+'
    MINUS = '-'
    MULT = '*'
    DIV = '/'

    # Operadores relacionales
    LT = '<'
    GT = '>'
    LE = '<='
    GE = '>='
    EQ = '=='
    NE = '!='

    # Operador de asignacion
    ASSIGN = '='

    # Operador de salto
    GOTO = 'goto'
    GOTOF = 'gotof'
    GOTOT = 'gotot'

    # Operadores de I/O
    PRINT = 'print'

    # Operadores de funciones
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
        self.operand_stack = []
        self.type_stack = []
        self.operator_stack = []
        self.jump_stack = []

        # Fila de cuadruplos
        self.quadruples = []

        # Contador de temporales
        self.temp_counter = 1

        # Contador de cuadruplos (usado para saltos)
        self.quad_counter = 0

    # ---------- Metodos para Generacion de Temporales ----------
    def generate_temp(self) -> str:
        """
        Genera un nombre para una variable temporal
        
        """
        temp_name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp_name
    
    def add_quadruple(self, operator, left_operand, right_operand, result) -> int:
        """
        Añade un cuadruplo a la fila y devuelve su indice
        """
        quad = Quadruple(operator, left_operand, right_operand, result)
        self.quadruples.append(quad)
        idex = self.quad_counter
        self.quad_counter += 1
        return idex
    
    def fill_quadruple(self, index: int, result):
        """
        Compelta un cuadruplo con direccion de salto pendiente
        """
        if 0 <= index < len(self.quadruples):
            self.quadruples[index].result = result
    
    # ---------- Metodos par Operaciones Aritmeticas y Relacionales ----------
    def process_arithmetic_expression(self, operator_types: List[OperatorType]):
        """Procesa operadores aritméticos de la pila que tienen mayor o igual precedencia"""
        if self.operator_stack and self.operator_stack[-1] in operator_types:
            # Hay un operador de mayor o igual precedencia
            operator = self.operator_stack.pop()
            
            # Obtener operandos y tipos
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            
            # Verificar compatibilidad de tipos
            result_type = get_result_type(left_type.value, right_type.value, operator.value)
            if result_type == ERROR:
                raise ValueError(f"Error de tipos: Operación incompatible {left_type.name} {operator.value} {right_type.name}")
            
            # Generar resultado temporal
            temp = self.generate_temp()
            
            # Añadir cuádruplo
            self.add_quadruple(operator, left_operand, right_operand, temp)
            
            # Añadir resultado a las pilas
            self.operand_stack.append(temp)
            self.type_stack.append(Type.INT if result_type == INT else Type.FLOAT)
    
    def process_relational_expression(self):
        """Procesa una operación relacional"""
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
            result_type = get_result_type(left_type.value, right_type.value, operator.value)
            if result_type == ERROR:
                raise ValueError(f"Error de tipos: Operación incompatible {left_type.name} {operator.value} {right_type.name}")
            
            # Generar resultado temporal
            temp = self.generate_temp()
            
            # Añadir cuádruplo
            self.add_quadruple(operator, left_operand, right_operand, temp)
            
            # Añadir resultado a las pilas (operaciones relacionales devuelven siempre INT)
            self.operand_stack.append(temp)
            self.type_stack.append(Type.INT)

    # ---------- Metodos para Estatus Lineales (Asignacion, Print) ----------
    def process_assignment(self):
        """Procesa una operación de asignación"""
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

    #def process_print(self, elements: List[Tuple[Any, Type]]):
        #"""Genera cuádruplos para una instrucción print"""
        #for element, element_type in elements:
            #self.add_quadruple(OperatorType.PRINT, element, None, None)
    
    # ---------- Soporte de Estructurar de Control ----------
    # Continuación de quad_generator.py (dentro de la clase QuadrupleGenerator)
    def generate_gotof(self, condition):
        """Genera un GOTOF para una condición y devuelve su índice"""
        index = self.add_quadruple(OperatorType.GOTOF, condition, None, None)
        return index

    def generate_goto(self):
        """Genera un GOTO incondicional y devuelve su índice"""
        index = self.add_quadruple(OperatorType.GOTO, None, None, None)
        return index
