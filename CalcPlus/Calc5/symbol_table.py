"""Calc5 executor support symbol table reused from Calc4."""


class SymbolTableError(RuntimeError):
    """Base exception for symbol-table errors."""


class DuplicateDeclarationError(SymbolTableError):
    """Raised when a name is declared twice in the same scope."""


class UndefinedVariableError(SymbolTableError):
    """Raised when an undeclared name is read or assigned."""


class SymbolTable:
    """Tracks declarations and values with a stack of lexical scopes."""

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
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) == 1:
            return
        self.scopes.pop()

    def declare(self, name: str):
        scope = self._current_scope()
        if name in scope:
            raise DuplicateDeclarationError(f"이미 선언된 변수입니다: {name}")
        scope[name] = 0

    def assign(self, name: str, value: int):
        scope = self._find_scope_containing(name)
        if scope is None:
            raise UndefinedVariableError(f"선언되지 않은 변수입니다: {name}")
        scope[name] = value

    def lookup(self, name: str) -> int:
        scope = self._find_scope_containing(name)
        if scope is None:
            raise UndefinedVariableError(f"선언되지 않은 변수입니다: {name}")
        return scope[name]
