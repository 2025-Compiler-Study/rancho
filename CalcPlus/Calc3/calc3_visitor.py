"""Calc-3 interpreter visitor built on top of CalcVisitor."""

from typing import Callable, List, Optional, Union

from calcVisitor import CalcVisitor

Number = Union[int, float]


class Calc3Visitor(CalcVisitor):
    """CalcVisitor를 상속해 Calc-3의 I/O 문장만 확장한 Visitor."""

    def __init__(
        self,
        read_fn: Optional[Callable[[], str]] = None,
        write_fn: Optional[Callable[[Number], None]] = None,
    ):
        super().__init__()
        # 기존 memory를 그대로 사용하되 Calc3 명칭(env)도 함께 제공한다.
        self.env = self.memory
        self.outputs: List[Number] = []
        self._read_fn = read_fn or input
        self._write_fn = write_fn or self._default_write

    @staticmethod
    def _default_write(value: Number) -> None:
        print(value)

    def _read_int(self) -> int:
        try:
            raw = self._read_fn()
        except EOFError:
            return 0

        if raw is None:
            return 0

        text = str(raw).strip()
        if text == "":
            return 0

        try:
            return int(text)
        except ValueError:
            return 0

    def visitCalc3(self, ctx):
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        return dict(self.memory)

    def visitReadAssign(self, ctx):
        var_name = ctx.VAR().getText()
        value = self._read_int()
        self.memory[var_name] = value
        return value

    def visitWrite(self, ctx):
        value = self.visit(ctx.expr())
        self.outputs.append(value)
        self._write_fn(value)
        return value

    def visitIfElse(self, ctx):
        if self.visit(ctx.cond()):
            self.visit(ctx.thenBlock)
        elif ctx.elseBlock is not None:
            self.visit(ctx.elseBlock)
        return None
