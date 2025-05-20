from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

class Type(Enum):
    INT = 0
    FLOAT = 1
    VOID = 2
    ERROR = -1

@dataclass
class Variable:
    name: str
    type: Type
    address: int = 0  # Dirección virtual asignada a la variable

@dataclass
class Function:
    name: str
    type: Type
    params: List[Variable] = field(default_factory=list)
    vars_table: Dict[str, Variable] = field(default_factory=dict)
    start_address: int = 0  # Dirección de inicio de la función (índice del cuádruplo)
    local_vars_count: int = 0  # Contador de variables locales
    temp_vars_count: int = 0  # Contador de variables temporales usadas

class SymbolTable:
    def __init__(self):
        self.functions = {}  # Diccionario de funciones
        self.current_function = None  # Función actual siendo procesada
        self.global_vars = {}  # Variables globales

    def add_function(self, name: str, type: Type) -> bool:
        """
        Añade una función al directorio si no existe
        
        Args:
            name: Nombre de la función
            type: Tipo de retorno de la función
            
        Returns:
            bool: True si se añadió correctamente, False si ya existía
        """
        if name in self.functions:
            return False
        self.functions[name] = Function(name=name, type=type)
        self.current_function = name
        return True
    
    def add_variable(self, name: str, type: Type, is_global: bool = False) -> bool:
        """
        Añade una variable a la tabla de variables
        
        Args:
            name: Nombre de la variable
            type: Tipo de la variable
            is_global: Indica si es una variable global
            
        Returns:
            bool: True si se añadió correctamente, False si ya existía
        """
        if is_global:
            if name in self.global_vars:
                return False  # Variable global ya declarada
            self.global_vars[name] = Variable(name=name, type=type)
        else:
            if not self.current_function:
                return False  # No hay función actual
            if name in self.functions[self.current_function].vars_table:
                return False  # Variable local ya declarada
            
            self.functions[self.current_function].vars_table[name] = Variable(name=name, type=type)
        return True
    
    def add_param(self, name: str, type: Type) -> bool:
        """
        Añade un parámetro a la función actual
        
        Args:
            name: Nombre del parámetro
            type: Tipo del parámetro
            
        Returns:
            bool: True si se añadió correctamente, False si ya existía
        """
        if not self.current_function:
            return False  # No hay función actual
        
        if name in self.functions[self.current_function].vars_table:
            return False  # Parámetro ya declarado como variable local
        
        # Añadir el parámetro a la lista de parámetros y también a la tabla de variables
        param = Variable(name=name, type=type)
        self.functions[self.current_function].params.append(param)
        self.functions[self.current_function].vars_table[name] = param
        return True
    
    def lookup_variable(self, name: str) -> Optional[Variable]:
        """
        Busca una variable primero en la función actual y luego en las globales
        
        Args:
            name: Nombre de la variable a buscar
            
        Returns:
            Optional[Variable]: La variable encontrada o None si no existe
        """
        if self.current_function and name in self.functions[self.current_function].vars_table:
            return self.functions[self.current_function].vars_table[name]
        
        if name in self.global_vars:
            return self.global_vars[name]
        return None
    
    def lookup_function(self, name: str) -> Optional[Function]:
        """
        Busca una función en el directorio
        
        Args:
            name: Nombre de la función a buscar
            
        Returns:
            Optional[Function]: La función encontrada o None si no existe
        """
        return self.functions.get(name)
    
    def get_function_size(self, name: str) -> Dict[str, int]:
        """
        Obtiene información sobre el tamaño de memoria requerido por una función
        
        Args:
            name: Nombre de la función
            
        Returns:
            Dict[str, int]: Diccionario con contadores de variables locales, temporales y parámetros
        """
        if name not in self.functions:
            return {"local_vars": 0, "temp_vars": 0, "params": 0}
        
        func = self.functions[name]
        return {
            "local_vars": func.local_vars_count,
            "temp_vars": func.temp_vars_count,
            "params": len(func.params)
        }
    
    def get_variables_by_type(self, function_name: str = None) -> Dict[Type, List[Variable]]:
        """
        Obtiene todas las variables agrupadas por tipo
        
        Args:
            function_name: Nombre de la función (si es None, se usan variables globales)
            
        Returns:
            Dict[Type, List[Variable]]: Diccionario con variables agrupadas por tipo
        """
        result = {Type.INT: [], Type.FLOAT: []}
        
        # Definir qué tabla de variables usar
        vars_table = self.global_vars
        if function_name and function_name in self.functions:
            vars_table = self.functions[function_name].vars_table
        
        # Agrupar variables por tipo
        for var_name, var in vars_table.items():
            if var.type in result:
                result[var.type].append(var)
        
        return result