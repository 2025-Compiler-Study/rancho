"""Core tests for Calc5 expression and program AST nodes."""

import importlib.util
import unittest

from calc5_ast import (
    Assign,
    AstExecutor,
    AstNode,
    Block,
    BinaryExpr,
    CompareExpr,
    Declare,
    Expr,
    IntLiteral,
    IfElse,
    Program,
    ReadCall,
    VarRef,
    Write,
    build_expression,
    build_program,
    build_program_with_diagnostics,
    execute_source,
    evaluate,
    format_ast,
)
from symbol_table import DuplicateDeclarationError, UndefinedVariableError


HAS_ANTLR = importlib.util.find_spec("antlr4") is not None


def example_ast() -> BinaryExpr:
    return BinaryExpr(
        "+",
        BinaryExpr("*", IntLiteral(5), IntLiteral(3)),
        BinaryExpr(
            "*",
            VarRef("a"),
            BinaryExpr(
                "-",
                IntLiteral(5),
                BinaryExpr("/", IntLiteral(9), IntLiteral(3)),
            ),
        ),
    )


def example_program_ast() -> Program:
    """Subject assignment 1, example 2 without parse-tree punctuation."""
    return Program(
        [
            Declare("a"),
            Declare("b"),
            Assign("a", IntLiteral(1)),
            Assign("b", ReadCall()),
            Block(
                [
                    Declare("c"),
                    Assign("c", BinaryExpr("+", VarRef("a"), VarRef("b"))),
                    Write(VarRef("c")),
                ]
            ),
            Assign("b", IntLiteral(0)),
        ]
    )


class AstNodeTest(unittest.TestCase):
    def test_leaf_nodes_store_their_semantic_value(self):
        literal = IntLiteral(5)
        variable = VarRef("a")

        self.assertIsInstance(literal, AstNode)
        self.assertIsInstance(literal, Expr)
        self.assertEqual(literal.value, 5)
        self.assertEqual(variable.name, "a")
        self.assertEqual(literal.children(), ())
        self.assertEqual(variable.children(), ())

    def test_binary_expression_keeps_ordered_children(self):
        left = IntLiteral(5)
        right = IntLiteral(3)
        expression = BinaryExpr("*", left, right)

        self.assertEqual(expression.op, "*")
        self.assertEqual(expression.children(), (left, right))

    def test_program_and_statement_nodes_keep_only_ast_children(self):
        value = BinaryExpr("+", VarRef("a"), VarRef("b"))
        assignment = Assign("c", value)
        block = Block([Declare("c"), assignment, Write(VarRef("c"))])
        program = Program([Declare("a"), block])

        self.assertEqual(assignment.children(), (value,))
        self.assertEqual(block.children(), tuple(block.statements))
        self.assertEqual(program.children(), tuple(program.statements))

    def test_if_else_keeps_condition_then_and_optional_else_in_order(self):
        condition = CompareExpr("<", VarRef("a"), IntLiteral(10))
        then_block = Block([Write(IntLiteral(1))])
        else_block = Block([Write(IntLiteral(0))])
        statement = IfElse(condition, then_block, else_block)

        self.assertEqual(statement.children(), (condition, then_block, else_block))
        self.assertEqual(condition.children(), (condition.left, condition.right))


class AstBehaviorTest(unittest.TestCase):
    def test_formats_an_ast_without_parenthesis_nodes(self):
        self.assertEqual(
            format_ast(example_ast()),
            "(+ (* 5 3) (* a (- 5 (/ 9 3))))",
        )

    def test_evaluates_the_complete_example(self):
        self.assertEqual(evaluate(example_ast(), {"a": 4}), 23)

    def test_formats_the_program_example(self):
        self.assertEqual(
            format_ast(example_program_ast()),
            "(program (declare a) (declare b) (assign a 1) (assign b (read)) "
            "(block (declare c) (assign c (+ a b)) (write c)) (assign b 0))",
        )


