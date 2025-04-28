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
		PLUS=17, MINUS=18, MULT=19, DIV=20, LT=21, GT=22, NE=23, EQUAL=24, SEMICOLON=25, 
		LPAREN=26, RPAREN=27, LBRACE=28, RBRACE=29, COLON=30, COMMA=31, WS=32, 
		COMMENT=33;
	public static final int
		RULE_programa = 0, RULE_type = 1, RULE_vars = 2, RULE_varDecList = 3, 
		RULE_varDec = 4, RULE_idList = 5, RULE_body = 6, RULE_statementList = 7, 
		RULE_statement = 8, RULE_assign = 9, RULE_expresion = 10, RULE_exp = 11, 
		RULE_termino = 12, RULE_factor = 13, RULE_cte = 14, RULE_print = 15, RULE_expList = 16, 
		RULE_condition = 17, RULE_cycle = 18, RULE_funcs = 19, RULE_funcList = 20, 
		RULE_funcDec = 21, RULE_paramList = 22, RULE_param = 23, RULE_fcall = 24, 
		RULE_argList = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "type", "vars", "varDecList", "varDec", "idList", "body", 
			"statementList", "statement", "assign", "expresion", "exp", "termino", 
			"factor", "cte", "print", "expList", "condition", "cycle", "funcs", "funcList", 
			"funcDec", "paramList", "param", "fcall", "argList"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'main'", "'end'", "'if'", "'else'", "'while'", "'do'", 
			"'print'", "'void'", "'int'", "'float'", "'var'", null, null, null, null, 
			"'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'!='", "'='", "';'", "'('", 
			"')'", "'{'", "'}'", "':'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAM", "MAIN", "END", "IF", "ELSE", "WHILE", "DO", "PRINT", 
			"VOID", "INT", "FLOAT", "VAR", "ID", "CTE_INT", "CTE_FLOAT", "CTE_STRING", 
			"PLUS", "MINUS", "MULT", "DIV", "LT", "GT", "NE", "EQUAL", "SEMICOLON", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "COMMA", "WS", "COMMENT"
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
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(58);
				funcs();
				}
				break;
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
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expresion);
		try {
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				exp();
				setState(113);
				match(GT);
				setState(114);
				exp();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(116);
				exp();
				setState(117);
				match(LT);
				setState(118);
				exp();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(120);
				exp();
				setState(121);
				match(NE);
				setState(122);
				exp();
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
	public static class ExpContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(BabyDuckParser.PLUS, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(BabyDuckParser.MINUS, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_exp);
		try {
			setState(135);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				termino();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				termino();
				setState(128);
				match(PLUS);
				setState(129);
				exp();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(131);
				termino();
				setState(132);
				match(MINUS);
				setState(133);
				exp();
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
	public static class TerminoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode MULT() { return getToken(BabyDuckParser.MULT, 0); }
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode DIV() { return getToken(BabyDuckParser.DIV, 0); }
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_termino);
		try {
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				factor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				factor();
				setState(139);
				match(MULT);
				setState(140);
				termino();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(142);
				factor();
				setState(143);
				match(DIV);
				setState(144);
				termino();
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
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode PLUS() { return getToken(BabyDuckParser.PLUS, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(BabyDuckParser.MINUS, 0); }
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_factor);
		try {
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				match(LPAREN);
				setState(149);
				expresion();
				setState(150);
				match(RPAREN);
				}
				break;
			case PLUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				match(PLUS);
				setState(153);
				factor();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(154);
				match(MINUS);
				setState(155);
				factor();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(156);
				match(ID);
				}
				break;
			case CTE_INT:
			case CTE_FLOAT:
				enterOuterAlt(_localctx, 5);
				{
				setState(157);
				cte();
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
			setState(160);
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
		public ExpListContext expList() {
			return getRuleContext(ExpListContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public TerminalNode CTE_STRING() { return getToken(BabyDuckParser.CTE_STRING, 0); }
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_print);
		try {
			setState(173);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				match(PRINT);
				setState(163);
				match(LPAREN);
				setState(164);
				expList(0);
				setState(165);
				match(RPAREN);
				setState(166);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(168);
				match(PRINT);
				setState(169);
				match(LPAREN);
				setState(170);
				match(CTE_STRING);
				setState(171);
				match(RPAREN);
				setState(172);
				match(SEMICOLON);
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
	public static class ExpListContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ExpListContext expList() {
			return getRuleContext(ExpListContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BabyDuckParser.COMMA, 0); }
		public ExpListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expList; }
	}

	public final ExpListContext expList() throws RecognitionException {
		return expList(0);
	}

	private ExpListContext expList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpListContext _localctx = new ExpListContext(_ctx, _parentState);
		ExpListContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(176);
			expresion();
			}
			_ctx.stop = _input.LT(-1);
			setState(183);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expList);
					setState(178);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(179);
					match(COMMA);
					setState(180);
					expresion();
					}
					} 
				}
				setState(185);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
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
		enterRule(_localctx, 34, RULE_condition);
		try {
			setState(202);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				match(IF);
				setState(187);
				match(LPAREN);
				setState(188);
				expresion();
				setState(189);
				match(RPAREN);
				setState(190);
				body();
				setState(191);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(193);
				match(IF);
				setState(194);
				match(LPAREN);
				setState(195);
				expresion();
				setState(196);
				match(RPAREN);
				setState(197);
				body();
				setState(198);
				match(ELSE);
				setState(199);
				body();
				setState(200);
				match(SEMICOLON);
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
		enterRule(_localctx, 36, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(WHILE);
			setState(205);
			match(LPAREN);
			setState(206);
			expresion();
			setState(207);
			match(RPAREN);
			setState(208);
			match(DO);
			setState(209);
			body();
			setState(210);
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
		public FuncListContext funcList() {
			return getRuleContext(FuncListContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VOID) {
				{
				setState(212);
				funcList();
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
	public static class FuncListContext extends ParserRuleContext {
		public List<FuncDecContext> funcDec() {
			return getRuleContexts(FuncDecContext.class);
		}
		public FuncDecContext funcDec(int i) {
			return getRuleContext(FuncDecContext.class,i);
		}
		public FuncListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcList; }
	}

	public final FuncListContext funcList() throws RecognitionException {
		FuncListContext _localctx = new FuncListContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_funcList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(215);
				funcDec();
				}
				}
				setState(218); 
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
			setState(220);
			match(VOID);
			setState(221);
			match(ID);
			setState(222);
			match(LPAREN);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(223);
				paramList();
				}
			}

			setState(226);
			match(RPAREN);
			setState(227);
			match(SEMICOLON);
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(228);
				vars();
				}
			}

			setState(231);
			body();
			setState(232);
			match(SEMICOLON);
			setState(233);
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
			setState(235);
			param();
			setState(240);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(236);
				match(COMMA);
				setState(237);
				param();
				}
				}
				setState(242);
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
			setState(243);
			match(ID);
			setState(244);
			match(COLON);
			setState(245);
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
			setState(247);
			match(ID);
			setState(248);
			match(LPAREN);
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 67559424L) != 0)) {
				{
				setState(249);
				argList();
				}
			}

			setState(252);
			match(RPAREN);
			setState(253);
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
			setState(255);
			expresion();
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(256);
				match(COMMA);
				setState(257);
				expresion();
				}
				}
				setState(262);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return expList_sempred((ExpListContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expList_sempred(ExpListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001!\u0108\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n}\b\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0003\u000b\u0088\b\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u0093\b\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u009f\b\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0003\u000f\u00ae\b\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00b6\b\u0010"+
		"\n\u0010\f\u0010\u00b9\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u00cb\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0003"+
		"\u0013\u00d6\b\u0013\u0001\u0014\u0004\u0014\u00d9\b\u0014\u000b\u0014"+
		"\f\u0014\u00da\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015"+
		"\u00e1\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00e6\b"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0005\u0016\u00ef\b\u0016\n\u0016\f\u0016\u00f2\t\u0016"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0003\u0018\u00fb\b\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u0103\b\u0019\n\u0019"+
		"\f\u0019\u0106\t\u0019\u0001\u0019\u0000\u0001 \u001a\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.02\u0000\u0002\u0001\u0000\n\u000b\u0001\u0000\u000e\u000f\u010c"+
		"\u00004\u0001\u0000\u0000\u0000\u0002A\u0001\u0000\u0000\u0000\u0004C"+
		"\u0001\u0000\u0000\u0000\u0006G\u0001\u0000\u0000\u0000\bK\u0001\u0000"+
		"\u0000\u0000\nP\u0001\u0000\u0000\u0000\fX\u0001\u0000\u0000\u0000\u000e"+
		"_\u0001\u0000\u0000\u0000\u0010h\u0001\u0000\u0000\u0000\u0012j\u0001"+
		"\u0000\u0000\u0000\u0014|\u0001\u0000\u0000\u0000\u0016\u0087\u0001\u0000"+
		"\u0000\u0000\u0018\u0092\u0001\u0000\u0000\u0000\u001a\u009e\u0001\u0000"+
		"\u0000\u0000\u001c\u00a0\u0001\u0000\u0000\u0000\u001e\u00ad\u0001\u0000"+
		"\u0000\u0000 \u00af\u0001\u0000\u0000\u0000\"\u00ca\u0001\u0000\u0000"+
		"\u0000$\u00cc\u0001\u0000\u0000\u0000&\u00d5\u0001\u0000\u0000\u0000("+
		"\u00d8\u0001\u0000\u0000\u0000*\u00dc\u0001\u0000\u0000\u0000,\u00eb\u0001"+
		"\u0000\u0000\u0000.\u00f3\u0001\u0000\u0000\u00000\u00f7\u0001\u0000\u0000"+
		"\u00002\u00ff\u0001\u0000\u0000\u000045\u0005\u0001\u0000\u000056\u0005"+
		"\r\u0000\u000068\u0005\u0019\u0000\u000079\u0003\u0004\u0002\u000087\u0001"+
		"\u0000\u0000\u000089\u0001\u0000\u0000\u00009;\u0001\u0000\u0000\u0000"+
		":<\u0003&\u0013\u0000;:\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000"+
		"<=\u0001\u0000\u0000\u0000=>\u0005\u0002\u0000\u0000>?\u0003\f\u0006\u0000"+
		"?@\u0005\u0003\u0000\u0000@\u0001\u0001\u0000\u0000\u0000AB\u0007\u0000"+
		"\u0000\u0000B\u0003\u0001\u0000\u0000\u0000CD\u0005\f\u0000\u0000DE\u0003"+
		"\u0006\u0003\u0000E\u0005\u0001\u0000\u0000\u0000FH\u0003\b\u0004\u0000"+
		"GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000"+
		"\u0000IJ\u0001\u0000\u0000\u0000J\u0007\u0001\u0000\u0000\u0000KL\u0003"+
		"\n\u0005\u0000LM\u0005\u001e\u0000\u0000MN\u0003\u0002\u0001\u0000NO\u0005"+
		"\u0019\u0000\u0000O\t\u0001\u0000\u0000\u0000PU\u0005\r\u0000\u0000QR"+
		"\u0005\u001f\u0000\u0000RT\u0005\r\u0000\u0000SQ\u0001\u0000\u0000\u0000"+
		"TW\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000"+
		"\u0000V\u000b\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000XZ\u0005"+
		"\u001c\u0000\u0000Y[\u0003\u000e\u0007\u0000ZY\u0001\u0000\u0000\u0000"+
		"Z[\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000\\]\u0005\u001d\u0000"+
		"\u0000]\r\u0001\u0000\u0000\u0000^`\u0003\u0010\b\u0000_^\u0001\u0000"+
		"\u0000\u0000`a\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000ab\u0001"+
		"\u0000\u0000\u0000b\u000f\u0001\u0000\u0000\u0000ci\u0003\u0012\t\u0000"+
		"di\u0003\"\u0011\u0000ei\u0003$\u0012\u0000fi\u00030\u0018\u0000gi\u0003"+
		"\u001e\u000f\u0000hc\u0001\u0000\u0000\u0000hd\u0001\u0000\u0000\u0000"+
		"he\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hg\u0001\u0000\u0000"+
		"\u0000i\u0011\u0001\u0000\u0000\u0000jk\u0005\r\u0000\u0000kl\u0005\u0018"+
		"\u0000\u0000lm\u0003\u0014\n\u0000mn\u0005\u0019\u0000\u0000n\u0013\u0001"+
		"\u0000\u0000\u0000o}\u0003\u0016\u000b\u0000pq\u0003\u0016\u000b\u0000"+
		"qr\u0005\u0016\u0000\u0000rs\u0003\u0016\u000b\u0000s}\u0001\u0000\u0000"+
		"\u0000tu\u0003\u0016\u000b\u0000uv\u0005\u0015\u0000\u0000vw\u0003\u0016"+
		"\u000b\u0000w}\u0001\u0000\u0000\u0000xy\u0003\u0016\u000b\u0000yz\u0005"+
		"\u0017\u0000\u0000z{\u0003\u0016\u000b\u0000{}\u0001\u0000\u0000\u0000"+
		"|o\u0001\u0000\u0000\u0000|p\u0001\u0000\u0000\u0000|t\u0001\u0000\u0000"+
		"\u0000|x\u0001\u0000\u0000\u0000}\u0015\u0001\u0000\u0000\u0000~\u0088"+
		"\u0003\u0018\f\u0000\u007f\u0080\u0003\u0018\f\u0000\u0080\u0081\u0005"+
		"\u0011\u0000\u0000\u0081\u0082\u0003\u0016\u000b\u0000\u0082\u0088\u0001"+
		"\u0000\u0000\u0000\u0083\u0084\u0003\u0018\f\u0000\u0084\u0085\u0005\u0012"+
		"\u0000\u0000\u0085\u0086\u0003\u0016\u000b\u0000\u0086\u0088\u0001\u0000"+
		"\u0000\u0000\u0087~\u0001\u0000\u0000\u0000\u0087\u007f\u0001\u0000\u0000"+
		"\u0000\u0087\u0083\u0001\u0000\u0000\u0000\u0088\u0017\u0001\u0000\u0000"+
		"\u0000\u0089\u0093\u0003\u001a\r\u0000\u008a\u008b\u0003\u001a\r\u0000"+
		"\u008b\u008c\u0005\u0013\u0000\u0000\u008c\u008d\u0003\u0018\f\u0000\u008d"+
		"\u0093\u0001\u0000\u0000\u0000\u008e\u008f\u0003\u001a\r\u0000\u008f\u0090"+
		"\u0005\u0014\u0000\u0000\u0090\u0091\u0003\u0018\f\u0000\u0091\u0093\u0001"+
		"\u0000\u0000\u0000\u0092\u0089\u0001\u0000\u0000\u0000\u0092\u008a\u0001"+
		"\u0000\u0000\u0000\u0092\u008e\u0001\u0000\u0000\u0000\u0093\u0019\u0001"+
		"\u0000\u0000\u0000\u0094\u0095\u0005\u001a\u0000\u0000\u0095\u0096\u0003"+
		"\u0014\n\u0000\u0096\u0097\u0005\u001b\u0000\u0000\u0097\u009f\u0001\u0000"+
		"\u0000\u0000\u0098\u0099\u0005\u0011\u0000\u0000\u0099\u009f\u0003\u001a"+
		"\r\u0000\u009a\u009b\u0005\u0012\u0000\u0000\u009b\u009f\u0003\u001a\r"+
		"\u0000\u009c\u009f\u0005\r\u0000\u0000\u009d\u009f\u0003\u001c\u000e\u0000"+
		"\u009e\u0094\u0001\u0000\u0000\u0000\u009e\u0098\u0001\u0000\u0000\u0000"+
		"\u009e\u009a\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000"+
		"\u009e\u009d\u0001\u0000\u0000\u0000\u009f\u001b\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a1\u0007\u0001\u0000\u0000\u00a1\u001d\u0001\u0000\u0000\u0000"+
		"\u00a2\u00a3\u0005\b\u0000\u0000\u00a3\u00a4\u0005\u001a\u0000\u0000\u00a4"+
		"\u00a5\u0003 \u0010\u0000\u00a5\u00a6\u0005\u001b\u0000\u0000\u00a6\u00a7"+
		"\u0005\u0019\u0000\u0000\u00a7\u00ae\u0001\u0000\u0000\u0000\u00a8\u00a9"+
		"\u0005\b\u0000\u0000\u00a9\u00aa\u0005\u001a\u0000\u0000\u00aa\u00ab\u0005"+
		"\u0010\u0000\u0000\u00ab\u00ac\u0005\u001b\u0000\u0000\u00ac\u00ae\u0005"+
		"\u0019\u0000\u0000\u00ad\u00a2\u0001\u0000\u0000\u0000\u00ad\u00a8\u0001"+
		"\u0000\u0000\u0000\u00ae\u001f\u0001\u0000\u0000\u0000\u00af\u00b0\u0006"+
		"\u0010\uffff\uffff\u0000\u00b0\u00b1\u0003\u0014\n\u0000\u00b1\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b2\u00b3\n\u0001\u0000\u0000\u00b3\u00b4\u0005\u001f"+
		"\u0000\u0000\u00b4\u00b6\u0003\u0014\n\u0000\u00b5\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8!\u0001\u0000\u0000\u0000"+
		"\u00b9\u00b7\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005\u0004\u0000\u0000"+
		"\u00bb\u00bc\u0005\u001a\u0000\u0000\u00bc\u00bd\u0003\u0014\n\u0000\u00bd"+
		"\u00be\u0005\u001b\u0000\u0000\u00be\u00bf\u0003\f\u0006\u0000\u00bf\u00c0"+
		"\u0005\u0019\u0000\u0000\u00c0\u00cb\u0001\u0000\u0000\u0000\u00c1\u00c2"+
		"\u0005\u0004\u0000\u0000\u00c2\u00c3\u0005\u001a\u0000\u0000\u00c3\u00c4"+
		"\u0003\u0014\n\u0000\u00c4\u00c5\u0005\u001b\u0000\u0000\u00c5\u00c6\u0003"+
		"\f\u0006\u0000\u00c6\u00c7\u0005\u0005\u0000\u0000\u00c7\u00c8\u0003\f"+
		"\u0006\u0000\u00c8\u00c9\u0005\u0019\u0000\u0000\u00c9\u00cb\u0001\u0000"+
		"\u0000\u0000\u00ca\u00ba\u0001\u0000\u0000\u0000\u00ca\u00c1\u0001\u0000"+
		"\u0000\u0000\u00cb#\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005\u0006\u0000"+
		"\u0000\u00cd\u00ce\u0005\u001a\u0000\u0000\u00ce\u00cf\u0003\u0014\n\u0000"+
		"\u00cf\u00d0\u0005\u001b\u0000\u0000\u00d0\u00d1\u0005\u0007\u0000\u0000"+
		"\u00d1\u00d2\u0003\f\u0006\u0000\u00d2\u00d3\u0005\u0019\u0000\u0000\u00d3"+
		"%\u0001\u0000\u0000\u0000\u00d4\u00d6\u0003(\u0014\u0000\u00d5\u00d4\u0001"+
		"\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\'\u0001\u0000"+
		"\u0000\u0000\u00d7\u00d9\u0003*\u0015\u0000\u00d8\u00d7\u0001\u0000\u0000"+
		"\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u00d8\u0001\u0000\u0000"+
		"\u0000\u00da\u00db\u0001\u0000\u0000\u0000\u00db)\u0001\u0000\u0000\u0000"+
		"\u00dc\u00dd\u0005\t\u0000\u0000\u00dd\u00de\u0005\r\u0000\u0000\u00de"+
		"\u00e0\u0005\u001a\u0000\u0000\u00df\u00e1\u0003,\u0016\u0000\u00e0\u00df"+
		"\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000\u0000\u00e1\u00e2"+
		"\u0001\u0000\u0000\u0000\u00e2\u00e3\u0005\u001b\u0000\u0000\u00e3\u00e5"+
		"\u0005\u0019\u0000\u0000\u00e4\u00e6\u0003\u0004\u0002\u0000\u00e5\u00e4"+
		"\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000\u0000\u0000\u00e6\u00e7"+
		"\u0001\u0000\u0000\u0000\u00e7\u00e8\u0003\f\u0006\u0000\u00e8\u00e9\u0005"+
		"\u0019\u0000\u0000\u00e9\u00ea\u0005\u0019\u0000\u0000\u00ea+\u0001\u0000"+
		"\u0000\u0000\u00eb\u00f0\u0003.\u0017\u0000\u00ec\u00ed\u0005\u001f\u0000"+
		"\u0000\u00ed\u00ef\u0003.\u0017\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000"+
		"\u00ef\u00f2\u0001\u0000\u0000\u0000\u00f0\u00ee\u0001\u0000\u0000\u0000"+
		"\u00f0\u00f1\u0001\u0000\u0000\u0000\u00f1-\u0001\u0000\u0000\u0000\u00f2"+
		"\u00f0\u0001\u0000\u0000\u0000\u00f3\u00f4\u0005\r\u0000\u0000\u00f4\u00f5"+
		"\u0005\u001e\u0000\u0000\u00f5\u00f6\u0003\u0002\u0001\u0000\u00f6/\u0001"+
		"\u0000\u0000\u0000\u00f7\u00f8\u0005\r\u0000\u0000\u00f8\u00fa\u0005\u001a"+
		"\u0000\u0000\u00f9\u00fb\u00032\u0019\u0000\u00fa\u00f9\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0001\u0000\u0000\u0000\u00fb\u00fc\u0001\u0000\u0000"+
		"\u0000\u00fc\u00fd\u0005\u001b\u0000\u0000\u00fd\u00fe\u0005\u0019\u0000"+
		"\u0000\u00fe1\u0001\u0000\u0000\u0000\u00ff\u0104\u0003\u0014\n\u0000"+
		"\u0100\u0101\u0005\u001f\u0000\u0000\u0101\u0103\u0003\u0014\n\u0000\u0102"+
		"\u0100\u0001\u0000\u0000\u0000\u0103\u0106\u0001\u0000\u0000\u0000\u0104"+
		"\u0102\u0001\u0000\u0000\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105"+
		"3\u0001\u0000\u0000\u0000\u0106\u0104\u0001\u0000\u0000\u0000\u00158;"+
		"IUZah|\u0087\u0092\u009e\u00ad\u00b7\u00ca\u00d5\u00da\u00e0\u00e5\u00f0"+
		"\u00fa\u0104";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}