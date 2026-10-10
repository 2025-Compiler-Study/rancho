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


if __name__ == "__main__":
    unittest.main()
