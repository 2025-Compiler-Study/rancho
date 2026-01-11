# test_parse.py
import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from CalcVisitor import CalcVisitor
from CalcListener import CalcListener
from Calc1Visitor import Calc1Visitor
from Calc1WarningListener import Calc1WarningListener

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

class TestCalc1(unittest.TestCase):
    def _parse(self, program: str):
        input_stream = InputStream(program)
        lexer = CalcPlusLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalcPlusParser(stream)
        return parser.calc1()

    def test_variable_evaluation(self):
        program = "a=1;b=a+2;c=b*3;a=a+1;d=(5-e)*2;"
        tree = self._parse(program)
        visitor = Calc1Visitor()
        memory = visitor.visit(tree)

        self.assertEqual(
            memory,
            {
                "a": 2,
                "b": 3,
                "c": 9,
                "d": 10,
                "e": 0,
            },
        )

    def test_use_before_assignment_warnings(self):
        program = "\n".join(
            [
                "a = b + 3;",
                "c = a + d;",
                "b = b + 1;",
            ]
        )
        tree = self._parse(program)
        listener = Calc1WarningListener()
        ParseTreeWalker().walk(listener, tree)

        warnings = [
            (warn["line"], warn["column"], warn["name"]) for warn in listener.warnings
        ]

        self.assertEqual(
            warnings,
            [
                (1, 4, "b"),
                (2, 8, "d"),
                (3, 4, "b"),
            ],
        )

if __name__ == '__main__':
    unittest.main()
