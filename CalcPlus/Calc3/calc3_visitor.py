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
        super().__init__()
        self.env = self.memory
        self.outputs: list[Number] = []
        # self.read_fn = read_fn or input
        self.read_fn = read_fn
        # self.write_fn = write_fn or self._default_write
        self.write_fn = write_fn

    '''
    static method의 장점? 인스턴스화 하지 않아도 쓸 수 있어서 인가?
    '''
    @staticmethod
    def _default_write(value: Number) -> None:
        print(value)

    '''
    input(), print()
    '''
    def _read_int(self) -> int:
        try:
            raw = self.read_fn()
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

    '''
      stmt    :   VAR '=' expr ';'   # ExprAssign
             |   VAR '=' 'read' '(' ')' ';' # ReadAssign

    '''
    def visitReadAssign(self, ctx):
        var_name = ctx.VAR().getText()
        value = self._read_int()
        self.memory[var_name] = value
        return value

    def visitWrite(self, ctx):
        value = self.visit(ctx.expr())
        self.outputs.append(value)
        self.write_fn(value)
        return value

'''
# 기존 상속 방식으로 못하는 시점이 오게 됨



memory
{
  a =
  {
    a 

  }

}

'''