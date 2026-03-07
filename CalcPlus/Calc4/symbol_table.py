"""Calc4 스코프 심볼 테이블 스텁."""


class SymbolTable:
    """블록 스코프 구현용 최소 인터페이스만 정의한다."""

    def __init__(self):
        self.scopes: list[dict[str, int]] = [{}]

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