class AstExecutorTest(unittest.TestCase):
    def test_executes_example_two_with_injected_input_and_output(self):
        output: list[int] = []
        executor = AstExecutor(read_fn=lambda: 10, write_fn=output.append)

        executor.execute(example_program_ast())

        self.assertEqual(output, [11])
        self.assertEqual(executor.outputs, [11])
        self.assertEqual(executor.symbols.lookup("a"), 1)
        self.assertEqual(executor.symbols.lookup("b"), 0)

    def test_block_declaration_is_not_available_after_the_block(self):
        executor = AstExecutor(read_fn=lambda: 0, write_fn=lambda _: None)
        executor.execute(example_program_ast())

        with self.assertRaisesRegex(RuntimeError, "선언되지 않은 변수"):
            executor.symbols.lookup("c")

    def test_stops_immediately_when_a_name_is_declared_twice_in_one_scope(self):
        program = Program([Declare("a"), Declare("a"), Write(IntLiteral(99))])
        output: list[int] = []

        with self.assertRaises(DuplicateDeclarationError):
            AstExecutor(write_fn=output.append).execute(program)

        self.assertEqual(output, [])

    def test_stops_immediately_when_assigning_an_undeclared_name(self):
        program = Program([Assign("a", IntLiteral(1)), Write(IntLiteral(99))])
        output: list[int] = []

        with self.assertRaises(UndefinedVariableError):
            AstExecutor(write_fn=output.append).execute(program)

        self.assertEqual(output, [])

    def test_stops_immediately_when_reading_an_undeclared_name(self):
        program = Program([Write(VarRef("a"))])

        with self.assertRaises(UndefinedVariableError):
            AstExecutor(write_fn=lambda _: None).execute(program)

    def test_inner_block_can_update_an_outer_variable(self):
        program = Program(
            [
                Declare("a"),
                Block([Assign("a", IntLiteral(3))]),
                Write(VarRef("a")),
            ]
        )
        output: list[int] = []

        AstExecutor(write_fn=output.append).execute(program)

        self.assertEqual(output, [3])

    def test_executes_only_the_then_block_when_condition_is_true(self):
        program = Program(
            [
                Declare("a"),
                Assign("a", IntLiteral(3)),
                IfElse(
                    CompareExpr(">=", VarRef("a"), IntLiteral(3)),
                    Block([Write(IntLiteral(1))]),
                    Block([Write(IntLiteral(0))]),
                ),
            ]
        )
        output: list[int] = []

        AstExecutor(write_fn=output.append).execute(program)

        self.assertEqual(output, [1])

    def test_executes_else_block_only_when_condition_is_false(self):
        program = Program(
            [
                IfElse(
                    CompareExpr("==", IntLiteral(1), IntLiteral(2)),
                    Block([Write(IntLiteral(1))]),
                    Block([Write(IntLiteral(0))]),
                )
            ]
        )
        output: list[int] = []

        AstExecutor(write_fn=output.append).execute(program)

        self.assertEqual(output, [0])

    def test_skips_if_body_when_false_without_else(self):
        program = Program(
            [
                IfElse(
                    CompareExpr("!=", IntLiteral(1), IntLiteral(1)),
                    Block([Write(IntLiteral(99))]),
                )
            ]
        )
        output: list[int] = []

        AstExecutor(write_fn=output.append).execute(program)

        self.assertEqual(output, [])


@unittest.skipUnless(HAS_ANTLR, "antlr4 Python runtime is not installed")
class AntlrAstBuilderTest(unittest.TestCase):
    def test_builds_integer_and_variable_leaves(self):
        self.assertEqual(build_expression("5"), IntLiteral(5))
        self.assertEqual(build_expression("a"), VarRef("a"))

    def test_operator_precedence_is_preserved_by_the_tree(self):
        self.assertEqual(
            build_expression("1 + 2 * 3"),
            BinaryExpr(
                "+",
                IntLiteral(1),
                BinaryExpr("*", IntLiteral(2), IntLiteral(3)),
            ),
        )

    def test_parentheses_change_grouping_without_becoming_a_node(self):
        self.assertEqual(
            build_expression("(1 + 2) * 3"),
            BinaryExpr(
                "*",
                BinaryExpr("+", IntLiteral(1), IntLiteral(2)),
                IntLiteral(3),
            ),
        )

    def test_builds_the_complete_example(self):
        expression = build_expression("5 * 3 + a * (5 - 9 / 3)")

        self.assertEqual(expression, example_ast())
        self.assertEqual(evaluate(expression, {"a": 4}), 23)

    def test_builds_subject_example_two_as_a_program_ast(self):
        source = """
        int a, b;
        a = 1;
        b = read();
        {
            int c;
            c = a + b;
            write(c);
        }
        b = 0;
        """

        self.assertEqual(build_program(source), example_program_ast())

    def test_builds_if_else_with_comparison_and_both_blocks(self):
        self.assertEqual(
            build_program(
                """
                int a;
                a = 3;
                if (a >= 3) {
                    write(a);
                } else {
                    write(0);
                }
                """
            ),
            Program(
                [
                    Declare("a"),
                    Assign("a", IntLiteral(3)),
                    IfElse(
                        CompareExpr(">=", VarRef("a"), IntLiteral(3)),
                        Block([Write(VarRef("a"))]),
                        Block([Write(IntLiteral(0))]),
                    ),
                ]
            ),
        )

    def test_builds_if_without_else(self):
        self.assertEqual(
            build_program("if (1 != 2) { write(1); }"),
            Program(
                [
                    IfElse(
                        CompareExpr("!=", IntLiteral(1), IntLiteral(2)),
                        Block([Write(IntLiteral(1))]),
                    )
                ]
            ),
        )


