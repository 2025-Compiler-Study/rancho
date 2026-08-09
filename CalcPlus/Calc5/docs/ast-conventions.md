# AST naming conventions

`ast_nodes.py` follows the Python style guidance below.

- AST node classes use `CapWords`: `AstNode`, `Expr`, `IntLiteral`, `VarRef`,
  and `BinaryExpr`.
  Source: [PEP 8 — Class Names](https://peps.python.org/pep-0008/#class-names)
- Instance attributes use `lowercase_with_underscores`. The current attributes
  are single words (`value`, `name`, `op`, `left`, `right`), so no underscore is
  needed.
  Source: [PEP 8 — Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names)
- Indentation uses four spaces.
  Source: [PEP 8 — Indentation](https://peps.python.org/pep-0008/#indentation)
