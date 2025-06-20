from antlr4 import *
from generated.src.BabyDuckParser import BabyDuckParser
from generated.src.BabyDuckVisitor import BabyDuckVisitor
from semantic_cube import get_result_type, INT, FLOAT, ERROR
from symbol_table import SymbolTable, Type, Variable, Function
from quad_generator import QuadrupleGenerator, OperatorType
from memory_manager import SegmentType, DataType
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
        self.errors.append(f"Error semántico en línea {line}:{column} - {message}")

    def visitPrograma(self, ctx: BabyDuckParser.ProgramaContext):
        # Establecer el contexto global para variables globales
        program_name = ctx.ID().getText()
        self.symbol_table.add_function(program_name, Type.VOID)
        self.symbol_table.current_function = program_name  # Establecer como función actual para variables globales
        self.quad_generator.set_current_function("global")

        # Añadir función main implícitamente - DEBE HACERSE AQUÍ
        # Guardar el contexto actual antes de agregar main
        saved_context = self.symbol_table.current_function
        self.symbol_table.add_function("main", Type.VOID)
        # Restaurar el contexto para procesar variables globales
        self.symbol_table.current_function = saved_context

        # Procesar variables globales si existen (en contexto del programa)
        if ctx.vars_():
            self.visit(ctx.vars_())

        # Generar cuádruplo de GOTO para saltar a main (lo completaremos después)
        main_jump = self.quad_generator.generate_goto()

        # Procesar las declaraciones de funciones si existen
        if ctx.funcs():
            self.visit(ctx.funcs())

        # Cambiar a la función main para el cuerpo principal
        self.symbol_table.current_function = "main"
        self.quad_generator.set_current_function("main")

        # Guardar la dirección de inicio de main
        main_start = self.quad_generator.quad_counter

        # Ahora podemos acceder a la función main porque ya la hemos añadido
        self.symbol_table.functions["main"].start_address = main_start

        # Completar el cuádruplo de salto a main
        self.quad_generator.fill_quadruple(main_jump, main_start)

        # Visitar el cuerpo principal
        self.visit(ctx.body())

        # Generar cuádruplo de fin de programa (ENDFUNC para main)
        self.quad_generator.generate_endfunc()

        # Retornar tanto la tabla de símbolos como los cuádruplos generados
        return self.symbol_table, self.quad_generator.quadruples
    
    def visitVars(self, ctx: BabyDuckParser.VarsContext):
        # Visitar las declaraciones de variables
        return self.visit(ctx.varDecList())
    
    def visitVarDecList(self, ctx: BabyDuckParser.VarDecListContext):
        # Visitar cada declaración de variable
        for var_dec in ctx.varDec():
            self.visit(var_dec)
        return None
    
    def visitVarDec(self, ctx: BabyDuckParser.VarDecContext):
        # Obtener el tipo de la variable
        type_ctx = ctx.type_()
        var_type = Type.INT if type_ctx.INT() else Type.FLOAT

        # Obtener los IDs y añadir cada variable a la tabla
        id_list = ctx.idList()

        # Determinar si es global: las variables son globales si no estamos en main ni en una función específica
        # Las variables globales se declaran cuando current_function es el nombre del programa
        current_func = self.symbol_table.current_function

        # Simplificar: es global si no estamos en main
        is_global = current_func != "main"

        # Mapear Type a DataType para la asignación de memoria
        data_type = DataType.INT if var_type == Type.INT else DataType.FLOAT
        segment_type = SegmentType.GLOBAL if is_global else SegmentType.LOCAL

        for id_token in id_list.ID():
            var_name = id_token.getText()
            if not self.symbol_table.add_variable(var_name, var_type, is_global):
                self.add_error(ctx, f"La variable '{var_name}' ya ha sido declarada.")
                continue

            # Asignar dirección virtual a la variable
            address = self.quad_generator.memory_manager.get_address(segment_type, data_type)

            # Asociar la variable con su dirección
            self.quad_generator.set_var_address(var_name, address)

            # Actualizar la dirección en la tabla de símbolos
            var = self.symbol_table.lookup_variable(var_name)
            if var:
                var.address = address

        return None
    
    def visitFuncs(self, ctx: BabyDuckParser.FuncsContext):
        # Visitar cada declaración de función
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
        
        # Establecer la función actual
        self.symbol_table.current_function = func_name
        self.quad_generator.set_current_function(func_name)
            
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
        self.quad_generator.generate_endfunc()
        
        # Actualizar el número de variables locales y temporales usadas en la función
        func = self.symbol_table.functions[func_name]
        func.local_vars_count = len(func.vars_table)
        func.temp_vars_count = self.quad_generator.memory_manager.temp_counter

        if func.start_address != func_start:
            print(f"Advertencia: La direccion de inicio para la funcion '{func_name}' cambió de {func_start} a {func.start_address}")
            func.start_address = func_start
        
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
        
        # Mapear Type a DataType para la asignación de memoria
        data_type = DataType.INT if param_type == Type.INT else DataType.FLOAT
        
        # Añadir el parámetro a la función actual
        if not self.symbol_table.add_param(param_name, param_type):
            self.add_error(ctx, f"Parámetro '{param_name}' ya declarado en la función")
            return None
            
        # Asignar dirección virtual al parámetro (como variable local)
        address = self.quad_generator.memory_manager.get_address(SegmentType.LOCAL, data_type)
        
        # Asociar el parámetro con su dirección
        self.quad_generator.set_var_address(param_name, address)
        
        # Actualizar la dirección en la tabla de símbolos
        var = self.symbol_table.lookup_variable(param_name)
        if var:
            var.address = address
            
        return None
    
    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Obtener el identificador al que se asigna
        var_name = ctx.ID().getText()
        var = self.symbol_table.lookup_variable(var_name)

        if not var:
            self.add_error(ctx, f"Variable '{var_name}' no declarada.")
            return Type.ERROR
        
        # Obtener la dirección virtual de la variable
        var_address = self.quad_generator.get_var_address(var_name)
        if var_address is None:
            self.add_error(ctx, f"No se encontró dirección para variable '{var_name}'.")
            return Type.ERROR
        
        # Añadir la variable a la pila de operandos y tipos
        self.quad_generator.operand_stack.append(var_address)
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
        # Visitar la primera expresión
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
            
            return Type.VOID  # Para operaciones relacionales usamos Type.VOID como marcador booleano
        
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
                    operand_type = self.quad_generator.type_stack.pop()
                    
                    # Obtener dirección para la constante 0
                    zero_address = self.quad_generator.get_constant_address(0)
                    
                    # Generar temporal para el valor negado
                    temp_address = self.quad_generator.get_temp_address(operand_type)
                    
                    # Añadir cuádruplo para la negación
                    self.quad_generator.add_quadruple(OperatorType.MINUS, zero_address, operand, temp_address)
                    
                    # Añadir a las pilas
                    self.quad_generator.operand_stack.append(temp_address)
                    self.quad_generator.type_stack.append(operand_type)
                
                return result_type
            
            # Si es un ID
            elif ctx.ID():
                var_name = ctx.ID().getText()
                var = self.symbol_table.lookup_variable(var_name)
                
                if not var:
                    self.add_error(ctx, f"Variable '{var_name}' no declarada")
                    return Type.ERROR
                
                # Obtener dirección virtual
                var_address = self.quad_generator.get_var_address(var_name)
                if var_address is None:
                    self.add_error(ctx, f"No se encontró dirección para variable '{var_name}'.")
                    return Type.ERROR
                
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(var_address)
                self.quad_generator.type_stack.append(var.type)
                
                # Si hay un signo negativo, negar el valor
                if has_unary_minus:
                    operand = self.quad_generator.operand_stack.pop()
                    operand_type = self.quad_generator.type_stack.pop()
                    
                    # Obtener dirección para la constante 0
                    zero_address = self.quad_generator.get_constant_address(0)
                    
                    # Generar temporal para el valor negado
                    temp_address = self.quad_generator.get_temp_address(operand_type)
                    
                    # Añadir cuádruplo para la negación
                    self.quad_generator.add_quadruple(OperatorType.MINUS, zero_address, operand, temp_address)
                    
                    # Añadir a las pilas
                    self.quad_generator.operand_stack.append(temp_address)
                    self.quad_generator.type_stack.append(operand_type)
                
                return var.type
            
            # Si es una constante
            elif ctx.cte():
                cte_type = self.visit(ctx.cte())
                cte_text = ctx.cte().getText()
                
                # Convertir texto a valor numérico
                if cte_type == Type.INT:
                    cte_val = int(cte_text)
                else:  # Type.FLOAT
                    cte_val = float(cte_text)
                
                # Obtener dirección para la constante
                cte_address = self.quad_generator.get_constant_address(cte_val)
                
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(cte_address)
                self.quad_generator.type_stack.append(cte_type)
                
                # Si hay un signo negativo, negar el valor
                if has_unary_minus:
                    operand = self.quad_generator.operand_stack.pop()
                    operand_type = self.quad_generator.type_stack.pop()
                    
                    # Obtener dirección para la constante 0
                    zero_address = self.quad_generator.get_constant_address(0)
                    
                    # Generar temporal para el valor negado
                    temp_address = self.quad_generator.get_temp_address(operand_type)
                    
                    # Añadir cuádruplo para la negación
                    self.quad_generator.add_quadruple(OperatorType.MINUS, zero_address, operand, temp_address)
                    
                    # Añadir a las pilas
                    self.quad_generator.operand_stack.append(temp_address)
                    self.quad_generator.type_stack.append(operand_type)
                
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
                
                # Obtener dirección virtual
                var_address = self.quad_generator.get_var_address(var_name)
                if var_address is None:
                    self.add_error(ctx, f"No se encontró dirección para variable '{var_name}'.")
                    return Type.ERROR
                    
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(var_address)
                self.quad_generator.type_stack.append(var.type)
                
                return var.type
                
            # Si es una constante
            elif ctx.cte():
                cte_type = self.visit(ctx.cte())
                cte_text = ctx.cte().getText()
                
                # Convertir texto a valor numérico
                if cte_type == Type.INT:
                    cte_val = int(cte_text)
                else:  # Type.FLOAT
                    cte_val = float(cte_text)
                
                # Obtener dirección para la constante
                cte_address = self.quad_generator.get_constant_address(cte_val)
                
                # Añadir a las pilas
                self.quad_generator.operand_stack.append(cte_address)
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
        for value_address, value_type in printable_list:
            self.quad_generator.add_quadruple(OperatorType.PRINT, value_address, None, None)
        
        return Type.VOID
        
    def visitPrintableList(self, ctx: BabyDuckParser.PrintableListContext):
        # Lista de elementos imprimibles (valor, tipo)
        printables = []

        # Visitar cada elemento imprimible
        for printable in ctx.printable():
            # Si es una expresión, procesarla y obtener su valor de la pila
            if printable.expresion():
                expr_type = self.visit(printable.expresion())

                # Verificar que la pila no esté vacía antes de hacer pop
                if not self.quad_generator.operand_stack:
                    self.add_error(printable, "Error interno: pila de operandos vacía al procesar expresión en print")
                    continue

                value_address = self.quad_generator.operand_stack.pop()
                value_type = self.quad_generator.type_stack.pop()
                printables.append((value_address, value_type))

            # Si es una cadena, es una constante literal
            elif printable.CTE_STRING():
                value = printable.CTE_STRING().getText()
                # Obtener dirección para la constante string
                value_address = self.quad_generator.get_constant_address(value)
                printables.append((value_address, Type.VOID))  # Las cadenas no tienen un tipo específico en BabyDuck

        return printables

    def visitPrintable(self, ctx: BabyDuckParser.PrintableContext):
        # Este método ya no se usa directamente, la lógica se movió a visitPrintableList
        # para evitar el doble procesamiento que causaba el error de pila vacía
        if ctx.expresion():
            return self.visit(ctx.expresion())
        return None
        
    def visitCondition(self, ctx: BabyDuckParser.ConditionContext):
        # Visitar la expresión de la condición
        expr_type = self.visit(ctx.expresion())
        
        # Para condiciones, se espera que el tipo resultante sea "booleano" (representado por Type.VOID)
        if expr_type != Type.VOID:
            self.add_error(ctx, f"Se esperaba una expresión booleana en la condición, se encontró {expr_type.name}")
        
        # Obtener la condición del tope de la pila
        condition_address = self.quad_generator.operand_stack.pop()
        self.quad_generator.type_stack.pop()
        
        # Generar el GOTOF para la condición
        gotof_index = self.quad_generator.generate_gotof(condition_address)
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
            
            # Añadir el GOTO al final a la pila de saltos
            self.quad_generator.jump_stack.append(goto_end_index)
            
            # Visitar el cuerpo del else
            self.visit(ctx.body(1))
            
            # Completar el GOTO al final
            end_quad_index = self.quad_generator.quad_counter
            self.quad_generator.fill_quadruple(goto_end_index, end_quad_index)
            
            # Sacar el GOTO de la pila de saltos
            self.quad_generator.jump_stack.pop()
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
        
        # Visitar la expresión del while (debe ser "booleana")
        expr_type = self.visit(ctx.expresion())
        
        # Para condiciones de ciclos, se espera que el tipo resultante sea "booleano"
        if expr_type != Type.VOID:
            self.add_error(ctx, f"Se esperaba una expresión booleana en la condición del ciclo, se encontró {expr_type.name}")
        
        # Obtener la condición del tope de la pila
        condition_address = self.quad_generator.operand_stack.pop()
        self.quad_generator.type_stack.pop()
        
        # Generar el GOTOF para la condición
        gotof_index = self.quad_generator.generate_gotof(condition_address)
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
        self.quad_generator.generate_era(func_name)
        
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
                arg_address = self.quad_generator.operand_stack.pop()
                self.quad_generator.type_stack.pop()
                
                # Tipo esperado del parámetro
                param_type = expected_params[i].type
                
                # Verificar compatibilidad de tipos
                if arg_type != param_type and not (arg_type == Type.INT and param_type == Type.FLOAT):
                    self.add_error(expr_ctx, f"Tipo incompatible en argumento {i+1}: esperaba {param_type.name}, recibió {arg_type.name}")
                
                # Generar cuádruplo para el parámetro
                self.quad_generator.generate_param(arg_address, i+1)
                    
        # Generar GOSUB para la llamada a función
        self.quad_generator.generate_gosub(func_name, func.start_address)
        
        return func.type
        
    def visitArgList(self, ctx: BabyDuckParser.ArgListContext):
        # No hacemos nada aquí, los argumentos se procesan en visitFcall
        return None