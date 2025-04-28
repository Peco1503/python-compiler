# Generated from ./src/BabyDuck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BabyDuckParser import BabyDuckParser
else:
    from BabyDuckParser import BabyDuckParser

# This class defines a complete generic visitor for a parse tree produced by BabyDuckParser.

class BabyDuckVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BabyDuckParser#programa.
    def visitPrograma(self, ctx:BabyDuckParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#type.
    def visitType(self, ctx:BabyDuckParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#vars.
    def visitVars(self, ctx:BabyDuckParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#varDecList.
    def visitVarDecList(self, ctx:BabyDuckParser.VarDecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#varDec.
    def visitVarDec(self, ctx:BabyDuckParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#idList.
    def visitIdList(self, ctx:BabyDuckParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#body.
    def visitBody(self, ctx:BabyDuckParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#statementList.
    def visitStatementList(self, ctx:BabyDuckParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#statement.
    def visitStatement(self, ctx:BabyDuckParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#assign.
    def visitAssign(self, ctx:BabyDuckParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#expresion.
    def visitExpresion(self, ctx:BabyDuckParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#exp.
    def visitExp(self, ctx:BabyDuckParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#termino.
    def visitTermino(self, ctx:BabyDuckParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#factor.
    def visitFactor(self, ctx:BabyDuckParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#cte.
    def visitCte(self, ctx:BabyDuckParser.CteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#print.
    def visitPrint(self, ctx:BabyDuckParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#condition.
    def visitCondition(self, ctx:BabyDuckParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#cycle.
    def visitCycle(self, ctx:BabyDuckParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#funcs.
    def visitFuncs(self, ctx:BabyDuckParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#funcDec.
    def visitFuncDec(self, ctx:BabyDuckParser.FuncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#paramList.
    def visitParamList(self, ctx:BabyDuckParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#param.
    def visitParam(self, ctx:BabyDuckParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#fcall.
    def visitFcall(self, ctx:BabyDuckParser.FcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#argList.
    def visitArgList(self, ctx:BabyDuckParser.ArgListContext):
        return self.visitChildren(ctx)



del BabyDuckParser