# Generated from CalcPlus.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# This class defines a complete generic visitor for a parse tree produced by CalcPlusParser.

class CalcPlusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcPlusParser#program.
    def visitProgram(self, ctx:CalcPlusParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Declare.
    def visitDeclare(self, ctx:CalcPlusParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#ExprAssign.
    def visitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#ReadAssign.
    def visitReadAssign(self, ctx:CalcPlusParser.ReadAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Write.
    def visitWrite(self, ctx:CalcPlusParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#IfElse.
    def visitIfElse(self, ctx:CalcPlusParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#StmtBlock.
    def visitStmtBlock(self, ctx:CalcPlusParser.StmtBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#MulDiv.
    def visitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#AddSub.
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Var.
    def visitVar(self, ctx:CalcPlusParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Parens.
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#Int.
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#cond.
    def visitCond(self, ctx:CalcPlusParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcPlusParser#block.
    def visitBlock(self, ctx:CalcPlusParser.BlockContext):
        return self.visitChildren(ctx)



del CalcPlusParser