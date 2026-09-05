"""Tests for Calc5 Markdown and Mermaid AST exports."""

import unittest

from ast_exporter import AstExporter
from calc5_ast import BinaryExpr, IntLiteral, VarRef


class AstExporterTest(unittest.TestCase):
    def setUp(self):
        self.source = "5 * 3 + a * (5 - 9 / 3)"
        self.expression = BinaryExpr(
            "+",
            BinaryExpr("*", IntLiteral(5), IntLiteral(3)),
            BinaryExpr(
                "*",
                VarRef("a"),
                BinaryExpr("-", IntLiteral(5), BinaryExpr("/", IntLiteral(9), IntLiteral(3))),
            ),
        )
        self.exporter = AstExporter()

    def test_markdown_includes_source_tree_and_evaluation_order(self):
        output = self.exporter.to_markdown(self.source, self.expression)

        self.assertIn("# Calc5 AST Report", output)
        self.assertIn("```calc\n5 * 3 + a * (5 - 9 / 3)\n```", output)
        self.assertIn("[n9] BinaryExpr(op='/')", output)
        self.assertIn("13. apply [n9] BinaryExpr(op='/')", output)
        self.assertNotIn("Parens", output)

    def test_mermaid_links_ast_edges_and_call_sequence(self):
        output = self.exporter.to_mermaid(self.source, self.expression)

        self.assertIn("flowchart TD", output)
        self.assertIn("N1 -->|left| N2", output)
        self.assertIn("N1 -->|right| N5", output)
        self.assertIn('S01["01 enter n1"]:::call', output)
        self.assertIn("S12 --> S13", output)


if __name__ == "__main__":
    unittest.main()
