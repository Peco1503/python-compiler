#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilador para el lenguaje BabyDuck
Autor: Basado en el trabajo de Franco Enrique Lugo Meza A00833951
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
    
    # Convertir los simbols a una lista para poder imprimirlos
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
        
    except ParseCancellationException as e:
        print(f"\nError de sintaxis: {str(e)}")
    except RecognitionException as e:
        print(f"\nError de reconocimiento: {str(e)}")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == '__main__':
    main(sys.argv)