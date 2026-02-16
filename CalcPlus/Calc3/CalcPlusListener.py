# Generated from CalcPlus.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# This class defines a complete listener for a parse tree produced by CalcPlusParser.
class CalcPlusListener(ParseTreeListener):

    # Enter a parse tree produced by CalcPlusParser#calc3.
    def enterCalc3(self, ctx:CalcPlusParser.Calc3Context):
        pass

    # Exit a parse tree produced by CalcPlusParser#calc3.
    def exitCalc3(self, ctx:CalcPlusParser.Calc3Context):
        pass


    # Enter a parse tree produced by CalcPlusParser#ExprAssign.
    def enterExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#ExprAssign.
    def exitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#ReadAssign.
    def enterReadAssign(self, ctx:CalcPlusParser.ReadAssignContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#ReadAssign.
    def exitReadAssign(self, ctx:CalcPlusParser.ReadAssignContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#IfElse.
    def enterIfElse(self, ctx:CalcPlusParser.IfElseContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#IfElse.
    def exitIfElse(self, ctx:CalcPlusParser.IfElseContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#Write.
    def enterWrite(self, ctx:CalcPlusParser.WriteContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#Write.
    def exitWrite(self, ctx:CalcPlusParser.WriteContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#cond.
    def enterCond(self, ctx:CalcPlusParser.CondContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#cond.
    def exitCond(self, ctx:CalcPlusParser.CondContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#block.
    def enterBlock(self, ctx:CalcPlusParser.BlockContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#block.
    def exitBlock(self, ctx:CalcPlusParser.BlockContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#MulDiv.
    def enterMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#MulDiv.
    def exitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#AddSub.
    def enterAddSub(self, ctx:CalcPlusParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#AddSub.
    def exitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#Var.
    def enterVar(self, ctx:CalcPlusParser.VarContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#Var.
    def exitVar(self, ctx:CalcPlusParser.VarContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#Parens.
    def enterParens(self, ctx:CalcPlusParser.ParensContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#Parens.
    def exitParens(self, ctx:CalcPlusParser.ParensContext):
        pass


    # Enter a parse tree produced by CalcPlusParser#Int.
    def enterInt(self, ctx:CalcPlusParser.IntContext):
        pass

    # Exit a parse tree produced by CalcPlusParser#Int.
    def exitInt(self, ctx:CalcPlusParser.IntContext):
        pass



del CalcPlusParser