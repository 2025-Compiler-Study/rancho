# Markdown and Mermaid AST Exports

`ast_exporter.py`는 Calc5 식 AST를 문서에 붙여 넣기 좋은 Markdown 또는
Mermaid 형식으로 내보낸다. 두 형식 모두 AST의 구조와 왼쪽 우선 재귀 호출
순서를 포함한다.

저장소 루트의 ANTLR 가상환경을 활성화한 뒤 Calc5에서 실행한다.

```bash
cd /home/jake/project/CS/compiler/rancho
source .venv/bin/activate
cd CalcPlus/Calc5
```

## Markdown 보고서

```bash
python ast_exporter.py '5 * 3 + a * (5 - 9 / 3)' \
  --format markdown --output ast-report.md
```

생성 파일에는 입력 코드, 들여쓰기 AST 구조, `enter`/`visit`/`apply` 호출 순서가
포함된다.

## Mermaid 다이어그램

```bash
python ast_exporter.py '5 * 3 + a * (5 - 9 / 3)' \
  --format mermaid --output ast-diagram.mmd
```

생성한 `.mmd` 내용을 Mermaid를 지원하는 Markdown 문서의 `mermaid` 코드 블록에
붙여 넣거나 Mermaid Live Editor에서 열 수 있다. `AST structure` subgraph는
부모-자식 관계를, `Evaluation call order` subgraph는 실제 재귀 호출 순서를
보여 준다.
