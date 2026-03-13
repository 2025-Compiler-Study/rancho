# calc1_warning_listener.py
"""Calc-1 과제용 미정의 변수 경고 Listener."""

from __future__ import annotations

from CalcPlusListener import CalcPlusListener
from CalcPlusParser import CalcPlusParser


class Calc1WarningListener(CalcPlusListener):
    """
    변수 정의/사용 타이밍을 추적해 경고를 수집한다.

    규칙:
    - 식에서 변수를 사용할 때(`enterVar`) 아직 정의되지 않았다면 경고.
    - 대입문이 끝날 때(`exitExprAssign`) 좌변 변수를 정의된 것으로 등록.
    """

    def __init__(self) -> None:
        super().__init__()

        # 대입문이 완료된 변수 이름 집합.
        self.defined: set[str] = set()

        # 구조화된 경고 목록.
        # 예: {"name": "b", "line": 1, "column": 4, "message": "..."}
        self.warnings: list[dict[str, int | str]] = []

        # 사람이 읽기 쉬운 문자열 경고 목록(라인/컬럼 포함).
        self.errors: list[str] = []

    def enterVar(self, ctx: CalcPlusParser.VarContext) -> None:
        """
        변수 사용 시점 검사.

        이 콜백은 expr의 `#Var`에서만 호출되므로 우변 변수 검사에 적합하다.
        """
        name = ctx.VAR().getText()
        if name in self.defined:
            return

        token = ctx.VAR().getSymbol()
        line = token.line
        column = token.column
        message = self._format_error(name, line, column)

        self.warnings.append(
            {
                "name": name,
                "line": line,
                "column": column,
                "message": message,
            }
        )
        self.errors.append(message)

    def exitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext) -> None:
        """대입문 종료 시 좌변 변수를 정의된 집합에 등록한다."""
        var_name = ctx.VAR().getText()
        self.defined.add(var_name)

    @staticmethod
    def _format_error(name: str, line: int, column: int) -> str:
        """라인/컬럼 포함 표준 경고 문자열."""
        return f"Line {line}, Column {column}: {name}(은)는 선언되지 않은 변수 입니다."

