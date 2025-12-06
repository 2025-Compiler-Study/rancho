# test_parse.py
import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from CalcVisitor import CalcVisitor
from CalcListener import CalcListener

class TestCalc0(unittest.TestCase):
    def test_evaluation(self):
        # input_expr = "10 + 2"
        input_expr = "10 + 2 * (5 - 9 / 3)"
        input_stream = InputStream(input_expr)
        
        lexer = CalcPlusLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalcPlusParser(stream)
        tree = parser.calc0()
        
        # visitor
        visitor = CalcVisitor()
        visitor_result = visitor.visit(tree)

        # listener
        listener = CalcListener()
        ParseTreeWalker().walk(listener, tree)
        listener_result = listener.result()
        
        self.assertEqual(listener_result, 14)
        self.assertEqual(visitor_result, 14)

if __name__ == '__main__':
    unittest.main()
