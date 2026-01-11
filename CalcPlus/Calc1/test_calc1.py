# test_calc1.py
import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from generated.CalcPlusLexer import CalcPlusLexer
from generated.CalcPlusParser import CalcPlusParser
from calc1_visitor import Calc1Visitor
from calc1_warning_listener import Calc1WarningListener


def parse_program(program: str):
    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(stream)
    return parser.calc1()


class Calc1VisitorTest(unittest.TestCase):
    def test_variable_memory(self):
        program = "A=1;\
<<<<<<< Updated upstream
            b=A+2;\
            c=b*3;A=A+1;d=(5-e)*2;"
=======
        b=A+2;c=b*3;A=A+1;d=(5-e)*2;"
>>>>>>> Stashed changes
        tree = parse_program(program)
        visitor = Calc1Visitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
<<<<<<< Updated upstream
                "A": 42,
=======
                "a": 2,
>>>>>>> Stashed changes
                "b": 3,
                "c": 9,
                "d": 10,
                "e": 0,
            },
        )


class Calc1WarningListenerTest(unittest.TestCase):
    def test_use_before_definition(self):
        program = "\n".join(
            [
                "a = b + 3;",
                "c = a + d;",
                "b = b + 1;",
            ]
        )
        tree = parse_program(program)
        listener = Calc1WarningListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        warnings = [
            (warn["line"], warn["column"], warn["name"])
            for warn in listener.warnings
        ]

        self.assertEqual(
            warnings,
            [
                (1, 4, "b"),
                (2, 8, "d"),
                (3, 4, "b"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
