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
    
    def visitParamList(self, ctx: BabyDuckParser.ParamListContext):
        # Visitar cad parametro
        for param_ctx in ctx.param():
            self.visit(param_ctx)
        return None
    
    def visitParam(self, ctx: BabyDuckParser.ParamContext):
        # Obtener nombre y tipo del parametro
        param_name = ctx.ID().getText()
        param_type = Type.INT if ctx.INT() else Type.FLOAT

        # Añadir el parametro a la funcion actual
        if not self.symbol_table.add_param(param_name, param_type):
            self.add_error(ctx, f"El parametro '{param_name}' ya ha sido declarado.")

        return None
    
    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Obtener el identificador al que se asigna
        var_name = ctx.ID().getText()
        var = self.symbol_table.lookup_variable(var_name)

        if not var:
            self.add_error(ctx, f"Variable '{var_name}' no declarada.")
            return Type.ERROR
        
        # Verifiar el tipo de la expresion
        expr_type = self.visit(ctx.expresion())

        # Verificar compatbilidad de tipos en la asignacion
        result_type = get_result_type(var.type.value, expr_type.value, '=')
        if result_type == ERROR:
            self.add_error(ctx, f"Tipo incompatible en asignacion: no se puede asignar {expr_type.name} a {var.type.name}.")

        return Type.VOID
    
    def visitExpresion(self, ctx: BabyDuckParser.ExpresionContext):
        # Visitar la primer expresion
        left_type = self.visit(ctx.exp(0))

        # Si hay un operador relacional
        if len(ctx.exp()) > 1:
            # Obtener el operador
            if ctx.GT():
                op = '>'
            elif ctx.LT():
                op = '<'
            elif ctx.NE():
                op = '!='
            elif ctx.LE():
                op = '<='
            elif ctx.GE():
                op = '>='
            elif ctx.EQ():
                op = '=='
            else:
                op = 'unknown'

            # Visitar la segunda expresion
            right_type = self.visit(ctx.exp(1))

            # Verificar compatbilidad 
            result = get_result_type(left_type.value, right_type.value, op)
            if result == ERROR:
                self.add_error(ctx, f"Operacion incompatible {left_type.name} {op} {right_type.name}")
                return Type.ERROR
            
            return Type.INT # Operaciones relacionales devuelven INT (0 o 1)
        
        return left_type # Si no hay operador relacional, devolver el tipo de la expresion
    
    def visitExp(self, ctx: BabyDuckParser.ExpContext):
        # Visitar el primer término
        current_type = self.visit(ctx.termino(0))
        
        # Si hay más términos con operadores + o -
        for i in range(1, len(ctx.termino())):
            term_type = self.visit(ctx.termino(i))
            # El operador está en la posición i-1
            op = '+' if ctx.PLUS(i-1) else '-'
            
            # Verificar compatibilidad
            result = get_result_type(current_type.value, term_type.value, op)
            if result == ERROR:
                self.add_error(ctx, f"Operación incompatible: {current_type.name} {op} {term_type.name}")
                return Type.ERROR
                
            current_type = Type.INT if result == INT else Type.FLOAT
            
        return current_type
        
    def visitTermino(self, ctx: BabyDuckParser.TerminoContext):
        # Visitar el primer factor
        current_type = self.visit(ctx.factor(0))
        
        # Si hay más factores con operadores * o /
        for i in range(1, len(ctx.factor())):
            factor_type = self.visit(ctx.factor(i))
            # El operador está en la posición i-1
            op = '*' if ctx.MULT(i-1) else '/'
            
            # Verificar compatibilidad
            result = get_result_type(current_type.value, factor_type.value, op)
            if result == ERROR:
                self.add_error(ctx, f"Operación incompatible: {current_type.name} {op} {factor_type.name}")
                return Type.ERROR
                
            current_type = Type.INT if result == INT else Type.FLOAT
            
        return current_type
        
    def visitFactor(self, ctx: BabyDuckParser.FactorContext):
        # Si es una expresión entre paréntesis
        if ctx.expresion():
            return self.visit(ctx.expresion())
            
        # Si es un ID
        elif ctx.ID():
            var_name = ctx.ID().getText()
            var = self.symbol_table.lookup_variable(var_name)
            
            if not var:
                self.add_error(ctx, f"Variable '{var_name}' no declarada")
                return Type.ERROR
                
            return var.type
            
        # Si es una constante
        elif ctx.cte():
            return self.visit(ctx.cte())
            
        return Type.ERROR
        
    def visitCte(self, ctx: BabyDuckParser.CteContext):
        # Determinar el tipo de la constante
        if ctx.CTE_INT():
            return Type.INT
        elif ctx.CTE_FLOAT():
            return Type.FLOAT
            
        return Type.ERROR
        
    def visitPrint(self, ctx: BabyDuckParser.PrintContext):
        # Visitar la lista de imprimibles
        self.visit(ctx.printableList())
        return Type.VOID
        
    def visitPrintableList(self, ctx: BabyDuckParser.PrintableListContext):
        # Visitar cada elemento imprimible
        for printable in ctx.printable():
            self.visit(printable)
        return None
        
    def visitPrintable(self, ctx: BabyDuckParser.PrintableContext):
        # Si es una expresión, verificar su tipo
        if ctx.expresion():
            return self.visit(ctx.expresion())
        # Si es una cadena, no necesitamos verificar nada
        return None
        
    def visitCondition(self, ctx: BabyDuckParser.ConditionContext):
        # Verificar que la expresión de la condición sea booleana
        expr_type = self.visit(ctx.expresion())
        
        # Visitar el cuerpo del if
        self.visit(ctx.body(0))
        
        # Si hay else, visitar también su cuerpo
        if len(ctx.body()) > 1:
            self.visit(ctx.body(1))
            
        return Type.VOID
        
    def visitCycle(self, ctx: BabyDuckParser.CycleContext):
        # Verificar que la expresión del while sea booleana
        expr_type = self.visit(ctx.expresion())
        
        # Visitar el cuerpo del ciclo
        self.visit(ctx.body())
        
        return Type.VOID
        
    def visitFcall(self, ctx: BabyDuckParser.FcallContext):
        # Obtener el nombre de la función llamada
        func_name = ctx.ID().getText()
        func = self.symbol_table.lookup_function(func_name)
        
        if not func:
            self.add_error(ctx, f"Función '{func_name}' no declarada")
            return Type.ERROR
            
        # Verificar que el número de argumentos coincida con el número de parámetros
        arg_list = ctx.argList()
        expected_params = func.params
        
        if arg_list and not expected_params:
            self.add_error(ctx, f"La función '{func_name}' no espera argumentos")
            return func.type
            
        if not arg_list and expected_params:
            self.add_error(ctx, f"La función '{func_name}' espera {len(expected_params)} argumentos")
            return func.type
            
        if arg_list:
            # Contar expresiones en la lista de argumentos
            arg_count = len(arg_list.expresion())
            if arg_count != len(expected_params):
                self.add_error(ctx, f"La función '{func_name}' espera {len(expected_params)} argumentos, pero recibió {arg_count}")
                return func.type
                
            # Verificar el tipo de cada argumento
            for i, expr_ctx in enumerate(arg_list.expresion()):
                arg_type = self.visit(expr_ctx)
                param_type = expected_params[i].type
                
                # Verificar compatibilidad de tipos
                if arg_type != param_type and not (arg_type == Type.INT and param_type == Type.FLOAT):
                    self.add_error(expr_ctx, f"Tipo incompatible en argumento {i+1}: esperaba {param_type.name}, recibió {arg_type.name}")
                    
        return func.type
        
    def visitArgList(self, ctx: BabyDuckParser.ArgListContext):
        # Visitar cada expresión en la lista de argumentos
        for expr_ctx in ctx.expresion():
            self.visit(expr_ctx)
        return None

