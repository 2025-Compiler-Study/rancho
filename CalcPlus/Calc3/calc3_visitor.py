"""CalcVisitor 기반으로 만든 Calc-3 인터프리터 Visitor 스켈레톤."""

from typing import Callable, Optional, Union

from calcVisitor import CalcVisitor

Number = Union[int, float]


class Calc3Visitor(CalcVisitor):
    """CalcVisitor를 상속해 Calc-3의 I/O 문장만 확장한 방문자."""

    def __init__(
        self,
        read_fn: Optional[Callable[[], str]] = None,
        write_fn: Optional[Callable[[Number], None]] = None,
    ):
        ...

    @staticmethod
    def _default_write(value: Number) -> None:
        ...

    def _read_int(self) -> int:
        ...

    def visitCalc3(self, ctx):
        ...

    def visitReadAssign(self, ctx):
        ...

    def visitWrite(self, ctx):
        ...
