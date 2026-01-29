# CalcVisitor.py
from CalcPlusVisitor import CalcPlusVisitor
from CalcPlusParser import CalcPlusParser

'''
왼쪽에 stmt는 값을 반환
expression은 값, 계산함
';' 세미콜론을 만나야 평가함
calc1 에서는 예외처리 없으므로 무시
'''
class CalcVisitor(CalcPlusVisitor):
    # calc0 : expr EOF

    # def calc1_visitor(self, ctx:CalcPlusParser.Calc0Context):
    #     return self.visit(ctx.expr())

    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visit(ctx.expr())

    def visitCalc1(self, ctx:CalcPlusParser.Calc1Context):
        for stmt_ctx in ctx.stmt():
            print(f"[visitCalc1] stmt: {stmt_ctx.getText()}")
            self.visit(stmt_ctx)
    
    # expr ('*'|'/') expr 
    def visitMulDiv(self, ctx):
        # print(f"ctx.expr(0).getText() : {ctx.expr(0).getText()}")
        # print(f"ctx.expr(1).getText() : {ctx.expr(1).getText()}")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        # print(f"op : {op}")
        return left * right if op == '*' else left / right
    
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        # ctx.expr(0)
        # print(f"ctx.expr(0).getText() : {ctx.expr(0).getText()}")
        # print(f"ctx.expr(1).getText() : {ctx.expr(1).getText()}")
        left = self.visit(ctx.expr(0))
        # print(f"left : {left}")
        right = self.visit(ctx.expr(1))
        # print(f"right : {right}")
        op = ctx.getChild(1).getText()
        # print(f"op : {op}")
        return left + right if op == '+' else left - right
    
    # INT
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        # print(f"type(ctx.INT(): {type(ctx.INT())}")
        # print(f"type(ctx.INT().getText(): {type(ctx.INT().getText())}")
        return int(ctx.INT().getText())
    
    # 괄호 ( )
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        # print(f"ctx.expr(): {ctx.expr()}")
        # print(f"self.visit(ctx.expr()): {self.visit(ctx.expr())}")
        return self.visit(ctx.expr())

    # stmt: VAR '=' expr ';'  # ExprAssign
    def visitExprAssign(self, ctx:CalcPlusParser.ExprAssignContext):
        left_name = ctx.VAR().getText()
        right_value = self.visit(ctx.expr())
        print(f"[stmt] left: {left_name}, right: {right_value}")
        return right_value
'''
중위 연산자 -> 후위 연산자
- 10 + 2 * (5 - 9 / 3)
- 10 + 2
- 리스너의 순회방식을 차용한다.
- 후위순회?
트리모양을 생각한다.
https://www.web4college.com/converters/infix-to-postfix-prefix.php
'''

class CalcVisitorPostfix(CalcPlusVisitor):
    # calc0 : expr EOF
    # 해당 연산자를 방문하는 역할만 하는가?
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        print(f"{ctx.expr().getText()=}")
        print(f"{self.visit(ctx.expr())=}")
        return self.visit(ctx.expr())

    # expr ('*'|'/') expr 
    def visitMulDiv(self, ctx):
        print(f"ctx.expr(0).getText() : {ctx.expr(0).getText()}")
        print(f"ctx.expr(1).getText() : {ctx.expr(1).getText()}")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        print(f"op : {op}")
        cur_expression = f"{left} {right} {op}"
        return cur_expression
    
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        print(f"ctx.expr(0).getText() : {ctx.expr(0).getText()}")
        print(f"ctx.expr(1).getText() : {ctx.expr(1).getText()}")
        left = self.visit(ctx.expr(0))
        print(f"left : {left}")
        right = self.visit(ctx.expr(1))
        print(f"right : {right}")
        op = ctx.getChild(1).getText()
        print(f"op : {op}")
        cur_expression = f"{left} {right} {op}"
        return cur_expression

    # INT
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        print(f"type(ctx.INT(): {type(ctx.INT())}")
        print(f"type(ctx.INT().getText(): {type(ctx.INT().getText())}")
        return int(ctx.INT().getText())

    # 괄호 ( )
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        print(f"# ctx.expr(): {ctx.expr()}")
        print(f"self.visit(ctx.expr()): {self.visit(ctx.expr())}")
        return self.visit(ctx.expr())
