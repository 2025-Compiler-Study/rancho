# 테스트: Calc-1
import unittest
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from CalcVisitor import CalcVisitor
# from calc1_warning_listener import Calc1WarningListener
from CalcListener import CalcListener

def parse_program(program: str):
    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(stream)
    return parser.calc1()

'''
class CalcVisitorTest(unittest.TestCase):
    def test_variable_memory(self):
        program = "A=1;\
            b=A+2;\
            c=b*3;A=A+1;d=(5-e)*2;"
        tree = parse_program(program)
        visitor = CalcVisitor()
        result = visitor.visit(tree)

        self.assertEqual(
            result,
            {
                "A": 2,
                "b": 3,
                "c": 9,
                "d": 10,
                "e": 0,
            },
        )
'''

'''
가능한 이유는 간단해. listener.warnings가 dict 리스트고, 각 dict가 {"line": ..., "column": ..., "name": ...} 구조를 보장하기 때문이야. 그래서 리스트 내포로 필요한 값만 추려서 튜플 리스트를 만들 수 있어.

구체적으로:

listener.warnings는 enterVar에서 warning = {"line": token.line, "column": token.column, "name": name} 형태로 추가됨
그러니 warn["line"], warn["column"], warn["name"]는 항상 존재
리스트 내포는 그 키들을 순서대로 튜플로 뽑아 [(line, column, name), ...]를 만든다
이 결과를 self.assertEqual로 기대값과 비교하는 게 자연스러움
즉, warnings의 자료구조가 정해져 있기 때문에 저렇게 꺼내도 안전하고, 테스트 의도(순서와 내용 비교)에도 맞아.
'''
class CalcListenerTest(unittest.TestCase):
    def test_use_before_definition(self):
        program = "\n".join(
            [
                # "a = b + 3;",
                # "c = a + d;",
                # "dd = b * 1;"
                "A = b * 1 + g;" # Error Var는 문자만 가능하게 antlr g4 파일에 정의 되어있기 때문
                               # => VAR : [A-Za-z]+ ;
            ]
        )

        tree = parse_program(program)
        listener = CalcListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        errors = [
            # (warn["line"], warn["column"], warn["name"])
            (f"{warn}")
            for warn in listener.errors
        ]

        self.assertEqual(
            errors,
            [
                # (1, 4, "b"),
                # (2, 8, "d"),
                # (3, 4, "b"),
                "b(은)는 선언되지 않은 변수 입니다.",
                "g(은)는 선언되지 않은 변수 입니다."
            ],
        )

if __name__ == "__main__":
    unittest.main()
