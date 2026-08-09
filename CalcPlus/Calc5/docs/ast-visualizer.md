# AST Visualizer

`ast_visualizer.py`는 Calc5 식을 AST로 변환한 결과와, 그 AST를 따라
`eval_expr`가 호출될 순서를 함께 보여 주는 CLI 도구다. AST 자체만을
대상으로 하므로 식을 실행하거나 변수 값을 요구하지 않는다.

## 실행

Calc5 디렉터리에서 실행한다.

```bash
python3 ast_visualizer.py '5 * 3 + a * (5 - 9 / 3)'
```

출력은 두 부분으로 나뉜다.

1. `AST 구조`: 부모-자식 관계를 보여 준다. 노드 ID는 pre-order로 붙는다.
2. `해석 호출 순서`: `eval_expr`가 왼쪽 자식부터 재귀 호출한다고 가정한
   enter, visit, apply 순서를 보여 준다. 각 항목은 AST 구조의 같은 노드 ID를
   사용한다.

예를 들어 `5 * 3 + a * (5 - 9 / 3)`에서 `/` 노드의 `apply`는 `-` 노드의
`apply`보다 먼저 나타난다. 따라서 괄호 노드를 AST에 남기지 않아도 `9 / 3`의
결과가 `5 - ...`의 오른쪽 피연산자가 된다는 구조와 해석 순서를 확인할 수 있다.

## 그래프 파일

`--dot`으로 의존성 없는 Graphviz DOT 파일을 만들 수도 있다.

```bash
python3 ast_visualizer.py '5 * 3 + a * (5 - 9 / 3)' --dot ast.dot
dot -Tsvg ast.dot -o ast.svg
```

DOT 생성 자체에는 Python Graphviz 패키지가 필요하지 않다. SVG 또는 PNG로
렌더링하는 두 번째 명령에는 시스템의 Graphviz `dot` 명령이 필요하다.

## 범위

현재 Calc5 AST가 구현 중인 `IntLiteral`, `VarRef`, `BinaryExpr` 식만
지원한다. 선언문과 블록 등 프로그램 전체의 AST 노드가 추가되면 같은 노드 ID
체계를 statement에도 확장할 수 있다.
