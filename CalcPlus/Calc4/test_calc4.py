"""Calc4 시작용 테스트 골격."""

import unittest


IMPORT_ERROR = None

try:
    from antlr4 import CommonTokenStream, InputStream
    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser
except Exception as exc:  # pragma: no cover
    IMPORT_ERROR = exc


def parse_program(program: str):
    if IMPORT_ERROR is not None:
        raise RuntimeError(
            "Calc4 파서 import에 실패했습니다. 먼저 생성 파일을 갱신하세요:\n"
            "  antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4\n"
            f"원본 오류: {IMPORT_ERROR}"
        )

    input_stream = InputStream(program)
    lexer = CalcPlusLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcPlusParser(token_stream)
    tree = parser.calc4()
    return parser, tree


def parse_expr(expression: str):
    if IMPORT_ERROR is not None:
        raise RuntimeError(
            "Calc4 파서 import에 실패했습니다. 먼저 생성 파일을 갱신하세요:\n"
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
class Calc4ParserSmokeTest(unittest.TestCase):
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


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class Calc4VisitorContractTest(unittest.TestCase):
    def _make_visitor(self):
        try:
            from calc4_visitor import Calc4Visitor
        except Exception as exc:
            raise RuntimeError(f"calc4_visitor.py / Calc4Visitor import 실패: {exc}") from exc
        return Calc4Visitor()

    def test_program_execution_visits_statements(self):
        _, tree = parse_program(
            "\n".join(
                [
                    "int a;",
                    "a = 1;",
                    "write(a);",
                ]
            )
        )
        visitor = self._make_visitor()
        visitor.write_fn = lambda value: None

        visitor.visit(tree)

        self.assertEqual(visitor.outputs, [1])

    def test_program_rejects_duplicate_declaration_in_same_scope(self):
        from symbol_table import DuplicateDeclarationError

        _, tree = parse_program(
            "\n".join(
                [
                    "int a;",
                    "int a;",
                ]
            )
        )
        visitor = self._make_visitor()

        with self.assertRaises(DuplicateDeclarationError):
            visitor.visit(tree)

    def test_program_rejects_duplicate_declaration_in_one_statement(self):
        from symbol_table import DuplicateDeclarationError

        _, tree = parse_program("int a, a;")
        visitor = self._make_visitor()

        with self.assertRaises(DuplicateDeclarationError):
            visitor.visit(tree)

    def test_program_allows_shadowing_in_nested_block(self):
        _, tree = parse_program(
            "\n".join(
                [
                    "int a;",
                    "a = 1;",
                    "{",
                    "    int a;",
                    "    a = 2;",
                    "    write(a);",
                    "}",
                    "write(a);",
                ]
            )
        )
        visitor = self._make_visitor()
        visitor.write_fn = lambda value: None

        visitor.visit(tree)

        self.assertEqual(visitor.outputs, [2, 1])

    @unittest.expectedFailure
    def test_wrong_example_treats_nested_shadowing_as_duplicate_declaration(self):
        from symbol_table import DuplicateDeclarationError

        _, tree = parse_program(
            "\n".join(
                [
                    "int a;",
                    "{",
                    "    int a;",
                    "}",
                ]
            )
        )
        visitor = self._make_visitor()

        with self.assertRaises(DuplicateDeclarationError):
            visitor.visit(tree)

    def test_program_rejects_block_local_variable_after_block(self):
        from symbol_table import UndefinedVariableError

        _, tree = parse_program(
            "\n".join(
                [
                    "{",
                    "    int a;",
                    "    a = 1;",
                    "}",
                    "write(a);",
                ]
            )
        )
        visitor = self._make_visitor()
        visitor.write_fn = lambda value: None

        with self.assertRaises(UndefinedVariableError):
            visitor.visit(tree)


@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class Calc4VisitorExecutionTest(unittest.TestCase):

    def test_visit_var(self):
        from calc4_visitor import Calc4Visitor

        parser, tree = parse_expr("a")
        visitor = Calc4Visitor()
        visitor.symbols.declare("a")
        visitor.symbols.assign("a", 7)

        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertEqual(visitor.visit(tree), 7)

    def test_visit_undefined_var_raises(self):
        from calc4_visitor import Calc4Visitor
        from symbol_table import UndefinedVariableError

        parser, tree = parse_expr("a")
        visitor = Calc4Visitor()

        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        with self.assertRaises(UndefinedVariableError):
            visitor.visit(tree)

    def test_visit_mul_div(self):
        from calc4_visitor import Calc4Visitor

        parser, tree = parse_expr("123 * 4")
        visitor = Calc4Visitor()

        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertEqual(visitor.visit(tree), 492)

    def test_visit_plus_minus(self):
        from calc4_visitor import Calc4Visitor

        parser, tree = parse_expr("123 + 4")
        visitor = Calc4Visitor()

        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertEqual(visitor.visit(tree), 127)

    def test_visit_int_returns_integer_literal_value(self):
        from calc4_visitor import Calc4Visitor

        parser, tree = parse_expr("123")
        visitor = Calc4Visitor()

        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertEqual(visitor.visit(tree), 123)



@unittest.skipIf(IMPORT_ERROR is not None, "ANTLR Python 파일/런타임이 준비되지 않음")
class SymbolTableContractTest(unittest.TestCase):
    def test_symbol_table_declare_assign_lookup(self):
        from symbol_table import SymbolTable

        table = SymbolTable()

        table.declare("a")
        table.assign("a", 3)

        self.assertEqual(table.lookup("a"), 3)

    def test_symbol_table_rejects_duplicate_declaration(self):
        from symbol_table import DuplicateDeclarationError, SymbolTable

        table = SymbolTable()

        table.declare("a")
        with self.assertRaises(DuplicateDeclarationError):
            table.declare("a")

    def test_symbol_table_rejects_undefined_assignment_and_lookup(self):
        from symbol_table import SymbolTable, UndefinedVariableError

        table = SymbolTable()

        with self.assertRaises(UndefinedVariableError):
            table.assign("a", 1)

        with self.assertRaises(UndefinedVariableError):
            table.lookup("a")

    def test_symbol_table_allows_shadowing_between_scopes(self):
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
