# my_calc1_test.py

import unittest

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from calc1_visitor import CalcVisitor
from calc1_warning_listener import Calc1WarningListener

def parse_program(program: str):
    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(stream)
    return parser.calc1()

class CacVisitrTest(unittest.TestCase):
    def test_variable_memory(self):
        program = "a=1;b=a+2;c=b*3;a=a+1;d=(5-e)*2";
        tree = parse_program(program)
        visitor = CalcVisitor()
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
    
    def test_assignment_uses_previsou_values(self):
        program = "a=1;a=a+1+a;"
        tree = parse_program(program)
        visitor = CalcVisitor()
        result = visitor.visit(tree)

        self.assertEqual(result, {"a", 3})