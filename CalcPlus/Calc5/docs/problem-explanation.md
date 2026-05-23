# Calc5 Problem Explanation

Calc5의 핵심은 실행 흐름을 두 단계로 나누는 것이다.

Calc4까지는 ANTLR가 만든 Parse Tree를 Visitor가 직접 순회하며 바로 실행했다.
Calc5에서는 Parse Tree를 먼저 AST로 바꾸고, 그 AST를 별도 Executor가 실행한다.

## 왜 AST를 만드는가

Parse Tree는 문법을 그대로 반영한다. 괄호, 중간 규칙, 문법상 필요한 구조가 모두 남아 있다.
AST는 프로그램의 의미를 실행하기 좋은 형태로 정리한다.

예를 들어 `int a, b;`는 Parse Tree에서는 하나의 선언문이지만, AST에서는 보통 `Declare("a")`, `Declare("b")` 두 노드로 나누는 편이 실행하기 쉽다.

## Calc5에서 나눌 책임

- `ast_nodes.py`: AST가 어떤 노드로 구성되는지 정의한다.
- `ast_builder.py`: Parse Tree를 AST로 바꾼다.
- `ast_printer.py`: AST 구조를 사람이 볼 수 있게 출력한다.
- `ast_executor.py`: AST를 실행한다.
- `symbol_table.py`: 실행 중 변수 선언, 조회, 대입, 스코프를 관리한다.

## 중요한 변경점

문법 진입점은 `program`이다. 이전 Calc4의 `calc4` 진입점 이름을 그대로 쓰면 Calc5 테스트와 구현 방향이 흐려진다.

Parse Tree Builder와 AST Executor는 둘 다 Symbol Table을 가질 수 있다. Builder 단계에서는 정적 의미 오류를 모으고, Executor 단계에서는 실제 실행 값을 관리한다.
