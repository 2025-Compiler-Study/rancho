# calc1_visitor.py
"""Visitor 구현체로 Calc-1 변수 계산 과제 #1을 해결한다."""

from generated.CalcPlusVisitor import CalcPlusVisitor
from generated.CalcPlusParser import CalcPlusParser


class Calc1Visitor(CalcPlusVisitor):
    """calc1 진입부터 stmt 반복을 방문하며 변수 메모리를 유지한다."""

    def __init__(self):
        super().__init__()
        self.memory: dict[str, int] = {}

    def visitCalc1(self, ctx: CalcPlusParser.Calc1Context):
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        # dict 복사로 외부에서 내부 상태를 안전하게 사용하도록 함
        return dict(self.memory)

    '''
    시멘틱이란
    - 뒤에 있는 수식의 결과 해석 방식
    '''
    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitVar(self, ctx: CalcPlusParser.VarContext):
        var_name = ctx.VAR().getText()
        # 미정의 변수는 사양에 따라 0으로 취급하고 정의 집합에 추가
        if var_name not in self.memory:
            self.memory[var_name] = 0
        return self.memory[var_name]

    def visitInt(self, ctx: CalcPlusParser.IntContext):
        return int(ctx.INT().getText())

    def visitParens(self, ctx: CalcPlusParser.ParensContext):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: CalcPlusParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left * right if op == "*" else left / right

    def visitAddSub(self, ctx: CalcPlusParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left + right if op == "+" else left - right
