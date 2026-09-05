# Calc5 Test Structure

테스트는 코어 AST와 표현 방식을 분리한다.

## `test_calc5.py`

작은 TDD 순서로 핵심 동작을 확인한다.

1. `IntLiteral`, `VarRef`, `BinaryExpr`의 값과 자식 순서
2. 수동 AST의 LISP 출력
3. 변수값을 사용한 재귀 계산
4. ANTLR Parse Tree의 정수·변수 변환
5. 연산 우선순위와 괄호 그룹화
6. 전체 예제 expression의 AST와 결과

ANTLR 런타임이 없으면 Builder 통합 테스트만 skip되고, 순수 AST 테스트는 실행된다.

## 시각화 테스트

- `test_ast_visualizer.py`: 터미널 트리, 방문 순서, DOT
- `test_ast_html_visualizer.py`: HTML 트리와 단계 제어
- `test_ast_exporter.py`: Markdown과 Mermaid

시각화 테스트는 수동 AST를 사용해 ANTLR과 독립적으로 먼저 검증한다. 별도 통합 테스트에서 `build_expression()` 결과도 같은 비주얼라이저에 전달한다.

## 다음 TDD 항목

1. 미정의 변수
2. 0으로 나누기
3. 지원하지 않는 연산자
4. 비교 expression
5. statement와 Program AST
