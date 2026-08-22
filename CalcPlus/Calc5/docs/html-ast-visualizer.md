# Interactive AST Visualizer

`ast_html_visualizer.py`는 Calc5 식으로부터 독립 HTML 파일을 생성한다.
브라우저에서 파일을 열면 AST 구조와 `eval_expr` 호출 순서를 같은 노드 ID로
연결해 볼 수 있다.

```bash
cd CalcPlus/Calc5
python3 ast_html_visualizer.py '5 * 3 + a * (5 - 9 / 3)' --output ast.html
```

생성된 `ast.html`을 브라우저로 연다.

- 트리 노드를 선택하면 그 노드의 모든 `enter`, `visit`, `apply` trace가 강조된다.
- trace 항목 또는 이전/다음 단계 버튼을 선택하면 해당 AST 노드가 강조된다.
- 리터럴, 변수 참조, 이항 연산은 서로 다른 색으로 나타난다.

이 도구는 식을 실행하지 않는다. `apply`는 각 이항 연산이 두 자식 평가 뒤에
적용되는 시점을 뜻하므로, 변수 값이 없어도 해석 순서를 확인할 수 있다.
