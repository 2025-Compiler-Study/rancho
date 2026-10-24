"""Calc5 AST, ANTLR builders, formatter, and small program executor.

Expressions are reusable inside statements.  The supported statement subset is
declarations, assignments, read, write, blocks, comparisons, and if/else.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping

from symbol_table import SymbolTable, SymbolTableError


class AstNode:
    """Base class for every Calc5 AST node."""

    def children(self) -> tuple[AstNode, ...]:
        """Return only structural AST children, in source/execution order."""
        return ()

    def __eq__(self, other: object) -> bool:
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        fields = ", ".join(
            f"{name}={value!r}" for name, value in self.__dict__.items()
        )
        return f"{type(self).__name__}({fields})"


class Expr(AstNode):
    """Base class for AST nodes that evaluate to an integer."""


class Stmt(AstNode):
    """Base class for AST nodes that perform an action."""


class IntLiteral(Expr):
    def __init__(self, value: int):
        self.value = value


class VarRef(Expr):
    def __init__(self, name: str):
        self.name = name


class ReadCall(Expr):
    """Expression node for the value returned by ``read()``."""


class BinaryExpr(Expr):
    def __init__(self, op: str, left: Expr, right: Expr):
        self.op = op
        self.left = left
        self.right = right

    def children(self) -> tuple[Expr, Expr]:
        return self.left, self.right


class CompareExpr(AstNode):
    """Compare two integer expressions and produce a boolean control value."""

    def __init__(self, op: str, left: Expr, right: Expr):
        self.op = op
        self.left = left
        self.right = right

    def children(self) -> tuple[Expr, Expr]:
        return self.left, self.right


class Program(AstNode):
    def __init__(self, statements: list[Stmt]):
        self.statements = statements

    def children(self) -> tuple[Stmt, ...]:
        return tuple(self.statements)


class Declare(Stmt):
    def __init__(self, name: str):
        self.name = name


class Assign(Stmt):
    def __init__(self, target: str, value: Expr):
        self.target = target
        self.value = value

    def children(self) -> tuple[Expr]:
        return (self.value,)


class Write(Stmt):
    def __init__(self, value: Expr):
        self.value = value

    def children(self) -> tuple[Expr]:
        return (self.value,)


class Block(Stmt):
    def __init__(self, statements: list[Stmt]):
        self.statements = statements

    def children(self) -> tuple[Stmt, ...]:
        return tuple(self.statements)


class IfElse(Stmt):
    def __init__(
        self,
        condition: CompareExpr,
        then_block: Block,
        else_block: Block | None = None,
    ):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def children(self) -> tuple[AstNode, ...]:
        if self.else_block is None:
            return self.condition, self.then_block
        return self.condition, self.then_block, self.else_block


class AstBuilder:
    """ANTLR Parse Tree를 실행하기 쉬운 의미 중심 AST로 변환한다."""

    def __init__(self):
        # 과제 #4: AST를 만들면서 선언/사용 오류도 검사한다.
        # 오류가 하나 나더라도 전체 프로그램을 계속 순회해야 하므로,
        # Executor처럼 예외를 즉시 밖으로 던지지 않고 errors에 모아 둔다.
        self.symbols = SymbolTable()
        self.errors: list[SymbolTableError] = []

    def visit(self, tree):
        return tree.accept(self)

    def visitProgram(self, ctx):
        # program은 여러 statement를 순서대로 보관하는 최상위 AST 노드다.
        return Program(self._visit_statements(ctx.stmt()))

    def visitDeclare(self, ctx):
        # 문법의 ``int a, b;``는 실행 단위에 맞춰 Declare 두 개로 나눈다.
        declarations = []
        for token in ctx.VAR():
            name = token.getText()
            self._declare(name)
            declarations.append(Declare(name))
        return declarations

    def visitExprAssign(self, ctx):
        target = ctx.VAR().getText()
        # 오른쪽 식 내부의 변수도 먼저 모두 검사/변환한다.
        value = self.visit(ctx.expr())
        # 대입 대상 역시 이미 선언된 변수여야 한다.
        self._use(target)
        return Assign(target, value)

    def visitReadAssign(self, ctx):
        target = ctx.VAR().getText()
        self._use(target)
        return Assign(target, ReadCall())

    def visitWrite(self, ctx):
        return Write(self.visit(ctx.expr()))

    def visitStmtBlock(self, ctx):
        return self.visit(ctx.block())

    def visitBlock(self, ctx):
        # { ... } 안에서 선언한 변수는 밖에서 보이면 안 된다.
        # Builder도 Executor와 같은 scope 규칙으로 검사해야 한다.
        self.symbols.push_scope()
        try:
            return Block(self._visit_statements(ctx.stmt()))
        finally:
            self.symbols.pop_scope()

    def visitIfElse(self, ctx):
        # AST에는 조건과 두 block을 모두 보관한다.
        # 어느 block을 실행할지는 #3 Executor가 실행 시점에 결정한다.
        condition = self.visit(ctx.cond())
        then_block = self.visit(ctx.thenBlock)
        else_block = self.visit(ctx.elseBlock) if ctx.elseBlock is not None else None
        return IfElse(condition, then_block, else_block)

    def visitCond(self, ctx):
        # cond : expr 비교연산자 expr
        # 비교 결과는 숫자식과 구분되는 CompareExpr로 표현한다.
        return CompareExpr(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr(0)),
            self.visit(ctx.expr(1)),
        )

    def visitInt(self, ctx):
        return IntLiteral(int(ctx.getText()))

    def visitVar(self, ctx):
        name = ctx.getText()
        self._use(name)
        return VarRef(name)

    def visitParens(self, ctx):
        # 괄호 자체는 AST 노드가 아니다. Parse Tree에서 이미 grouping이 결정됐다.
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        return self._binary_expr(ctx)

    def visitAddSub(self, ctx):
        return self._binary_expr(ctx)

    def _visit_statements(self, contexts) -> list[Stmt]:
        statements: list[Stmt] = []
        for context in contexts:
            built = self.visit(context)
            if isinstance(built, list):
                statements.extend(built)
            else:
                statements.append(built)
        return statements

    def _binary_expr(self, ctx):
        return BinaryExpr(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr(0)),
            self.visit(ctx.expr(1)),
        )

    def _declare(self, name: str) -> None:
        try:
            self.symbols.declare(name)
        except SymbolTableError as error:
            # 중복 선언을 기록한 뒤에도 이후 statement를 계속 검사한다.
            self.errors.append(error)

    def _use(self, name: str) -> None:
        try:
            self.symbols.lookup(name)
        except SymbolTableError as error:
            # 미선언 사용도 기록만 하고 전체 Parse Tree 순회를 계속한다.
            self.errors.append(error)


def _parse(source: str, rule_name: str):
    from antlr4 import CommonTokenStream, InputStream
    from antlr4.Token import Token

    from CalcPlusLexer import CalcPlusLexer
    from CalcPlusParser import CalcPlusParser

    lexer = CalcPlusLexer(InputStream(source))
    parser = CalcPlusParser(CommonTokenStream(lexer))
    tree = getattr(parser, rule_name)()

    if parser.getNumberOfSyntaxErrors() or parser.getCurrentToken().type != Token.EOF:
        raise SyntaxError(f"유효한 {rule_name}이(가) 아닙니다: {source!r}")
    return tree


def build_expression(source: str) -> Expr:
    """Parse one complete Calc5 expression and return its AST."""
    return AstBuilder().visit(_parse(source, "expr"))


def build_program(source: str) -> Program:
    """Parse one complete Calc5 program and return its AST."""
    return AstBuilder().visit(_parse(source, "program"))


def build_program_with_diagnostics(
    source: str,
) -> tuple[Program, list[SymbolTableError]]:
    """AST와 전체 순회 중 모은 문맥 오류를 함께 반환한다."""
    builder = AstBuilder()
    program = builder.visit(_parse(source, "program"))
    return program, builder.errors


def execute_source(
    source: str,
    *,
    read_fn: Callable[[], int] | None = None,
    write_fn: Callable[[int], None] | None = None,
    error_fn: Callable[[str], None] | None = None,
) -> list[SymbolTableError]:
    """오류가 없을 때만 AST를 실행하는 Calc5 #4의 전체 진입점이다."""
    program, errors = build_program_with_diagnostics(source)
    if errors:
        # 오류가 있으면 부분 실행 결과가 생기지 않도록 Executor를 호출하지 않는다.
        report = error_fn if error_fn is not None else print
        for error in errors:
            report(str(error))
        return errors
    AstExecutor(read_fn=read_fn, write_fn=write_fn).execute(program)
    return []


