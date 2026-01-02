# test_calc2.py
import unittest
from antlr4 import InputStream, CommonTokenStream
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from calc2_visitor import Calc2Visitor


def parse_program(program: str):
    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(stream)
    return parser.calc2()


class Calc2VisitorTest(unittest.TestCase):
    def test_if_else_then_branch(self):
        program = "\n".join(
            [
                "a = 1;",
                "if (a >= 1) {",
                "    b = a + 2;",
                "    c = b * 3;",
                "} else {",
                "    b = a;",
                "    c = b;",
                "}",
                "a = a + 1;",
                "d = (5 - e) * 2;",
            ]
        )
        tree = parse_program(program)
        visitor = Calc2Visitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
                "a": 2,
                "b": 3,
                "c": 9,
                "d": 10,
                "e": 0,
            },
        )

    def test_if_else_else_branch(self):
        program = "\n".join(
            [
                "a = 0;",
                "if (a > 0) {",
                "    b = 1;",
                "} else {",
                "    b = 2;",
                "    c = b + 3;",
                "}",
            ]
        )
        tree = parse_program(program)
        visitor = Calc2Visitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
                "a": 0,
                "b": 2,
                "c": 5,
            },
        )

    def test_if_without_else_does_not_override(self):
        program = "\n".join(
            [
                "b = 5;",
                "if (1 > 2) {",
                "    b = 1;",
                "}",
                "c = 7;",
            ]
        )
        tree = parse_program(program)
        visitor = Calc2Visitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
                "b": 5,
                "c": 7,
            },
        )

    def test_comparison_operators(self):
        program = "\n".join(
            [
                "result = 0;",
                "if (2 > 1) { result = result + 1; }",
                "if (2 >= 2) { result = result + 2; }",
                "if (2 < 3) { result = result + 4; }",
                "if (2 <= 2) { result = result + 8; }",
                "if (2 == 2) { result = result + 16; }",
                "if (2 != 3) { result = result + 32; }",
            ]
        )
        tree = parse_program(program)
        visitor = Calc2Visitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
                "result": 63,
            },
        )

    def test_undefined_variable_in_condition(self):
        program = "\n".join(
            [
                "a = 1;",
                "if (b == 0) {",
                "    a = a + 1;",
                "}",
            ]
        )
        tree = parse_program(program)
        visitor = Calc2Visitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
                "a": 2,
                "b": 0,
            },
        )


if __name__ == "__main__":
    unittest.main()
