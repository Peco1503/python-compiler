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
		RULE_termino = 12, RULE_factor = 13, RULE_cte = 14, RULE_print = 15, RULE_condition = 16, 
		RULE_cycle = 17, RULE_funcs = 18, RULE_funcDec = 19, RULE_paramList = 20, 
		RULE_param = 21, RULE_fcall = 22, RULE_argList = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "type", "vars", "varDecList", "varDec", "idList", "body", 
			"statementList", "statement", "assign", "expresion", "exp", "termino", 
			"factor", "cte", "print", "condition", "cycle", "funcs", "funcDec", "paramList", 
			"param", "fcall", "argList"
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
			setState(48);
			match(PROGRAM);
			setState(49);
			match(ID);
			setState(50);
			match(SEMICOLON);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(51);
				vars();
				}
			}

			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VOID) {
				{
				setState(54);
				funcs();
				}
			}

			setState(57);
			match(MAIN);
			setState(58);
			body();
			setState(59);
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
			setState(61);
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
			setState(63);
			match(VAR);
			setState(64);
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
			setState(67); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(66);
				varDec();
				}
				}
				setState(69); 
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
			setState(71);
			idList();
			setState(72);
			match(COLON);
			setState(73);
			type();
			setState(74);
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
			setState(76);
			match(ID);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(77);
				match(COMMA);
				setState(78);
				match(ID);
				}
				}
				setState(83);
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
			setState(84);
			match(LBRACE);
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8528L) != 0)) {
				{
				setState(85);
				statementList();
				}
			}

			setState(88);
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
			setState(91); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(90);
				statement();
				}
				}
				setState(93); 
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
			setState(100);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(96);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(97);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(98);
				fcall();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(99);
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
			setState(102);
			match(ID);
			setState(103);
			match(EQUAL);
			setState(104);
			expresion();
			setState(105);
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
			setState(107);
			exp();
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 132120576L) != 0)) {
				{
				setState(108);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 132120576L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(109);
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
			setState(112);
			termino();
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(113);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(114);
				termino();
				}
				}
				setState(119);
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
			setState(120);
			factor();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(121);
				_la = _input.LA(1);
				if ( !(_la==MULT || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(122);
				factor();
				}
				}
				setState(127);
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
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PLUS || _la==MINUS) {
				{
				setState(128);
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

			setState(137);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				{
				setState(131);
				match(LPAREN);
				setState(132);
				expresion();
				setState(133);
				match(RPAREN);
				}
				break;
			case ID:
				{
				setState(135);
				match(ID);
				}
				break;
			case CTE_INT:
			case CTE_FLOAT:
				{
				setState(136);
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
			setState(139);
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
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public TerminalNode CTE_STRING() { return getToken(BabyDuckParser.CTE_STRING, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
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
			setState(141);
			match(PRINT);
			setState(142);
			match(LPAREN);
			setState(145);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_STRING:
				{
				setState(143);
				match(CTE_STRING);
				}
				break;
			case ID:
			case CTE_INT:
			case CTE_FLOAT:
			case PLUS:
			case MINUS:
			case LPAREN:
				{
				setState(144);
				expresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(147);
			match(RPAREN);
			setState(148);
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
		enterRule(_localctx, 32, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(IF);
			setState(151);
			match(LPAREN);
			setState(152);
			expresion();
			setState(153);
			match(RPAREN);
			setState(154);
			body();
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(155);
				match(ELSE);
				setState(156);
				body();
				}
			}

			setState(159);
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
		enterRule(_localctx, 34, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(WHILE);
			setState(162);
			match(LPAREN);
			setState(163);
			expresion();
			setState(164);
			match(RPAREN);
			setState(165);
			match(DO);
			setState(166);
			body();
			setState(167);
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
		enterRule(_localctx, 36, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(169);
				funcDec();
				}
				}
				setState(172); 
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
		enterRule(_localctx, 38, RULE_funcDec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(VOID);
			setState(175);
			match(ID);
			setState(176);
			match(LPAREN);
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(177);
				paramList();
				}
			}

			setState(180);
			match(RPAREN);
			setState(181);
			match(SEMICOLON);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(182);
				vars();
				}
			}

			setState(185);
			body();
			setState(186);
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
		enterRule(_localctx, 40, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			param();
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(189);
				match(COMMA);
				setState(190);
				param();
				}
				}
				setState(195);
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
		enterRule(_localctx, 42, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(ID);
			setState(197);
			match(COLON);
			setState(198);
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
		enterRule(_localctx, 44, RULE_fcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(ID);
			setState(201);
			match(LPAREN);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 537321472L) != 0)) {
				{
				setState(202);
				argList();
				}
			}

			setState(205);
			match(RPAREN);
			setState(206);
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
		enterRule(_localctx, 46, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			expresion();
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(209);
				match(COMMA);
				setState(210);
				expresion();
				}
				}
				setState(215);
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
		"\u0004\u0001$\u00d9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0003\u00005\b\u0000\u0001\u0000\u0003\u0000"+
		"8\b\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0004\u0003"+
		"D\b\u0003\u000b\u0003\f\u0003E\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005P\b"+
		"\u0005\n\u0005\f\u0005S\t\u0005\u0001\u0006\u0001\u0006\u0003\u0006W\b"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007\\\b\u0007\u000b"+
		"\u0007\f\u0007]\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\be\b\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0003\no\b"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000bt\b\u000b\n\u000b\f"+
		"\u000bw\t\u000b\u0001\f\u0001\f\u0001\f\u0005\f|\b\f\n\f\f\f\u007f\t\f"+
		"\u0001\r\u0003\r\u0082\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u008a\b\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u0092\b\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0003\u0010\u009e\b\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0004\u0012\u00ab\b\u0012\u000b\u0012\f"+
		"\u0012\u00ac\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013"+
		"\u00b3\b\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00b8\b"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0005\u0014\u00c0\b\u0014\n\u0014\f\u0014\u00c3\t\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u00cc\b\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0005\u0017\u00d4\b\u0017\n\u0017\f\u0017\u00d7"+
		"\t\u0017\u0001\u0017\u0000\u0000\u0018\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.\u0000\u0005"+
		"\u0001\u0000\n\u000b\u0001\u0000\u0015\u001a\u0001\u0000\u0011\u0012\u0001"+
		"\u0000\u0013\u0014\u0001\u0000\u000e\u000f\u00d8\u00000\u0001\u0000\u0000"+
		"\u0000\u0002=\u0001\u0000\u0000\u0000\u0004?\u0001\u0000\u0000\u0000\u0006"+
		"C\u0001\u0000\u0000\u0000\bG\u0001\u0000\u0000\u0000\nL\u0001\u0000\u0000"+
		"\u0000\fT\u0001\u0000\u0000\u0000\u000e[\u0001\u0000\u0000\u0000\u0010"+
		"d\u0001\u0000\u0000\u0000\u0012f\u0001\u0000\u0000\u0000\u0014k\u0001"+
		"\u0000\u0000\u0000\u0016p\u0001\u0000\u0000\u0000\u0018x\u0001\u0000\u0000"+
		"\u0000\u001a\u0081\u0001\u0000\u0000\u0000\u001c\u008b\u0001\u0000\u0000"+
		"\u0000\u001e\u008d\u0001\u0000\u0000\u0000 \u0096\u0001\u0000\u0000\u0000"+
		"\"\u00a1\u0001\u0000\u0000\u0000$\u00aa\u0001\u0000\u0000\u0000&\u00ae"+
		"\u0001\u0000\u0000\u0000(\u00bc\u0001\u0000\u0000\u0000*\u00c4\u0001\u0000"+
		"\u0000\u0000,\u00c8\u0001\u0000\u0000\u0000.\u00d0\u0001\u0000\u0000\u0000"+
		"01\u0005\u0001\u0000\u000012\u0005\r\u0000\u000024\u0005\u001c\u0000\u0000"+
		"35\u0003\u0004\u0002\u000043\u0001\u0000\u0000\u000045\u0001\u0000\u0000"+
		"\u000057\u0001\u0000\u0000\u000068\u0003$\u0012\u000076\u0001\u0000\u0000"+
		"\u000078\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u00009:\u0005\u0002"+
		"\u0000\u0000:;\u0003\f\u0006\u0000;<\u0005\u0003\u0000\u0000<\u0001\u0001"+
		"\u0000\u0000\u0000=>\u0007\u0000\u0000\u0000>\u0003\u0001\u0000\u0000"+
		"\u0000?@\u0005\f\u0000\u0000@A\u0003\u0006\u0003\u0000A\u0005\u0001\u0000"+
		"\u0000\u0000BD\u0003\b\u0004\u0000CB\u0001\u0000\u0000\u0000DE\u0001\u0000"+
		"\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000F\u0007"+
		"\u0001\u0000\u0000\u0000GH\u0003\n\u0005\u0000HI\u0005!\u0000\u0000IJ"+
		"\u0003\u0002\u0001\u0000JK\u0005\u001c\u0000\u0000K\t\u0001\u0000\u0000"+
		"\u0000LQ\u0005\r\u0000\u0000MN\u0005\"\u0000\u0000NP\u0005\r\u0000\u0000"+
		"OM\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000QR\u0001\u0000\u0000\u0000R\u000b\u0001\u0000\u0000\u0000SQ\u0001"+
		"\u0000\u0000\u0000TV\u0005\u001f\u0000\u0000UW\u0003\u000e\u0007\u0000"+
		"VU\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000"+
		"\u0000XY\u0005 \u0000\u0000Y\r\u0001\u0000\u0000\u0000Z\\\u0003\u0010"+
		"\b\u0000[Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001"+
		"\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\u000f\u0001\u0000\u0000"+
		"\u0000_e\u0003\u0012\t\u0000`e\u0003 \u0010\u0000ae\u0003\"\u0011\u0000"+
		"be\u0003,\u0016\u0000ce\u0003\u001e\u000f\u0000d_\u0001\u0000\u0000\u0000"+
		"d`\u0001\u0000\u0000\u0000da\u0001\u0000\u0000\u0000db\u0001\u0000\u0000"+
		"\u0000dc\u0001\u0000\u0000\u0000e\u0011\u0001\u0000\u0000\u0000fg\u0005"+
		"\r\u0000\u0000gh\u0005\u001b\u0000\u0000hi\u0003\u0014\n\u0000ij\u0005"+
		"\u001c\u0000\u0000j\u0013\u0001\u0000\u0000\u0000kn\u0003\u0016\u000b"+
		"\u0000lm\u0007\u0001\u0000\u0000mo\u0003\u0016\u000b\u0000nl\u0001\u0000"+
		"\u0000\u0000no\u0001\u0000\u0000\u0000o\u0015\u0001\u0000\u0000\u0000"+
		"pu\u0003\u0018\f\u0000qr\u0007\u0002\u0000\u0000rt\u0003\u0018\f\u0000"+
		"sq\u0001\u0000\u0000\u0000tw\u0001\u0000\u0000\u0000us\u0001\u0000\u0000"+
		"\u0000uv\u0001\u0000\u0000\u0000v\u0017\u0001\u0000\u0000\u0000wu\u0001"+
		"\u0000\u0000\u0000x}\u0003\u001a\r\u0000yz\u0007\u0003\u0000\u0000z|\u0003"+
		"\u001a\r\u0000{y\u0001\u0000\u0000\u0000|\u007f\u0001\u0000\u0000\u0000"+
		"}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0019\u0001\u0000"+
		"\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u0080\u0082\u0007\u0002\u0000"+
		"\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000"+
		"\u0000\u0082\u0089\u0001\u0000\u0000\u0000\u0083\u0084\u0005\u001d\u0000"+
		"\u0000\u0084\u0085\u0003\u0014\n\u0000\u0085\u0086\u0005\u001e\u0000\u0000"+
		"\u0086\u008a\u0001\u0000\u0000\u0000\u0087\u008a\u0005\r\u0000\u0000\u0088"+
		"\u008a\u0003\u001c\u000e\u0000\u0089\u0083\u0001\u0000\u0000\u0000\u0089"+
		"\u0087\u0001\u0000\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a"+
		"\u001b\u0001\u0000\u0000\u0000\u008b\u008c\u0007\u0004\u0000\u0000\u008c"+
		"\u001d\u0001\u0000\u0000\u0000\u008d\u008e\u0005\b\u0000\u0000\u008e\u0091"+
		"\u0005\u001d\u0000\u0000\u008f\u0092\u0005\u0010\u0000\u0000\u0090\u0092"+
		"\u0003\u0014\n\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0091\u0090\u0001"+
		"\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0094\u0005"+
		"\u001e\u0000\u0000\u0094\u0095\u0005\u001c\u0000\u0000\u0095\u001f\u0001"+
		"\u0000\u0000\u0000\u0096\u0097\u0005\u0004\u0000\u0000\u0097\u0098\u0005"+
		"\u001d\u0000\u0000\u0098\u0099\u0003\u0014\n\u0000\u0099\u009a\u0005\u001e"+
		"\u0000\u0000\u009a\u009d\u0003\f\u0006\u0000\u009b\u009c\u0005\u0005\u0000"+
		"\u0000\u009c\u009e\u0003\f\u0006\u0000\u009d\u009b\u0001\u0000\u0000\u0000"+
		"\u009d\u009e\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000"+
		"\u009f\u00a0\u0005\u001c\u0000\u0000\u00a0!\u0001\u0000\u0000\u0000\u00a1"+
		"\u00a2\u0005\u0006\u0000\u0000\u00a2\u00a3\u0005\u001d\u0000\u0000\u00a3"+
		"\u00a4\u0003\u0014\n\u0000\u00a4\u00a5\u0005\u001e\u0000\u0000\u00a5\u00a6"+
		"\u0005\u0007\u0000\u0000\u00a6\u00a7\u0003\f\u0006\u0000\u00a7\u00a8\u0005"+
		"\u001c\u0000\u0000\u00a8#\u0001\u0000\u0000\u0000\u00a9\u00ab\u0003&\u0013"+
		"\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000"+
		"\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ac\u00ad\u0001\u0000\u0000"+
		"\u0000\u00ad%\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\t\u0000\u0000"+
		"\u00af\u00b0\u0005\r\u0000\u0000\u00b0\u00b2\u0005\u001d\u0000\u0000\u00b1"+
		"\u00b3\u0003(\u0014\u0000\u00b2\u00b1\u0001\u0000\u0000\u0000\u00b2\u00b3"+
		"\u0001\u0000\u0000\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u00b5"+
		"\u0005\u001e\u0000\u0000\u00b5\u00b7\u0005\u001c\u0000\u0000\u00b6\u00b8"+
		"\u0003\u0004\u0002\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b7\u00b8"+
		"\u0001\u0000\u0000\u0000\u00b8\u00b9\u0001\u0000\u0000\u0000\u00b9\u00ba"+
		"\u0003\f\u0006\u0000\u00ba\u00bb\u0005\u001c\u0000\u0000\u00bb\'\u0001"+
		"\u0000\u0000\u0000\u00bc\u00c1\u0003*\u0015\u0000\u00bd\u00be\u0005\""+
		"\u0000\u0000\u00be\u00c0\u0003*\u0015\u0000\u00bf\u00bd\u0001\u0000\u0000"+
		"\u0000\u00c0\u00c3\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2)\u0001\u0000\u0000\u0000"+
		"\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c4\u00c5\u0005\r\u0000\u0000\u00c5"+
		"\u00c6\u0005!\u0000\u0000\u00c6\u00c7\u0003\u0002\u0001\u0000\u00c7+\u0001"+
		"\u0000\u0000\u0000\u00c8\u00c9\u0005\r\u0000\u0000\u00c9\u00cb\u0005\u001d"+
		"\u0000\u0000\u00ca\u00cc\u0003.\u0017\u0000\u00cb\u00ca\u0001\u0000\u0000"+
		"\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000"+
		"\u0000\u00cd\u00ce\u0005\u001e\u0000\u0000\u00ce\u00cf\u0005\u001c\u0000"+
		"\u0000\u00cf-\u0001\u0000\u0000\u0000\u00d0\u00d5\u0003\u0014\n\u0000"+
		"\u00d1\u00d2\u0005\"\u0000\u0000\u00d2\u00d4\u0003\u0014\n\u0000\u00d3"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d4\u00d7\u0001\u0000\u0000\u0000\u00d5"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6"+
		"/\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001\u0000\u0000\u0000\u001447"+
		"EQV]dnu}\u0081\u0089\u0091\u009d\u00ac\u00b2\u00b7\u00c1\u00cb\u00d5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}