class AstExecutorOperatorTest(unittest.TestCase):
    """Fine-grained #3 execution cases, registered below one per operator."""


class AntlrConditionalBuilderTest(unittest.TestCase):
    """#4 Parse Tree-to-AST cases for every conditional grammar variation."""


AntlrConditionalBuilderTest = unittest.skipUnless(
    HAS_ANTLR, "antlr4 Python runtime is not installed"
)(AntlrConditionalBuilderTest)


def _add_executor_binary_operator_case(op: str, left: int, right: int, expected: int):
    def test(self):
        self.assertEqual(
            AstExecutor().eval_expr(BinaryExpr(op, IntLiteral(left), IntLiteral(right))),
            expected,
        )

    setattr(AstExecutorOperatorTest, f"test_evaluates_{left}_{op_name(op)}_{right}", test)


def _add_executor_comparison_case(op: str, left: int, right: int, expected: bool):
    def test(self):
        self.assertEqual(
            AstExecutor().eval_condition(CompareExpr(op, IntLiteral(left), IntLiteral(right))),
            expected,
        )

    name = f"test_compares_{left}_{op_name(op)}_{right}"
    setattr(AstExecutorOperatorTest, name, test)


def _add_executor_branch_case(label: str, condition: CompareExpr, expected: list[int]):
    def test(self):
        output: list[int] = []
        AstExecutor(write_fn=output.append).execute(
            Program([IfElse(condition, Block([Write(IntLiteral(1))]), Block([Write(IntLiteral(0))]))])
        )
        self.assertEqual(output, expected)

    setattr(AstExecutorOperatorTest, f"test_branch_{label}", test)


def op_name(op: str) -> str:
    return {"+": "plus", "-": "minus", "*": "times", "/": "divided_by",
            "==": "equal", "!=": "not_equal", ">": "greater_than",
            ">=": "greater_or_equal", "<": "less_than", "<=": "less_or_equal"}[op]


for _op, _left, _right, _expected in (
    ("+", 2, 3, 5),
    ("-", 2, 3, -1),
    ("*", 4, 3, 12),
    ("/", 7, 2, 3),
):
    _add_executor_binary_operator_case(_op, _left, _right, _expected)

for _op, _left, _right, _expected in (
    ("==", 2, 2, True),
    ("!=", 2, 2, False),
    (">", 3, 2, True),
    (">=", 3, 3, True),
    ("<", 2, 3, True),
    ("<=", 3, 3, True),
):
    _add_executor_comparison_case(_op, _left, _right, _expected)

for _label, _condition, _expected in (
    ("equal", CompareExpr("==", IntLiteral(1), IntLiteral(1)), [1]),
    ("not_equal", CompareExpr("!=", IntLiteral(1), IntLiteral(1)), [0]),
    ("greater_than", CompareExpr(">", IntLiteral(2), IntLiteral(1)), [1]),
    ("greater_or_equal", CompareExpr(">=", IntLiteral(2), IntLiteral(2)), [1]),
    ("less_than", CompareExpr("<", IntLiteral(1), IntLiteral(2)), [1]),
    ("less_or_equal", CompareExpr("<=", IntLiteral(2), IntLiteral(2)), [1]),
):
    _add_executor_branch_case(_label, _condition, _expected)


