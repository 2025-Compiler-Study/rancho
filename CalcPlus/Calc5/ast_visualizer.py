"""Visualize a Calc5 expression AST and its recursive evaluation order.

The visualizer does not execute an expression. It shows the recursive order in
which ``eval_expr`` would enter an operation, visit its left and right
operands, then apply that operation. Parentheses are absent from the AST: the
parent-child relationship preserves their grouping.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ast_nodes import AstNode, BinaryExpr, IntLiteral, VarRef


class ExpressionAstBuilder:
    """Build the expression subset of Calc5's AST from an ANTLR parse tree."""

    def visit(self, tree):
        return tree.accept(self)

    def visitInt(self, ctx):
        return IntLiteral(int(ctx.getText()))

    def visitVar(self, ctx):
        return VarRef(ctx.getText())

    def visitParens(self, ctx):
        """Discard parentheses while retaining their grouping in the child tree."""
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


class AstVisualizer:
    """Formats an expression AST as a tree, trace, or Graphviz DOT graph."""

    def format(self, root: AstNode) -> str:
        """Return a tree and left-to-right recursive evaluation trace."""
        node_ids = self._node_ids(root)
        tree_lines = ["AST 구조", *self._tree_lines(root, node_ids)]
        trace_lines = [
            "해석 호출 순서 (eval_expr, 왼쪽 → 오른쪽)",
            *self._trace_lines(root, node_ids),
        ]
        return "\n".join([*tree_lines, "", *trace_lines])

    def to_dot(self, root: AstNode) -> str:
        """Return a dependency-free Graphviz DOT representation of ``root``."""
        node_ids = self._node_ids(root)
        lines = [
            "digraph Calc5Ast {",
            '  graph [label="Calc5 expression AST", labelloc="t"];',
            "  rankdir=TB;",
            '  node [fontname="Arial"];',
        ]

        for node, node_id in self._nodes_in_preorder(root, node_ids):
            label, shape, fillcolor = self._dot_node_style(node)
            lines.append(
                f'  {node_id} [label="{label}", shape="{shape}", '
                f'style="filled", fillcolor="{fillcolor}"];'
            )
            if isinstance(node, BinaryExpr):
                lines.append(f'  {node_id} -> {node_ids[id(node.left)]} [label="left"];')
                lines.append(f'  {node_id} -> {node_ids[id(node.right)]} [label="right"];')

        lines.append("}")
        return "\n".join(lines)

    def _node_ids(self, root: AstNode) -> dict[int, str]:
        """Give each node a stable pre-order ID without requiring it be hashable."""
        nodes: dict[int, str] = {}

        def visit(node: AstNode) -> None:
            nodes[id(node)] = f"n{len(nodes) + 1}"
            for child in node.children():
                visit(child)

        visit(root)
        return nodes

    def _nodes_in_preorder(
        self, root: AstNode, node_ids: dict[int, str]
    ) -> list[tuple[AstNode, str]]:
        nodes: list[tuple[AstNode, str]] = []

        def visit(node: AstNode) -> None:
            nodes.append((node, node_ids[id(node)]))
            for child in node.children():
                visit(child)

        visit(root)
        return nodes

    def _tree_lines(self, root: AstNode, node_ids: dict[int, str]) -> list[str]:
        lines = [f"[{node_ids[id(root)]}] {self._label(root)}"]

        def visit(node: AstNode, prefix: str) -> None:
            if not isinstance(node, BinaryExpr):
                return

            children = (("left", node.left), ("right", node.right))
            for index, (relation, child) in enumerate(children):
                is_last = index == len(children) - 1
                branch = "└──" if is_last else "├──"
                lines.append(
                    f"{prefix}{branch} {relation}: [{node_ids[id(child)]}] "
                    f"{self._label(child)}"
                )
                visit(child, prefix + ("    " if is_last else "│   "))

        visit(root, "")
        return lines

    def _trace_lines(self, root: AstNode, node_ids: dict[int, str]) -> list[str]:
        steps: list[tuple[str, AstNode]] = []

        def visit(node: AstNode) -> None:
            if isinstance(node, BinaryExpr):
                steps.append(("enter", node))
                visit(node.left)
                visit(node.right)
                steps.append(("apply", node))
            else:
                steps.append(("visit", node))

        visit(root)
        return [
            f"{number:02d}. {event} [{node_ids[id(node)]}] {self._label(node)}"
            for number, (event, node) in enumerate(steps, start=1)
        ]

    @staticmethod
    def _label(node: AstNode) -> str:
        if isinstance(node, BinaryExpr):
            return f"BinaryExpr(op='{node.op}')"
        if isinstance(node, IntLiteral):
            return f"IntLiteral(value={node.value})"
        if isinstance(node, VarRef):
            return f"VarRef(name='{node.name}')"
        return type(node).__name__

    @staticmethod
    def _dot_node_style(node: AstNode) -> tuple[str, str, str]:
        if isinstance(node, BinaryExpr):
            return f"BinaryExpr\\noperator: {node.op}", "box", "#dbeafe"
        if isinstance(node, IntLiteral):
            return f"IntLiteral\\nvalue: {node.value}", "ellipse", "#f3f4f6"
        if isinstance(node, VarRef):
            return f"VarRef\\nname: {node.name}", "ellipse", "#ede9fe"
        return type(node).__name__, "box", "#ffffff"


def build_expression(source: str) -> AstNode:
    """Parse one complete expression and build its AST."""
    from antlr4 import CommonTokenStream, InputStream
    from antlr4.Token import Token

    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser

    lexer = CalcPlusLexer(InputStream(source))
    parser = CalcPlusParser(CommonTokenStream(lexer))
    tree = parser.expr()

    if parser.getNumberOfSyntaxErrors() or parser.getCurrentToken().type != Token.EOF:
        raise SyntaxError(f"유효한 식이 아닙니다: {source!r}")

    return ExpressionAstBuilder().visit(tree)


def main(argv: list[str] | None = None) -> int:
    """Render an expression supplied as an argument, or prompt interactively."""
    parser = argparse.ArgumentParser(
        description="Calc5 expression AST and evaluation-order visualizer"
    )
    parser.add_argument("expression", nargs="?", help="visualize할 Calc5 식")
    parser.add_argument("--dot", metavar="PATH", help="Graphviz DOT 파일을 저장할 경로")
    args = parser.parse_args(argv)

    source = args.expression if args.expression is not None else input("expression> ")
    ast = build_expression(source)
    visualizer = AstVisualizer()
    print(visualizer.format(ast))

    if args.dot:
        dot_path = Path(args.dot)
        dot_path.write_text(visualizer.to_dot(ast), encoding="utf-8")
        print(f"\nDOT 파일 저장: {dot_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
