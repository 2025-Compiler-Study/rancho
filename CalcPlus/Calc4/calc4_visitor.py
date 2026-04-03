"""Calc4 visitor 골격.

구현 전에는 각 의미 규칙이 명시적으로 비어 있음을 드러내기 위해
`NotImplementedError`를 발생시킨다.
"""

import operator

from CalcPlusParser import CalcPlusParser
from CalcPlusVisitor import CalcPlusVisitor

from symbol_table import SymbolTable


class Calc4Visitor(CalcPlusVisitor):
    def __init__(self, read_fn=None, write_fn=None):
        self.symbols = SymbolTable()
        self.memory: dict[str, int] = {}
        self.outputs: list[int] = []
        self.read_fn = read_fn or self._default_read
        self.write_fn = write_fn or self._default_write

    def _default_read(self):
        return int(input())

    def _default_write(self, value: int):
        print(value)

    def _var_name(self, token) -> str:
        return token.getText()

    def _binary_op(self, ctx, op_map: dict[str, callable]):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return op_map[op](left, right)

    def _comparison(self, ctx, op_map: dict[str, callable]):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return op_map[op](left, right)

    def visitCalc4(self, ctx: CalcPlusParser.Calc4Context):
        raise NotImplementedError("Calc4 프로그램 실행을 구현하세요.")

    def visitDeclare(self, ctx: CalcPlusParser.DeclareContext):
        raise NotImplementedError("변수 선언 처리를 구현하세요.")

    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        var_name = self._var_name(ctx.VAR())
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitReadAssign(self, ctx: CalcPlusParser.ReadAssignContext):
        var_name = self._var_name(ctx.VAR())
        value = self.read_fn()
        self.memory[var_name] = value
        return value

    def visitWrite(self, ctx: CalcPlusParser.WriteContext):
        value = self.visit(ctx.expr())
        self.outputs.append(value)
        self.write_fn(value)
        return value

    def visitIfElse(self, ctx: CalcPlusParser.IfElseContext):
        condition = self.visit(ctx.cond())
        if condition:
            self.visit(ctx.thenBlock)
        elif ctx.elseBlock is not None:
            self.visit(ctx.elseBlock)
        return None

    def visitStmtBlock(self, ctx: CalcPlusParser.StmtBlockContext):
        return self.visit(ctx.block())

    def visitBlock(self, ctx: CalcPlusParser.BlockContext):
        raise NotImplementedError("블록 scope 진입/탈출을 구현하세요.")

    def visitCond(self, ctx: CalcPlusParser.CondContext):
        return self._comparison(
            ctx,
            {
                "==": operator.eq,
                "!=": operator.ne,
                ">": operator.gt,
                ">=": operator.ge,
                "<": operator.lt,
                "<=": operator.le,
            }
        )

    def visitVar(self, ctx: CalcPlusParser.VarContext):
        var_name = self._var_name(ctx.VAR())
        if var_name not in self.memory:
            return var_name
        return self.memory[var_name]

    def visitInt(self, ctx: CalcPlusParser.IntContext):
        return int(ctx.INT().getText())

    def visitParens(self, ctx: CalcPlusParser.ParensContext):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: CalcPlusParser.MulDivContext):
        return self._binary_op(
            ctx,
            {
                "*": operator.mul,
                "/": operator.truediv,
            },
        )

    def visitAddSub(self, ctx: CalcPlusParser.AddSubContext):
        return self._binary_op(
            ctx,
            {
                "+": operator.add,
                "-": operator.sub,
            },
        )
