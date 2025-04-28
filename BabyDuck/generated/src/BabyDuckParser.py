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
        4,1,33,264,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,0,3,0,57,8,0,1,0,3,0,60,8,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,
        1,2,1,3,4,3,72,8,3,11,3,12,3,73,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        5,5,84,8,5,10,5,12,5,87,9,5,1,6,1,6,3,6,91,8,6,1,6,1,6,1,7,4,7,96,
        8,7,11,7,12,7,97,1,8,1,8,1,8,1,8,1,8,3,8,105,8,8,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,125,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,136,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        147,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        159,8,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,3,15,174,8,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,182,8,
        16,10,16,12,16,185,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,203,8,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,19,3,19,214,8,19,1,20,4,20,217,8,
        20,11,20,12,20,218,1,21,1,21,1,21,1,21,3,21,225,8,21,1,21,1,21,1,
        21,3,21,230,8,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,5,22,239,8,22,
        10,22,12,22,242,9,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,3,24,251,
        8,24,1,24,1,24,1,24,1,25,1,25,1,25,5,25,259,8,25,10,25,12,25,262,
        9,25,1,25,0,1,32,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,0,2,1,0,10,11,1,0,14,15,268,0,52,1,0,
        0,0,2,65,1,0,0,0,4,67,1,0,0,0,6,71,1,0,0,0,8,75,1,0,0,0,10,80,1,
        0,0,0,12,88,1,0,0,0,14,95,1,0,0,0,16,104,1,0,0,0,18,106,1,0,0,0,
        20,124,1,0,0,0,22,135,1,0,0,0,24,146,1,0,0,0,26,158,1,0,0,0,28,160,
        1,0,0,0,30,173,1,0,0,0,32,175,1,0,0,0,34,202,1,0,0,0,36,204,1,0,
        0,0,38,213,1,0,0,0,40,216,1,0,0,0,42,220,1,0,0,0,44,235,1,0,0,0,
        46,243,1,0,0,0,48,247,1,0,0,0,50,255,1,0,0,0,52,53,5,1,0,0,53,54,
        5,13,0,0,54,56,5,25,0,0,55,57,3,4,2,0,56,55,1,0,0,0,56,57,1,0,0,
        0,57,59,1,0,0,0,58,60,3,38,19,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,
        1,0,0,0,61,62,5,2,0,0,62,63,3,12,6,0,63,64,5,3,0,0,64,1,1,0,0,0,
        65,66,7,0,0,0,66,3,1,0,0,0,67,68,5,12,0,0,68,69,3,6,3,0,69,5,1,0,
        0,0,70,72,3,8,4,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,7,1,0,0,0,75,76,3,10,5,0,76,77,5,30,0,0,77,78,3,2,1,0,
        78,79,5,25,0,0,79,9,1,0,0,0,80,85,5,13,0,0,81,82,5,31,0,0,82,84,
        5,13,0,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,11,1,0,0,0,87,85,1,0,0,0,88,90,5,28,0,0,89,91,3,14,7,0,90,89,
        1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,29,0,0,93,13,1,0,0,0,
        94,96,3,16,8,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,
        0,0,0,98,15,1,0,0,0,99,105,3,18,9,0,100,105,3,34,17,0,101,105,3,
        36,18,0,102,105,3,48,24,0,103,105,3,30,15,0,104,99,1,0,0,0,104,100,
        1,0,0,0,104,101,1,0,0,0,104,102,1,0,0,0,104,103,1,0,0,0,105,17,1,
        0,0,0,106,107,5,13,0,0,107,108,5,24,0,0,108,109,3,20,10,0,109,110,
        5,25,0,0,110,19,1,0,0,0,111,125,3,22,11,0,112,113,3,22,11,0,113,
        114,5,22,0,0,114,115,3,22,11,0,115,125,1,0,0,0,116,117,3,22,11,0,
        117,118,5,21,0,0,118,119,3,22,11,0,119,125,1,0,0,0,120,121,3,22,
        11,0,121,122,5,23,0,0,122,123,3,22,11,0,123,125,1,0,0,0,124,111,
        1,0,0,0,124,112,1,0,0,0,124,116,1,0,0,0,124,120,1,0,0,0,125,21,1,
        0,0,0,126,136,3,24,12,0,127,128,3,24,12,0,128,129,5,17,0,0,129,130,
        3,22,11,0,130,136,1,0,0,0,131,132,3,24,12,0,132,133,5,18,0,0,133,
        134,3,22,11,0,134,136,1,0,0,0,135,126,1,0,0,0,135,127,1,0,0,0,135,
        131,1,0,0,0,136,23,1,0,0,0,137,147,3,26,13,0,138,139,3,26,13,0,139,
        140,5,19,0,0,140,141,3,24,12,0,141,147,1,0,0,0,142,143,3,26,13,0,
        143,144,5,20,0,0,144,145,3,24,12,0,145,147,1,0,0,0,146,137,1,0,0,
        0,146,138,1,0,0,0,146,142,1,0,0,0,147,25,1,0,0,0,148,149,5,26,0,
        0,149,150,3,20,10,0,150,151,5,27,0,0,151,159,1,0,0,0,152,153,5,17,
        0,0,153,159,3,26,13,0,154,155,5,18,0,0,155,159,3,26,13,0,156,159,
        5,13,0,0,157,159,3,28,14,0,158,148,1,0,0,0,158,152,1,0,0,0,158,154,
        1,0,0,0,158,156,1,0,0,0,158,157,1,0,0,0,159,27,1,0,0,0,160,161,7,
        1,0,0,161,29,1,0,0,0,162,163,5,8,0,0,163,164,5,26,0,0,164,165,3,
        32,16,0,165,166,5,27,0,0,166,167,5,25,0,0,167,174,1,0,0,0,168,169,
        5,8,0,0,169,170,5,26,0,0,170,171,5,16,0,0,171,172,5,27,0,0,172,174,
        5,25,0,0,173,162,1,0,0,0,173,168,1,0,0,0,174,31,1,0,0,0,175,176,
        6,16,-1,0,176,177,3,20,10,0,177,183,1,0,0,0,178,179,10,1,0,0,179,
        180,5,31,0,0,180,182,3,20,10,0,181,178,1,0,0,0,182,185,1,0,0,0,183,
        181,1,0,0,0,183,184,1,0,0,0,184,33,1,0,0,0,185,183,1,0,0,0,186,187,
        5,4,0,0,187,188,5,26,0,0,188,189,3,20,10,0,189,190,5,27,0,0,190,
        191,3,12,6,0,191,192,5,25,0,0,192,203,1,0,0,0,193,194,5,4,0,0,194,
        195,5,26,0,0,195,196,3,20,10,0,196,197,5,27,0,0,197,198,3,12,6,0,
        198,199,5,5,0,0,199,200,3,12,6,0,200,201,5,25,0,0,201,203,1,0,0,
        0,202,186,1,0,0,0,202,193,1,0,0,0,203,35,1,0,0,0,204,205,5,6,0,0,
        205,206,5,26,0,0,206,207,3,20,10,0,207,208,5,27,0,0,208,209,5,7,
        0,0,209,210,3,12,6,0,210,211,5,25,0,0,211,37,1,0,0,0,212,214,3,40,
        20,0,213,212,1,0,0,0,213,214,1,0,0,0,214,39,1,0,0,0,215,217,3,42,
        21,0,216,215,1,0,0,0,217,218,1,0,0,0,218,216,1,0,0,0,218,219,1,0,
        0,0,219,41,1,0,0,0,220,221,5,9,0,0,221,222,5,13,0,0,222,224,5,26,
        0,0,223,225,3,44,22,0,224,223,1,0,0,0,224,225,1,0,0,0,225,226,1,
        0,0,0,226,227,5,27,0,0,227,229,5,25,0,0,228,230,3,4,2,0,229,228,
        1,0,0,0,229,230,1,0,0,0,230,231,1,0,0,0,231,232,3,12,6,0,232,233,
        5,25,0,0,233,234,5,25,0,0,234,43,1,0,0,0,235,240,3,46,23,0,236,237,
        5,31,0,0,237,239,3,46,23,0,238,236,1,0,0,0,239,242,1,0,0,0,240,238,
        1,0,0,0,240,241,1,0,0,0,241,45,1,0,0,0,242,240,1,0,0,0,243,244,5,
        13,0,0,244,245,5,30,0,0,245,246,3,2,1,0,246,47,1,0,0,0,247,248,5,
        13,0,0,248,250,5,26,0,0,249,251,3,50,25,0,250,249,1,0,0,0,250,251,
        1,0,0,0,251,252,1,0,0,0,252,253,5,27,0,0,253,254,5,25,0,0,254,49,
        1,0,0,0,255,260,3,20,10,0,256,257,5,31,0,0,257,259,3,20,10,0,258,
        256,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,
        51,1,0,0,0,262,260,1,0,0,0,21,56,59,73,85,90,97,104,124,135,146,
        158,173,183,202,213,218,224,229,240,250,260
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
    RULE_expList = 16
    RULE_condition = 17
    RULE_cycle = 18
    RULE_funcs = 19
    RULE_funcList = 20
    RULE_funcDec = 21
    RULE_paramList = 22
    RULE_param = 23
    RULE_fcall = 24
    RULE_argList = 25

    ruleNames =  [ "programa", "type", "vars", "varDecList", "varDec", "idList", 
                   "body", "statementList", "statement", "assign", "expresion", 
                   "exp", "termino", "factor", "cte", "print", "expList", 
                   "condition", "cycle", "funcs", "funcList", "funcDec", 
                   "paramList", "param", "fcall", "argList" ]

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
            self.state = 52
            self.match(BabyDuckParser.PROGRAM)
            self.state = 53
            self.match(BabyDuckParser.ID)
            self.state = 54
            self.match(BabyDuckParser.SEMICOLON)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 55
                self.vars_()


            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 58
                self.funcs()


            self.state = 61
            self.match(BabyDuckParser.MAIN)
            self.state = 62
            self.body()
            self.state = 63
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
            self.state = 65
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
            self.state = 67
            self.match(BabyDuckParser.VAR)
            self.state = 68
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
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.varDec()
                self.state = 73 
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
            self.state = 75
            self.idList()
            self.state = 76
            self.match(BabyDuckParser.COLON)
            self.state = 77
            self.type_()
            self.state = 78
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
            self.state = 80
            self.match(BabyDuckParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 81
                self.match(BabyDuckParser.COMMA)
                self.state = 82
                self.match(BabyDuckParser.ID)
                self.state = 87
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
            self.state = 88
            self.match(BabyDuckParser.LBRACE)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8528) != 0):
                self.state = 89
                self.statementList()


            self.state = 92
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
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.statement()
                self.state = 97 
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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.fcall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 103
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
            self.state = 106
            self.match(BabyDuckParser.ID)
            self.state = 107
            self.match(BabyDuckParser.EQUAL)
            self.state = 108
            self.expresion()
            self.state = 109
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
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.exp()
                self.state = 113
                self.match(BabyDuckParser.GT)
                self.state = 114
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.exp()
                self.state = 117
                self.match(BabyDuckParser.LT)
                self.state = 118
                self.exp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.exp()
                self.state = 121
                self.match(BabyDuckParser.NE)
                self.state = 122
                self.exp()
                pass


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

        def termino(self):
            return self.getTypedRuleContext(BabyDuckParser.TerminoContext,0)


        def PLUS(self):
            return self.getToken(BabyDuckParser.PLUS, 0)

        def exp(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpContext,0)


        def MINUS(self):
            return self.getToken(BabyDuckParser.MINUS, 0)

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
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.termino()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.termino()
                self.state = 128
                self.match(BabyDuckParser.PLUS)
                self.state = 129
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.termino()
                self.state = 132
                self.match(BabyDuckParser.MINUS)
                self.state = 133
                self.exp()
                pass


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

        def factor(self):
            return self.getTypedRuleContext(BabyDuckParser.FactorContext,0)


        def MULT(self):
            return self.getToken(BabyDuckParser.MULT, 0)

        def termino(self):
            return self.getTypedRuleContext(BabyDuckParser.TerminoContext,0)


        def DIV(self):
            return self.getToken(BabyDuckParser.DIV, 0)

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
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.factor()
                self.state = 139
                self.match(BabyDuckParser.MULT)
                self.state = 140
                self.termino()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.factor()
                self.state = 143
                self.match(BabyDuckParser.DIV)
                self.state = 144
                self.termino()
                pass


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

        def PLUS(self):
            return self.getToken(BabyDuckParser.PLUS, 0)

        def factor(self):
            return self.getTypedRuleContext(BabyDuckParser.FactorContext,0)


        def MINUS(self):
            return self.getToken(BabyDuckParser.MINUS, 0)

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(BabyDuckParser.CteContext,0)


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
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(BabyDuckParser.LPAREN)
                self.state = 149
                self.expresion()
                self.state = 150
                self.match(BabyDuckParser.RPAREN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(BabyDuckParser.PLUS)
                self.state = 153
                self.factor()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.match(BabyDuckParser.MINUS)
                self.state = 155
                self.factor()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(BabyDuckParser.ID)
                pass
            elif token in [14, 15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 157
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
            self.state = 160
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

        def expList(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpListContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def CTE_STRING(self):
            return self.getToken(BabyDuckParser.CTE_STRING, 0)

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
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(BabyDuckParser.PRINT)
                self.state = 163
                self.match(BabyDuckParser.LPAREN)
                self.state = 164
                self.expList(0)
                self.state = 165
                self.match(BabyDuckParser.RPAREN)
                self.state = 166
                self.match(BabyDuckParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(BabyDuckParser.PRINT)
                self.state = 169
                self.match(BabyDuckParser.LPAREN)
                self.state = 170
                self.match(BabyDuckParser.CTE_STRING)
                self.state = 171
                self.match(BabyDuckParser.RPAREN)
                self.state = 172
                self.match(BabyDuckParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpresionContext,0)


        def expList(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpListContext,0)


        def COMMA(self):
            return self.getToken(BabyDuckParser.COMMA, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_expList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpList" ):
                listener.enterExpList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpList" ):
                listener.exitExpList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpList" ):
                return visitor.visitExpList(self)
            else:
                return visitor.visitChildren(self)



    def expList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BabyDuckParser.ExpListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.expresion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BabyDuckParser.ExpListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expList)
                    self.state = 178
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 179
                    self.match(BabyDuckParser.COMMA)
                    self.state = 180
                    self.expresion() 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 34, self.RULE_condition)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(BabyDuckParser.IF)
                self.state = 187
                self.match(BabyDuckParser.LPAREN)
                self.state = 188
                self.expresion()
                self.state = 189
                self.match(BabyDuckParser.RPAREN)
                self.state = 190
                self.body()
                self.state = 191
                self.match(BabyDuckParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(BabyDuckParser.IF)
                self.state = 194
                self.match(BabyDuckParser.LPAREN)
                self.state = 195
                self.expresion()
                self.state = 196
                self.match(BabyDuckParser.RPAREN)
                self.state = 197
                self.body()
                self.state = 198
                self.match(BabyDuckParser.ELSE)
                self.state = 199
                self.body()
                self.state = 200
                self.match(BabyDuckParser.SEMICOLON)
                pass


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
        self.enterRule(localctx, 36, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BabyDuckParser.WHILE)
            self.state = 205
            self.match(BabyDuckParser.LPAREN)
            self.state = 206
            self.expresion()
            self.state = 207
            self.match(BabyDuckParser.RPAREN)
            self.state = 208
            self.match(BabyDuckParser.DO)
            self.state = 209
            self.body()
            self.state = 210
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

        def funcList(self):
            return self.getTypedRuleContext(BabyDuckParser.FuncListContext,0)


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
        self.enterRule(localctx, 38, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 212
                self.funcList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncListContext(ParserRuleContext):
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
            return BabyDuckParser.RULE_funcList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncList" ):
                listener.enterFuncList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncList" ):
                listener.exitFuncList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncList" ):
                return visitor.visitFuncList(self)
            else:
                return visitor.visitChildren(self)




    def funcList(self):

        localctx = BabyDuckParser.FuncListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 215
                self.funcDec()
                self.state = 218 
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
        self.enterRule(localctx, 42, self.RULE_funcDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BabyDuckParser.VOID)
            self.state = 221
            self.match(BabyDuckParser.ID)
            self.state = 222
            self.match(BabyDuckParser.LPAREN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 223
                self.paramList()


            self.state = 226
            self.match(BabyDuckParser.RPAREN)
            self.state = 227
            self.match(BabyDuckParser.SEMICOLON)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 228
                self.vars_()


            self.state = 231
            self.body()
            self.state = 232
            self.match(BabyDuckParser.SEMICOLON)
            self.state = 233
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
        self.enterRule(localctx, 44, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.param()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 236
                self.match(BabyDuckParser.COMMA)
                self.state = 237
                self.param()
                self.state = 242
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
        self.enterRule(localctx, 46, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(BabyDuckParser.ID)
            self.state = 244
            self.match(BabyDuckParser.COLON)
            self.state = 245
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
        self.enterRule(localctx, 48, self.RULE_fcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BabyDuckParser.ID)
            self.state = 248
            self.match(BabyDuckParser.LPAREN)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67559424) != 0):
                self.state = 249
                self.argList()


            self.state = 252
            self.match(BabyDuckParser.RPAREN)
            self.state = 253
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
        self.enterRule(localctx, 50, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.expresion()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 256
                self.match(BabyDuckParser.COMMA)
                self.state = 257
                self.expresion()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expList_sempred(self, localctx:ExpListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




