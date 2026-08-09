"""Tiny Parse Tree -> AST example for Calc5 expressions only."""

from __future__ import annotations

from dataclasses import dataclass


class Expr:
    pass


@dataclass(frozen=True)
class Num(Expr):
    value: int


@dataclass(frozen=True)
class Var(Expr):
    name: str


@dataclass(frozen=True)
class Bin(Expr):
    op: str
    left: Expr
    right: Expr


class AstBuilder:
    def visit(self, tree):
        return tree.accept(self)

    def visitInt(self, ctx):
        return Num(int(ctx.getText()))

    def visitVar(self, ctx):
        return Var(ctx.getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        return self._bin(ctx)

    def visitAddSub(self, ctx):
        return self._bin(ctx)

    def _bin(self, ctx):
        return Bin(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr(0)),
            self.visit(ctx.expr(1)),
        )


def parse_expr(source: str) -> Expr:
    from antlr4 import CommonTokenStream, InputStream

    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser

    lexer = CalcPlusLexer(InputStream(source))
    parser = CalcPlusParser(CommonTokenStream(lexer))
    tree = parser.expr()

    if parser.getNumberOfSyntaxErrors():
        raise SyntaxError(source)

    return AstBuilder().visit(tree)


def format_ast(expr: Expr) -> str:
    if isinstance(expr, Num):
        return str(expr.value)
    if isinstance(expr, Var):
        return expr.name
    if isinstance(expr, Bin):
        return f"({expr.op} {format_ast(expr.left)} {format_ast(expr.right)})"
    raise TypeError(expr)


if __name__ == "__main__":
    ast = parse_expr("5 * 3 + a * (5 - 9 / 3)")
    print(format_ast(ast))
