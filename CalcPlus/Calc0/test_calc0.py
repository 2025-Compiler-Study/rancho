import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from CalcVisitor import CalcVisitor
from CalcListener import CalcListener


def parse_expr(expr: str):
    input_stream = InputStream(expr)
    lexer = CalcPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(stream)
    return parser.calc0()


class Calc0Test(unittest.TestCase):
    def test_visitor(self):
        tree = parse_expr("10 + 2 * (5 - 9 / 3)")
        result = CalcVisitor().visit(tree)
        self.assertEqual(result, 14)

    def test_listener(self):
        tree = parse_expr("10 + 2 * (5 - 9 / 3)")
        listener = CalcListener()
        ParseTreeWalker().walk(listener, tree)
        self.assertEqual(listener.result(), 14)

    def test_simple_add(self):
        tree = parse_expr("10 + 2")
        result = CalcVisitor().visit(tree)
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()
