# Generated from CalcPlus.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# This class defines a complete generic visitor for a parse tree produced by CalcPlusParser.

class CalcPlusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcPlusParser#calc0.
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CalcPlusParser#MulDiv.
    def visitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#AddSub.
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Parens.
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Int.
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        return self.visitChildren(ctx)



del CalcPlusParser