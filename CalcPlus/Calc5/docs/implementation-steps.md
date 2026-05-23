# Calc5 Implementation Steps

## 1. AST 노드 확정

`ast_nodes.py`의 노드가 Calc5 과제를 표현하기에 충분한지 확인한다.
최소 노드는 다음과 같다.

- `Program`
- `Declare`
- `Assign`
- `Write`
- `Block`
- `IfElse`
- `IntLiteral`
- `VarRef`
- `ReadCall`
- `BinaryExpr`

## 2. expression builder 구현

가장 먼저 `Int`, `Var`, `Parens`, `MulDiv`, `AddSub`, `Cond`를 AST expression으로 바꾼다.
괄호는 AST 노드로 남기지 않고 내부 expression만 반환하는 편이 단순하다.

## 3. statement builder 구현

그 다음 statement를 변환한다.

- `int a, b;`는 여러 `Declare` 노드로 분리한다.
- `a = expr;`는 `Assign` 노드로 만든다.
- `a = read();`는 `Assign("a", ReadCall())` 형태로 만들 수 있다.
- `write(expr);`는 `Write` 노드로 만든다.
- block은 statement 리스트를 가진 `Block` 노드로 만든다.

## 4. AST 출력 구현

`ast_printer.py`에서 JSON, LISP, 들여쓰기 방식 중 하나를 골라 출력한다.
출력 목표는 정답 포맷이 아니라 AST 구조 확인이다.

## 5. AST Executor 구현

`ast_executor.py`에서 `Program`부터 순서대로 실행한다.
식 노드는 값을 반환하고, 문장 노드는 상태를 바꾼다.
변수 관리는 `symbol_table.py`를 사용한다.

## 6. Builder 오류 수집

마지막으로 Builder 단계에서 선언 전 사용, 중복 선언 같은 오류를 모을지 결정한다.
Calc5 과제는 전체 Parse Tree를 순회한 뒤 오류를 출력하라는 요구가 있으므로, 즉시 예외와 오류 리스트 방식 중 하나를 명확히 선택한다.
