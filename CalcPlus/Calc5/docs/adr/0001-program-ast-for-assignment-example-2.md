# ADR-0001: 과제 예제 2를 위한 Program AST 도입

- 상태: accepted
- 날짜: 2026-09-19
- 관련 코드: `calc5_ast.py`, `ast_visualizer.py`, `symbol_table.py`

## 맥락

기존 Calc5는 expression만 AST로 변환하고 계산했다. 과제 1 예제 2는 선언, 대입, `read()`, `write()`, 중첩 block과 변수 스코프를 포함하므로 expression AST만으로는 프로그램의 실행 순서와 범위를 표현할 수 없다. 기존 ANTLR 문법은 이미 이 구문을 파싱할 수 있다.

## 결정

`calc5_ast.py`에 `Stmt` 계층과 `Program`, `Declare`, `Assign`, `ReadCall`, `Write`, `Block`을 추가한다. expression 노드(`IntLiteral`, `VarRef`, `BinaryExpr`)는 statement의 값 부분에서 그대로 재사용한다.

`AstBuilder`는 `int a, b;`를 `Declare("a")`, `Declare("b")` 두 노드로 평탄화한다. `AstExecutor`는 기존 `SymbolTable`을 사용하고 block 진입·종료 때 scope를 push/pop한다. 입출력은 테스트 가능하도록 함수로 주입한다.

기존 `ast_visualizer.py`는 모든 노드의 `children()`을 순회해 expression과 Program을 함께 출력한다.

## 고려한 대안

1. Parse Tree를 직접 실행한다.
   - 기각. 괄호, 세미콜론, 문법용 중간 노드가 실행 모델에 섞이고 시각화 대상과 실행 대상이 달라진다.
2. 선언문 하나를 `Declare(["a", "b"])`로 유지한다.
   - 기각. 심볼 테이블의 선언 단위와 AST 노드가 달라져 중복 선언 오류와 비주얼라이저 순서가 덜 직관적이다.
3. `if/else`, 비교식까지 한 번에 구현한다.
   - 기각. 작은 TDD 단위라는 목표에 맞지 않는다. 조건문은 별도 확장으로 남긴다.

## 결과와 트레이드오프

장점은 parse tree와 분리된 의미 중심 프로그램 트리, 재사용되는 expression AST, 실제 block 스코프 검증, 입출력 없는 결정적 테스트다.

단점은 expression 전용 `evaluate()`와 프로그램용 `AstExecutor`가 공존한다는 점이다. `evaluate()`는 기존 호출 호환성을 유지하는 순수 expression API이고, `read()` 및 문장은 `AstExecutor`에서만 실행한다.

## 검증

- `test_calc5.py`: 수동 AST 구조, `format_ast()`, ANTLR Program Builder, `read=10`일 때 `write=11`, block 종료 후 `c`가 사라지는지 검증한다.
- `test_ast_visualizer.py`: Program의 `stmt[n]` child edge와 DOT 출력을 검증한다.
- 전체 테스트는 `.venv/bin/python -m unittest -v`로 실행한다.

## 후속 작업

1. `cond`, 비교 연산, `IfElse` AST와 실행기를 별도 TDD 단계로 추가한다.
2. HTML/Mermaid exporter에 Program 표현이 필요해질 때 같은 `children()` 계약으로 확장한다.
3. Builder 단계의 의미 오류 수집 정책을 결정한다.
