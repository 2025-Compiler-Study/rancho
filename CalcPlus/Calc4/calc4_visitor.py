"""Calc4 visitor 골격.

구현 전에는 각 의미 규칙이 명시적으로 비어 있음을 드러내기 위해
`NotImplementedError`를 발생시킨다.
"""

from CalcPlusParser import CalcPlusParser
from CalcPlusVisitor import CalcPlusVisitor

from symbol_table import SymbolTable


class Calc4Visitor(CalcPlusVisitor):
    def __init__(self, read_fn=None, write_fn=None):
        self.symbols = SymbolTable()
        self.read_fn = read_fn or self._default_read
        self.write_fn = write_fn or self._default_write

    def _default_read(self):
        return int(input())

    def _default_write(self, value: int):
        print(value)

    def _var_name(self, token) -> str:
        return token.getText()

    def _binary_op(self, ctx, op_map: dict[str, callable]):
        raise NotImplementedError(
            f"{type(ctx).__name__}의 좌/우 식 계산과 연산자 분기를 구현하세요."
        )

    def _comparison(self, ctx, op_map: dict[str, callable]):
        raise NotImplementedError(
            f"{type(ctx).__name__}의 비교 연산 평가를 구현하세요."
        )

    def visitCalc4(self, ctx: CalcPlusParser.Calc4Context):
        raise NotImplementedError("Calc4 프로그램 실행을 구현하세요.")

    def visitDeclare(self, ctx: CalcPlusParser.DeclareContext):
        raise NotImplementedError("변수 선언 처리를 구현하세요.")

    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        raise NotImplementedError("대입문 처리를 구현하세요.")

    def visitReadAssign(self, ctx: CalcPlusParser.ReadAssignContext):
        raise NotImplementedError("read() 대입 처리를 구현하세요.")

    def visitWrite(self, ctx: CalcPlusParser.WriteContext):
        raise NotImplementedError("write() 출력을 구현하세요.")

    def visitIfElse(self, ctx: CalcPlusParser.IfElseContext):
        raise NotImplementedError("if/else 분기를 구현하세요.")

    def visitStmtBlock(self, ctx: CalcPlusParser.StmtBlockContext):
        raise NotImplementedError("블록 문장 방문을 구현하세요.")

    def visitBlock(self, ctx: CalcPlusParser.BlockContext):
        raise NotImplementedError("블록 scope 진입/탈출을 구현하세요.")

    def visitCond(self, ctx: CalcPlusParser.CondContext):
        raise NotImplementedError("조건식 평가를 구현하세요.")

    def visitVar(self, ctx: CalcPlusParser.VarContext):
        # raise NotImplementedError("변수 조회를 구현하세요.")
        var_name = ctx.VAR().getText()
        if var_name not in self.memory:
            raise NotImplementedError(f"{var_name}는 정의되지 않았습니다.")
            # throw error
            # self.memory[var_name] = 0
        return self.memory[var_name]

    def visitInt(self, ctx: CalcPlusParser.IntContext):
        # raise NotImplementedError("정수 리터럴 평가를 구현하세요.")
        var = int(ctx.INT().getText())
        return var

    def visitParens(self, ctx: CalcPlusParser.ParensContext):
        raise NotImplementedError("괄호식 평가를 구현하세요.")

    def visitMulDiv(self, ctx: CalcPlusParser.MulDivContext):
        # raise NotImplementedError("곱셈/나눗셈 평가를 구현하세요.")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        result = left / right if op == '/' else left * right 
        return result

    def visitAddSub(self, ctx: CalcPlusParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        result = left - right if op == '-' else left + right 
        return result
