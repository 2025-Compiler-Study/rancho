"""Core tests for the compact Calc5 expression AST."""

import importlib.util
import unittest

from calc5_ast import (
    AstNode,
    BinaryExpr,
    Expr,
    IntLiteral,
    VarRef,
    build_expression,
    evaluate,
    format_ast,
)


HAS_ANTLR = importlib.util.find_spec("antlr4") is not None


def example_ast() -> BinaryExpr:
    return BinaryExpr(
        "+",
        BinaryExpr("*", IntLiteral(5), IntLiteral(3)),
        BinaryExpr(
            "*",
            VarRef("a"),
            BinaryExpr(
                "-",
                IntLiteral(5),
                BinaryExpr("/", IntLiteral(9), IntLiteral(3)),
            ),
        ),
    )


class AstNodeTest(unittest.TestCase):
    def test_leaf_nodes_store_their_semantic_value(self):
        literal = IntLiteral(5)
        variable = VarRef("a")

        self.assertIsInstance(literal, AstNode)
        self.assertIsInstance(literal, Expr)
        self.assertEqual(literal.value, 5)
        self.assertEqual(variable.name, "a")
        self.assertEqual(literal.children(), ())
        self.assertEqual(variable.children(), ())

    def test_binary_expression_keeps_ordered_children(self):
        left = IntLiteral(5)
        right = IntLiteral(3)
        expression = BinaryExpr("*", left, right)

        self.assertEqual(expression.op, "*")
        self.assertEqual(expression.children(), (left, right))


class AstBehaviorTest(unittest.TestCase):
    def test_formats_an_ast_without_parenthesis_nodes(self):
        self.assertEqual(
            format_ast(example_ast()),
            "(+ (* 5 3) (* a (- 5 (/ 9 3))))",
        )

    def test_evaluates_the_complete_example(self):
        self.assertEqual(evaluate(example_ast(), {"a": 4}), 23)


@unittest.skipUnless(HAS_ANTLR, "antlr4 Python runtime is not installed")
class AntlrAstBuilderTest(unittest.TestCase):
    def test_builds_integer_and_variable_leaves(self):
        self.assertEqual(build_expression("5"), IntLiteral(5))
        self.assertEqual(build_expression("a"), VarRef("a"))

    def test_operator_precedence_is_preserved_by_the_tree(self):
        self.assertEqual(
            build_expression("1 + 2 * 3"),
            BinaryExpr(
                "+",
                IntLiteral(1),
                BinaryExpr("*", IntLiteral(2), IntLiteral(3)),
            ),
        )

    def test_parentheses_change_grouping_without_becoming_a_node(self):
        self.assertEqual(
            build_expression("(1 + 2) * 3"),
            BinaryExpr(
                "*",
                BinaryExpr("+", IntLiteral(1), IntLiteral(2)),
                IntLiteral(3),
            ),
        )

    def test_builds_the_complete_example(self):
        expression = build_expression("5 * 3 + a * (5 - 9 / 3)")

        self.assertEqual(expression, example_ast())
        self.assertEqual(evaluate(expression, {"a": 4}), 23)


if __name__ == "__main__":
    unittest.main()
