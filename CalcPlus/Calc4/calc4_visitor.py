"""Calc4 실행 visitor."""

import operator

from CalcPlusParser import CalcPlusParser
from CalcPlusVisitor import CalcPlusVisitor

from symbol_table import SymbolTable


class Calc4Visitor(CalcPlusVisitor):
    def __init__(self, read_fn=None, write_fn=None):
        self.symbols = SymbolTable()
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
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    def visitDeclare(self, ctx: CalcPlusParser.DeclareContext):
        for token in ctx.VAR():
            # 선언 규칙은 SymbolTable 한 곳에서 검사
            self.symbols.declare(self._var_name(token))
        return None

    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        var_name = self._var_name(ctx.VAR())
        value = self.visit(ctx.expr())
        # 대입도 SymbolTable을 거치게 해야 일관적 처리 가능
        self.symbols.assign(var_name, value)
        return value

    def visitReadAssign(self, ctx: CalcPlusParser.ReadAssignContext):
        var_name = self._var_name(ctx.VAR())
        value = self.read_fn()
        # read() 결과도 일반 대입과 같은 선언 검사 규칙을 따름
        self.symbols.assign(var_name, value)
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
        # 블록은 새 스코프를 만들고, 끝나면 내부 선언을 버려야 한다.
        self.symbols.push_scope()
        try:
            for stmt in ctx.stmt():
                self.visit(stmt)
        finally:
            self.symbols.pop_scope()
        return None

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
        # 변수 읽기는 SymbolTable 조회로 통일해 선언 전 사용을 에러로 만든다.
        return self.symbols.lookup(var_name)

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
