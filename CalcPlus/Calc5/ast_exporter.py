"""Export a Calc5 expression AST as Markdown or Mermaid."""

from __future__ import annotations

import argparse
from pathlib import Path

from calc5_ast import AstNode, BinaryExpr, IntLiteral, VarRef
from calc5_ast import build_expression


class AstExporter:
    """Creates portable text representations of an expression AST."""

    def to_markdown(self, source: str, root: AstNode) -> str:
        """Return a Markdown report with AST structure and evaluation trace."""
        node_ids, nodes = self._nodes(root)
        tree = "\n".join(self._tree_lines(root, node_ids))
        trace = "\n".join(self._trace_lines(root, node_ids))
        return "\n".join(
            [
                "# Calc5 AST Report",
                "",
                "## Input expression",
                "",
                "```calc",
                source,
                "```",
                "",
                "## AST structure",
                "",
                "```text",
                tree,
                "```",
                "",
                "## Evaluation call order",
                "",
                "`eval_expr` visits the left child, then the right child, and applies a binary operator last.",
                "",
                "```text",
                trace,
                "```",
                "",
                "Parentheses are intentionally absent: their grouping is preserved by the AST parent-child structure.",
            ]
        )

    def to_mermaid(self, source: str, root: AstNode) -> str:
        """Return a Mermaid flowchart for the AST and its call sequence."""
        node_ids, nodes = self._nodes(root)
        lines = [
            "---",
            "title: Calc5 AST and evaluation order",
            "---",
            "flowchart TD",
            "    classDef binary fill:#dbeafe,stroke:#2563eb,color:#172033;",
            "    classDef literal fill:#f3f4f6,stroke:#6b7280,color:#172033;",
            "    classDef variable fill:#ede9fe,stroke:#7c3aed,color:#172033;",
            "    classDef call fill:#fffbeb,stroke:#d97706,color:#172033;",
            "",
            "    subgraph AST[AST structure]",
        ]

        for node in nodes:
            node_id = node_ids[id(node)].upper()
            lines.append(
                f'        {node_id}["{self._mermaid_escape(self._mermaid_label(node))}"]:::{self._kind(node)}'
            )
            if isinstance(node, BinaryExpr):
                lines.append(f"        {node_id} -->|left| {node_ids[id(node.left)].upper()}")
                lines.append(f"        {node_id} -->|right| {node_ids[id(node.right)].upper()}")

        lines.extend(["    end", "", "    subgraph TRACE[Evaluation call order: eval_expr]"])
        trace = self._trace_steps(root)
        for index, (event, node) in enumerate(trace, start=1):
            step_id = f"S{index:02d}"
            node_id = node_ids[id(node)]
            label = f"{index:02d} {event} {node_id}"
            lines.append(f'        {step_id}["{self._mermaid_escape(label)}"]:::call')
            if index > 1:
                lines.append(f"        S{index - 1:02d} --> {step_id}")

        lines.extend(
            [
                "    end",
                "",
                f"    %% Source: {source}",
                "    %% Parentheses are not AST nodes; the AST edges preserve grouping.",
            ]
        )
        return "\n".join(lines)

    def _nodes(self, root: AstNode) -> tuple[dict[int, str], list[AstNode]]:
        ids: dict[int, str] = {}
        nodes: list[AstNode] = []

        def visit(node: AstNode) -> None:
            ids[id(node)] = f"n{len(nodes) + 1}"
            nodes.append(node)
            for child in node.children():
                visit(child)

        visit(root)
        return ids, nodes

    def _tree_lines(self, root: AstNode, node_ids: dict[int, str]) -> list[str]:
        lines = [f"[{node_ids[id(root)]}] {self._label(root)}"]

        def visit(node: AstNode, prefix: str) -> None:
            if not isinstance(node, BinaryExpr):
                return
            for index, (relation, child) in enumerate((("left", node.left), ("right", node.right))):
                is_last = index == 1
                branch = "└──" if is_last else "├──"
                lines.append(
                    f"{prefix}{branch} {relation}: [{node_ids[id(child)]}] {self._label(child)}"
                )
                visit(child, prefix + ("    " if is_last else "│   "))

        visit(root, "")
        return lines

    def _trace_lines(self, root: AstNode, node_ids: dict[int, str]) -> list[str]:
        return [
            f"{number:02d}. {event} [{node_ids[id(node)]}] {self._label(node)}"
            for number, (event, node) in enumerate(self._trace_steps(root), start=1)
        ]

    @staticmethod
    def _trace_steps(root: AstNode) -> list[tuple[str, AstNode]]:
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
        return steps

    @staticmethod
    def _label(node: AstNode) -> str:
        if isinstance(node, BinaryExpr):
            return f"BinaryExpr(op='{node.op}')"
        if isinstance(node, IntLiteral):
            return f"IntLiteral(value={node.value})"
        if isinstance(node, VarRef):
            return f"VarRef(name='{node.name}')"
        return type(node).__name__

    def _mermaid_label(self, node: AstNode) -> str:
        if isinstance(node, BinaryExpr):
            return f"BinaryExpr<br/>operator: {node.op}"
        if isinstance(node, IntLiteral):
            return f"IntLiteral<br/>value: {node.value}"
        if isinstance(node, VarRef):
            return f"VarRef<br/>name: {node.name}"
        return self._label(node)

    @staticmethod
    def _mermaid_escape(value: str) -> str:
        return value.replace("&", "&amp;").replace("\"", "&quot;").replace("<", "&lt;").replace(">", "&gt;")

    @staticmethod
    def _kind(node: AstNode) -> str:
        if isinstance(node, BinaryExpr):
            return "binary"
        if isinstance(node, IntLiteral):
            return "literal"
        if isinstance(node, VarRef):
            return "variable"
        return "call"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export a Calc5 AST as Markdown or Mermaid")
    parser.add_argument("expression", help="export할 Calc5 식")
    parser.add_argument("--format", choices=("markdown", "mermaid"), default="markdown")
    parser.add_argument("--output", help="출력 파일 경로; 생략하면 표준 출력")
    args = parser.parse_args(argv)

    root = build_expression(args.expression)
    exporter = AstExporter()
    output = (
        exporter.to_markdown(args.expression, root)
        if args.format == "markdown"
        else exporter.to_mermaid(args.expression, root)
    )

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"파일 저장: {args.output}")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
