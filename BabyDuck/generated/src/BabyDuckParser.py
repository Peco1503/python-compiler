# Generated from ./src/BabyDuck.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,217,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,3,0,53,8,0,1,
        0,3,0,56,8,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,4,3,68,8,3,
        11,3,12,3,69,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,80,8,5,10,5,12,
        5,83,9,5,1,6,1,6,3,6,87,8,6,1,6,1,6,1,7,4,7,92,8,7,11,7,12,7,93,
        1,8,1,8,1,8,1,8,1,8,3,8,101,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,3,10,111,8,10,1,11,1,11,1,11,5,11,116,8,11,10,11,12,11,119,9,
        11,1,12,1,12,1,12,5,12,124,8,12,10,12,12,12,127,9,12,1,13,3,13,130,
        8,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,138,8,13,1,14,1,14,1,15,
        1,15,1,15,1,15,3,15,146,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,158,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,18,4,18,171,8,18,11,18,12,18,172,1,19,1,19,1,19,
        1,19,3,19,179,8,19,1,19,1,19,1,19,3,19,184,8,19,1,19,1,19,1,19,1,
        20,1,20,1,20,5,20,192,8,20,10,20,12,20,195,9,20,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,3,22,204,8,22,1,22,1,22,1,22,1,23,1,23,1,23,5,
        23,212,8,23,10,23,12,23,215,9,23,1,23,0,0,24,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,10,11,1,
        0,21,23,1,0,17,18,1,0,19,20,1,0,14,15,216,0,48,1,0,0,0,2,61,1,0,
        0,0,4,63,1,0,0,0,6,67,1,0,0,0,8,71,1,0,0,0,10,76,1,0,0,0,12,84,1,
        0,0,0,14,91,1,0,0,0,16,100,1,0,0,0,18,102,1,0,0,0,20,107,1,0,0,0,
        22,112,1,0,0,0,24,120,1,0,0,0,26,129,1,0,0,0,28,139,1,0,0,0,30,141,
        1,0,0,0,32,150,1,0,0,0,34,161,1,0,0,0,36,170,1,0,0,0,38,174,1,0,
        0,0,40,188,1,0,0,0,42,196,1,0,0,0,44,200,1,0,0,0,46,208,1,0,0,0,
        48,49,5,1,0,0,49,50,5,13,0,0,50,52,5,25,0,0,51,53,3,4,2,0,52,51,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,56,3,36,18,0,55,54,1,0,0,
        0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,2,0,0,58,59,3,12,6,0,59,60,
        5,3,0,0,60,1,1,0,0,0,61,62,7,0,0,0,62,3,1,0,0,0,63,64,5,12,0,0,64,
        65,3,6,3,0,65,5,1,0,0,0,66,68,3,8,4,0,67,66,1,0,0,0,68,69,1,0,0,
        0,69,67,1,0,0,0,69,70,1,0,0,0,70,7,1,0,0,0,71,72,3,10,5,0,72,73,
        5,30,0,0,73,74,3,2,1,0,74,75,5,25,0,0,75,9,1,0,0,0,76,81,5,13,0,
        0,77,78,5,31,0,0,78,80,5,13,0,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,81,1,0,0,0,84,86,5,28,0,0,
        85,87,3,14,7,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,5,
        29,0,0,89,13,1,0,0,0,90,92,3,16,8,0,91,90,1,0,0,0,92,93,1,0,0,0,
        93,91,1,0,0,0,93,94,1,0,0,0,94,15,1,0,0,0,95,101,3,18,9,0,96,101,
        3,32,16,0,97,101,3,34,17,0,98,101,3,44,22,0,99,101,3,30,15,0,100,
        95,1,0,0,0,100,96,1,0,0,0,100,97,1,0,0,0,100,98,1,0,0,0,100,99,1,
        0,0,0,101,17,1,0,0,0,102,103,5,13,0,0,103,104,5,24,0,0,104,105,3,
        20,10,0,105,106,5,25,0,0,106,19,1,0,0,0,107,110,3,22,11,0,108,109,
        7,1,0,0,109,111,3,22,11,0,110,108,1,0,0,0,110,111,1,0,0,0,111,21,
        1,0,0,0,112,117,3,24,12,0,113,114,7,2,0,0,114,116,3,24,12,0,115,
        113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,
        23,1,0,0,0,119,117,1,0,0,0,120,125,3,26,13,0,121,122,7,3,0,0,122,
        124,3,26,13,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,
        126,1,0,0,0,126,25,1,0,0,0,127,125,1,0,0,0,128,130,7,2,0,0,129,128,
        1,0,0,0,129,130,1,0,0,0,130,137,1,0,0,0,131,132,5,26,0,0,132,133,
        3,20,10,0,133,134,5,27,0,0,134,138,1,0,0,0,135,138,5,13,0,0,136,
        138,3,28,14,0,137,131,1,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,
        27,1,0,0,0,139,140,7,4,0,0,140,29,1,0,0,0,141,142,5,8,0,0,142,145,
        5,26,0,0,143,146,5,16,0,0,144,146,3,20,10,0,145,143,1,0,0,0,145,
        144,1,0,0,0,146,147,1,0,0,0,147,148,5,27,0,0,148,149,5,25,0,0,149,
        31,1,0,0,0,150,151,5,4,0,0,151,152,5,26,0,0,152,153,3,20,10,0,153,
        154,5,27,0,0,154,157,3,12,6,0,155,156,5,5,0,0,156,158,3,12,6,0,157,
        155,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,25,0,0,160,
        33,1,0,0,0,161,162,5,6,0,0,162,163,5,26,0,0,163,164,3,20,10,0,164,
        165,5,27,0,0,165,166,5,7,0,0,166,167,3,12,6,0,167,168,5,25,0,0,168,
        35,1,0,0,0,169,171,3,38,19,0,170,169,1,0,0,0,171,172,1,0,0,0,172,
        170,1,0,0,0,172,173,1,0,0,0,173,37,1,0,0,0,174,175,5,9,0,0,175,176,
        5,13,0,0,176,178,5,26,0,0,177,179,3,40,20,0,178,177,1,0,0,0,178,
        179,1,0,0,0,179,180,1,0,0,0,180,181,5,27,0,0,181,183,5,25,0,0,182,
        184,3,4,2,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,
        186,3,12,6,0,186,187,5,25,0,0,187,39,1,0,0,0,188,193,3,42,21,0,189,
        190,5,31,0,0,190,192,3,42,21,0,191,189,1,0,0,0,192,195,1,0,0,0,193,
        191,1,0,0,0,193,194,1,0,0,0,194,41,1,0,0,0,195,193,1,0,0,0,196,197,
        5,13,0,0,197,198,5,30,0,0,198,199,3,2,1,0,199,43,1,0,0,0,200,201,
        5,13,0,0,201,203,5,26,0,0,202,204,3,46,23,0,203,202,1,0,0,0,203,
        204,1,0,0,0,204,205,1,0,0,0,205,206,5,27,0,0,206,207,5,25,0,0,207,
        45,1,0,0,0,208,213,3,20,10,0,209,210,5,31,0,0,210,212,3,20,10,0,
        211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,
        214,47,1,0,0,0,215,213,1,0,0,0,20,52,55,69,81,86,93,100,110,117,
        125,129,137,145,157,172,178,183,193,203,213
    ]

