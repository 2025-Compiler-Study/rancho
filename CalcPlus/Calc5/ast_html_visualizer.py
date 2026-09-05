"""Create a standalone browser viewer for a Calc5 expression AST."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from calc5_ast import (
    AstNode,
    BinaryExpr,
    IntLiteral,
    VarRef,
)
from calc5_ast import build_expression


def render_html(source: str, root: AstNode) -> str:
    """Return a self-contained interactive HTML page for ``root``.

    Selecting an AST node highlights every trace entry for that node. Selecting
    a trace entry focuses the AST node being entered, visited, or applied.
    """
    nodes, root_id = _serialize_tree(root)
    trace = _serialize_trace(root, nodes)
    data_json = json.dumps(
        {"source": source, "rootId": root_id, "nodes": nodes, "trace": trace},
        ensure_ascii=False,
    ).replace("</", "<\\/")
    return _HTML_TEMPLATE.replace("__VISUALIZER_DATA__", data_json)


def _serialize_tree(root: AstNode) -> tuple[list[dict], str]:
    nodes: list[dict] = []
    node_ids: dict[int, str] = {}

    def visit(node: AstNode) -> str:
        node_id = f"n{len(nodes) + 1}"
        node_ids[id(node)] = node_id
        item = {
            "id": node_id,
            "label": _label(node),
            "kind": _kind(node),
            "children": [],
        }
        nodes.append(item)

        if isinstance(node, BinaryExpr):
            item["children"] = [
                {"relation": "left", "id": visit(node.left)},
                {"relation": "right", "id": visit(node.right)},
            ]
        return node_id

    root_id = visit(root)
    return nodes, root_id


def _serialize_trace(root: AstNode, nodes: list[dict]) -> list[dict]:
    node_ids = {id_: node["id"] for id_, node in _node_identity_map(root, nodes).items()}
    trace: list[dict] = []

    def visit(node: AstNode) -> None:
        if isinstance(node, BinaryExpr):
            trace.append(("enter", node))
            visit(node.left)
            visit(node.right)
            trace.append(("apply", node))
        else:
            trace.append(("visit", node))

    visit(root)
    return [
        {
            "number": number,
            "event": event,
            "nodeId": node_ids[id(node)],
            "label": _label(node),
        }
        for number, (event, node) in enumerate(trace, start=1)
    ]


def _node_identity_map(root: AstNode, nodes: list[dict]) -> dict[int, dict]:
    """Pair pre-order AST nodes with their previously serialized entries."""
    ast_nodes: list[AstNode] = []

    def visit(node: AstNode) -> None:
        ast_nodes.append(node)
        for child in node.children():
            visit(child)

    visit(root)
    return {id(node): serialized for node, serialized in zip(ast_nodes, nodes, strict=True)}


def _label(node: AstNode) -> str:
    if isinstance(node, BinaryExpr):
        return f"BinaryExpr(op='{node.op}')"
    if isinstance(node, IntLiteral):
        return f"IntLiteral(value={node.value})"
    if isinstance(node, VarRef):
        return f"VarRef(name='{node.name}')"
    return type(node).__name__


def _kind(node: AstNode) -> str:
    if isinstance(node, BinaryExpr):
        return "binary"
    if isinstance(node, IntLiteral):
        return "literal"
    if isinstance(node, VarRef):
        return "variable"
    return "other"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create an interactive Calc5 AST viewer")
    parser.add_argument("expression", help="visualize할 Calc5 식")
    parser.add_argument("--output", default="ast-visualizer.html", help="생성할 HTML 경로")
    args = parser.parse_args(argv)

    output_path = Path(args.output)
    source = args.expression
    root = build_expression(source)
    output_path.write_text(render_html(source, root), encoding="utf-8")
    print(f"HTML 파일 저장: {output_path}")
    return 0


_HTML_TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Calc5 AST Visualizer</title>
  <style>
    :root { color: #172033; background: #f6f8fc; font-family: Inter, Pretendard, system-ui, sans-serif; }
    * { box-sizing: border-box; }
    body { margin: 0; padding: 28px; }
    header, .source, main { max-width: 1440px; margin-left: auto; margin-right: auto; }
    header { margin-bottom: 18px; }
    h1 { margin: 0 0 8px; font-size: 26px; }
    h2 { margin: 0 0 14px; font-size: 16px; }
    .hint { margin: 0; color: #56627a; }
    .source, section { border: 1px solid #dce3f0; border-radius: 12px; background: #fff; box-shadow: 0 8px 24px rgba(37, 54, 88, .05); }
    .source { margin-bottom: 20px; padding: 16px 18px; }
    .source-label { display: block; margin-bottom: 8px; color: #53617b; font-size: 12px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
    code { color: #172033; font: 600 16px/1.55 ui-monospace, SFMono-Regular, Menlo, monospace; white-space: pre-wrap; }
    main { display: grid; grid-template-columns: minmax(360px, 1.25fr) minmax(330px, .75fr); gap: 20px; }
    section { min-width: 0; padding: 18px; }
    .tree, .tree ul { margin: 0; padding-left: 22px; list-style: none; }
    .tree { padding-left: 0; }
    .tree ul { margin-left: 15px; border-left: 1px solid #cad5e8; }
    .tree li { position: relative; margin: 10px 0; }
    .tree li::before { position: absolute; top: 24px; left: -22px; width: 15px; border-top: 1px solid #cad5e8; content: ""; }
    .tree > li::before { display: none; }
    .edge-label { display: inline-block; min-width: 44px; margin-right: 6px; color: #7c879c; font: 12px ui-monospace, monospace; }
    .node { cursor: pointer; border: 1px solid #c7d3e8; border-radius: 8px; padding: 9px 11px; color: #172033; background: #f8fbff; font: 600 13px/1.3 ui-monospace, SFMono-Regular, Menlo, monospace; text-align: left; }
    .node.binary { border-color: #93c5fd; background: #dbeafe; }
    .node.literal { border-color: #d1d5db; background: #f3f4f6; }
    .node.variable { border-color: #c4b5fd; background: #ede9fe; }
    .node.selected { outline: 3px solid #fbbf24; outline-offset: 2px; }
    .controls { display: flex; gap: 8px; align-items: center; margin-bottom: 12px; }
    .control { cursor: pointer; border: 1px solid #b9c7dc; border-radius: 7px; padding: 7px 10px; color: #172033; background: #fff; font-weight: 700; }
    .control:hover { background: #eff6ff; }
    #step-status { margin-left: auto; color: #526078; font-size: 13px; }
    .trace { max-height: 620px; overflow: auto; margin: 0; padding: 0; list-style: none; }
    .trace button { display: grid; width: 100%; cursor: pointer; grid-template-columns: 30px 48px 1fr; gap: 8px; border: 0; border-left: 3px solid transparent; padding: 9px 10px; color: #26334c; background: transparent; font: 13px/1.35 ui-monospace, SFMono-Regular, Menlo, monospace; text-align: left; }
    .trace button:hover { background: #f5f8fd; }
    .trace button.active { border-left-color: #2563eb; color: #1d4ed8; background: #eff6ff; }
    .trace button.related { background: #fffbeb; }
    .step-number { color: #71809a; }
    .step-event { font-weight: 700; }
    @media (max-width: 860px) { body { padding: 16px; } main { grid-template-columns: 1fr; } .trace { max-height: 360px; } }
  </style>
</head>
<body>
  <header>
    <h1>Calc5 AST Visualizer</h1>
    <p class="hint">괄호는 별도 노드가 아니며, AST의 부모-자식 관계와 호출 순서가 그룹화와 해석 순서를 표현합니다.</p>
  </header>
  <div class="source"><span class="source-label">Input expression</span><code id="source"></code></div>
  <main>
    <section><h2>AST 구조</h2><ul class="tree" id="tree"></ul></section>
    <section>
      <h2>해석 호출 순서 <small>(eval_expr, 왼쪽 → 오른쪽)</small></h2>
      <div class="controls"><button class="control" id="previous" type="button">이전 단계</button><button class="control" id="next" type="button">다음 단계</button><span id="step-status"></span></div>
      <ol class="trace" id="trace"></ol>
    </section>
  </main>
  <script>
    const visualizerData = __VISUALIZER_DATA__;
    const nodesById = new Map(visualizerData.nodes.map(node => [node.id, node]));
    const tree = document.querySelector('#tree');
    const trace = document.querySelector('#trace');
    let activeStep = 0;
    document.querySelector('#source').textContent = visualizerData.source;

    function selectNode(nodeId) {
      document.querySelectorAll('.node').forEach(element => element.classList.toggle('selected', element.dataset.nodeId === nodeId));
      document.querySelectorAll('.trace button').forEach(element => element.classList.toggle('related', element.dataset.nodeId === nodeId));
    }

    function selectStep(index) {
      activeStep = Math.max(0, Math.min(index, visualizerData.trace.length - 1));
      const step = visualizerData.trace[activeStep];
      document.querySelectorAll('.trace button').forEach((element, itemIndex) => element.classList.toggle('active', itemIndex === activeStep));
      selectNode(step.nodeId);
      document.querySelector('#step-status').textContent = step.number + ' / ' + visualizerData.trace.length + ' 단계';
      document.querySelector('.trace button[data-step="' + activeStep + '"]').scrollIntoView({ block: 'nearest' });
    }

    function renderNode(nodeId, relation) {
      const node = nodesById.get(nodeId);
      const item = document.createElement('li');
      if (relation) {
        const edge = document.createElement('span');
        edge.className = 'edge-label';
        edge.textContent = relation + ':';
        item.appendChild(edge);
      }
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'node ' + node.kind;
      button.dataset.nodeId = node.id;
      button.textContent = '[' + node.id + '] ' + node.label;
      button.addEventListener('click', () => selectNode(node.id));
      item.appendChild(button);
      if (node.children.length) {
        const children = document.createElement('ul');
        node.children.forEach(child => children.appendChild(renderNode(child.id, child.relation)));
        item.appendChild(children);
      }
      return item;
    }

    tree.appendChild(renderNode(visualizerData.rootId, ''));
    visualizerData.trace.forEach((step, index) => {
      const item = document.createElement('li');
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.step = index;
      button.dataset.nodeId = step.nodeId;
      button.innerHTML = '<span class="step-number">' + String(step.number).padStart(2, '0') + '.</span><span class="step-event">' + step.event + '</span><span>[' + step.nodeId + '] ' + step.label + '</span>';
      button.addEventListener('click', () => selectStep(index));
      item.appendChild(button);
      trace.appendChild(item);
    });
    document.querySelector('#previous').addEventListener('click', () => selectStep(activeStep - 1));
    document.querySelector('#next').addEventListener('click', () => selectStep(activeStep + 1));
    selectStep(0);
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    raise SystemExit(main())