def format_ast(node: AstNode) -> str:
    """Return a compact LISP-style representation of an AST."""
    if isinstance(node, IntLiteral):
        return str(node.value)
    if isinstance(node, VarRef):
        return node.name
    if isinstance(node, ReadCall):
        return "(read)"
    if isinstance(node, BinaryExpr):
        return f"({node.op} {format_ast(node.left)} {format_ast(node.right)})"
    if isinstance(node, CompareExpr):
        return f"({node.op} {format_ast(node.left)} {format_ast(node.right)})"
    if isinstance(node, Declare):
        return f"(declare {node.name})"
    if isinstance(node, Assign):
        return f"(assign {node.target} {format_ast(node.value)})"
    if isinstance(node, Write):
        return f"(write {format_ast(node.value)})"
    if isinstance(node, Block):
        return f"(block {' '.join(format_ast(stmt) for stmt in node.statements)})"
    if isinstance(node, IfElse):
        parts = ["if", format_ast(node.condition), format_ast(node.then_block)]
        if node.else_block is not None:
            parts.append(format_ast(node.else_block))
        return f"({' '.join(parts)})"
    if isinstance(node, Program):
        return f"(program {' '.join(format_ast(stmt) for stmt in node.statements)})"
    raise TypeError(f"지원하지 않는 AST 노드입니다: {type(node).__name__}")


