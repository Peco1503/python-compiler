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
    address: int = 0 # Para la generacion de codigo posterior

@dataclass
class Function:
    name: str
    type: Type
    params: List[Variable] = field(default_factory=list)
    vars_table: Dict[str, Variable] = field(default_factory=dict)
    start_address: int = 0 # Para la generacion de codigo posterior

class SymbolTable:
    def __init__(self):
        self.functions = {} # Diccionario de funciones
        self.current_function: None # Funcion actual siendo procesada
        self.global_vars = {} # Variables globales

    def add_function(self, name: str, type: Type) -> bool:
        """
        Añade una funcion al directorio si no existe
        """
        if name in self.functions:
            return False
        self.functions[name] = Function(name=name, type=type)
        self.current_function = name
        return True
    
    def add_variable(self, name: str, type: Type, is_global: bool = False) -> bool:
        """
        Añade una variable al directorio de variables
        """
        if is_global:
            if name in self.global_vars:
                return False # Variable global ya declarada
            self.global_vars[name] = Variable(name=name, type=type)
        else:
            if not self.current_function:
                return False # No hay funcion actual
            if name in self.functions[self.current_function].vars_table:
                return False # Variable local ya declarada
            
            self.functions[self.current_function].vars_table[name] = Variable(name=name, type=type)
        return True
    
    def add_param(self, name: str, type: Type) -> bool:
        """
        Añade un parrametro a la funcion actual 
        """
        if not self.current_function:
            return False # No hay funcion actual
        
        if name in self.functions[self.current_function].vars_table:
            return False # Parametro ya declarado como variable local
        
        # Añadir el parametro a la lista de parametros y tambien a la tabla de variables
        param = Variable(name=name, type=type)
        self.functions[self.current_function].params.append(param)
        self.functions[self.current_function].vars_table[name] = param
        return True
    
    def lookup_variable(self, name: str) -> Optional[Variable]:
        """
        Busca una variable primero en la funcion actual y luego en las globales
        """

        if self.current_function and name in self.functions[self.current_function].vars_table:
            return self.functions[self.current_function].vars_table[name]
        
        if name in self.global_vars:
            return self.global_vars[name]
        return None

    
    def lookup_function(self, name: str) -> Optional[Function]:
        """
        Busca una function en el direcot
        """
        return self.functions.get(name)
    
