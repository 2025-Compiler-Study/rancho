# Generated from CalcPlus.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# 참고:
# 이 파일은 ANTLR이 자동 생성한 Listener 뼈대입니다.
# 사람이 추가한 주석은 학습/유지보수용이며,
# CalcPlus.g4로 다시 생성하면 덮어써질 수 있습니다.


class CalcPlusListener(ParseTreeListener):
    """
    CalcPlus 파스 트리용 기본 Listener 클래스.

    호출 순서:
    - enterXxx: 노드에 "들어갈 때"(상향식 기준으로는 전위 순회 시점)
    - exitXxx: 노드에서 "나올 때"(자식 처리 완료 후)

    주로 다음 작업에 적합합니다.
    - 스코프 push/pop
    - 이벤트/로그 수집
    - 문법 경고 누적
    """

    # 진입 콜백: calc0 규칙 노드에 들어갈 때 호출.
    def enterCalc0(self, ctx:CalcPlusParser.Calc0Context):
        pass

    # 종료 콜백: calc0 규칙 노드 처리가 끝날 때 호출.
    def exitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        pass

    # 진입 콜백: expr의 #MulDiv 대안 노드에 들어갈 때 호출.
    # 형태: expr op expr, op는 '*' 또는 '/'.
    def enterMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        pass

    # 종료 콜백: #MulDiv 노드 처리가 끝날 때 호출.
    def exitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        pass

    # 진입 콜백: expr의 #AddSub 대안 노드에 들어갈 때 호출.
    # 형태: expr op expr, op는 '+' 또는 '-'.
    def enterAddSub(self, ctx:CalcPlusParser.AddSubContext):
        pass

    # 종료 콜백: #AddSub 노드 처리가 끝날 때 호출.
    def exitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        pass

    # 진입 콜백: expr의 #Var 대안 노드에 들어갈 때 호출.
    # 단일 VAR 토큰을 포함합니다.
    def enterVar(self, ctx:CalcPlusParser.VarContext):
        pass

    # 종료 콜백: #Var 노드 처리가 끝날 때 호출.
    def exitVar(self, ctx:CalcPlusParser.VarContext):
        pass

    # 진입 콜백: expr의 #Parens 대안 노드에 들어갈 때 호출.
    # 괄호로 둘러싼 내부 expr 1개를 포함합니다.
    def enterParens(self, ctx:CalcPlusParser.ParensContext):
        pass

    # 종료 콜백: #Parens 노드 처리가 끝날 때 호출.
    def exitParens(self, ctx:CalcPlusParser.ParensContext):
        pass

    # 진입 콜백: expr의 #Int 대안 노드에 들어갈 때 호출.
    # 단일 INT 토큰을 포함합니다.
    def enterInt(self, ctx:CalcPlusParser.IntContext):
        pass

    # 종료 콜백: #Int 노드 처리가 끝날 때 호출.
    def exitInt(self, ctx:CalcPlusParser.IntContext):
        pass

    # 진입 콜백: calc1 규칙 노드에 들어갈 때 호출.
    def enterCalc1(self, ctx:CalcPlusParser.Calc1Context):
        pass

    # 종료 콜백: calc1 규칙 노드 처리가 끝날 때 호출.
    def exitCalc1(self, ctx:CalcPlusParser.Calc1Context):
        pass

    # 진입 콜백: stmt의 #ExprAssign 대안 노드에 들어갈 때 호출.
    # 형태: VAR '=' expr ';'
    def enterExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        pass

    # 종료 콜백: #ExprAssign 노드 처리가 끝날 때 호출.
    def exitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        pass

    # 진입 콜백: stmt의 #IfElse 대안 노드에 들어갈 때 호출.
    # 형태: 'if' '(' cond ')' block ('else' block)?
    def enterIfElse(self, ctx:CalcPlusParser.IfElseContext):
        pass

    # 종료 콜백: #IfElse 노드 처리가 끝날 때 호출.
    def exitIfElse(self, ctx:CalcPlusParser.IfElseContext):
        pass

    # 진입 콜백: calc2 규칙 노드에 들어갈 때 호출.
    def enterCalc2(self, ctx:CalcPlusParser.Calc2Context):
        pass

    # 종료 콜백: calc2 규칙 노드 처리가 끝날 때 호출.
    def exitCalc2(self, ctx:CalcPlusParser.Calc2Context):
        pass

    # 진입 콜백: cond 규칙 노드에 들어갈 때 호출.
    # 형태: expr 비교연산자 expr
    def enterCond(self, ctx:CalcPlusParser.CondContext):
        pass

    # 종료 콜백: cond 규칙 노드 처리가 끝날 때 호출.
    def exitCond(self, ctx:CalcPlusParser.CondContext):
        pass

    # 진입 콜백: block 규칙 노드에 들어갈 때 호출.
    # 형태: '{' (stmt)* '}'
    def enterBlock(self, ctx:CalcPlusParser.BlockContext):
        pass

    # 종료 콜백: block 규칙 노드 처리가 끝날 때 호출.
    def exitBlock(self, ctx:CalcPlusParser.BlockContext):
        pass


del CalcPlusParser
