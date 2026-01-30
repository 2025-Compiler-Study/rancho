# calc1_warning_listener.py
from CalcPlusListener import CalcPlusListener


class Calc1WarningListener(CalcPlusListener):
    def __init__(self):
        super().__init__()
        # 대입문이 끝난 뒤 정의된 변수 이름들.
        self.defined = set()
        # 경고 목록: {line, column, name} 형태의 dict를 저장.
        self.warnings = []
        # 디버그 출력을 위한 현재 대입 대상.
        self._pending_assign = None

    def enterExprAssign(self, ctx):
        # "VAR '=' expr ';'" 진입 시 좌변을 기록(디버그용).
        self._pending_assign = ctx.VAR().getText()
        print(f"[enterExprAssign] lhs={self._pending_assign}")

    def exitExprAssign(self, ctx):
        # 대입문을 빠져나오면 좌변 변수를 정의된 것으로 처리.
        if self._pending_assign is not None:
            self.defined.add(self._pending_assign)
            print(f"[exitExprAssign] define {self._pending_assign}")
        self._pending_assign = None

    def enterVar(self, ctx):
        # expr 안의 VAR: 정의 이전 사용 여부를 검사.
        name = ctx.VAR().getText()
        token = ctx.VAR().symbol
        if name not in self.defined:
            warning = {"line": token.line, "column": token.column, "name": name}
            self.warnings.append(warning)
            print(
                f"[warn] Line {token.line} Column {token.column}: "
                f"Variable '{name}' is not defined."
            )
        else:
            print(f"[use] {name} is defined")
