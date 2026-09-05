# Calc5 Overview

Calc5는 ANTLR Parse Tree를 의미 중심 AST로 바꾼 뒤 별도 단계에서 시각화하거나 계산한다. 현재 구현은 expression에 집중하며, 프로그램 statement는 이후 작은 TDD 단계로 추가한다.

## 현재 실행 흐름

```text
source expression
    -> ANTLR Lexer / Parser
    -> Parse Tree
    -> calc5_ast.AstBuilder
    -> expression AST
    -> AstVisualizer / HTML / Exporter / evaluate()
```

## 현재 AST

`calc5_ast.py`가 다음 세 expression 노드와 공통 부모를 정의한다.

- `AstNode`: 모든 AST 노드의 부모
- `Expr`: 값을 만드는 expression의 부모
- `IntLiteral`: 정수 리터럴
- `VarRef`: 변수 참조
- `BinaryExpr`: 연산자와 left/right expression

모든 현재 연산자는 이항 연산자라 expression 트리는 각 내부 노드가 자식 둘을 갖는다. 그러나 깊이가 균일하지 않으므로 완전 이진 트리일 필요는 없다. 프로그램과 블록을 추가하면 전체 AST는 여러 statement 자식을 가질 수 있는 일반 트리가 된다.

## ANTLR 연결

`CalcPlus.g4`의 대안 라벨이 Builder 메서드로 연결된다.

| 문법 라벨 | Builder | AST 결과 |
| --- | --- | --- |
| `Int` | `visitInt` | `IntLiteral` |
| `Var` | `visitVar` | `VarRef` |
| `MulDiv` | `visitMulDiv` | `BinaryExpr` |
| `AddSub` | `visitAddSub` | `BinaryExpr` |
| `Parens` | `visitParens` | 괄호 없이 내부 expression |

`build_expression()`은 입력 전체가 expression 하나인지 EOF까지 확인한 뒤 AST를 반환한다.

## 파일 역할

| 파일 | 역할 |
| --- | --- |
| `CalcPlus.g4` | 문법 원본 |
| `calc5_ast.py` | 노드, Builder, LISP 출력, 계산 |
| `ast_visualizer.py` | 터미널 트리, 평가 순서, DOT |
| `ast_html_visualizer.py` | 대화형 HTML |
| `ast_exporter.py` | Markdown, Mermaid |
| `symbol_table.py` | 향후 statement 실행용 스코프 테이블 |
| `test_calc5.py` | 핵심 AST TDD 테스트 |
| `test_ast_visualizer.py` | 텍스트/DOT 테스트 |
| `test_ast_html_visualizer.py` | HTML 테스트 |
| `test_ast_exporter.py` | Markdown/Mermaid 테스트 |

ANTLR 생성 Python 파일과 `*.tokens`, `*.interp`는 직접 수정하지 않는다.

## TDD 확장 순서

1. `IntLiteral`, `VarRef`, `BinaryExpr`
2. 수동 AST 출력과 계산
3. ANTLR의 정수·변수 Parse Tree 변환
4. 이항 연산 우선순위와 괄호
5. 전체 예제의 시각화와 계산
6. 오류 처리
7. statement와 Program AST
8. Symbol Table 및 전체 프로그램 실행
