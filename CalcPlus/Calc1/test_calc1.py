# test_calc1.py
"""Calc-1 Listener(미정의 변수 경고) 테스트."""

import unittest

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from CalcListener import CalcListener
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser


def parse_program(program: str):
    """프로그램 문자열을 calc1 시작 규칙으로 파싱한 트리를 반환."""
    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(stream)
    return parser.calc1()


class CalcListenerTest(unittest.TestCase):
    """미정의 변수 검사 규칙을 검증한다."""

    def test_use_before_definition_with_line_and_column(self):
        """
        미정의 변수 사용 시 에러에 line/column이 포함되어야 한다.

        예상 경고:
        - 1행 4열: b
        - 2행 8열: d
        - 3행 4열: b (좌변 대입 전에 우변에서 먼저 사용됨)
        """
        program = "\n".join(
            [
                "a = b + 3;",
                "c = a + d;",
                "b = b + 1;",
            ]
        )

        tree = parse_program(program)
        listener = CalcListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(
            listener.errors,
            [
                "Line 1, Column 4: b(은)는 선언되지 않은 변수 입니다.",
                "Line 2, Column 8: d(은)는 선언되지 않은 변수 입니다.",
                "Line 3, Column 4: b(은)는 선언되지 않은 변수 입니다.",
            ],
        )


    def test_self_assignment_reports_undefined_rhs(self):
        """
        자기 자신 대입이라도 우변이 먼저 평가되므로 미정의 경고가 나와야 한다.
        """
        program = "a = a + 1;"
        tree = parse_program(program)
        listener = CalcListener()
        ParseTreeWalker().walk(listener, tree)

        self.assertEqual(
            listener.errors,
            ["Line 1, Column 4: a(은)는 선언되지 않은 변수 입니다."],
        )

    def test_use_after_definition_has_no_error(self):
        """먼저 정의된 변수를 이후 식에서 쓰면 경고가 없어야 한다."""
        program = "x = 1;\ny = x + 2;"
        tree = parse_program(program)
        listener = CalcListener()
        ParseTreeWalker().walk(listener, tree)

        self.assertEqual(listener.errors, [])
        self.assertEqual(listener.warnings, [])


if __name__ == "__main__":
    unittest.main()

