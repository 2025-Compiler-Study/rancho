from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from CalcPlusLexer import CalcPlusLexer
from CalcPlusParser import CalcPlusParser
from graphviz import Digraph

def draw_tree(tree, parser):
    dot = Digraph(comment="Parse Tree")

    node_id = 0

    def visit(node):
        nonlocal node_id
        my_id = str(node_id)
        node_id += 1

        if isinstance(node, TerminalNode):
            label = node.getText()
        else:
            label = parser.ruleNames[node.getRuleIndex()]

        dot.node(my_id, label)

        if hasattr(node, 'children') and node.children:
            for child in node.children:
                child_id = visit(child)
                dot.edge(my_id, child_id)

        return my_id

    visit(tree)
    dot.render("parse_tree", format="png", cleanup=True)

def main():
    expr = input("expression> ")

    input_stream = InputStream(expr)
    lexer = CalcPlusLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CalcPlusParser(tokens)

    # ✅ 시작 규칙
    tree = parser.calc0()

    draw_tree(tree, parser)
    print("Saved as parse_tree.png")

if __name__ == "__main__":
    main()
