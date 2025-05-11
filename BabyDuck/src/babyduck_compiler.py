#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilador para el lenguaje BabyDuck

"""

import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

# Agregar el directorio 'generated' al path para poder importar los módulos generados
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'generated'))

from BabyDuckLexer import BabyDuckLexer
from BabyDuckParser import BabyDuckParser
from semantic_analyzer import SemanticAnalyzer, SemanticError

class SyntaxErrorListener(ErrorListener):
    """
    Listener personalizado para errores de sintaxis
    """
    def __init__(self):
        self.errors = []
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Error sintáctico en línea {line}:{column} - {msg}"
        self.errors.append(error_msg)
        raise ParseCancellationException(error_msg)
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

def print_tokens(lexer):
    """
    Imprime todos los tokens identificados por el lexer
    """
    print("\n=== ANÁLISIS LÉXICO (TOKENS) ===")
    
    # Convertir los symbolicNames a una lista para poder imprimirlos
    symbolicNames = lexer.symbolicNames
    
    tokens = []
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_type = token.type
        token_text = token.text
        token_line = token.line
        token_column = token.column
        token_name = symbolicNames[token_type] if token_type < len(symbolicNames) else "UNKNOWN"
        
        tokens.append((token_type, token_name, token_text, token_line, token_column))
        token = lexer.nextToken()
    
    # Imprimir los tokens en formato de tabla
    print(f"{'Tipo':<6} {'Nombre':<15} {'Texto':<20} {'Línea':<6} {'Columna':<8}")
    print("-" * 60)
    for token_type, token_name, token_text, token_line, token_column in tokens:
        print(f"{token_type:<6} {token_name:<15} {token_text:<20} {token_line:<6} {token_column:<8}")
    
    # Devolver el número de tokens encontrados
    return len(tokens)

def print_parse_tree(tree, parser, indent=0):
    """
    Imprime el árbol de análisis sintáctico con sangría
    """
    if tree is None:
        return
    
    # Si es una hoja (token terminal)
    if isinstance(tree, TerminalNode):
        token = tree.getSymbol()
        print("  " * indent + f"Token: {parser.symbolicNames[token.type]} '{token.text}'")
        return
    
    # Si es un nodo no terminal
    rule_name = parser.ruleNames[tree.getRuleContext().getRuleIndex()]
    print("  " * indent + f"Regla: {rule_name}")
    
    # Procesar los hijos
    for i in range(tree.getChildCount()):
        print_parse_tree(tree.getChild(i), parser, indent + 1)

def print_symbol_table(symbol_table):
    """
    Imprime el directorio de funciones y las tablas de variables
    """
    print("\n=== DIRECTORIO DE FUNCIONES ===")
    print(f"{'Nombre':<15} {'Tipo':<10} {'#Params':<10} {'#Vars':<10}")
    print("-" * 50)

    for func_name, func in symbol_table.functions.items():
        print(f"{func_name:<15} {func.type.name:<10} {len(func.params):<10} {len(func.vars_table):<10}")

    # Imprimir variables globales
    print("\n=== VARIABLES GLOBALES ===")
    if symbol_table.global_vars:
        print(f"{'Nombre':<15} {'Tipo':<10}")
        print("-" * 30)
        for var_name, var in symbol_table.global_vars.items():
            print(f"{var_name:<15} {var.type.name:<10}")
    else:
        print("No hay variables globales")
    
    # Imprimir variables de cada función
    for func_name, func in symbol_table.functions.items():
        print(f"\n=== VARIABLES DE '{func_name}' ===")
        if func.vars_table:
            print(f"{'Nombre':<15} {'Tipo':<10} {'Es Parámetro':<15}")
            print("-" * 45)
            for var_name, var in func.vars_table.items():
                is_param = "Sí" if var_name in [p.name for p in func.params] else "No"
                print(f"{var_name:<15} {var.type.name:<10} {is_param:<15}")
        else:
            print(f"La función '{func_name}' no tiene variables locales")

def print_quadruples(quadruples):
    """
    Imprime los cuádruplos generados
    """
    print("\n=== CÓDIGO INTERMEDIO (CUÁDRUPLOS) ===")
    print(f"{'#':<4} {'Operador':<10} {'Operando1':<15} {'Operando2':<15} {'Resultado':<15}")
    print("-" * 60)
    
    for i, quad in enumerate(quadruples):
        print(f"{i:<4} {str(quad.operator):<10} {str(quad.left_operand) if quad.left_operand is not None else 'None':<15} {str(quad.right_operand) if quad.right_operand is not None else 'None':<15} {str(quad.result) if quad.result is not None else 'None':<15}")

def main(argv):
    # Verificar argumentos
    if len(argv) > 1:
        input_file = argv[1]
        try:
            input_stream = FileStream(input_file, encoding='utf-8')
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            return
    else:
        # Si no hay archivo, leer de entrada estándar
        print("Escribe tu código BabyDuck (termina con Ctrl+D en Unix o Ctrl+Z en Windows):")
        input_stream = InputStream(sys.stdin.read())
    
    # Crear lexer (scanner)
    lexer = BabyDuckLexer(input_stream)
    
    # Imprimir tokens y guardar su número
    token_count = print_tokens(lexer)
    print(f"\nTotal de tokens encontrados: {token_count}")
    
    # Resetear el lexer para el parser
    lexer.reset()
    token_stream = CommonTokenStream(lexer)
    
    # Crear parser
    parser = BabyDuckParser(token_stream)
    
    # Configurar manejo de errores
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    try:
        # Realizar análisis sintáctico
        print("\n=== ANÁLISIS SINTÁCTICO ===")
        tree = parser.programa()
        
        # Si llegamos aquí, no hubo errores sintácticos
        print("Análisis sintáctico exitoso.")
        
        # Mostrar el árbol sintáctico
        print("\n=== ÁRBOL SINTÁCTICO ===")
        print_parse_tree(tree, parser)

        # Realizar análisis semántico
        print("\n=== ANÁLISIS SEMÁNTICO ===")
        semantic_analyzer = SemanticAnalyzer()
        try:
            result = semantic_analyzer.visit(tree)
            
            # Desempaquetar los resultados
            if isinstance(result, tuple) and len(result) == 2:
                symbol_table, quadruples = result
            else:
                symbol_table = result
                quadruples = []
            
            # Verificar si hubo errores semánticos
            if semantic_analyzer.errors:
                print("Errores semánticos encontrados:")
                for error in semantic_analyzer.errors:
                    print(f"  - {error}")
            else:
                print("Análisis semántico exitoso.")
                
                # Mostrar el directorio de funciones y tablas de variables
                print_symbol_table(symbol_table)
                
                # Mostrar los cuádruplos generados
                print_quadruples(quadruples)
                
                print(f"\nTotal de cuádruplos generados: {len(quadruples)}")
                print(f"Total de temporales utilizados: {semantic_analyzer.quad_generator.temp_counter - 1}")
                
        except SemanticError as e:
            print(f"Error semántico: {str(e)}")
        
    except ParseCancellationException as e:
        print(f"\nError de sintaxis: {str(e)}")
    except RecognitionException as e:
        print(f"\nError de reconocimiento: {str(e)}")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == '__main__':
    main(sys.argv)