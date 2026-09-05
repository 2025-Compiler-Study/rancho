# Calc5 Expression AST 작업 기록과 사용법

## 1. 작업 목표

Calc5의 첫 구현 범위는 다음 expression 하나를 ANTLR로 분석하고, 의미 중심 AST로 변환하고, 시각화하고, 변수값을 넣어 계산하는 것이다.

```text
5 * 3 + a * (5 - 9 / 3)
```

Calc4까지의 Parse Tree 직접 실행 대신 다음 흐름을 만든다.

```text
source expression
    -> ANTLR Lexer / Parser
    -> Parse Tree
    -> AstBuilder
    -> expression AST
    -> Visualizer 또는 evaluate()
```

현재 단계에서는 `Program`, 선언, 대입, `read`, `write`, block, `if/else`를 구현하지 않는다. expression 변환과 실행을 먼저 작은 단위로 검증한다.

## 2. 작업 결과

AST 관련 핵심 구현을 `calc5_ast.py` 하나로 통합했다.

`calc5_ast.py`가 담당하는 내용은 다음과 같다.

- `AstNode`, `Expr`: 공통 부모 노드
- `IntLiteral`: 정수 리터럴
- `VarRef`: 변수 참조
- `BinaryExpr`: 이항 연산
- `AstBuilder`: ANTLR Parse Tree를 expression AST로 변환
- `build_expression()`: 입력 문자열을 파싱하고 AST를 반환
- `format_ast()`: AST를 LISP 형식으로 출력
- `evaluate()`: AST를 재귀적으로 계산

기존 시각화 도구는 모두 같은 `calc5_ast.py`의 노드를 사용하도록 연결했다.

- `ast_visualizer.py`: 터미널 트리, 해석 호출 순서, Graphviz DOT
- `ast_html_visualizer.py`: 브라우저용 대화형 HTML
- `ast_exporter.py`: Markdown과 Mermaid

역할이 겹치던 다음 파일은 통합 과정에서 제거했다.

- `ast_nodes.py`
- `ast_builder.py`
- `ast_executor.py`
- `ast_printer.py`
- `simple_ast.py`
- 중복 노드·간이 AST 테스트

`symbol_table.py`는 이후 statement와 block scope를 구현할 때 사용하기 위해 유지한다.

## 3. 현재 파일 구조

```text
Calc5/
├── CalcPlus.g4
├── calc5_ast.py
├── ast_visualizer.py
├── ast_html_visualizer.py
├── ast_exporter.py
├── symbol_table.py
├── test_calc5.py
├── test_ast_visualizer.py
├── test_ast_html_visualizer.py
└── test_ast_exporter.py
```

다음 파일들은 `CalcPlus.g4`에서 ANTLR이 생성한 파일이므로 직접 수정하지 않는다.

```text
CalcPlusLexer.py
CalcPlusParser.py
CalcPlusVisitor.py
CalcPlusListener.py
CalcPlus.tokens
CalcPlus.interp
CalcPlusLexer.tokens
CalcPlusLexer.interp
```

문법을 변경한 경우에만 생성 파일을 갱신한다.

```bash
antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4
```

## 4. AST 구조 해설

대상 expression은 연산 우선순위와 괄호를 반영하면 다음과 같다.

```text
(5 * 3) + (a * (5 - (9 / 3)))
```

AST에서는 연산자가 부모, 피연산자가 자식이 된다.

```text
              +
           /     \
          *       *
        /  \     /  \
       5    3   a    -
                   /   \
                  5     /
                       / \
                      9   3
```

`+`가 루트인 이유는 전체 expression에서 가장 마지막에 적용되는 연산이기 때문이다. `/`는 `-`보다 먼저 계산되므로 `-`의 오른쪽 자식이 된다.

현재 expression AST는 모든 연산자가 피연산자 두 개를 가지므로 이진 트리다. 모든 내부 노드가 자식 두 개를 갖지만 깊이가 균일하지 않으므로 완전 이진 트리는 아니다. 이후 `Program`과 `Block`이 statement 목록을 가지게 되면 AST 전체는 일반 트리가 된다.

괄호는 별도 AST 노드로 만들지 않는다.

```python
def visitParens(self, ctx):
    return self.visit(ctx.expr())
```

괄호가 만든 그룹은 이미 부모와 자식의 연결 관계에 보존되기 때문이다.

## 5. ANTLR과 AST 연결

`build_expression()`은 다음 순서로 동작한다.

```python
lexer = CalcPlusLexer(InputStream(source))
parser = CalcPlusParser(CommonTokenStream(lexer))
tree = parser.expr()
ast = AstBuilder().visit(tree)
```

현재는 프로그램 전체가 아니라 expression만 구현하므로 `parser.program()` 대신 `parser.expr()`을 사용한다. 또한 expression 뒤에 처리되지 않은 토큰이 남지 않았는지 EOF까지 확인한다.

ANTLR 문법의 대안 라벨과 Builder 메서드는 다음처럼 대응한다.

