"""Calc4 블록 스코프 심볼 테이블."""

class SymbolTableError(RuntimeError):
    """심볼 테이블 관련 오류의 공통 기반 예외."""


class DuplicateDeclarationError(SymbolTableError):
    """같은 스코프 안에서 변수를 다시 선언한 경우."""


class UndefinedVariableError(SymbolTableError):
    """선언되지 않은 변수를 읽거나 쓴 경우."""


class SymbolTable:
    """스코프 스택으로 변수 선언, 대입, 조회를 관리한다."""

    def __init__(self):
        self.scopes: list[dict[str, int]] = [{}]

    def _current_scope(self) -> dict[str, int]:
        return self.scopes[-1]

    def _find_scope_containing(self, name: str) -> dict[str, int] | None:
        # 안쪽 블록의 선언이 바깥 선언을 가려야 하므로 뒤에서부터 찾는다.
        for scope in reversed(self.scopes):
            if name in scope:
                return scope
        return None

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        # 전역 스코프는 프로그램 전체의 기본 저장소라서 제거하지 않는다.
        if len(self.scopes) == 1:
            return
        self.scopes.pop()

    def declare(self, name: str):
        scope = self._current_scope()
        # 재선언 금지는 현재 스코프만 검사해야 바깥 변수 shadowing이 가능하다.
        if name in scope:
            raise DuplicateDeclarationError(f"이미 선언된 변수입니다: {name}")
        scope[name] = 0

    def assign(self, name: str, value: int):
        # 대입은 가장 가까운 선언을 갱신해야 내부 블록과 외부 블록이 함께 동작한다.
        scope = self._find_scope_containing(name)
        if scope is None:
            raise UndefinedVariableError(f"선언되지 않은 변수입니다: {name}")
        scope[name] = value

    def lookup(self, name: str) -> int:
        # 조회도 같은 탐색 규칙을 써야 수식 평가와 대입 대상이 같은 변수를 본다.
        scope = self._find_scope_containing(name)
        if scope is None:
            raise UndefinedVariableError(f"선언되지 않은 변수입니다: {name}")
        return scope[name]
