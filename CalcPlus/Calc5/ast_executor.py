"""Calc5 AST executor skeleton."""

from typing import Any
from symbol_table import SymbolTable


class AstExecutor:
    """Executes Calc5 AST nodes after the parse-tree build phase."""

    def __init__(self, read_fn=None, write_fn=None):
        self.symbols = SymbolTable()
        self.outputs: list[int] = []
        self.read_fn = read_fn or self._default_read
        self.write_fn = write_fn or self._default_write

    def _default_read(self) -> int:
        return int(input())

    def _default_write(self, value: int):
        print(value)

    def execute(self, program: Any):
        raise NotImplementedError("AST Program 실행을 구현하세요.")

    def execute_stmt(self, stmt: Any):
        raise NotImplementedError("statement 노드 실행을 구현하세요.")

    def eval_expr(self, expr: Any) -> int:
        raise NotImplementedError("expression 노드 평가를 구현하세요.")
