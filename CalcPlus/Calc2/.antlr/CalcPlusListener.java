// Generated from /home/jake/project/CS/compiler/rancho/CalcPlus/Calc2/CalcPlus.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalcPlusParser}.
 */
public interface CalcPlusListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalcPlusParser#calc0}.
	 * @param ctx the parse tree
	 */
	void enterCalc0(CalcPlusParser.Calc0Context ctx);
	/**
	 * Exit a parse tree produced by {@link CalcPlusParser#calc0}.
	 * @param ctx the parse tree
	 */
	void exitCalc0(CalcPlusParser.Calc0Context ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(CalcPlusParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(CalcPlusParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(CalcPlusParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(CalcPlusParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Var}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVar(CalcPlusParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Var}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVar(CalcPlusParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParens(CalcPlusParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParens(CalcPlusParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Int}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInt(CalcPlusParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Int}
	 * labeled alternative in {@link CalcPlusParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInt(CalcPlusParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcPlusParser#calc1}.
	 * @param ctx the parse tree
	 */
	void enterCalc1(CalcPlusParser.Calc1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CalcPlusParser#calc1}.
	 * @param ctx the parse tree
	 */
	void exitCalc1(CalcPlusParser.Calc1Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprAssign}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterExprAssign(CalcPlusParser.ExprAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprAssign}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitExprAssign(CalcPlusParser.ExprAssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(CalcPlusParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(CalcPlusParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcPlusParser#calc2}.
	 * @param ctx the parse tree
	 */
	void enterCalc2(CalcPlusParser.Calc2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CalcPlusParser#calc2}.
	 * @param ctx the parse tree
	 */
	void exitCalc2(CalcPlusParser.Calc2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CalcPlusParser#cond}.
	 * @param ctx the parse tree
	 */
	void enterCond(CalcPlusParser.CondContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcPlusParser#cond}.
	 * @param ctx the parse tree
	 */
	void exitCond(CalcPlusParser.CondContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalcPlusParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(CalcPlusParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcPlusParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(CalcPlusParser.BlockContext ctx);
}