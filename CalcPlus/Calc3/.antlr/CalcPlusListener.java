// Generated from /home/jake/project/CS/compiler/rancho/CalcPlus/Calc3/CalcPlus.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalcPlusParser}.
 */
public interface CalcPlusListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalcPlusParser#calc3}.
	 * @param ctx the parse tree
	 */
	void enterCalc3(CalcPlusParser.Calc3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CalcPlusParser#calc3}.
	 * @param ctx the parse tree
	 */
	void exitCalc3(CalcPlusParser.Calc3Context ctx);
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
	 * Enter a parse tree produced by the {@code ReadAssign}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterReadAssign(CalcPlusParser.ReadAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReadAssign}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitReadAssign(CalcPlusParser.ReadAssignContext ctx);
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
	 * Enter a parse tree produced by the {@code Write}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterWrite(CalcPlusParser.WriteContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Write}
	 * labeled alternative in {@link CalcPlusParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitWrite(CalcPlusParser.WriteContext ctx);
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
}