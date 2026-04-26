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

    '''
    - scope top에 있는 것에 push함
    '''
    def push_scope(self):
        new_block = {}
        self.scopes.append(new_block)

    # 현재 블록을 빠져나옴
    def pop_scope(self):
        # 스택이 비어있는 때 빼야할 때 에러가 아닌 경우는? => 빈 블록
        if len(self.scopes):
          self.scopes.pop()

    # TODO: 구현과제 #2에서는 같은 블록 내에 재선언 시 에러 처리해야함
    def declare(self, name: str):
        # TODO: 스코프 스택이 비어있는 경우 감안. 예외처리
        top_scope = self.scopes[-1]
        '''
        if top_scope[str]:
          raise NotImplementedError("변수 재선언")
        '''
        top_scope[str] = 0
        raise NotImplementedError("현재 scope에 변수 선언을 구현하세요.")

    '''
    - 전역변수는 신경쓰지 않음
    - 현재 스코프만 감안함
    '''
    def assign(self, name: str, value: int):
        # TODO:self.self.scopes가 비어있는 경우 감안
        top_scope = self.scopes[-1]
        top_scope[str] = value

    def lookup(self, name: str) -> int:
        scope = self._find_scope_containing(str)
        if scope:
          return scope[str]
        # 없는 경우에 에러 처리할 것인가?, 밖에서 처리하게 할 것인가? 역할을 어디에 맡길것인가?
        return None
