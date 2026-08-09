# calc1_warning_listener.py
"""Listener 구현체로 Calc-1 과제 #2(미정의 변수 경고)를 해결한다."""

from generated.CalcPlusListener import CalcPlusListener
from generated.CalcPlusParser import CalcPlusParser


class Calc1WarningListener(CalcPlusListener):
    """enter/exit 이벤트를 사용해 변수 정의 여부를 추적한다."""

    def __init__(self):
        super().__init__()
        self.defined: set[str] = set()
        self.warnings: list[dict[str, int | str]] = []

    def exitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        # 좌변 변수는 이 시점에서 정의된 것으로 취급
        var_name = ctx.VAR().getText()
        self.defined.add(var_name)

    def exitVar(self, ctx: CalcPlusParser.VarContext):
        var_name = ctx.VAR().getText()
        if var_name in self.defined:
            return

        token = ctx.VAR().getSymbol()
        self.warnings.append(
            {
                "name": var_name,
                "line": token.line,
                "column": token.column,
            }
        )
