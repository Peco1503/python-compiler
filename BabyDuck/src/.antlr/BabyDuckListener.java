// Generated from /Users/francoelugo/Documents/8vo/python-compiler/BabyDuck/src/BabyDuck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BabyDuckParser}.
 */
public interface BabyDuckListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(BabyDuckParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(BabyDuckParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(BabyDuckParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(BabyDuckParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(BabyDuckParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(BabyDuckParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#varDecList}.
	 * @param ctx the parse tree
	 */
	void enterVarDecList(BabyDuckParser.VarDecListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#varDecList}.
	 * @param ctx the parse tree
	 */
	void exitVarDecList(BabyDuckParser.VarDecListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#varDec}.
	 * @param ctx the parse tree
	 */
	void enterVarDec(BabyDuckParser.VarDecContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#varDec}.
	 * @param ctx the parse tree
	 */
	void exitVarDec(BabyDuckParser.VarDecContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#idList}.
	 * @param ctx the parse tree
	 */
	void enterIdList(BabyDuckParser.IdListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#idList}.
	 * @param ctx the parse tree
	 */
	void exitIdList(BabyDuckParser.IdListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(BabyDuckParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(BabyDuckParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#statementList}.
	 * @param ctx the parse tree
	 */
	void enterStatementList(BabyDuckParser.StatementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#statementList}.
	 * @param ctx the parse tree
	 */
	void exitStatementList(BabyDuckParser.StatementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(BabyDuckParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(BabyDuckParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(BabyDuckParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(BabyDuckParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(BabyDuckParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(BabyDuckParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(BabyDuckParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(BabyDuckParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(BabyDuckParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(BabyDuckParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(BabyDuckParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(BabyDuckParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(BabyDuckParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(BabyDuckParser.CteContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(BabyDuckParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(BabyDuckParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#expList}.
	 * @param ctx the parse tree
	 */
	void enterExpList(BabyDuckParser.ExpListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#expList}.
	 * @param ctx the parse tree
	 */
	void exitExpList(BabyDuckParser.ExpListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(BabyDuckParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(BabyDuckParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#cycle}.
	 * @param ctx the parse tree
	 */
	void enterCycle(BabyDuckParser.CycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#cycle}.
	 * @param ctx the parse tree
	 */
	void exitCycle(BabyDuckParser.CycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void enterFuncs(BabyDuckParser.FuncsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void exitFuncs(BabyDuckParser.FuncsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#funcList}.
	 * @param ctx the parse tree
	 */
	void enterFuncList(BabyDuckParser.FuncListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#funcList}.
	 * @param ctx the parse tree
	 */
	void exitFuncList(BabyDuckParser.FuncListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#funcDec}.
	 * @param ctx the parse tree
	 */
	void enterFuncDec(BabyDuckParser.FuncDecContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#funcDec}.
	 * @param ctx the parse tree
	 */
	void exitFuncDec(BabyDuckParser.FuncDecContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(BabyDuckParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(BabyDuckParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(BabyDuckParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(BabyDuckParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#fcall}.
	 * @param ctx the parse tree
	 */
	void enterFcall(BabyDuckParser.FcallContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#fcall}.
	 * @param ctx the parse tree
	 */
	void exitFcall(BabyDuckParser.FcallContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(BabyDuckParser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(BabyDuckParser.ArgListContext ctx);
}