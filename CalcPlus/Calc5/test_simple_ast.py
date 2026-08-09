import importlib.util
import unittest

from simple_ast import Bin, Num, Var, format_ast, parse_expr


HAS_ANTLR = importlib.util.find_spec("antlr4") is not None


class SimpleAstFormatTest(unittest.TestCase):
    def test_format_manual_ast(self):
        ast = Bin("+", Bin("*", Num(5), Num(3)), Var("a"))

        self.assertEqual(format_ast(ast), "(+ (* 5 3) a)")


@unittest.skipUnless(HAS_ANTLR, "antlr4 Python runtime is not installed")
class SimpleAstParserTest(unittest.TestCase):
    def test_parse_expression_to_ast(self):
        ast = parse_expr("5 * 3 + a * (5 - 9 / 3)")

        self.assertEqual(
            ast,
            Bin(
                "+",
                Bin("*", Num(5), Num(3)),
                Bin("*", Var("a"), Bin("-", Num(5), Bin("/", Num(9), Num(3)))),
            ),
        )

    def test_format_parsed_ast(self):
        ast = parse_expr("5 * 3 + a * (5 - 9 / 3)")

        self.assertEqual(format_ast(ast), "(+ (* 5 3) (* a (- 5 (/ 9 3))))")


if __name__ == "__main__":
    unittest.main()
