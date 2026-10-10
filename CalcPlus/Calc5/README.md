# Calc5 Compact AST

Calc5는 ANTLR Parse Tree를 직접 실행하지 않고 의미 중심 AST로 변환한 뒤 시각화하거나 실행한다. 현재는 expression과 program subset(선언·대입·`read`·`write`·block·비교·`if/else`)을 지원한다.

- expression 구조와 원리: [`docs/calc5-expression-ast-guide.md`](docs/calc5-expression-ast-guide.md)
- Program 확장과 검증: [`docs/calc5-program-ast-guide.md`](docs/calc5-program-ast-guide.md)
- 설계 결정(ADR): [`docs/adr/0001-program-ast-for-assignment-example-2.md`](docs/adr/0001-program-ast-for-assignment-example-2.md)

## 흐름

```text
source
  -> CalcPlusLexer / CalcPlusParser
  -> Parse Tree
  -> calc5_ast.AstBuilder
  -> expression AST 또는 Program AST
  -> AstVisualizer / AstExecutor
```

`BinaryExpr`는 left/right를 갖는 이진 트리다. `Program`, `Block`은 여러 statement 자식을 가지므로 전체 AST는 일반 트리다. 괄호는 노드로 남지 않고 부모-자식 연결로 그룹화가 보존된다.

## 핵심 파일

- `CalcPlus.g4`: ANTLR 문법 원본
- `calc5_ast.py`: AST 노드, Builder, formatter, expression 계산, 프로그램 실행기
- `symbol_table.py`: 선언과 lexical block scope
- `ast_visualizer.py`: 터미널 트리와 Graphviz DOT
- `test_calc5.py`, `test_ast_visualizer.py`: TDD 핵심 테스트

`CalcPlusLexer.py`, `CalcPlusParser.py`, `CalcPlusVisitor.py`, `CalcPlusListener.py`, `*.tokens`, `*.interp`는 ANTLR 생성 파일이므로 직접 수정하지 않는다.

## 빠른 시작

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest -v
```

expression 시각화:

```bash
.venv/bin/python ast_visualizer.py '5 * 3 + a * (5 - 9 / 3)'
```

Program 시각화:

```bash
.venv/bin/python ast_visualizer.py --program $'int a;\na = 1;\nwrite(a);'
```
