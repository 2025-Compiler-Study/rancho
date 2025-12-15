# CalcListener.py
from CalcPlusListener import CalcPlusListener
from CalcPlusParser import CalcPlusParser

class CalcListener(CalcPlusListener):
    def __init__(self):
        self.stack = []

    def exitInt(self, ctx:CalcPlusParser.IntContext):
        self.stack.append(int(ctx.INT().getText()))

    def exitParens(self, ctx:CalcPlusParser.ParensContext):
        # 괄호는 내부 expr이 이미 처리되었으니 추가 작업이 필요 없음
        pass

    def exitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(left * right if op == '*' else left / right)

    def exitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(left + right if op == '+' else left - right)

    def result(self):
        return self.stack[-1] if self.stack else None
