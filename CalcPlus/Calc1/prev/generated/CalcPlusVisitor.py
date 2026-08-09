# Generated from CalcPlus.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalcPlusParser import CalcPlusParser
else:
    from CalcPlusParser import CalcPlusParser

# 참고:
# 이 파일은 ANTLR이 자동 생성한 방문자(Visitor) 뼈대입니다.
# 사람이 추가한 주석은 학습/유지보수용이며,
# CalcPlus.g4로 다시 생성하면 덮어써질 수 있습니다.


class CalcPlusVisitor(ParseTreeVisitor):
    """
    CalcPlus 파스 트리용 기본 Visitor 클래스.

    매핑 규칙:
    - g4 규칙 `foo` -> `visitFoo` 메서드 생성
    - 라벨 대안 `#Bar` -> `visitBar` 메서드 생성
    - 기본 구현은 `visitChildren(ctx)`를 호출해
      자식 노드들을 재귀 방문만 수행합니다.

    실사용 시에는 필요한 메서드만 오버라이드해서
    계산기, 인터프리터, 타입체커 등을 구현합니다.
    """

    # calc0: expr EOF;
    # 식 1개를 프로그램 시작 규칙으로 파싱한 루트 노드 방문.
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visitChildren(ctx)

    # expr: expr ('*'|'/') expr # MulDiv
    # 곱셈/나눗셈 식 노드 방문.
    def visitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        return self.visitChildren(ctx)

    # expr: expr ('+'|'-') expr # AddSub
    # 덧셈/뺄셈 식 노드 방문.
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        return self.visitChildren(ctx)

    # expr: VAR # Var
    # 변수 참조 식 노드 방문.
    def visitVar(self, ctx:CalcPlusParser.VarContext):
        return self.visitChildren(ctx)

    # expr: '(' expr ')' # Parens
    # 괄호로 감싼 하위 식 노드 방문.
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        return self.visitChildren(ctx)

    # expr: INT # Int
    # 정수 리터럴 노드 방문.
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        return self.visitChildren(ctx)

    # calc1: (stmt)+ EOF;
    # 문장 중심 프로그램(대입/if-else)을 시작 규칙으로 방문.
    def visitCalc1(self, ctx:CalcPlusParser.Calc1Context):
        return self.visitChildren(ctx)

    # stmt: VAR '=' expr ';' # ExprAssign
    # 대입문 노드 방문.
    def visitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        return self.visitChildren(ctx)

    # stmt: 'if' '(' cond ')' block ('else' block)? # IfElse
    # 조건문 노드 방문(else 블록은 선택).
    def visitIfElse(self, ctx:CalcPlusParser.IfElseContext):
        return self.visitChildren(ctx)

    # calc2: (stmt)+ EOF;
    # calc1과 유사한 문장 시작 규칙 노드 방문.
    def visitCalc2(self, ctx:CalcPlusParser.Calc2Context):
        return self.visitChildren(ctx)

    # cond: expr ('=='|'!='|'>'|'>='|'<'|'<=') expr;
    # 비교 조건식 노드 방문.
    def visitCond(self, ctx:CalcPlusParser.CondContext):
        return self.visitChildren(ctx)

    # block: '{' (stmt)* '}';
    # 중괄호 블록 노드 방문.
    def visitBlock(self, ctx:CalcPlusParser.BlockContext):
        return self.visitChildren(ctx)


del CalcPlusParser