def _add_executor_program_case(
    label: str, program: Program, expected: list[int], read_value: int = 0
):
    def test(self):
        output: list[int] = []
        AstExecutor(read_fn=lambda: read_value, write_fn=output.append).execute(program)
        self.assertEqual(output, expected)

    setattr(AstExecutorOperatorTest, f"test_executes_{label}", test)


for _label, _program, _expected, _read_value in (
    (
        "default_value_after_declaration",
        Program([Declare("a"), Write(VarRef("a"))]),
        [0],
        0,
    ),
    (
        "variable_value_in_an_expression",
        Program([Declare("a"), Assign("a", IntLiteral(4)), Write(BinaryExpr("*", VarRef("a"), IntLiteral(2)))]),
        [8],
        0,
    ),
    (
        "nested_arithmetic_expression",
        Program([Write(BinaryExpr("-", BinaryExpr("*", IntLiteral(4), IntLiteral(3)), IntLiteral(5)))]),
        [7],
        0,
    ),
    (
        "read_assignment",
        Program([Declare("a"), Assign("a", ReadCall()), Write(VarRef("a"))]),
        [9],
        9,
    ),
    (
        "inner_shadow_does_not_change_outer_value",
        Program([Declare("a"), Assign("a", IntLiteral(1)), Block([Declare("a"), Assign("a", IntLiteral(2)), Write(VarRef("a"))]), Write(VarRef("a"))]),
        [2, 1],
        0,
    ),
    (
        "selected_branch_can_update_outer_value",
        Program([Declare("a"), IfElse(CompareExpr("==", IntLiteral(1), IntLiteral(1)), Block([Assign("a", IntLiteral(5))])), Write(VarRef("a"))]),
        [5],
        0,
    ),
    (
        "else_branch_can_update_outer_value",
        Program([Declare("a"), IfElse(CompareExpr("==", IntLiteral(1), IntLiteral(2)), Block([Assign("a", IntLiteral(5))]), Block([Assign("a", IntLiteral(6))])), Write(VarRef("a"))]),
        [6],
        0,
    ),
):
    _add_executor_program_case(_label, _program, _expected, _read_value)


def _add_conditional_builder_case(label: str, source: str, expected: Program):
    def test(self):
        self.assertEqual(build_program(source), expected)

    setattr(AntlrConditionalBuilderTest, f"test_builds_{label}", test)


for _op, _left, _right in (
    ("==", 1, 1),
    ("!=", 1, 2),
    (">", 2, 1),
    (">=", 2, 2),
    ("<", 1, 2),
    ("<=", 2, 2),
):
    _add_conditional_builder_case(
        f"if_with_{op_name(_op)}_condition",
        f"if ({_left} {_op} {_right}) {{ write(1); }}",
        Program([IfElse(CompareExpr(_op, IntLiteral(_left), IntLiteral(_right)), Block([Write(IntLiteral(1))]))]),
    )

_add_conditional_builder_case(
    "if_with_arithmetic_condition",
    "if (1 + 2 * 3 >= 7) { write(1); }",
    Program([IfElse(CompareExpr(">=", BinaryExpr("+", IntLiteral(1), BinaryExpr("*", IntLiteral(2), IntLiteral(3))), IntLiteral(7)), Block([Write(IntLiteral(1))]))]),
)
_add_conditional_builder_case(
    "if_with_multiple_then_statements",
    "if (1 == 1) { write(1); write(2); }",
    Program([IfElse(CompareExpr("==", IntLiteral(1), IntLiteral(1)), Block([Write(IntLiteral(1)), Write(IntLiteral(2))]))]),
)
_add_conditional_builder_case(
    "if_else_with_multiple_else_statements",
    "if (1 == 2) { write(1); } else { write(2); write(3); }",
    Program([IfElse(CompareExpr("==", IntLiteral(1), IntLiteral(2)), Block([Write(IntLiteral(1))]), Block([Write(IntLiteral(2)), Write(IntLiteral(3))]))]),
)
_add_conditional_builder_case(
    "if_with_declaration_in_then_block",
    "if (1 == 1) { int a; a = 1; write(a); }",
    Program([IfElse(CompareExpr("==", IntLiteral(1), IntLiteral(1)), Block([Declare("a"), Assign("a", IntLiteral(1)), Write(VarRef("a"))]))]),
)
_add_conditional_builder_case(
    "nested_if",
    "if (1 == 1) { if (2 > 1) { write(1); } }",
    Program([IfElse(CompareExpr("==", IntLiteral(1), IntLiteral(1)), Block([IfElse(CompareExpr(">", IntLiteral(2), IntLiteral(1)), Block([Write(IntLiteral(1))]))]))]),
)
_add_conditional_builder_case(
    "if_inside_a_block",
    "{ if (1 < 2) { write(1); } }",
    Program([Block([IfElse(CompareExpr("<", IntLiteral(1), IntLiteral(2)), Block([Write(IntLiteral(1))]))])]),
)
_add_conditional_builder_case(
    "if_followed_by_statement",
    "if (1 <= 2) { write(1); } write(2);",
    Program([IfElse(CompareExpr("<=", IntLiteral(1), IntLiteral(2)), Block([Write(IntLiteral(1))])), Write(IntLiteral(2))]),
)


