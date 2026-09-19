"""Visualize Calc5 expression or program ASTs and their structural visit order."""

from __future__ import annotations

import argparse
from pathlib import Path

from calc5_ast import (
    Assign,
    AstNode,
    BinaryExpr,
    Block,
    Declare,
    IntLiteral,
    Program,
    ReadCall,
    VarRef,
    Write,
    build_expression,
    build_program,
)


class AstVisualizer:
    """Formats a Calc5 AST as a tree, trace, or Graphviz DOT graph."""

    def format(self, root: AstNode) -> str:
        """Return a tree and source-order structural visit trace."""
        node_ids = self._node_ids(root)
        tree_lines = ["AST 구조", *self._tree_lines(root, node_ids)]
        trace_lines = [
            "해석 호출 순서 (왼쪽 → 오른쪽 / 문장 위 → 아래)",
            *self._trace_lines(root, node_ids),
        ]
        return "\n".join([*tree_lines, "", *trace_lines])

    def to_dot(self, root: AstNode) -> str:
        """Return a dependency-free Graphviz DOT representation of ``root``."""
        node_ids = self._node_ids(root)
        lines = [
            "digraph Calc5Ast {",
            '  graph [label="Calc5 AST", labelloc="t"];',
            "  rankdir=TB;",
            '  node [fontname="Arial"];',
        ]

        for node, node_id in self._nodes_in_preorder(root, node_ids):
            label, shape, fillcolor = self._dot_node_style(node)
            lines.append(
                f'  {node_id} [label="{label}", shape="{shape}", '
                f'style="filled", fillcolor="{fillcolor}"];'
            )
            for index, child in enumerate(node.children()):
                relation = self._child_relation(node, index)
                lines.append(
                    f'  {node_id} -> {node_ids[id(child)]} [label="{relation}"];'
                )

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
            children = node.children()
            for index, child in enumerate(children):
                is_last = index == len(children) - 1
                branch = "└──" if is_last else "├──"
                relation = self._child_relation(node, index)
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
            elif isinstance(node, (Program, Block, Assign, Write)):
                steps.append(("enter", node))
                for child in node.children():
                    visit(child)
                steps.append(("apply", node))
            else:
                steps.append(("visit", node))

        visit(root)
        return [
            f"{number:02d}. {event} [{node_ids[id(node)]}] {self._label(node)}"
            for number, (event, node) in enumerate(steps, start=1)
        ]

    @staticmethod
    def _child_relation(node: AstNode, index: int) -> str:
        if isinstance(node, BinaryExpr):
            return ("left", "right")[index]
        if isinstance(node, (Assign, Write)):
            return "value"
        if isinstance(node, (Program, Block)):
            return f"stmt[{index}]"
        return f"child[{index}]"

    @staticmethod
    def _label(node: AstNode) -> str:
        if isinstance(node, Program):
            return "Program"
        if isinstance(node, Block):
            return "Block"
        if isinstance(node, Declare):
            return f"Declare(name='{node.name}')"
        if isinstance(node, Assign):
            return f"Assign(target='{node.target}')"
        if isinstance(node, Write):
            return "Write"
        if isinstance(node, ReadCall):
            return "ReadCall()"
        if isinstance(node, BinaryExpr):
            return f"BinaryExpr(op='{node.op}')"
        if isinstance(node, IntLiteral):
            return f"IntLiteral(value={node.value})"
        if isinstance(node, VarRef):
            return f"VarRef(name='{node.name}')"
        return type(node).__name__

    @staticmethod
    def _dot_node_style(node: AstNode) -> tuple[str, str, str]:
        if isinstance(node, Program):
            return "Program", "folder", "#dcfce7"
        if isinstance(node, Block):
            return "Block", "folder", "#fef3c7"
        if isinstance(node, Declare):
            return f"Declare\\nname: {node.name}", "box", "#f3f4f6"
        if isinstance(node, Assign):
            return f"Assign\\ntarget: {node.target}", "box", "#fde68a"
        if isinstance(node, Write):
            return "Write", "box", "#fed7aa"
        if isinstance(node, ReadCall):
            return "ReadCall", "ellipse", "#fed7aa"
        if isinstance(node, BinaryExpr):
            return f"BinaryExpr\\noperator: {node.op}", "box", "#dbeafe"
        if isinstance(node, IntLiteral):
            return f"IntLiteral\\nvalue: {node.value}", "ellipse", "#f3f4f6"
        if isinstance(node, VarRef):
            return f"VarRef\\nname: {node.name}", "ellipse", "#ede9fe"
        return type(node).__name__, "box", "#ffffff"


def main(argv: list[str] | None = None) -> int:
    """Render an expression by default, or a complete program with ``--program``."""
    parser = argparse.ArgumentParser(description="Calc5 AST visualizer")
    parser.add_argument("source", nargs="?", help="visualize할 Calc5 입력")
    parser.add_argument(
        "--program", action="store_true", help="입력을 expression 대신 program으로 파싱"
    )
    parser.add_argument("--dot", metavar="PATH", help="Graphviz DOT 파일을 저장할 경로")
    args = parser.parse_args(argv)

    source = args.source if args.source is not None else input("source> ")
    ast = build_program(source) if args.program else build_expression(source)
    visualizer = AstVisualizer()
    print(visualizer.format(ast))

    if args.dot:
        dot_path = Path(args.dot)
        dot_path.write_text(visualizer.to_dot(ast), encoding="utf-8")
        print(f"\nDOT 파일 저장: {dot_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
