// Generated from /Users/francoelugo/Documents/8vo/python-compiler/BabyDuck/src/BabyDuck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BabyDuckParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAM=1, MAIN=2, END=3, IF=4, ELSE=5, WHILE=6, DO=7, PRINT=8, VOID=9, 
		INT=10, FLOAT=11, VAR=12, ID=13, CTE_INT=14, CTE_FLOAT=15, CTE_STRING=16, 
		PLUS=17, MINUS=18, MULT=19, DIV=20, LT=21, GT=22, LE=23, GE=24, EQ=25, 
		NE=26, EQUAL=27, SEMICOLON=28, LPAREN=29, RPAREN=30, LBRACE=31, RBRACE=32, 
		COLON=33, COMMA=34, WS=35, COMMENT=36;
	public static final int
		RULE_programa = 0, RULE_type = 1, RULE_vars = 2, RULE_varDecList = 3, 
		RULE_varDec = 4, RULE_idList = 5, RULE_body = 6, RULE_statementList = 7, 
		RULE_statement = 8, RULE_assign = 9, RULE_expresion = 10, RULE_exp = 11, 
		RULE_termino = 12, RULE_factor = 13, RULE_cte = 14, RULE_print = 15, RULE_printableList = 16, 
		RULE_printable = 17, RULE_condition = 18, RULE_cycle = 19, RULE_funcs = 20, 
		RULE_funcDec = 21, RULE_paramList = 22, RULE_param = 23, RULE_fcall = 24, 
		RULE_argList = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "type", "vars", "varDecList", "varDec", "idList", "body", 
			"statementList", "statement", "assign", "expresion", "exp", "termino", 
			"factor", "cte", "print", "printableList", "printable", "condition", 
			"cycle", "funcs", "funcDec", "paramList", "param", "fcall", "argList"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'main'", "'end'", "'if'", "'else'", "'while'", "'do'", 
			"'print'", "'void'", "'int'", "'float'", "'var'", null, null, null, null, 
			"'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
			"'='", "';'", "'('", "')'", "'{'", "'}'", "':'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "MAIN", "END", "IF", "ELSE", "WHILE", "DO", "PRINT", 
			"VOID", "INT", "FLOAT", "VAR", "ID", "CTE_INT", "CTE_FLOAT", "CTE_STRING", 
			"PLUS", "MINUS", "MULT", "DIV", "LT", "GT", "LE", "GE", "EQ", "NE", "EQUAL", 
			"SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "COMMA", 
			"WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BabyDuck.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BabyDuckParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(BabyDuckParser.PROGRAM, 0); }
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public TerminalNode MAIN() { return getToken(BabyDuckParser.MAIN, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode END() { return getToken(BabyDuckParser.END, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(PROGRAM);
			setState(53);
			match(ID);
			setState(54);
			match(SEMICOLON);
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(55);
				vars();
				}
			}

			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VOID) {
				{
				setState(58);
				funcs();
				}
			}

			setState(61);
			match(MAIN);
			setState(62);
			body();
			setState(63);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BabyDuckParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(BabyDuckParser.FLOAT, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BabyDuckParser.VAR, 0); }
		public VarDecListContext varDecList() {
			return getRuleContext(VarDecListContext.class,0);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(VAR);
			setState(68);
			varDecList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDecListContext extends ParserRuleContext {
		public List<VarDecContext> varDec() {
			return getRuleContexts(VarDecContext.class);
		}
		public VarDecContext varDec(int i) {
			return getRuleContext(VarDecContext.class,i);
		}
		public VarDecListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecList; }
	}

	public final VarDecListContext varDecList() throws RecognitionException {
		VarDecListContext _localctx = new VarDecListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_varDecList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(70);
				varDec();
				}
				}
				setState(73); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDecContext extends ParserRuleContext {
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public TerminalNode COLON() { return getToken(BabyDuckParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public VarDecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDec; }
	}

	public final VarDecContext varDec() throws RecognitionException {
		VarDecContext _localctx = new VarDecContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_varDec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			idList();
			setState(76);
			match(COLON);
			setState(77);
			type();
			setState(78);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdListContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(BabyDuckParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BabyDuckParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public IdListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idList; }
	}

	public final IdListContext idList() throws RecognitionException {
		IdListContext _localctx = new IdListContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_idList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(ID);
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(81);
				match(COMMA);
				setState(82);
				match(ID);
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(BabyDuckParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(BabyDuckParser.RBRACE, 0); }
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(LBRACE);
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8528L) != 0)) {
				{
				setState(89);
				statementList();
				}
			}

			setState(92);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementListContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public StatementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementList; }
	}

	public final StatementListContext statementList() throws RecognitionException {
		StatementListContext _localctx = new StatementListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_statementList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(94);
				statement();
				}
				}
				setState(97); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 8528L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public FcallContext fcall() {
			return getRuleContext(FcallContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statement);
		try {
			setState(104);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(99);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(100);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(101);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(102);
				fcall();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(103);
				print();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(BabyDuckParser.EQUAL, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(ID);
			setState(107);
			match(EQUAL);
			setState(108);
			expresion();
			setState(109);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode GT() { return getToken(BabyDuckParser.GT, 0); }
		public TerminalNode LT() { return getToken(BabyDuckParser.LT, 0); }
		public TerminalNode NE() { return getToken(BabyDuckParser.NE, 0); }
		public TerminalNode LE() { return getToken(BabyDuckParser.LE, 0); }
		public TerminalNode GE() { return getToken(BabyDuckParser.GE, 0); }
		public TerminalNode EQ() { return getToken(BabyDuckParser.EQ, 0); }
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			exp();
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 132120576L) != 0)) {
				{
				setState(112);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 132120576L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(113);
				exp();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(BabyDuckParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(BabyDuckParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(BabyDuckParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(BabyDuckParser.MINUS, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			termino();
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(117);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(118);
				termino();
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(BabyDuckParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(BabyDuckParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(BabyDuckParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(BabyDuckParser.DIV, i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			factor();
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(125);
				_la = _input.LA(1);
				if ( !(_la==MULT || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(126);
				factor();
				}
				}
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(BabyDuckParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(BabyDuckParser.MINUS, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PLUS || _la==MINUS) {
				{
				setState(132);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(141);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				{
				setState(135);
				match(LPAREN);
				setState(136);
				expresion();
				setState(137);
				match(RPAREN);
				}
				break;
			case ID:
				{
				setState(139);
				match(ID);
				}
				break;
			case CTE_INT:
			case CTE_FLOAT:
				{
				setState(140);
				cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode CTE_INT() { return getToken(BabyDuckParser.CTE_INT, 0); }
		public TerminalNode CTE_FLOAT() { return getToken(BabyDuckParser.CTE_FLOAT, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			_la = _input.LA(1);
			if ( !(_la==CTE_INT || _la==CTE_FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(BabyDuckParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public PrintableListContext printableList() {
			return getRuleContext(PrintableListContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(PRINT);
			setState(146);
			match(LPAREN);
			setState(147);
			printableList();
			setState(148);
			match(RPAREN);
			setState(149);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintableListContext extends ParserRuleContext {
		public List<PrintableContext> printable() {
			return getRuleContexts(PrintableContext.class);
		}
		public PrintableContext printable(int i) {
			return getRuleContext(PrintableContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public PrintableListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printableList; }
	}

	public final PrintableListContext printableList() throws RecognitionException {
		PrintableListContext _localctx = new PrintableListContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_printableList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			printable();
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(152);
				match(COMMA);
				setState(153);
				printable();
				}
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintableContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CTE_STRING() { return getToken(BabyDuckParser.CTE_STRING, 0); }
		public PrintableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printable; }
	}

	public final PrintableContext printable() throws RecognitionException {
		PrintableContext _localctx = new PrintableContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_printable);
		try {
			setState(161);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case CTE_INT:
			case CTE_FLOAT:
			case PLUS:
			case MINUS:
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				expresion();
				}
				break;
			case CTE_STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				match(CTE_STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BabyDuckParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public TerminalNode ELSE() { return getToken(BabyDuckParser.ELSE, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(IF);
			setState(164);
			match(LPAREN);
			setState(165);
			expresion();
			setState(166);
			match(RPAREN);
			setState(167);
			body();
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(168);
				match(ELSE);
				setState(169);
				body();
				}
			}

			setState(172);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BabyDuckParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode DO() { return getToken(BabyDuckParser.DO, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(WHILE);
			setState(175);
			match(LPAREN);
			setState(176);
			expresion();
			setState(177);
			match(RPAREN);
			setState(178);
			match(DO);
			setState(179);
			body();
			setState(180);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public List<FuncDecContext> funcDec() {
			return getRuleContexts(FuncDecContext.class);
		}
		public FuncDecContext funcDec(int i) {
			return getRuleContext(FuncDecContext.class,i);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(182);
				funcDec();
				}
				}
				setState(185); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VOID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncDecContext extends ParserRuleContext {
		public TerminalNode VOID() { return getToken(BabyDuckParser.VOID, 0); }
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(BabyDuckParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(BabyDuckParser.SEMICOLON, i);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncDecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcDec; }
	}

	public final FuncDecContext funcDec() throws RecognitionException {
		FuncDecContext _localctx = new FuncDecContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_funcDec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(VOID);
			setState(188);
			match(ID);
			setState(189);
			match(LPAREN);
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(190);
				paramList();
				}
			}

			setState(193);
			match(RPAREN);
			setState(194);
			match(SEMICOLON);
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(195);
				vars();
				}
			}

			setState(198);
			body();
			setState(199);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamListContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			param();
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(202);
				match(COMMA);
				setState(203);
				param();
				}
				}
				setState(208);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode COLON() { return getToken(BabyDuckParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(ID);
			setState(210);
			match(COLON);
			setState(211);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FcallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public FcallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fcall; }
	}

	public final FcallContext fcall() throws RecognitionException {
		FcallContext _localctx = new FcallContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_fcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(ID);
			setState(214);
			match(LPAREN);
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 537321472L) != 0)) {
				{
				setState(215);
				argList();
				}
			}

			setState(218);
			match(RPAREN);
			setState(219);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgListContext extends ParserRuleContext {
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			expresion();
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(222);
				match(COMMA);
				setState(223);
				expresion();
				}
				}
				setState(228);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u00e6\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0003\u00009\b\u0000\u0001\u0000\u0003\u0000<\b\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0004\u0003H\b\u0003\u000b\u0003\f\u0003"+
		"I\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0005\u0005T\b\u0005\n\u0005\f\u0005W\t\u0005"+
		"\u0001\u0006\u0001\u0006\u0003\u0006[\b\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0004\u0007`\b\u0007\u000b\u0007\f\u0007a\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0003\bi\b\b\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\n\u0003\ns\b\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0005\u000bx\b\u000b\n\u000b\f\u000b{\t\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0005\f\u0080\b\f\n\f\f\f\u0083\t\f\u0001\r\u0003\r\u0086\b"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u008e\b\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u009b"+
		"\b\u0010\n\u0010\f\u0010\u009e\t\u0010\u0001\u0011\u0001\u0011\u0003\u0011"+
		"\u00a2\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0003\u0012\u00ab\b\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0004\u0014\u00b8\b\u0014\u000b\u0014"+
		"\f\u0014\u00b9\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015"+
		"\u00c0\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00c5\b"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0005\u0016\u00cd\b\u0016\n\u0016\f\u0016\u00d0\t\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u00d9\b\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0005\u0019\u00e1\b\u0019\n\u0019\f\u0019\u00e4"+
		"\t\u0019\u0001\u0019\u0000\u0000\u001a\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02\u0000\u0005"+
		"\u0001\u0000\n\u000b\u0001\u0000\u0015\u001a\u0001\u0000\u0011\u0012\u0001"+
		"\u0000\u0013\u0014\u0001\u0000\u000e\u000f\u00e4\u00004\u0001\u0000\u0000"+
		"\u0000\u0002A\u0001\u0000\u0000\u0000\u0004C\u0001\u0000\u0000\u0000\u0006"+
		"G\u0001\u0000\u0000\u0000\bK\u0001\u0000\u0000\u0000\nP\u0001\u0000\u0000"+
		"\u0000\fX\u0001\u0000\u0000\u0000\u000e_\u0001\u0000\u0000\u0000\u0010"+
		"h\u0001\u0000\u0000\u0000\u0012j\u0001\u0000\u0000\u0000\u0014o\u0001"+
		"\u0000\u0000\u0000\u0016t\u0001\u0000\u0000\u0000\u0018|\u0001\u0000\u0000"+
		"\u0000\u001a\u0085\u0001\u0000\u0000\u0000\u001c\u008f\u0001\u0000\u0000"+
		"\u0000\u001e\u0091\u0001\u0000\u0000\u0000 \u0097\u0001\u0000\u0000\u0000"+
		"\"\u00a1\u0001\u0000\u0000\u0000$\u00a3\u0001\u0000\u0000\u0000&\u00ae"+
		"\u0001\u0000\u0000\u0000(\u00b7\u0001\u0000\u0000\u0000*\u00bb\u0001\u0000"+
		"\u0000\u0000,\u00c9\u0001\u0000\u0000\u0000.\u00d1\u0001\u0000\u0000\u0000"+
		"0\u00d5\u0001\u0000\u0000\u00002\u00dd\u0001\u0000\u0000\u000045\u0005"+
		"\u0001\u0000\u000056\u0005\r\u0000\u000068\u0005\u001c\u0000\u000079\u0003"+
		"\u0004\u0002\u000087\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u0000"+
		"9;\u0001\u0000\u0000\u0000:<\u0003(\u0014\u0000;:\u0001\u0000\u0000\u0000"+
		";<\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=>\u0005\u0002\u0000"+
		"\u0000>?\u0003\f\u0006\u0000?@\u0005\u0003\u0000\u0000@\u0001\u0001\u0000"+
		"\u0000\u0000AB\u0007\u0000\u0000\u0000B\u0003\u0001\u0000\u0000\u0000"+
		"CD\u0005\f\u0000\u0000DE\u0003\u0006\u0003\u0000E\u0005\u0001\u0000\u0000"+
		"\u0000FH\u0003\b\u0004\u0000GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000"+
		"\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J\u0007\u0001"+
		"\u0000\u0000\u0000KL\u0003\n\u0005\u0000LM\u0005!\u0000\u0000MN\u0003"+
		"\u0002\u0001\u0000NO\u0005\u001c\u0000\u0000O\t\u0001\u0000\u0000\u0000"+
		"PU\u0005\r\u0000\u0000QR\u0005\"\u0000\u0000RT\u0005\r\u0000\u0000SQ\u0001"+
		"\u0000\u0000\u0000TW\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000"+
		"UV\u0001\u0000\u0000\u0000V\u000b\u0001\u0000\u0000\u0000WU\u0001\u0000"+
		"\u0000\u0000XZ\u0005\u001f\u0000\u0000Y[\u0003\u000e\u0007\u0000ZY\u0001"+
		"\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000"+
		"\\]\u0005 \u0000\u0000]\r\u0001\u0000\u0000\u0000^`\u0003\u0010\b\u0000"+
		"_^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000"+
		"\u0000ab\u0001\u0000\u0000\u0000b\u000f\u0001\u0000\u0000\u0000ci\u0003"+
		"\u0012\t\u0000di\u0003$\u0012\u0000ei\u0003&\u0013\u0000fi\u00030\u0018"+
		"\u0000gi\u0003\u001e\u000f\u0000hc\u0001\u0000\u0000\u0000hd\u0001\u0000"+
		"\u0000\u0000he\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hg\u0001"+
		"\u0000\u0000\u0000i\u0011\u0001\u0000\u0000\u0000jk\u0005\r\u0000\u0000"+
		"kl\u0005\u001b\u0000\u0000lm\u0003\u0014\n\u0000mn\u0005\u001c\u0000\u0000"+
		"n\u0013\u0001\u0000\u0000\u0000or\u0003\u0016\u000b\u0000pq\u0007\u0001"+
		"\u0000\u0000qs\u0003\u0016\u000b\u0000rp\u0001\u0000\u0000\u0000rs\u0001"+
		"\u0000\u0000\u0000s\u0015\u0001\u0000\u0000\u0000ty\u0003\u0018\f\u0000"+
		"uv\u0007\u0002\u0000\u0000vx\u0003\u0018\f\u0000wu\u0001\u0000\u0000\u0000"+
		"x{\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000"+
		"\u0000z\u0017\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000|\u0081"+
		"\u0003\u001a\r\u0000}~\u0007\u0003\u0000\u0000~\u0080\u0003\u001a\r\u0000"+
		"\u007f}\u0001\u0000\u0000\u0000\u0080\u0083\u0001\u0000\u0000\u0000\u0081"+
		"\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u0082"+
		"\u0019\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0084"+
		"\u0086\u0007\u0002\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0001\u0000\u0000\u0000\u0086\u008d\u0001\u0000\u0000\u0000\u0087"+
		"\u0088\u0005\u001d\u0000\u0000\u0088\u0089\u0003\u0014\n\u0000\u0089\u008a"+
		"\u0005\u001e\u0000\u0000\u008a\u008e\u0001\u0000\u0000\u0000\u008b\u008e"+
		"\u0005\r\u0000\u0000\u008c\u008e\u0003\u001c\u000e\u0000\u008d\u0087\u0001"+
		"\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008c\u0001"+
		"\u0000\u0000\u0000\u008e\u001b\u0001\u0000\u0000\u0000\u008f\u0090\u0007"+
		"\u0004\u0000\u0000\u0090\u001d\u0001\u0000\u0000\u0000\u0091\u0092\u0005"+
		"\b\u0000\u0000\u0092\u0093\u0005\u001d\u0000\u0000\u0093\u0094\u0003 "+
		"\u0010\u0000\u0094\u0095\u0005\u001e\u0000\u0000\u0095\u0096\u0005\u001c"+
		"\u0000\u0000\u0096\u001f\u0001\u0000\u0000\u0000\u0097\u009c\u0003\"\u0011"+
		"\u0000\u0098\u0099\u0005\"\u0000\u0000\u0099\u009b\u0003\"\u0011\u0000"+
		"\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000\u0000\u0000"+
		"\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000"+
		"\u009d!\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000\u009f"+
		"\u00a2\u0003\u0014\n\u0000\u00a0\u00a2\u0005\u0010\u0000\u0000\u00a1\u009f"+
		"\u0001\u0000\u0000\u0000\u00a1\u00a0\u0001\u0000\u0000\u0000\u00a2#\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a4\u0005\u0004\u0000\u0000\u00a4\u00a5\u0005"+
		"\u001d\u0000\u0000\u00a5\u00a6\u0003\u0014\n\u0000\u00a6\u00a7\u0005\u001e"+
		"\u0000\u0000\u00a7\u00aa\u0003\f\u0006\u0000\u00a8\u00a9\u0005\u0005\u0000"+
		"\u0000\u00a9\u00ab\u0003\f\u0006\u0000\u00aa\u00a8\u0001\u0000\u0000\u0000"+
		"\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0005\u001c\u0000\u0000\u00ad%\u0001\u0000\u0000\u0000\u00ae"+
		"\u00af\u0005\u0006\u0000\u0000\u00af\u00b0\u0005\u001d\u0000\u0000\u00b0"+
		"\u00b1\u0003\u0014\n\u0000\u00b1\u00b2\u0005\u001e\u0000\u0000\u00b2\u00b3"+
		"\u0005\u0007\u0000\u0000\u00b3\u00b4\u0003\f\u0006\u0000\u00b4\u00b5\u0005"+
		"\u001c\u0000\u0000\u00b5\'\u0001\u0000\u0000\u0000\u00b6\u00b8\u0003*"+
		"\u0015\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b8\u00b9\u0001\u0000"+
		"\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000"+
		"\u0000\u0000\u00ba)\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005\t\u0000"+
		"\u0000\u00bc\u00bd\u0005\r\u0000\u0000\u00bd\u00bf\u0005\u001d\u0000\u0000"+
		"\u00be\u00c0\u0003,\u0016\u0000\u00bf\u00be\u0001\u0000\u0000\u0000\u00bf"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c2\u0005\u001e\u0000\u0000\u00c2\u00c4\u0005\u001c\u0000\u0000\u00c3"+
		"\u00c5\u0003\u0004\u0002\u0000\u00c4\u00c3\u0001\u0000\u0000\u0000\u00c4"+
		"\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c7\u0003\f\u0006\u0000\u00c7\u00c8\u0005\u001c\u0000\u0000\u00c8+"+
		"\u0001\u0000\u0000\u0000\u00c9\u00ce\u0003.\u0017\u0000\u00ca\u00cb\u0005"+
		"\"\u0000\u0000\u00cb\u00cd\u0003.\u0017\u0000\u00cc\u00ca\u0001\u0000"+
		"\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001\u0000"+
		"\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf-\u0001\u0000\u0000"+
		"\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d1\u00d2\u0005\r\u0000\u0000"+
		"\u00d2\u00d3\u0005!\u0000\u0000\u00d3\u00d4\u0003\u0002\u0001\u0000\u00d4"+
		"/\u0001\u0000\u0000\u0000\u00d5\u00d6\u0005\r\u0000\u0000\u00d6\u00d8"+
		"\u0005\u001d\u0000\u0000\u00d7\u00d9\u00032\u0019\u0000\u00d8\u00d7\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000\u00d9\u00da\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0005\u001e\u0000\u0000\u00db\u00dc\u0005"+
		"\u001c\u0000\u0000\u00dc1\u0001\u0000\u0000\u0000\u00dd\u00e2\u0003\u0014"+
		"\n\u0000\u00de\u00df\u0005\"\u0000\u0000\u00df\u00e1\u0003\u0014\n\u0000"+
		"\u00e0\u00de\u0001\u0000\u0000\u0000\u00e1\u00e4\u0001\u0000\u0000\u0000"+
		"\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000"+
		"\u00e33\u0001\u0000\u0000\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u0015"+
		"8;IUZahry\u0081\u0085\u008d\u009c\u00a1\u00aa\u00b9\u00bf\u00c4\u00ce"+
		"\u00d8\u00e2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}