def _apply_binary_operator(op: str, left: int, right: int) -> int:
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        return left // right
    raise ValueError(f"지원하지 않는 연산자입니다: {op}")


def evaluate(expr: Expr, variables: Mapping[str, int]) -> int:
    """Evaluate a pure expression recursively using supplied variable values."""
    if isinstance(expr, IntLiteral):
        return expr.value
    if isinstance(expr, VarRef):
        return variables[expr.name]
    if isinstance(expr, BinaryExpr):
        return _apply_binary_operator(
            expr.op,
            evaluate(expr.left, variables),
            evaluate(expr.right, variables),
        )
    raise TypeError(f"지원하지 않는 식 노드입니다: {type(expr).__name__}")


class AstExecutor:
    """과제 #3: 완성된 AST를 lexical scope 규칙으로 실행한다."""

    def __init__(
        self,
        read_fn: Callable[[], int] | None = None,
        write_fn: Callable[[int], None] | None = None,
    ):
        self.symbols = SymbolTable()
        self.read_fn = read_fn if read_fn is not None else self._read_from_console
        self.write_fn = write_fn if write_fn is not None else print
        self.outputs: list[int] = []

    def execute(self, program: Program) -> None:
        if not isinstance(program, Program):
            raise TypeError("Program 노드만 실행할 수 있습니다")
        # Program의 statements는 원본 코드 순서이므로 앞에서부터 실행한다.
        for statement in program.statements:
            self.execute_stmt(statement)

    def execute_stmt(self, statement: Stmt) -> None:
        if isinstance(statement, Declare):
            self.symbols.declare(statement.name)
            return
        if isinstance(statement, Assign):
            # 오른쪽 식을 먼저 계산해야 대입할 실제 값이 나온다.
            self.symbols.assign(statement.target, self.eval_expr(statement.value))
            return
        if isinstance(statement, Write):
            value = self.eval_expr(statement.value)
            self.outputs.append(value)
            self.write_fn(value)
            return
        if isinstance(statement, Block):
            # Block의 지역 변수는 바깥 변수와 분리된 새 scope에 저장한다.
            self.symbols.push_scope()
            try:
                for child in statement.statements:
                    self.execute_stmt(child)
            finally:
                self.symbols.pop_scope()
            return
        if isinstance(statement, IfElse):
            # AST에는 then/else가 모두 있어도 실제로는 한 branch만 실행한다.
            if self.eval_condition(statement.condition):
                self.execute_stmt(statement.then_block)
            elif statement.else_block is not None:
                self.execute_stmt(statement.else_block)
            return
        raise TypeError(f"지원하지 않는 문장 노드입니다: {type(statement).__name__}")

    def eval_expr(self, expr: Expr) -> int:
        if isinstance(expr, IntLiteral):
            return expr.value
        if isinstance(expr, VarRef):
            return self.symbols.lookup(expr.name)
        if isinstance(expr, ReadCall):
            return self.read_fn()
        if isinstance(expr, BinaryExpr):
            # 재귀적으로 left, right를 계산한 뒤 마지막에 연산자를 적용한다.
            return _apply_binary_operator(
                expr.op,
                self.eval_expr(expr.left),
                self.eval_expr(expr.right),
            )
        raise TypeError(f"지원하지 않는 식 노드입니다: {type(expr).__name__}")

    def eval_condition(self, condition: CompareExpr) -> bool:
        left = self.eval_expr(condition.left)
        right = self.eval_expr(condition.right)

        if condition.op == "==":
            return left == right
        if condition.op == "!=":
            return left != right
        if condition.op == ">":
            return left > right
        if condition.op == ">=":
            return left >= right
        if condition.op == "<":
            return left < right
        if condition.op == "<=":
            return left <= right
        raise ValueError(f"지원하지 않는 비교 연산자입니다: {condition.op}")

    @staticmethod
    def _read_from_console() -> int:
        return int(input())