@unittest.skipUnless(HAS_ANTLR, "antlr4 Python runtime is not installed")
class AstBoundaryTest(unittest.TestCase):
    """Parser and executor failure cases that are separate from normal execution."""

    def test_rejects_an_empty_expression(self):
        with self.assertRaises(SyntaxError):
            build_expression("")

    def test_rejects_an_incomplete_expression(self):
        with self.assertRaises(SyntaxError):
            build_expression("1 +")

    def test_rejects_trailing_tokens_after_an_expression(self):
        with self.assertRaises(SyntaxError):
            build_expression("1 2")

    def test_rejects_an_unclosed_expression_parenthesis(self):
        with self.assertRaises(SyntaxError):
            build_expression("(1 + 2")

    def test_rejects_an_empty_program(self):
        with self.assertRaises(SyntaxError):
            build_program("")

    def test_rejects_a_declaration_without_a_semicolon(self):
        with self.assertRaises(SyntaxError):
            build_program("int a")

    def test_rejects_a_write_without_a_semicolon(self):
        with self.assertRaises(SyntaxError):
            build_program("write(1)")

    def test_executor_rejects_a_non_program_root(self):
        with self.assertRaises(TypeError):
            AstExecutor().execute(IntLiteral(1))

    def test_expression_evaluator_rejects_read_call_outside_an_executor(self):
        with self.assertRaises(TypeError):
            evaluate(ReadCall(), {})

    def test_executor_rejects_an_unknown_arithmetic_operator(self):
        with self.assertRaises(ValueError):
            AstExecutor().eval_expr(BinaryExpr("%", IntLiteral(4), IntLiteral(2)))

    def test_executor_rejects_an_unknown_comparison_operator(self):
        with self.assertRaises(ValueError):
            AstExecutor().eval_condition(CompareExpr("~=", IntLiteral(1), IntLiteral(1)))

    def test_format_ast_rejects_an_unknown_node_type(self):
        with self.assertRaises(TypeError):
            format_ast(AstNode())


@unittest.skipUnless(HAS_ANTLR, "antlr4 Python runtime is not installed")
class SemanticBuilderTest(unittest.TestCase):
    """#4: collect every semantic error before deciding whether to execute."""

    def test_collects_duplicate_and_undefined_name_errors_from_the_whole_program(self):
        _, errors = build_program_with_diagnostics(
            "int a; int a; b = 1; write(c);"
        )

        self.assertEqual(len(errors), 3)
        self.assertIsInstance(errors[0], DuplicateDeclarationError)
        self.assertTrue(all(isinstance(error, UndefinedVariableError) for error in errors[1:]))

    def test_collects_an_error_for_a_name_that_escapes_its_block(self):
        _, errors = build_program_with_diagnostics("{ int a; } write(a);")

        self.assertEqual(len(errors), 1)
        self.assertIsInstance(errors[0], UndefinedVariableError)

    def test_executes_valid_source_after_building_it(self):
        output: list[int] = []

        errors = execute_source(
            "int a; a = read(); if (a > 0) { write(a); } else { write(0); }",
            read_fn=lambda: 7,
            write_fn=output.append,
        )

        self.assertEqual(errors, [])
        self.assertEqual(output, [7])

    def test_does_not_execute_any_statement_when_builder_found_an_error(self):
        output: list[int] = []

        errors = execute_source("write(99); a = 1;", write_fn=output.append)

        self.assertEqual(len(errors), 1)
        self.assertEqual(output, [])


if __name__ == "__main__":
    unittest.main()
