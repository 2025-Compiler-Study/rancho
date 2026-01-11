# CalcVisitor.py
from CalcPlusVisitor import CalcPlusVisitor
from CalcPlusParser import CalcPlusParser

class CalcVisitor(CalcPlusVisitor):
    # calc0 : expr EOF
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visit(ctx.expr())
    
    # expr ('*'|'/') expr 
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left * right if op == '*' else left / right
    
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        # ctx.expr(0)
        # print(f"ctx : #{ctx}")
        print(f"ctx.expr(0) : #{ctx.expr(0)}")
        print(f"ctx.expr(1) : #{ctx.expr(1)}")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left + right if op == '+' else left - right
    
    # INT
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        return int(ctx.INT().getText())
    
    # 괄호 ( )
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        return self.visit(ctx.expr())

'''
class CalcVisitorPostfix(CalcPlusVisitor):
    # calc0 : expr EOF, 마지막인지 확인
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context)
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
'''

    