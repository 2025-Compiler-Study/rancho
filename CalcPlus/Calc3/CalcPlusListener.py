# ANTLR 4.9.2가 CalcPlus.g4에서 생성한 파일
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# 이 클래스는 CalcPlusParser가 만든 파스 트리를 위한 전체 리스너를 정의한다.
class CalcPlusListener(ParseTreeListener):

    # CalcPlusParser#calc0가 만든 파스 트리에 진입한다.
    def enterCalc0(self, ctx:CalcPlusParser.Calc0Context):
        pass

    # CalcPlusParser#calc0가 만든 파스 트리를 종료한다.
    def exitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        pass


    # CalcPlusParser#MulDiv가 만든 파스 트리에 진입한다.
    def enterMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        pass

    # CalcPlusParser#MulDiv가 만든 파스 트리를 종료한다.
    def exitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        pass


    # CalcPlusParser#AddSub가 만든 파스 트리에 진입한다.
    def enterAddSub(self, ctx:CalcPlusParser.AddSubContext):
        pass

    # CalcPlusParser#AddSub가 만든 파스 트리를 종료한다.
    def exitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        pass


    # CalcPlusParser#Var가 만든 파스 트리에 진입한다.
    def enterVar(self, ctx:CalcPlusParser.VarContext):
        pass

    # CalcPlusParser#Var가 만든 파스 트리를 종료한다.
    def exitVar(self, ctx:CalcPlusParser.VarContext):
        pass


    # CalcPlusParser#Parens가 만든 파스 트리에 진입한다.
    def enterParens(self, ctx:CalcPlusParser.ParensContext):
        pass

    # CalcPlusParser#Parens가 만든 파스 트리를 종료한다.
    def exitParens(self, ctx:CalcPlusParser.ParensContext):
        pass


    # CalcPlusParser#Int가 만든 파스 트리에 진입한다.
    def enterInt(self, ctx:CalcPlusParser.IntContext):
        pass

    # CalcPlusParser#Int가 만든 파스 트리를 종료한다.
    def exitInt(self, ctx:CalcPlusParser.IntContext):
        pass


    # CalcPlusParser#calc1가 만든 파스 트리에 진입한다.
    def enterCalc1(self, ctx:CalcPlusParser.Calc1Context):
        pass

    # CalcPlusParser#calc1가 만든 파스 트리를 종료한다.
    def exitCalc1(self, ctx:CalcPlusParser.Calc1Context):
        pass


    # CalcPlusParser#ExprAssign가 만든 파스 트리에 진입한다.
    def enterExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        pass

    # CalcPlusParser#ExprAssign가 만든 파스 트리를 종료한다.
    def exitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        pass


    # CalcPlusParser#ReadAssign가 만든 파스 트리에 진입한다.
    def enterReadAssign(self, ctx:CalcPlusParser.ReadAssignContext):
        pass

    # CalcPlusParser#ReadAssign가 만든 파스 트리를 종료한다.
    def exitReadAssign(self, ctx:CalcPlusParser.ReadAssignContext):
        pass


    # CalcPlusParser#IfElse가 만든 파스 트리에 진입한다.
    def enterIfElse(self, ctx:CalcPlusParser.IfElseContext):
        pass

    # CalcPlusParser#IfElse가 만든 파스 트리를 종료한다.
    def exitIfElse(self, ctx:CalcPlusParser.IfElseContext):
        pass


    # CalcPlusParser#Write가 만든 파스 트리에 진입한다.
    def enterWrite(self, ctx:CalcPlusParser.WriteContext):
        pass

    # CalcPlusParser#Write가 만든 파스 트리를 종료한다.
    def exitWrite(self, ctx:CalcPlusParser.WriteContext):
        pass


    # CalcPlusParser#calc2가 만든 파스 트리에 진입한다.
    def enterCalc2(self, ctx:CalcPlusParser.Calc2Context):
        pass

    # CalcPlusParser#calc2가 만든 파스 트리를 종료한다.
    def exitCalc2(self, ctx:CalcPlusParser.Calc2Context):
        pass


    # CalcPlusParser#cond가 만든 파스 트리에 진입한다.
    def enterCond(self, ctx:CalcPlusParser.CondContext):
        pass

    # CalcPlusParser#cond가 만든 파스 트리를 종료한다.
    def exitCond(self, ctx:CalcPlusParser.CondContext):
        pass


    # CalcPlusParser#block가 만든 파스 트리에 진입한다.
    def enterBlock(self, ctx:CalcPlusParser.BlockContext):
        pass

    # CalcPlusParser#block가 만든 파스 트리를 종료한다.
    def exitBlock(self, ctx:CalcPlusParser.BlockContext):
        pass


    # CalcPlusParser#calc3가 만든 파스 트리에 진입한다.
    def enterCalc3(self, ctx:CalcPlusParser.Calc3Context):
        pass

    # CalcPlusParser#calc3가 만든 파스 트리를 종료한다.
    def exitCalc3(self, ctx:CalcPlusParser.Calc3Context):
        pass



del CalcPlusParser