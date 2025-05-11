from antlr4 import *
from generated.src.BabyDuckParser import BabyDuckParser
from generated.src.BabyDuckVisitor import BabyDuckVisitor
from semantic_cube import get_result_type, INT, FLOAT, ERROR
from symbol_table import SymbolTable, Type, Variable, Function
from quad_generator import QuadrupleGenerator, OperatorType, Quadruple
from typing import Any, List, Dict, Tuple

class SemanticError(Exception):
    """Excepción para errores semánticos"""
    pass

class SemanticAnalyzer(BabyDuckVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.quad_generator = QuadrupleGenerator()  # Generador de cuádruplos

    def add_error(self, ctx, message):
        """Añade un error semántico"""
        line = ctx.start.line
        column = ctx.start.column
        self.errors.append(f"Error semántico en linea {line}:{column} - {message}")

    def visitPrograma(self, ctx: BabyDuckParser.ProgramaContext):
        # Añadir el programa como una "función" global
        program_name = ctx.ID().getText()
        self.symbol_table.add_function(program_name, Type.VOID)
        
        # Añadir función main implícitamente
        self.symbol_table.add_function("main", Type.VOID)
        
        # Visitar las declaraciones de variables y funciones
        if ctx.vars_():
            self.visit(ctx.vars_())
            
        if ctx.funcs():
            self.visit(ctx.funcs())
            
        # Cambiar a la función main para el cuerpo principal
        self.symbol_table.current_function = "main"
        
        # Visitar el cuerpo principal
        self.visit(ctx.body())
        
        # Verificar que todas las funciones declaradas han sido utilizadas
        # (esto se podría implementar si se desea)
        
        # Retornar tanto la tabla de símbolos como los cuádruplos generados
        return self.symbol_table, self.quad_generator.quadruples
    
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
        # Obtener el nombre de la función
        func_name = ctx.ID().getText()
        
        # Todas las funciones en BabyDuck son VOID
        func_type = Type.VOID
        
        # Añadir la función al directorio
        if not self.symbol_table.add_function(func_name, func_type):
            self.add_error(ctx, f"Función '{func_name}' ya declarada")
            return None
            
        # Guardar la dirección de inicio de la función
        func_start = self.quad_generator.quad_counter
        self.symbol_table.functions[func_name].start_address = func_start
        
        # Procesar parámetros si existen
        if ctx.paramList():
            self.visit(ctx.paramList())
            
        # Procesar variables locales si existen
        if ctx.vars_():
            self.visit(ctx.vars_())
            
        # Procesar el cuerpo de la función
        self.visit(ctx.body())
        
        # Generar cuádruplo de fin de función
        self.quad_generator.add_quadruple(OperatorType.ENDFUNC, None, None, None)
        
        return None
    
    def visitParamList(self, ctx: BabyDuckParser.ParamListContext):
        # Visitar cada parámetro
        for param_ctx in ctx.param():
            self.visit(param_ctx)
        return None
    
    def visitParam(self, ctx: BabyDuckParser.ParamContext):
        # Obtener nombre y tipo del parámetro
        param_name = ctx.ID().getText()
        param_type = Type.INT if ctx.type_().INT() else Type.FLOAT
        
        # Añadir el parámetro a la función actual
        if not self.symbol_table.add_param(param_name, param_type):
            self.add_error(ctx, f"Parámetro '{param_name}' ya declarado en la función")
            
        return None
    
    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Obtener el identificador al que se asigna
        var_name = ctx.ID().getText()
        var = self.symbol_table.lookup_variable(var_name)

        if not var:
            self.add_error(ctx, f"Variable '{var_name}' no declarada.")
            return Type.ERROR
        
        # Añadir la variable a la pila de operandos y tipos
        self.quad_generator.operand_stack.append(var_name)
        self.quad_generator.type_stack.append(var.type)
        
        # Añadir operador de asignación
        self.quad_generator.operator_stack.append(OperatorType.ASSIGN)
        
        # Visitar la expresión
        expr_type = self.visit(ctx.expresion())
        
        # Verificar compatibilidad de tipos en la asignación
        result_type = get_result_type(var.type.value, expr_type.value, '=')
        if result_type == ERROR:
            self.add_error(ctx, f"Tipo incompatible en asignación: no se puede asignar {expr_type.name} a {var.type.name}.")
            return Type.ERROR
        
        # Procesar la asignación
        self.quad_generator.process_assignment()
        
        return Type.VOID
    
    def visitExpresion(self, ctx: BabyDuckParser.ExpresionContext):
        # Visitar la primer expresión
        left_type = self.visit(ctx.exp(0))

        # Si hay un operador relacional
        if len(ctx.exp()) > 1:
            # Obtener el operador
            if ctx.GT():
                op = OperatorType.GT
            elif ctx.LT():
                op = OperatorType.LT
            elif ctx.NE():
                op = OperatorType.NE
            elif ctx.LE():
                op = OperatorType.LE
            elif ctx.GE():
                op = OperatorType.GE
            elif ctx.EQ():
                op = OperatorType.EQ
            else:
                op = None
            
            # Guardar el operador en la pila
            self.quad_generator.operator_stack.append(op)
            
            # Visitar la segunda expresión
            right_type = self.visit(ctx.exp(1))
            
            # Verificar compatibilidad 
            result = get_result_type(left_type.value, right_type.value, op.value)
            if result == ERROR:
                self.add_error(ctx, f"Operación incompatible {left_type.name} {op.value} {right_type.name}")
                return Type.ERROR
            
            # Procesar la expresión relacional
            self.quad_generator.process_relational_expression()
            
            return Type.INT  # Operaciones relacionales devuelven INT (0 o 1)
        
        return left_type  # Si no hay operador relacional, devolver el tipo de la expresión
    
    def visitExp(self, ctx: BabyDuckParser.ExpContext):
        # Visitar el primer término
        current_type = self.visit(ctx.termino(0))
        
        # Si hay más términos con operadores + o -
        for i in range(1, len(ctx.termino())):
            # El operador está en la posición i-1
            op = OperatorType.PLUS if ctx.PLUS(i-1) else OperatorType.MINUS
            self.quad_generator.operator_stack.append(op)
            
            # Visitar el siguiente término
            term_type = self.visit(ctx.termino(i))
            
            # Verificar compatibilidad
            result = get_result_type(current_type.value, term_type.value, op.value)
            if result == ERROR:
                self.add_error(ctx, f"Operación incompatible: {current_type.name} {op.value} {term_type.name}")
                return Type.ERROR
            
            # Procesar la expresión aritmética
            self.quad_generator.process_arithmetic_expression([OperatorType.PLUS, OperatorType.MINUS])
            
            # Actualizar el tipo actual (ahora está en el tope de la pila)
            current_type = self.quad_generator.type_stack[-1]
            
        return current_type
        
    def visitTermino(self, ctx: BabyDuckParser.TerminoContext):
        # Visitar el primer factor
        current_type = self.visit(ctx.factor(0))
        
        # Si hay más factores con operadores * o /
        for i in range(1, len(ctx.factor())):
            # El operador está en la posición i-1
            op = OperatorType.MULT if ctx.MULT(i-1) else OperatorType.DIV
            self.quad_generator.operator_stack.append(op)
            
            # Visitar el siguiente factor
            factor_type = self.visit(ctx.factor(i))
            
            # Verificar compatibilidad
            result = get_result_type(current_type.value, factor_type.value, op.value)
            if result == ERROR:
                self.add_error(ctx, f"Operación incompatible: {current_type.name} {op.value} {factor_type.name}")
                return Type.ERROR
            
            # Procesar la expresión aritmética
            self.quad_generator.process_arithmetic_expression([OperatorType.MULT, OperatorType.DIV])
            
            # Actualizar el tipo actual (ahora está en el tope de la pila)
            current_type = self.quad_generator.type_stack[-1]
            
        return current_type
        
    def visitFactor(self, ctx: BabyDuckParser.FactorContext):
        # Si es un signo unario
        if ctx.PLUS() or ctx.MINUS():
            has_unary_minus = ctx.MINUS() is not None
            
            # Si es una expresión entre paréntesis
            if ctx.expresion():
                result_type = self.visit(ctx.expresion())
                
                # Si hay un signo negativo, negar el valor
                if has_unary_minus:
                    operand = self.quad_generator.operand_stack.pop()
                    self.quad_generator.type_stack.pop()
                    
                    # Generar temporal para el valor negado
                    temp = self.quad_generator.generate_temp()
                    self.quad_generator.add_quadruple(OperatorType.MINUS, "0", operand, temp)
                    
                    # Añadir a las pilas
                    self.quad_generator.operand_stack.append(temp)
                    self.quad_generator.type_stack.append(result_type)
                
                return result_type
            
            # Si es un ID
            elif ctx.ID():
                var_name = ctx.ID().getText()
                var = self.symbol_table.lookup_variable(var_name)
                
                if not var:
                    self.add_error(ctx, f"Variable '{var_name}' no declarada")
                    return Type.ERROR
                
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(var_name)
                self.quad_generator.type_stack.append(var.type)
                
                # Si hay un signo negativo, negar el valor
                if has_unary_minus:
                    operand = self.quad_generator.operand_stack.pop()
                    self.quad_generator.type_stack.pop()
                    
                    # Generar temporal para el valor negado
                    temp = self.quad_generator.generate_temp()
                    self.quad_generator.add_quadruple(OperatorType.MINUS, "0", operand, temp)
                    
                    # Añadir a las pilas
                    self.quad_generator.operand_stack.append(temp)
                    self.quad_generator.type_stack.append(var.type)
                
                return var.type
            
            # Si es una constante
            elif ctx.cte():
                cte_type = self.visit(ctx.cte())
                cte_val = ctx.cte().getText()
                
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(cte_val)
                self.quad_generator.type_stack.append(cte_type)
                
                # Si hay un signo negativo, negar el valor
                if has_unary_minus:
                    operand = self.quad_generator.operand_stack.pop()
                    self.quad_generator.type_stack.pop()
                    
                    # Generar temporal para el valor negado
                    temp = self.quad_generator.generate_temp()
                    self.quad_generator.add_quadruple(OperatorType.MINUS, "0", operand, temp)
                    
                    # Añadir a las pilas
                    self.quad_generator.operand_stack.append(temp)
                    self.quad_generator.type_stack.append(cte_type)
                
                return cte_type
        else:
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
                    
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(var_name)
                self.quad_generator.type_stack.append(var.type)
                
                return var.type
                
            # Si es una constante
            elif ctx.cte():
                cte_type = self.visit(ctx.cte())
                cte_val = ctx.cte().getText()
                
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(cte_val)
                self.quad_generator.type_stack.append(cte_type)
                
                return cte_type
            
        return Type.ERROR
        
    def visitCte(self, ctx: BabyDuckParser.CteContext):
        # Determinar el tipo de la constante
        if ctx.CTE_INT():
            return Type.INT
        elif ctx.CTE_FLOAT():
            return Type.FLOAT
            
        return Type.ERROR
        
    def visitPrint(self, ctx: BabyDuckParser.PrintContext):
        # Visitar la lista de imprimibles y generar cuádruplos para cada elemento
        printable_list = self.visit(ctx.printableList())
        
        # Para cada elemento en la lista, generar un cuádruplo de print
        for value, value_type in printable_list:
            self.quad_generator.add_quadruple(OperatorType.PRINT, value, None, None)
        
        return Type.VOID
        
    def visitPrintableList(self, ctx: BabyDuckParser.PrintableListContext):
        # Lista de elementos imprimibles (valor, tipo)
        printables = []
        
        # Visitar cada elemento imprimible
        for printable in ctx.printable():
            result = self.visit(printable)
            
            # Si es una expresión, su valor está en el tope de la pila
            if printable.expresion():
                value = self.quad_generator.operand_stack.pop()
                value_type = self.quad_generator.type_stack.pop()
                printables.append((value, value_type))
            # Si es una cadena, es una constante literal
            elif printable.CTE_STRING():
                value = printable.CTE_STRING().getText()
                printables.append((value, Type.VOID))  # Las cadenas no tienen un tipo específico en BabyDuck
        
        return printables
        
    def visitPrintable(self, ctx: BabyDuckParser.PrintableContext):
        # Si es una expresión, verificar su tipo
        if ctx.expresion():
            return self.visit(ctx.expresion())
        # Si es una cadena, no necesitamos verificar nada
        return None
        
    def visitCondition(self, ctx: BabyDuckParser.ConditionContext):
        # Verificar que la expresión de la condición sea booleana
        expr_type = self.visit(ctx.expresion())
        
        # Obtener la condición del tope de la pila
        condition = self.quad_generator.operand_stack.pop()
        self.quad_generator.type_stack.pop()
        
        # Generar el GOTOF para la condición
        gotof_index = self.quad_generator.generate_gotof(condition)
        self.quad_generator.jump_stack.append(gotof_index)
        
        # Visitar el cuerpo del if
        self.visit(ctx.body(0))
        
        # Si hay else
        if len(ctx.body()) > 1:
            # Generar GOTO al final del else y guardar su índice
            goto_end_index = self.quad_generator.generate_goto()
            
            # Completar el GOTOF para saltar al else
            else_quad_index = self.quad_generator.quad_counter
            self.quad_generator.fill_quadruple(gotof_index, else_quad_index)
            
            # Sacar el GOTOF de la pila de saltos (ya lo completamos)
            self.quad_generator.jump_stack.pop()
            
            # Visitar el cuerpo del else
            self.visit(ctx.body(1))
            
            # Completar el GOTO al final
            end_quad_index = self.quad_generator.quad_counter
            self.quad_generator.fill_quadruple(goto_end_index, end_quad_index)
        else:
            # No hay else, completar el GOTOF para saltar al final
            end_quad_index = self.quad_generator.quad_counter
            self.quad_generator.fill_quadruple(gotof_index, end_quad_index)
            
            # Sacar el GOTOF de la pila de saltos (ya lo completamos)
            self.quad_generator.jump_stack.pop()
            
        return Type.VOID
        
    def visitCycle(self, ctx: BabyDuckParser.CycleContext):
        # Guardar la posición de inicio del ciclo
        start_index = self.quad_generator.quad_counter
        self.quad_generator.jump_stack.append(start_index)
        
        # Verificar que la expresión del while sea booleana
        expr_type = self.visit(ctx.expresion())
        
        # Obtener la condición del tope de la pila
        condition = self.quad_generator.operand_stack.pop()
        self.quad_generator.type_stack.pop()
        
        # Generar el GOTOF para la condición
        gotof_index = self.quad_generator.generate_gotof(condition)
        self.quad_generator.jump_stack.append(gotof_index)
        
        # Visitar el cuerpo del ciclo
        self.visit(ctx.body())
        
        # Generar el GOTO al inicio del ciclo
        self.quad_generator.add_quadruple(OperatorType.GOTO, None, None, start_index)
        
        # Completar el GOTOF para saltar al final del ciclo
        end_quad_index = self.quad_generator.quad_counter
        
        # Sacar el GOTOF de la pila y completarlo
        gotof = self.quad_generator.jump_stack.pop()
        self.quad_generator.fill_quadruple(gotof, end_quad_index)
        
        # Sacar el índice de inicio del ciclo (ya no lo necesitamos)
        self.quad_generator.jump_stack.pop()
        
        return Type.VOID
        
    def visitFcall(self, ctx: BabyDuckParser.FcallContext):
        # Obtener el nombre de la función llamada
        func_name = ctx.ID().getText()
        func = self.symbol_table.lookup_function(func_name)
        
        if not func:
            self.add_error(ctx, f"Función '{func_name}' no declarada")
            return Type.ERROR
            
        # Generar ERA para la llamada a función (reserva de espacio)
        self.quad_generator.add_quadruple(OperatorType.ERA, func_name, None, None)
        
        # Verificar los argumentos
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
                
            # Procesar cada argumento
            for i, expr_ctx in enumerate(arg_list.expresion()):
                # Visitar la expresión del argumento
                arg_type = self.visit(expr_ctx)
                
                # Obtener el valor del argumento de la pila
                arg_value = self.quad_generator.operand_stack.pop()
                self.quad_generator.type_stack.pop()
                
                # Tipo esperado del parámetro
                param_type = expected_params[i].type
                
                # Verificar compatibilidad de tipos
                if arg_type != param_type and not (arg_type == Type.INT and param_type == Type.FLOAT):
                    self.add_error(expr_ctx, f"Tipo incompatible en argumento {i+1}: esperaba {param_type.name}, recibió {arg_type.name}")
                
                # Generar cuádruplo para el parámetro
                self.quad_generator.add_quadruple(OperatorType.PARAM, arg_value, None, f"param{i+1}")
                    
        # Generar GOSUB para la llamada a función
        self.quad_generator.add_quadruple(OperatorType.GOSUB, func_name, None, func.start_address)
        
        return func.type
        
    def visitArgList(self, ctx: BabyDuckParser.ArgListContext):
        # No hacemos nada aquí, los argumentos se procesan en visitFcall
        return None