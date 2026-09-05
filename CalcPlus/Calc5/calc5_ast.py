"""Compact Calc5 expression AST, ANTLR builder, formatter, and evaluator.

The module intentionally supports expressions only. Statement and program
nodes can be added after the expression pipeline is stable.
"""

from __future__ import annotations

from collections.abc import Mapping


class AstNode:
    """Base class for every Calc5 AST node."""

    def children(self) -> tuple[AstNode, ...]:
        return ()

    def __eq__(self, other: object) -> bool:
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        fields = ", ".join(
            f"{name}={value!r}" for name, value in self.__dict__.items()
        )
        return f"{type(self).__name__}({fields})"


class Expr(AstNode):
    """Base class for AST nodes that evaluate to an integer."""


class IntLiteral(Expr):
    def __init__(self, value: int):
        self.value = value


class VarRef(Expr):
    def __init__(self, name: str):
        self.name = name


class BinaryExpr(Expr):
    def __init__(self, op: str, left: Expr, right: Expr):
        self.op = op
        self.left = left
        self.right = right

    def children(self) -> tuple[Expr, Expr]:
        return self.left, self.right


class AstBuilder:
    """Build the expression subset of Calc5's AST from an ANTLR parse tree."""

    def visit(self, tree):
        return tree.accept(self)

    def visitInt(self, ctx):
        return IntLiteral(int(ctx.getText()))

    def visitVar(self, ctx):
        return VarRef(ctx.getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        return self._binary_expr(ctx)

    def visitAddSub(self, ctx):
        return self._binary_expr(ctx)

    def _binary_expr(self, ctx):
        return BinaryExpr(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr(0)),
            self.visit(ctx.expr(1)),
        )


def build_expression(source: str) -> Expr:
    """Parse one complete Calc5 expression and return its AST."""
    from antlr4 import CommonTokenStream, InputStream
    from antlr4.Token import Token

    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser

    lexer = CalcPlusLexer(InputStream(source))
    parser = CalcPlusParser(CommonTokenStream(lexer))
    tree = parser.expr()

    if parser.getNumberOfSyntaxErrors() or parser.getCurrentToken().type != Token.EOF:
        raise SyntaxError(f"유효한 식이 아닙니다: {source!r}")

    return AstBuilder().visit(tree)


def format_ast(expr: Expr) -> str:
    """Return a compact LISP-style representation of an expression AST."""
    if isinstance(expr, IntLiteral):
        return str(expr.value)
    if isinstance(expr, VarRef):
        return expr.name
    if isinstance(expr, BinaryExpr):
        return f"({expr.op} {format_ast(expr.left)} {format_ast(expr.right)})"
    raise TypeError(f"지원하지 않는 AST 노드입니다: {type(expr).__name__}")


def evaluate(expr: Expr, variables: Mapping[str, int]) -> int:
    """Evaluate an expression recursively using the supplied variable values."""
    if isinstance(expr, IntLiteral):
        return expr.value
    if isinstance(expr, VarRef):
        return variables[expr.name]
    if not isinstance(expr, BinaryExpr):
        raise TypeError(f"지원하지 않는 AST 노드입니다: {type(expr).__name__}")

    left = evaluate(expr.left, variables)
    right = evaluate(expr.right, variables)

    if expr.op == "+":
        return left + right
    if expr.op == "-":
        return left - right
    if expr.op == "*":
        return left * right
    if expr.op == "/":
        return left // right
    raise ValueError(f"지원하지 않는 연산자입니다: {expr.op}")
