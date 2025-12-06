# Generated from CalcPlus.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# This class defines a complete listener for a parse tree produced by CalcPlusParser.
class CalcPlusListener(ParseTreeListener):

    # Enter a parse tree produced by CalcPlusParser#calc0.
    def enterCalc0(self, ctx:CalcPlusParser.Calc0Context):
        pass

    # Exit a parse tree produced by CalcPlusParser#calc0.
    def exitCalc0(self, ctx:CalcPlusParser.Calc0Context):
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