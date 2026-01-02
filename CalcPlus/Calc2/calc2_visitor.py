# calc2_visitor.py
"""Visitor-like evaluator for Calc-2 parse trees."""

from CalcPlusParser import CalcPlusParser


class Calc2Visitor:
    """Evaluates Calc-2 programs and returns final variable memory."""

    def __init__(self):
        self.memory: dict[str, int] = {}

    def visit(self, ctx):
        if ctx is None:
            return None
        method_name = f"visit{type(ctx).__name__}"
        method = getattr(self, method_name, None)
        if method is None:
            return self.visitChildren(ctx)
        return method(ctx)

    def visitChildren(self, ctx):
        result = None
        for child in ctx.getChildren():
            result = self.visit(child)
        return result

    def visitCalc2(self, ctx: CalcPlusParser.Calc2Context):
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        return dict(self.memory)

    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitIfElse(self, ctx: CalcPlusParser.IfElseContext):
        condition = self.visit(ctx.cond())
        if condition:
            self.visit(ctx.thenBlock)
        elif ctx.elseBlock is not None:
            self.visit(ctx.elseBlock)
        return None

    def visitBlock(self, ctx: CalcPlusParser.BlockContext):
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        return None

    def visitCond(self, ctx: CalcPlusParser.CondContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == "==":
            return left == right
        if op == "!=":
            return left != right
        if op == ">":
            return left > right
        if op == ">=":
            return left >= right
        if op == "<":
            return left < right
        if op == "<=":
            return left <= right
        raise ValueError(f"Unknown comparison operator: {op}")

    def visitVar(self, ctx: CalcPlusParser.VarContext):
        var_name = ctx.VAR().getText()
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
