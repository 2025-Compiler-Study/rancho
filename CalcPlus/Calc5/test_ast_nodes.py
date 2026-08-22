"""Unit tests for Calc5 AST node data structures."""

import unittest

from ast_nodes import AstNode, BinaryExpr, Expr, IntLiteral, VarRef


class AstNodeTest(unittest.TestCase):
    def test_expression_node_types_share_the_ast_hierarchy(self):
        self.assertIsInstance(IntLiteral(1), Expr)
        self.assertIsInstance(VarRef("total"), Expr)
        self.assertIsInstance(BinaryExpr("+", IntLiteral(1), IntLiteral(2)), Expr)
        self.assertIsInstance(IntLiteral(1), AstNode)

    def test_leaf_nodes_store_values_and_have_no_children(self):
        literal = IntLiteral(42)
        variable = VarRef("total")

        self.assertEqual(literal.value, 42)
        self.assertEqual(variable.name, "total")
        self.assertEqual(literal.children(), ())
        self.assertEqual(variable.children(), ())

    def test_binary_expression_keeps_left_and_right_children_in_order(self):
        left = IntLiteral(1)
        right = VarRef("total")
        expression = BinaryExpr("+", left, right)

        self.assertEqual(expression.op, "+")
        self.assertIs(expression.left, left)
        self.assertIs(expression.right, right)
        self.assertEqual(expression.children(), (left, right))

    def test_nodes_with_the_same_shape_compare_equal(self):
        self.assertEqual(
            BinaryExpr("*", IntLiteral(2), VarRef("count")),
            BinaryExpr("*", IntLiteral(2), VarRef("count")),
        )


if __name__ == "__main__":
    unittest.main()
