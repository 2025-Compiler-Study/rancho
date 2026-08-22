"""Tests for the browser-based AST visualizer."""

import unittest

from ast_html_visualizer import render_html
from ast_nodes import BinaryExpr, IntLiteral, VarRef


def example_basic_ast() -> BinaryExpr:
    return BinaryExpr("+", IntLiteral(1), IntLiteral(2))


def example_parenthesized_ast() -> BinaryExpr:
    return BinaryExpr(
        "*",
        BinaryExpr("+", IntLiteral(1), IntLiteral(2)),
        IntLiteral(3),
    )


class HtmlAstVisualizerTest(unittest.TestCase):
    def setUp(self):
        self.expression = BinaryExpr(
            "+", BinaryExpr("*", IntLiteral(5), IntLiteral(3)), VarRef("a")
        )

    def test_html_contains_tree_trace_and_step_controls(self):
        page = render_html("5 * 3 + a", self.expression)

        self.assertIn('const visualizerData = ', page)
        self.assertIn('"rootId": "n1"', page)
        self.assertIn('"event": "apply"', page)
        self.assertIn('이전 단계', page)
        self.assertIn('다음 단계', page)
        self.assertIn("selectNode", page)

    def test_html_escapes_closing_script_text_in_the_source(self):
        page = render_html("x </script> y", self.expression)

        self.assertIn('x <\\/script> y', page)

    def test_demo_ast_is_the_smallest_binary_expression(self):
        expression = example_basic_ast()
        page = render_html("1 + 2", expression)
        self.assertIn("IntLiteral(value=1)", page)
        self.assertIn("BinaryExpr", page)
        self.assertIn("left", page)

        self.assertEqual(expression, BinaryExpr("+", IntLiteral(1), IntLiteral(2)))


    def test_parenthesized_demo_keeps_grouping_without_a_parenthesis_node(self):
        expression = example_parenthesized_ast()

        self.assertEqual(
            expression,
            BinaryExpr("*", BinaryExpr("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)),
        )
        self.assertNotIn("Parenthesis", render_html("(1 + 2) * 3", expression))


if __name__ == "__main__":
    unittest.main()
