# Generated from ./src/BabyDuck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BabyDuckParser import BabyDuckParser
else:
    from BabyDuckParser import BabyDuckParser

# This class defines a complete listener for a parse tree produced by BabyDuckParser.
class BabyDuckListener(ParseTreeListener):

    # Enter a parse tree produced by BabyDuckParser#programa.
    def enterPrograma(self, ctx:BabyDuckParser.ProgramaContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#programa.
    def exitPrograma(self, ctx:BabyDuckParser.ProgramaContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#type.
    def enterType(self, ctx:BabyDuckParser.TypeContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#type.
    def exitType(self, ctx:BabyDuckParser.TypeContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#vars.
    def enterVars(self, ctx:BabyDuckParser.VarsContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#vars.
    def exitVars(self, ctx:BabyDuckParser.VarsContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#varDecList.
    def enterVarDecList(self, ctx:BabyDuckParser.VarDecListContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#varDecList.
    def exitVarDecList(self, ctx:BabyDuckParser.VarDecListContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#varDec.
    def enterVarDec(self, ctx:BabyDuckParser.VarDecContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#varDec.
    def exitVarDec(self, ctx:BabyDuckParser.VarDecContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#idList.
    def enterIdList(self, ctx:BabyDuckParser.IdListContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#idList.
    def exitIdList(self, ctx:BabyDuckParser.IdListContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#body.
    def enterBody(self, ctx:BabyDuckParser.BodyContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#body.
    def exitBody(self, ctx:BabyDuckParser.BodyContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#statementList.
    def enterStatementList(self, ctx:BabyDuckParser.StatementListContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#statementList.
    def exitStatementList(self, ctx:BabyDuckParser.StatementListContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#statement.
    def enterStatement(self, ctx:BabyDuckParser.StatementContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#statement.
    def exitStatement(self, ctx:BabyDuckParser.StatementContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#assign.
    def enterAssign(self, ctx:BabyDuckParser.AssignContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#assign.
    def exitAssign(self, ctx:BabyDuckParser.AssignContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#expresion.
    def enterExpresion(self, ctx:BabyDuckParser.ExpresionContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#expresion.
    def exitExpresion(self, ctx:BabyDuckParser.ExpresionContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#exp.
    def enterExp(self, ctx:BabyDuckParser.ExpContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#exp.
    def exitExp(self, ctx:BabyDuckParser.ExpContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#termino.
    def enterTermino(self, ctx:BabyDuckParser.TerminoContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#termino.
    def exitTermino(self, ctx:BabyDuckParser.TerminoContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#factor.
    def enterFactor(self, ctx:BabyDuckParser.FactorContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#factor.
    def exitFactor(self, ctx:BabyDuckParser.FactorContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#cte.
    def enterCte(self, ctx:BabyDuckParser.CteContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#cte.
    def exitCte(self, ctx:BabyDuckParser.CteContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#print.
    def enterPrint(self, ctx:BabyDuckParser.PrintContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#print.
    def exitPrint(self, ctx:BabyDuckParser.PrintContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#condition.
    def enterCondition(self, ctx:BabyDuckParser.ConditionContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#condition.
    def exitCondition(self, ctx:BabyDuckParser.ConditionContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#cycle.
    def enterCycle(self, ctx:BabyDuckParser.CycleContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#cycle.
    def exitCycle(self, ctx:BabyDuckParser.CycleContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#funcs.
    def enterFuncs(self, ctx:BabyDuckParser.FuncsContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#funcs.
    def exitFuncs(self, ctx:BabyDuckParser.FuncsContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#funcDec.
    def enterFuncDec(self, ctx:BabyDuckParser.FuncDecContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#funcDec.
    def exitFuncDec(self, ctx:BabyDuckParser.FuncDecContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#paramList.
    def enterParamList(self, ctx:BabyDuckParser.ParamListContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#paramList.
    def exitParamList(self, ctx:BabyDuckParser.ParamListContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#param.
    def enterParam(self, ctx:BabyDuckParser.ParamContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#param.
    def exitParam(self, ctx:BabyDuckParser.ParamContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#fcall.
    def enterFcall(self, ctx:BabyDuckParser.FcallContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#fcall.
    def exitFcall(self, ctx:BabyDuckParser.FcallContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#argList.
    def enterArgList(self, ctx:BabyDuckParser.ArgListContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#argList.
    def exitArgList(self, ctx:BabyDuckParser.ArgListContext):
        pass



del BabyDuckParser