# CalcVisitor.py
from CalcPlusVisitor import CalcPlusVisitor
from CalcPlusParser import CalcPlusParser

class CalcVisitor(CalcPlusVisitor):
    # calc0 : expr EOF
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visit(ctx.expr())
    
    # expr ('*'|'/') expr 
    def visitMulDiv(self, ctx):
        print(f"ctx.expr(0).getText() : {ctx.expr(0).getText()}")
        print(f"ctx.expr(1).getText() : {ctx.expr(1).getText()}")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        print(f"op : {op}")
        return left * right if op == '*' else left / right
    
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        # ctx.expr(0)
        print(f"ctx.expr(0).getText() : {ctx.expr(0).getText()}")
        print(f"ctx.expr(1).getText() : {ctx.expr(1).getText()}")
        left = self.visit(ctx.expr(0))
        print(f"left : {left}")
        right = self.visit(ctx.expr(1))
        print(f"right : {right}")
        op = ctx.getChild(1).getText()
        print(f"op : {op}")
        return left + right if op == '+' else left - right
    
    # INT
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        print(f"type(ctx.INT(): {type(ctx.INT())}")
        print(f"type(ctx.INT().getText(): {type(ctx.INT().getText())}")
        return int(ctx.INT().getText())
    
    # 괄호 ( )
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        # print(f"ctx.expr(): {ctx.expr()}")
        # print(f"self.visit(ctx.expr()): {self.visit(ctx.expr())}")
        return self.visit(ctx.expr())
'''
중위 연산자 -> 후위 연산자
- 10 + 2 * (5 - 9 / 3)
- 10 + 2
'''
class CalcVisitorPostfix(CalcPlusVisitor):
    # calc0 : expr EOF, 마지막인지 확인
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
      return self.visit(ctx.expr())

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        rigit = self.visist(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left * right if op == '*' else left /right
    
    def to_postfix_expr(self, infix_expr):
        # infix
        postfix_expr = None
        return postfix_expr

    