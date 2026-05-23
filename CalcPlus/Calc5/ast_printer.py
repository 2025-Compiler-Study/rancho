"""Calc5 AST printer skeleton."""

from ast_nodes import AstNode


class AstPrinter:
    """Formats AST nodes for debugging or visualization."""

    def format(self, node: AstNode) -> str:
        raise NotImplementedError("AST 출력 형식을 구현하세요.")
