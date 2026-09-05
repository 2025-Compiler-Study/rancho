# Calc5 Compact AST

Calc5는 ANTLR Parse Tree를 직접 실행하지 않고, 의미 중심 AST로 바꾼 뒤 시각화하거나 계산한다. 현재 범위는 다음 수식과 같은 expression이다.
상세한 작업 내역, AST 해설, ANTLR 연결, 실행 방법은 [`docs/calc5-expression-ast-guide.md`](docs/calc5-expression-ast-guide.md)에 정리되어 있다.
AST가 해당 모양이 되는 원리는 [`docs/ast-structure-explanation.md`](docs/ast-structure-explanation.md)에서 단계별로 설명한다.



```text
5 * 3 + a * (5 - 9 / 3)
```

## 흐름

```text
source expression
    -> CalcPlusLexer / CalcPlusParser
    -> Parse Tree
    -> calc5_ast.AstBuilder
    -> IntLiteral / VarRef / BinaryExpr
    -> AstVisualizer 또는 evaluate()
```

괄호는 AST 노드로 남지 않는다. 연산 우선순위와 괄호의 그룹화는 AST의 부모-자식 관계에 저장된다.

## 직접 관리하는 핵심 파일

- `CalcPlus.g4`: ANTLR 문법 원본
- `calc5_ast.py`: AST 노드, expression Builder, LISP 출력, 계산
- `ast_visualizer.py`: 터미널 트리와 Graphviz DOT 출력
- `ast_html_visualizer.py`: 브라우저용 대화형 HTML 출력
- `ast_exporter.py`: Markdown과 Mermaid 출력
- `test_calc5.py`: 노드, Builder, 출력, 계산 테스트
- `test_ast_visualizer.py`: 터미널/DOT 시각화 테스트
- `test_ast_html_visualizer.py`: HTML 시각화 테스트
- `test_ast_exporter.py`: 문서 출력 테스트

`CalcPlusLexer.py`, `CalcPlusParser.py`, `CalcPlusVisitor.py`, `CalcPlusListener.py`와 `*.tokens`, `*.interp`는 ANTLR 생성 파일이므로 직접 수정하지 않는다.

`symbol_table.py`는 나중에 선언문과 스코프를 추가할 때 사용한다.

## 환경 설정

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

생성된 파서는 ANTLR 4.9.2 기준이므로 Python 런타임도 같은 버전을 사용한다.

## 테스트

```bash
python3 -m unittest -v \
  test_calc5.py \
  test_ast_visualizer.py \
  test_ast_html_visualizer.py \
  test_ast_exporter.py
```

## 실행

터미널 트리:

```bash
python3 ast_visualizer.py '5 * 3 + a * (5 - 9 / 3)'
```

HTML:

```bash
python3 ast_html_visualizer.py \
  '5 * 3 + a * (5 - 9 / 3)' \
  --output ast.html
```

Mermaid:

```bash
python3 ast_exporter.py \
  '5 * 3 + a * (5 - 9 / 3)' \
  --format mermaid \
  --output ast.mmd
```

## 다음 확장 순서

1. 미정의 변수와 0 나누기 오류 테스트
2. 비교 expression
3. `Program`, 선언, 대입 AST 노드
4. `read`, `write`, block, `if/else`
5. Builder 의미 오류 수집과 Symbol Table 연결

문법을 변경한 경우에만 파서를 다시 생성한다.

```bash
antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4
```
