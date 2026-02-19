"""Calc-3 기본 테스트 스켈레톤.

이 파일은 시작 단계부터 바로 유용하도록 구성되었다:
- 파서 스모크 테스트는 문법 연결 상태를 빠르게 검증한다.
- Visitor 스켈레톤 테스트는 구현 전에는 골격을 제공하고, 준비 전까지 자동 스킵된다.
"""

import unittest


IMPORT_ERROR = None

try:
    from antlr4 import CommonTokenStream, InputStream
    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser
except Exception as exc:  # pragma: no cover - 환경 준비 가드
    IMPORT_ERROR = exc


def parse_program(program: str):
    """Calc-3 프로그램을 파싱해 (parser, tree)를 반환한다."""
    if IMPORT_ERROR is not None:
        raise RuntimeError(
            "Calc-3 파서 import에 실패했습니다. 먼저 Python 파서를 생성하세요:\n"
            "  antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4\n"
            f"원본 오류: {IMPORT_ERROR}"
        )

    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(token_stream)
    tree = parser.calc3()
    return parser, tree


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class Calc3ParserSmokeTest(unittest.TestCase):
    # 스모크 테스트: 핵심 경로가 깨지지 않았는지 빠르게 확인한다.
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


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class Calc3VisitorSkeletonTest(unittest.TestCase):
    # 스켈레톤 테스트: 구현 계약(입출력/상태)을 먼저 고정해 두는 골격 테스트다.
    def _make_visitor(self, **kwargs):
        try:
            from calc3_visitor import Calc3Visitor
        except Exception as exc:
            raise RuntimeError(f"calc3_visitor.py / Calc3Visitor import 실패: {exc}") from exc
        return Calc3Visitor(**kwargs)

    def test_eval_smoke(self):
        source = "\n".join(
            [
                "a = 1;",
                "if (a >= 1) { write(a); } else { write(0); }",
            ]
        )
        _, tree = parse_program(source)
        writes = []
        visitor = self._make_visitor(write_fn=writes.append)

        result = visitor.visit(tree)
        self.assertEqual(result, {"a": 1})
        self.assertEqual(visitor.outputs, [1])
        self.assertEqual(writes, [1])

    def test_read_assign_else_branch(self):
        source = "\n".join(
            [
                "a = read();",
                "if (a > 0) { write(a); } else { write(0 - a); }",
            ]
        )
        _, tree = parse_program(source)
        writes = []
        visitor = self._make_visitor(read_fn=lambda: "-2", write_fn=writes.append)

        result = visitor.visit(tree)
        self.assertEqual(result, {"a": -2})
        self.assertEqual(visitor.outputs, [2])
        self.assertEqual(writes, [2])

    def test_read_invalid_defaults_to_zero(self):
        source = "\n".join(
            [
                "a = read();",
                "write(a);",
            ]
        )
        _, tree = parse_program(source)
        writes = []
        visitor = self._make_visitor(read_fn=lambda: "abc", write_fn=writes.append)

        result = visitor.visit(tree)
        self.assertEqual(result, {"a": 0})
        self.assertEqual(visitor.outputs, [0])
        self.assertEqual(writes, [0])


if __name__ == "__main__":
    unittest.main()