class BabyDuckParser ( Parser ):

    grammarFileName = "BabyDuck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'main'", "'end'", "'if'", 
                     "'else'", "'while'", "'do'", "'print'", "'void'", "'int'", 
                     "'float'", "'var'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", 
                     "'!='", "'='", "';'", "'('", "')'", "'{'", "'}'", "':'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "MAIN", "END", "IF", "ELSE", 
                      "WHILE", "DO", "PRINT", "VOID", "INT", "FLOAT", "VAR", 
                      "ID", "CTE_INT", "CTE_FLOAT", "CTE_STRING", "PLUS", 
                      "MINUS", "MULT", "DIV", "LT", "GT", "NE", "EQUAL", 
                      "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COLON", "COMMA", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_type = 1
    RULE_vars = 2
    RULE_varDecList = 3
    RULE_varDec = 4
    RULE_idList = 5
    RULE_body = 6
    RULE_statementList = 7
    RULE_statement = 8
    RULE_assign = 9
    RULE_expresion = 10
    RULE_exp = 11
    RULE_termino = 12
    RULE_factor = 13
    RULE_cte = 14
    RULE_print = 15
    RULE_condition = 16
    RULE_cycle = 17
    RULE_funcs = 18
    RULE_funcDec = 19
    RULE_paramList = 20
    RULE_param = 21
    RULE_fcall = 22
    RULE_argList = 23

    ruleNames =  [ "programa", "type", "vars", "varDecList", "varDec", "idList", 
                   "body", "statementList", "statement", "assign", "expresion", 
                   "exp", "termino", "factor", "cte", "print", "condition", 
                   "cycle", "funcs", "funcDec", "paramList", "param", "fcall", 
                   "argList" ]

    EOF = Token.EOF
    PROGRAM=1
    MAIN=2
    END=3
    IF=4
    ELSE=5
    WHILE=6
    DO=7
    PRINT=8
    VOID=9
    INT=10
    FLOAT=11
    VAR=12
    ID=13
    CTE_INT=14
    CTE_FLOAT=15
    CTE_STRING=16
    PLUS=17
    MINUS=18
    MULT=19
    DIV=20
    LT=21
    GT=22
    NE=23
    EQUAL=24
    SEMICOLON=25
    LPAREN=26
    RPAREN=27
    LBRACE=28
    RBRACE=29
    COLON=30
    COMMA=31
    WS=32
    COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(BabyDuckParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def MAIN(self):
            return self.getToken(BabyDuckParser.MAIN, 0)

        def body(self):
            return self.getTypedRuleContext(BabyDuckParser.BodyContext,0)


        def END(self):
            return self.getToken(BabyDuckParser.END, 0)

        def vars_(self):
            return self.getTypedRuleContext(BabyDuckParser.VarsContext,0)


        def funcs(self):
            return self.getTypedRuleContext(BabyDuckParser.FuncsContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = BabyDuckParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(BabyDuckParser.PROGRAM)
            self.state = 49
            self.match(BabyDuckParser.ID)
            self.state = 50
            self.match(BabyDuckParser.SEMICOLON)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 51
                self.vars_()


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 54
                self.funcs()


            self.state = 57
            self.match(BabyDuckParser.MAIN)
            self.state = 58
            self.body()
            self.state = 59
            self.match(BabyDuckParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BabyDuckParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BabyDuckParser.FLOAT, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = BabyDuckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BabyDuckParser.VAR, 0)

        def varDecList(self):
            return self.getTypedRuleContext(BabyDuckParser.VarDecListContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = BabyDuckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(BabyDuckParser.VAR)
            self.state = 64
            self.varDecList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDecListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.VarDecContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.VarDecContext,i)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_varDecList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecList" ):
                listener.enterVarDecList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecList" ):
                listener.exitVarDecList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecList" ):
                return visitor.visitVarDecList(self)
            else:
                return visitor.visitChildren(self)




    def varDecList(self):

        localctx = BabyDuckParser.VarDecListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.varDec()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(BabyDuckParser.IdListContext,0)


        def COLON(self):
            return self.getToken(BabyDuckParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(BabyDuckParser.TypeContext,0)


        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_varDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDec" ):
                listener.enterVarDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDec" ):
                listener.exitVarDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDec" ):
                return visitor.visitVarDec(self)
            else:
                return visitor.visitChildren(self)




    def varDec(self):

        localctx = BabyDuckParser.VarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.idList()
            self.state = 72
            self.match(BabyDuckParser.COLON)
            self.state = 73
            self.type_()
            self.state = 74
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.ID)
            else:
                return self.getToken(BabyDuckParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = BabyDuckParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(BabyDuckParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 77
                self.match(BabyDuckParser.COMMA)
                self.state = 78
                self.match(BabyDuckParser.ID)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(BabyDuckParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(BabyDuckParser.RBRACE, 0)

        def statementList(self):
            return self.getTypedRuleContext(BabyDuckParser.StatementListContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BabyDuckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(BabyDuckParser.LBRACE)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8528) != 0):
                self.state = 85
                self.statementList()


            self.state = 88
            self.match(BabyDuckParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.StatementContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.StatementContext,i)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = BabyDuckParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.statement()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8528) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(BabyDuckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(BabyDuckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(BabyDuckParser.CycleContext,0)


        def fcall(self):
            return self.getTypedRuleContext(BabyDuckParser.FcallContext,0)


        def print_(self):
            return self.getTypedRuleContext(BabyDuckParser.PrintContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BabyDuckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.fcall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BabyDuckParser.EQUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,0)


        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = BabyDuckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BabyDuckParser.ID)
            self.state = 103
            self.match(BabyDuckParser.EQUAL)
            self.state = 104
            self.expresion()
            self.state = 105
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.ExpContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.ExpContext,i)


        def GT(self):
            return self.getToken(BabyDuckParser.GT, 0)

        def LT(self):
            return self.getToken(BabyDuckParser.LT, 0)

        def NE(self):
            return self.getToken(BabyDuckParser.NE, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = BabyDuckParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.exp()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0):
                self.state = 108
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.TerminoContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.TerminoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.PLUS)
            else:
                return self.getToken(BabyDuckParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.MINUS)
            else:
                return self.getToken(BabyDuckParser.MINUS, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BabyDuckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.termino()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.termino()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.FactorContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.MULT)
            else:
                return self.getToken(BabyDuckParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.DIV)
            else:
                return self.getToken(BabyDuckParser.DIV, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = BabyDuckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.factor()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.factor()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(BabyDuckParser.CteContext,0)


        def PLUS(self):
            return self.getToken(BabyDuckParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BabyDuckParser.MINUS, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = BabyDuckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17 or _la==18:
                self.state = 128
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 131
                self.match(BabyDuckParser.LPAREN)
                self.state = 132
                self.expresion()
                self.state = 133
                self.match(BabyDuckParser.RPAREN)
                pass
            elif token in [13]:
                self.state = 135
                self.match(BabyDuckParser.ID)
                pass
            elif token in [14, 15]:
                self.state = 136
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_INT(self):
            return self.getToken(BabyDuckParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(BabyDuckParser.CTE_FLOAT, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCte" ):
                return visitor.visitCte(self)
            else:
                return visitor.visitChildren(self)




    def cte(self):

        localctx = BabyDuckParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BabyDuckParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def CTE_STRING(self):
            return self.getToken(BabyDuckParser.CTE_STRING, 0)

        def expresion(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = BabyDuckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BabyDuckParser.PRINT)
            self.state = 142
            self.match(BabyDuckParser.LPAREN)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 143
                self.match(BabyDuckParser.CTE_STRING)
                pass
            elif token in [13, 14, 15, 17, 18, 26]:
                self.state = 144
                self.expresion()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 147
            self.match(BabyDuckParser.RPAREN)
            self.state = 148
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BabyDuckParser.IF, 0)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.BodyContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.BodyContext,i)


        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def ELSE(self):
            return self.getToken(BabyDuckParser.ELSE, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = BabyDuckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(BabyDuckParser.IF)
            self.state = 151
            self.match(BabyDuckParser.LPAREN)
            self.state = 152
            self.expresion()
            self.state = 153
            self.match(BabyDuckParser.RPAREN)
            self.state = 154
            self.body()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 155
                self.match(BabyDuckParser.ELSE)
                self.state = 156
                self.body()


            self.state = 159
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BabyDuckParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def DO(self):
            return self.getToken(BabyDuckParser.DO, 0)

        def body(self):
            return self.getTypedRuleContext(BabyDuckParser.BodyContext,0)


        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCycle" ):
                return visitor.visitCycle(self)
            else:
                return visitor.visitChildren(self)




    def cycle(self):

        localctx = BabyDuckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(BabyDuckParser.WHILE)
            self.state = 162
            self.match(BabyDuckParser.LPAREN)
            self.state = 163
            self.expresion()
            self.state = 164
            self.match(BabyDuckParser.RPAREN)
            self.state = 165
            self.match(BabyDuckParser.DO)
            self.state = 166
            self.body()
            self.state = 167
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.FuncDecContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.FuncDecContext,i)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs" ):
                return visitor.visitFuncs(self)
            else:
                return visitor.visitChildren(self)




    def funcs(self):

        localctx = BabyDuckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 169
                self.funcDec()
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BabyDuckParser.VOID, 0)

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.SEMICOLON)
            else:
                return self.getToken(BabyDuckParser.SEMICOLON, i)

        def body(self):
            return self.getTypedRuleContext(BabyDuckParser.BodyContext,0)


        def paramList(self):
            return self.getTypedRuleContext(BabyDuckParser.ParamListContext,0)


        def vars_(self):
            return self.getTypedRuleContext(BabyDuckParser.VarsContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_funcDec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDec" ):
                listener.enterFuncDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDec" ):
                listener.exitFuncDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDec" ):
                return visitor.visitFuncDec(self)
            else:
                return visitor.visitChildren(self)




    def funcDec(self):

        localctx = BabyDuckParser.FuncDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(BabyDuckParser.VOID)
            self.state = 175
            self.match(BabyDuckParser.ID)
            self.state = 176
            self.match(BabyDuckParser.LPAREN)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 177
                self.paramList()


            self.state = 180
            self.match(BabyDuckParser.RPAREN)
            self.state = 181
            self.match(BabyDuckParser.SEMICOLON)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 182
                self.vars_()


            self.state = 185
            self.body()
            self.state = 186
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.ParamContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = BabyDuckParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.param()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 189
                self.match(BabyDuckParser.COMMA)
                self.state = 190
                self.param()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def COLON(self):
            return self.getToken(BabyDuckParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(BabyDuckParser.TypeContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BabyDuckParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(BabyDuckParser.ID)
            self.state = 197
            self.match(BabyDuckParser.COLON)
            self.state = 198
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def argList(self):
            return self.getTypedRuleContext(BabyDuckParser.ArgListContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_fcall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFcall" ):
                listener.enterFcall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFcall" ):
                listener.exitFcall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFcall" ):
                return visitor.visitFcall(self)
            else:
                return visitor.visitChildren(self)




    def fcall(self):

        localctx = BabyDuckParser.FcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(BabyDuckParser.ID)
            self.state = 201
            self.match(BabyDuckParser.LPAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67559424) != 0):
                self.state = 202
                self.argList()


            self.state = 205
            self.match(BabyDuckParser.RPAREN)
            self.state = 206
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = BabyDuckParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expresion()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 209
                self.match(BabyDuckParser.COMMA)
                self.state = 210
                self.expresion()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





