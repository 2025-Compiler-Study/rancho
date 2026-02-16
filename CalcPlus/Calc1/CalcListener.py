# CalcListener.py
"""Calc-1의 미정의 변수 사용 경고를 처리하는 Listener 구현."""

from __future__ import annotations

from CalcPlusListener import CalcPlusListener
from CalcPlusParser import CalcPlusParser


class CalcListener(CalcPlusListener):
    """
    ParseTreeWalker와 함께 사용하는 경고 수집용 Listener.

    동작 원리:
    1) 변수 사용(`enterVar`) 시점에 해당 변수가 이미 정의되었는지 검사한다.
    2) 대입문 종료(`exitExprAssign`) 시점에 좌변 변수를 '정의됨' 집합에 추가한다.
       - 이렇게 해야 `a = a + 1;`에서 우변의 `a`를 미정의로 올바르게 잡을 수 있다.
    """

    def __init__(self) -> None:
        super().__init__()

        # 현재까지 "대입 완료"된 변수 이름 집합.
        self.defined: set[str] = set()

        # 사람이 바로 읽기 쉬운 에러 문자열 목록.
        # 예: "Line 1, Column 4: b(은)는 선언되지 않은 변수 입니다."
        self.errors: list[str] = []

        # 테스트/후처리를 위한 구조화된 경고 목록.
        # 각 원소: {"name": str, "line": int, "column": int, "message": str}
        self.warnings: list[dict[str, int | str]] = []

    def enterVar(self, ctx: CalcPlusParser.VarContext) -> None:
        """
        변수 사용 지점에서 미정의 변수 사용을 검사한다.

        `VarContext`는 expr 규칙의 `#Var` 대안에서만 생성되므로,
        대입문의 좌변 변수는 여기로 들어오지 않는다.
        """
        var_name = ctx.VAR().getText()

        # 이미 정의된 변수라면 경고 없이 통과.
        if var_name in self.defined:
            return

        # ANTLR 토큰에서 정확한 소스 위치(line/column)를 가져온다.
        token = ctx.VAR().getSymbol()
        line = token.line
        column = token.column

        # 요구사항: 에러 메시지에 라인/컬럼 포함.
        message = self._format_error(var_name, line, column)

        # 문자열 형태 + 구조화 형태를 모두 저장해 다양한 테스트에 대응.
        self.errors.append(message)
        self.warnings.append(
            {
                "name": var_name,
                "line": line,
                "column": column,
                "message": message,
            }
        )

    def exitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext) -> None:
        """
        대입문을 빠져나올 때 좌변 변수를 정의된 변수로 등록한다.

        중요:
        - enterExprAssign에서 등록하면 `a = a + 1;`의 우변 `a`가
          미정의 검사를 통과해 버리므로, 반드시 exit 시점에 등록한다.
        """
        lhs_name = ctx.VAR().getText()
        self.defined.add(lhs_name)

    @staticmethod
    def _format_error(var_name: str, line: int, column: int) -> str:
        """테스트/출력에서 재사용할 표준 에러 문자열을 만든다."""
        return f"Line {line}, Column {column}: {var_name}(은)는 선언되지 않은 변수 입니다."

    def result(self) -> list[str]:
        """기존 호출부 호환을 위한 보조 메서드."""
        return self.errors

