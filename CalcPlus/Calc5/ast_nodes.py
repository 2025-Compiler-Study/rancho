"""Calc5 AST node skeleton."""

from __future__ import annotations

from dataclasses import dataclass


class AstNode:
    """Base type for all Calc5 AST nodes."""


class Stmt(AstNode):
    """Base type for statement nodes."""


class Expr(AstNode):
    """Base type for expression nodes."""


@dataclass(frozen=True)
class Program(AstNode):
    statements: list[Stmt]


@dataclass(frozen=True)
class Declare(Stmt):
    name: str


@dataclass(frozen=True)
class Assign(Stmt):
    name: str
    value: Expr


@dataclass(frozen=True)
class Write(Stmt):
    value: Expr


@dataclass(frozen=True)
class Block(Stmt):
    statements: list[Stmt]


@dataclass(frozen=True)
class IfElse(Stmt):
    condition: Expr
    then_block: Block
    else_block: Block | None = None


@dataclass(frozen=True)
class IntLiteral(Expr):
    value: int


@dataclass(frozen=True)
class VarRef(Expr):
    name: str


@dataclass(frozen=True)
class ReadCall(Expr):
    pass


@dataclass(frozen=True)
class BinaryExpr(Expr):
    op: str
    left: Expr
    right: Expr
