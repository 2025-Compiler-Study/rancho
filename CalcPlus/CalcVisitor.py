# CalcVisitor.py
from CalcPlusVisitor import CalcPlusVisitor
from CalcPlusParser import CalcPlusParser

class CalcVisitor(CalcPlusVisitor):
    # calc0 : expr EOF
    def visitCalc0(self, ctx:CalcPlusParser.Calc0Context):
        return self.visit(ctx.expr())

    # expr ('*'|'/') expr
    def visitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == CalcPlusParser.MUL:
            return left * right
        return left / right

    # expr ('+'|'-') expr
    def visitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == CalcPlusParser.ADD:
            return left + right
        return left - right

    # INT
    def visitInt(self, ctx:CalcPlusParser.IntContext):
        return int(ctx.INT().getText())

    # '(' expr ')'
    def visitParens(self, ctx:CalcPlusParser.ParensContext):
        return self.visit(ctx.expr())
