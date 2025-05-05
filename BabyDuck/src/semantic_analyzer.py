from antlr4 import *
from generated.src.BabyDuckParser import BabyDuckParser
from generated.src.BabyDuckVisitor import BabyDuckVisitor
from semantic_cube import get_result_type, INT, FLOAT, ERROR
from symbol_table import SymbolTable, Type, Variable, Function
from typing import Any, List, Dict

class SemanticError(Exception):
    """Excepción para errores semánticos"""
    pass

class SemanticAnalyzer(BabyDuckVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def add_error(self, ctx, message):
        """Añade un error semántico"""
        line = ctx.start.line
        column = ctx.start.column
        self.errors.append(f"Error semántico en linea {line}:{column} - {message}")

    def visitPrograma(self, ctx: BabyDuckParser.ProgramaContext):
        # Añadir el programa como una "funcion" global
        program_name = ctx.ID().getText()
        self.symb_table.add_function(program_name, Type.VOID)

        # Añadir funcion main implicitamente
        self.symbol_table.add_function("main", Type.VOID)

        # Visitar las declaraciones de variables y funciones
        if ctx.vars_():
            self.visit(ctx.vars_())

        if ctx.funcs():
            self.visit(ctx.funcs_())

        # Cambiar a la funcion main para el cuerpo principal
        self.symbol_table.current_function = "main"

        # Visitar el cuerpo principal
        self.visit(ctx.body())

        # Visitar el cuerpo principal
        self.visit(ctx.body())

        # Verificar que todas las funciones declaradas han sido utilizadas
        for func_name in self.symbol_table.functions:
            if not self.symbol_table.functions[func_name].used:
                self.add_error(ctx, f"La función '{func_name}' no ha sido utilizada.")

        return self.symbol_table
    
    def visitVars(self, ctx: BabyDuckParser.VarsContext):
        # Visitar las declaraciones de variables
        return self.visit(ctx.varDecList())
    
    def visitVarDecList(self, ctx: BabyDuckParser.VarDecListContext):
        # Visitar cada declaracion de variable
        for vac_dec in ctx.varDec():
            self.visit(vac_dec)
        return None
    
    def visitVarDec(self, ctx: BabyDuckParser.VarDecContext):
        # Obtener el tipo de la variable
        type_ctx = ctx.type_()
        var_type = Type.INT if type_ctx.INT() else Type.FLOAT

        # Obtener los IDs y añadir cada variable a la tabla
        id_list = ctx.idList()
        is_global = self.symbol_table.current_function == "programa"

        for id_token in id_list.ID():
            var_name = id_token.getText()
            if not self.symbol_table.add_variable(var_name, var_type, is_global):
                self.add_error(ctx, f"La variable '{var_name}' ya ha sido declarada.")
        return None
    
    def visitFuncs(self, ctx: BabyDuckParser.FuncsContext):
        # Visitar cada declaracion de funcion
        for func_dec in ctx.funcDec():
            self.visit(func_dec)
        return None
    
    def visitFuncDec(self, ctx: BabyDuckParser.FuncDecContext):
        # Obtenere el nombre de la funcion
        func_name = ctx.ID().getText()

        # Todas las funciones en BabyDuck son VOID
        func_type = Type.VOID

        # Añadir la funcion al directorio
        if not self.symbol_table.add_function(func_name, func_type):
            self.add_error(ctx, f"Funcion '{func_name}' ya declarada.")
            return None
        
        # Processar parametros si ya existen
        if ctx.params():
            self.visit(ctx.params())

        # Procesar variables locales si ya existen
        if ctx.vars_():
            self.visit(ctx.vars_())

        # Procesar el cuerpo de la funcion
        self.visit(ctx.body())

        return None

