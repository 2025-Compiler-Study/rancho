"""Tests for the expression AST visualizer."""

import importlib.util
import unittest

from calc5_ast import BinaryExpr, IntLiteral, VarRef, build_expression
from ast_visualizer import AstVisualizer


HAS_ANTLR = importlib.util.find_spec("antlr4") is not None


class AstVisualizerFormatTest(unittest.TestCase):
    def setUp(self):
        self.expression = BinaryExpr(
            "+",
            BinaryExpr("*", IntLiteral(5), IntLiteral(3)),
            BinaryExpr(
                "*",
                VarRef("a"),
                BinaryExpr("-", IntLiteral(5), BinaryExpr("/", IntLiteral(9), IntLiteral(3))),
            ),
        )

    def test_format_shows_grouping_as_tree_without_parenthesis_node(self):
        output = AstVisualizer().format(self.expression)

        self.assertIn("[n1] BinaryExpr(op='+')", output)
        self.assertIn("left: [n2] BinaryExpr(op='*')", output)
        self.assertIn("right: [n5] BinaryExpr(op='*')", output)
        self.assertIn("[n7] BinaryExpr(op='-')", output)
        self.assertNotIn("Parens", output)

    def test_format_lists_left_to_right_evaluation_calls(self):
        output = AstVisualizer().format(self.expression)

        expected_trace = [
            "01. enter [n1] BinaryExpr(op='+')",
            "02. enter [n2] BinaryExpr(op='*')",
            "03. visit [n3] IntLiteral(value=5)",
            "05. apply [n2] BinaryExpr(op='*')",
            "06. enter [n5] BinaryExpr(op='*')",
            "10. enter [n9] BinaryExpr(op='/')",
            "13. apply [n9] BinaryExpr(op='/')",
            "16. apply [n1] BinaryExpr(op='+')",
        ]

        for line in expected_trace:
            self.assertIn(line, output)

    def test_dot_uses_the_same_nodes_and_child_labels(self):
        dot = AstVisualizer().to_dot(self.expression)

        self.assertIn('n1 [label="BinaryExpr\\noperator: +", shape="box"', dot)
        self.assertIn('n1 -> n2 [label="left"]', dot)
        self.assertIn('n1 -> n5 [label="right"]', dot)


@unittest.skipUnless(HAS_ANTLR, "antlr4 Python runtime is not installed")
class AstVisualizerParserTest(unittest.TestCase):
    def test_parenthesized_expression_is_built_without_a_parenthesis_node(self):
        ast = build_expression("5 * 3 + a * (5 - 9 / 3)")

        self.assertEqual(ast.op, "+")
        self.assertEqual(ast.left.op, "*")
        self.assertEqual(ast.right.op, "*")
        self.assertEqual(ast.right.right.op, "-")
        self.assertEqual(ast.right.right.right.op, "/")


if __name__ == "__main__":
    unittest.main()
