"""Calc5 start skeleton tests."""

import unittest


IMPORT_ERROR = None

try:
    from antlr4 import CommonTokenStream, InputStream
    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser
except Exception as exc:  # pragma: n`o cover
    IMPORT_ERROR = exc


def parse_program(program: str):
    if IMPORT_ERROR is not None:
        raise RuntimeError(
            "Calc5 파서 import에 실패했습니다. 먼저 생성 파일을 갱신하세요:\n"
            "  antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4\n"
            f"원본 오류: {IMPORT_ERROR}"
        )

    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(token_stream)
    tree = parser.program()
    return parser, tree


def parse_expr(expression: str):
    if IMPORT_ERROR is not None:
        raise RuntimeError(
            "Calc5 파서 import에 실패했습니다. 먼저 생성 파일을 갱신하세요:\n"
            "  antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4\n"
            f"원본 오류: {IMPORT_ERROR}"
        )

    input_stream = InputStream(expression)
    lexer = CalcPlusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(token_stream)
    tree = parser.expr()
    return parser, tree


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class Calc5ParserSmokeTest(unittest.TestCase):
    def test_entry_rule_is_program(self):
        parser, tree = parse_program("int a;")

        self.assertTrue(hasattr(parser, "program"))
        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertIsNotNone(tree)

    def test_parse_declare_assign_write(self):
        parser, tree = parse_program(
            "\n".join(
                [
                    "int a, b;",
                    "a = 1 + 2;",
                    "write(a);",
                ]
            )
        )
        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertIsNotNone(tree)

    def test_parse_nested_blocks_and_if(self):
        parser, tree = parse_program(
            "\n".join(
                [
                    "int a;",
                    "a = 1;",
                    "{",
                    "    int a;",
                    "    a = 2;",
                    "    if (a > 1) {",
                    "        write(a);",
                    "    }",
                    "}",
                ]
            )
        )
        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertIsNotNone(tree)


class Calc5AstNodeShapeTest(unittest.TestCase):
    def test_expression_nodes_can_form_a_binary_expression(self):
        from ast_nodes import BinaryExpr, IntLiteral, VarRef

        expr = BinaryExpr("+", IntLiteral(1), VarRef("a"))

        self.assertEqual(expr.op, "+")
        self.assertEqual(expr.left.value, 1)
        self.assertEqual(expr.right.name, "a")


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class Calc5AstBuilderContractTest(unittest.TestCase):
    def test_builder_program_is_explicit_stub(self):
        from ast_builder import AstBuilder

        _, tree = parse_program("int a;")
        builder = AstBuilder()

        with self.assertRaises(NotImplementedError):
            builder.visit(tree)


class Calc5AstPrinterContractTest(unittest.TestCase):
    def test_printer_is_explicit_stub(self):
        from ast_nodes import IntLiteral
        from ast_printer import AstPrinter

        printer = AstPrinter()

        with self.assertRaises(NotImplementedError):
            printer.format(IntLiteral(1))


class Calc5AstExecutorContractTest(unittest.TestCase):
    def test_executor_is_explicit_stub(self):
        from ast_executor import AstExecutor
        from ast_nodes import IntLiteral

        executor = AstExecutor()

        with self.assertRaises(NotImplementedError):
            executor.execute(IntLiteral(1))


class SymbolTableReuseTest(unittest.TestCase):
    def test_symbol_table_supports_shadowing_for_executor(self):
        from symbol_table import SymbolTable

        table = SymbolTable()
        table.declare("a")
        table.assign("a", 1)
        table.push_scope()
        table.declare("a")
        table.assign("a", 2)

        self.assertEqual(table.lookup("a"), 2)

        table.pop_scope()

        self.assertEqual(table.lookup("a"), 1)


if __name__ == "__main__":
    unittest.main()