| 문법 라벨 | Builder 메서드 | AST 결과 |
| --- | --- | --- |
| `Int` | `visitInt()` | `IntLiteral` |
| `Var` | `visitVar()` | `VarRef` |
| `MulDiv` | `visitMulDiv()` | `BinaryExpr` |
| `AddSub` | `visitAddSub()` | `BinaryExpr` |
| `Parens` | `visitParens()` | 내부 expression AST |

예를 들어 `9 / 3`은 다음 노드가 된다.

```python
BinaryExpr(
    "/",
    IntLiteral(9),
    IntLiteral(3),
)
```

## 6. 비주얼라이저 출력 해설

다음 명령을 실행하면 AST 구조와 재귀 해석 순서가 출력된다.

```bash
python3 ast_visualizer.py '5 * 3 + a * (5 - 9 / 3)'
```

`n1`, `n2` 같은 값은 비주얼라이저가 전위 순회 순서로 붙인 노드 ID다.

```text
부모 -> 왼쪽 자식 -> 오른쪽 자식
```

해석 순서에 표시되는 이벤트는 다음 의미다.

- `enter`: `BinaryExpr`에 진입
- `visit`: 자식이 없는 `IntLiteral` 또는 `VarRef` 방문
- `apply`: 왼쪽과 오른쪽 계산이 끝난 후 연산자 적용

비주얼라이저는 계산값을 만들지 않는다. `evaluate()`가 실행된다면 어떤 순서로 노드를 처리할지를 보여준다.

`a = 4`일 때 실제 값은 다음 순서로 계산된다.

```text
5 * 3  = 15
9 / 3  = 3
5 - 3  = 2
4 * 2  = 8
15 + 8 = 23
```

## 7. 개발 환경과 가상환경

Calc5 디렉터리로 이동한다.

```bash
cd /home/jake/project/CS/compiler/rancho/CalcPlus/Calc5
```

가상환경은 처음 한 번만 생성한다.

```bash
python3 -m venv .venv
```

새 터미널을 열 때마다 활성화한다.

```bash
source .venv/bin/activate
```

활성화되면 일반적으로 프롬프트 앞에 `(.venv)`가 표시된다. 필요한 ANTLR Python 런타임을 설치한다.

```bash
python -m pip install -r requirements.txt
```

작업을 마치면 가상환경을 종료한다.

```bash
deactivate
```

## 8. 사용법

### 터미널 AST 시각화

```bash
python3 ast_visualizer.py '5 * 3 + a * (5 - 9 / 3)'
```

### Graphviz DOT 생성

```bash
python3 ast_visualizer.py \
  '5 * 3 + a * (5 - 9 / 3)' \
  --dot ast.dot
```

Graphviz가 설치되어 있다면 SVG로 변환할 수 있다.

```bash
dot -Tsvg ast.dot -o ast.svg
```

### HTML 비주얼라이저

```bash
python3 ast_html_visualizer.py \
  '5 * 3 + a * (5 - 9 / 3)' \
  --output ast.html
```

생성된 `ast.html`을 브라우저로 열면 노드와 해석 단계를 클릭해서 확인할 수 있다.

### LISP 형식 출력

```bash
python3 -c '
from calc5_ast import build_expression, format_ast

ast = build_expression("5 * 3 + a * (5 - 9 / 3)")
print(format_ast(ast))
'
```

예상 출력:

```text
(+ (* 5 3) (* a (- 5 (/ 9 3))))
```

### 변수값을 넣어 계산

```bash
python3 -c '
from calc5_ast import build_expression, evaluate

ast = build_expression("5 * 3 + a * (5 - 9 / 3)")
print(evaluate(ast, {"a": 4}))
'
```

예상 출력:

```text
23
```

### Markdown 보고서

```bash
python3 ast_exporter.py \
  '5 * 3 + a * (5 - 9 / 3)' \
  --format markdown \
  --output ast-report.md
```

### Mermaid 다이어그램

```bash
python3 ast_exporter.py \
  '5 * 3 + a * (5 - 9 / 3)' \
  --format mermaid \
  --output ast-diagram.mmd
```

## 9. 테스트

전체 테스트를 실행한다.

```bash
python3 -m unittest -v
```

테스트는 다음 순서의 책임을 확인한다.

1. AST leaf node
2. `BinaryExpr`의 left/right 순서
3. 수동 AST의 LISP 출력
4. 수동 AST 계산
5. ANTLR 정수와 변수 변환
6. 연산자 우선순위
7. 괄호 그룹화
8. 전체 예제 변환과 계산
9. 터미널, DOT, HTML, Markdown, Mermaid 시각화

현재 검증 결과는 18개 테스트 통과다.

## 10. 현재 제한과 다음 단계

현재 구현 범위는 expression이다.

아직 구현하지 않은 항목은 다음과 같다.

- 선언되지 않은 변수에 대한 전용 오류
- 0으로 나누기 오류 정책
- 음수의 정수 나눗셈 정책
- 비교 expression
- `Program`, 선언, 대입
- `read`, `write`
- block과 `if/else`
- Symbol Table 연결
- Builder의 의미 오류 수집

추천 확장 순서는 오류 테스트, 비교 expression, statement 노드, Symbol Table, 전체 프로그램 실행 순서다.
