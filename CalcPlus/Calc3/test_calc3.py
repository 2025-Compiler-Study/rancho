"""Basic test skeleton for Calc-3.

This file is designed to be useful from day one:
- Parser smoke tests validate grammar wiring.
- Visitor tests are scaffolded and auto-skipped until implemented.
"""

import unittest


IMPORT_ERROR = None

try:
    from antlr4 import CommonTokenStream, InputStream
    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser
except Exception as exc:  # pragma: no cover - setup guard
    IMPORT_ERROR = exc


def parse_program(program: str):
    """Parse a Calc-3 program and return (parser, tree)."""
    if IMPORT_ERROR is not None:
        raise RuntimeError(
            "Calc-3 parser imports failed. Generate Python parser first:\n"
            "  antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4\n"
            f"Original error: {IMPORT_ERROR}"
        )

    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(token_stream)
    tree = parser.calc3()
    return parser, tree


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python files/runtime not ready")
class Calc3ParserSmokeTest(unittest.TestCase):
    def test_parse_simple_assign(self):
        parser, tree = parse_program("a = 1 + 2;\n")
        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertIsNotNone(tree)

    def test_parse_read_write_if_else(self):
        source = "\n".join(
            [
                "a = read();",
                "if (a > 0) {",
                "    write(a);",
                "} else {",
                "    write(0);",
                "}",
            ]
        )
        parser, tree = parse_program(source)
        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertIsNotNone(tree)


class Calc3VisitorSkeletonTest(unittest.TestCase):
    def _make_visitor(self):
        try:
            from calc3_visitor import Calc3Visitor
        except Exception as exc:
            raise RuntimeError(f"calc3_visitor.py / Calc3Visitor import failed: {exc}") from exc
        return Calc3Visitor()

    def test_eval_smoke(self):
        source = "\n".join(
            [
                "a = 1;",
                "if (a >= 1) { write(a); } else { write(0); }",
            ]
        )
        _, tree = parse_program(source)
        visitor = self._make_visitor()

        # TODO: Define exact return contract for visitor (e.g., memory dict).
        result = visitor.visit(tree)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
