# ADR-0002: 비교 조건과 if/else를 AST Executor에서 실행한다

- 상태: accepted
- 날짜: 2026-10-10
- 관련 코드: `calc5_ast.py`, `ast_visualizer.py`, `test_calc5.py`

## 맥락

CalcPlus 문법은 `cond`와 `if/else`를 이미 지원하지만, 기존 AST Executor는 선언, 대입, read/write, block까지만 실행했다. 이 때문에 문법상 유효한 조건문 프로그램을 AST로 만들거나 실행할 수 없었다.

## 결정

비교식은 `CompareExpr(op, left, right)`로, 제어문은 `IfElse(condition, then_block, else_block=None)`로 표현한다. `AstExecutor.eval_condition()`이 비교 연산을 계산하고 `execute_stmt()`가 조건 결과에 따라 정확히 한 block만 실행한다.

각 분기는 기존 `Block` 실행 경로를 재사용한다. 따라서 분기별 scope 생성·제거와 SymbolTable 오류 정책은 변경하지 않는다.

## 고려한 대안

1. 비교 결과를 정수 `0`/`1`을 반환하는 `BinaryExpr`로 표현한다.
   - 기각. 산술식과 제어 조건의 의미와 허용 연산자가 섞여 시각화와 오류 메시지가 불명확해진다.
2. Parse Tree를 Executor가 직접 순회해 분기한다.
   - 기각. 과제 #3의 AST만 실행한다는 요구와 맞지 않는다.
3. 조건문 구현을 계속 미룬다.
   - 기각. 문법에 이미 있는 프로그램 statement 범위를 실행하지 못한 채 남는다.

## 결과와 트레이드오프

조건문까지 의미 중심 AST에서 실행할 수 있고, 텍스트/DOT 비주얼라이저에도 condition/then/else 관계가 드러난다. 반면 node 종류와 Builder·Executor 분기가 늘어난다.

## 검증

- 참 조건에서 then block만 실행한다.
- 거짓 조건에서 else block만 실행한다.
- else 없는 거짓 조건은 아무 동작도 하지 않는다.
- ANTLR source를 `build_program()`으로 변환한 뒤 Executor가 실행한다.
- 비주얼라이저가 조건과 두 분기 관계를 표시한다.

## 후속 작업

1. 조건문 안의 block shadowing과 오류 상황을 추가 테스트한다.
2. HTML/Mermaid exporter에도 Program과 조건문 표현이 필요할 때 `children()` 계약을 재사용한다.
