# ANTLR 4.9.2가 CalcPlus.g4에서 생성한 파일
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# 이 클래스는 CalcPlusParser가 만든 파스 트리를 위한 전체 방문자를 정의한다.

class CalcPlusVisitor(ParseTreeVisitor):

    # CalcPlusParser#calc0가 만든 파스 트리를 방문한다.
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visitChildren(ctx)


    # CalcPlusParser#MulDiv가 만든 파스 트리를 방문한다.
    def visitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#AddSub가 만든 파스 트리를 방문한다.
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#Var가 만든 파스 트리를 방문한다.
    def visitVar(self, ctx:CalcPlusParser.VarContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#Parens가 만든 파스 트리를 방문한다.
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#Int가 만든 파스 트리를 방문한다.
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#calc1가 만든 파스 트리를 방문한다.
    def visitCalc1(self, ctx:CalcPlusParser.Calc1Context):
        return self.visitChildren(ctx)


    # CalcPlusParser#ExprAssign가 만든 파스 트리를 방문한다.
    def visitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#ReadAssign가 만든 파스 트리를 방문한다.
    def visitReadAssign(self, ctx:CalcPlusParser.ReadAssignContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#IfElse가 만든 파스 트리를 방문한다.
    def visitIfElse(self, ctx:CalcPlusParser.IfElseContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#Write가 만든 파스 트리를 방문한다.
    def visitWrite(self, ctx:CalcPlusParser.WriteContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#calc2가 만든 파스 트리를 방문한다.
    def visitCalc2(self, ctx:CalcPlusParser.Calc2Context):
        return self.visitChildren(ctx)


    # CalcPlusParser#cond가 만든 파스 트리를 방문한다.
    def visitCond(self, ctx:CalcPlusParser.CondContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#block가 만든 파스 트리를 방문한다.
    def visitBlock(self, ctx:CalcPlusParser.BlockContext):
        return self.visitChildren(ctx)


    # CalcPlusParser#calc3가 만든 파스 트리를 방문한다.
    def visitCalc3(self, ctx:CalcPlusParser.Calc3Context):
        return self.visitChildren(ctx)



del CalcPlusParser