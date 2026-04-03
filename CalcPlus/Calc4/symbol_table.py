"""Calc4 스코프 심볼 테이블 골격."""

# TODO 
'''초기화된다
동작이 여러 개

- 중첩 블럭
- 선언
  - 재선언 
- 할당
## 2단계
push, pop은 확장
lookup
등등 고려

'''

class SymbolTableError(RuntimeError):
    """심볼 테이블 관련 오류의 공통 기반 예외."""


class DuplicateDeclarationError(SymbolTableError):
    """같은 스코프 안에서 변수를 다시 선언한 경우."""


class UndefinedVariableError(SymbolTableError):
    """선언되지 않은 변수를 읽거나 쓴 경우."""


class SymbolTable:
    """블록 스코프 구현용 최소 인터페이스와 헬퍼를 정의한다."""
    '''
    현재 블럭에 찾고자하는 변수가 있는가?
    '''

    def __init__(self):
        self.scopes: list[dict[str, int]] = [{}]

    def _current_scope(self) -> dict[str, int]:
        return self.scopes[-1]

    def _find_scope_containing(self, name: str) -> dict[str, int] | None:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope
        return None

    def push_scope(self):
        raise NotImplementedError("블록 진입 시 scope push를 구현하세요.")

    def pop_scope(self):
        raise NotImplementedError("블록 종료 시 scope pop을 구현하세요.")

    def declare(self, name: str):
        raise NotImplementedError("현재 scope에 변수 선언을 구현하세요.")

    def assign(self, name: str, value: int):
        raise NotImplementedError("가장 가까운 선언 위치에 값 대입을 구현하세요.")

    def lookup(self, name: str) -> int:
        raise NotImplementedError("안쪽 scope부터 변수 조회를 구현하세요.")
