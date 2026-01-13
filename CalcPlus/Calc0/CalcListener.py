# CalcListener.py
from CalcPlusListener import CalcPlusListener
from CalcPlusParser import CalcPlusParser

'''
stack을 쓰므로 return은 stack에 있는 값만함
스택에 담아둠
중위 연산자 -> 후위 연산자
- 10 + 2 * (5 - 9 / 3)
- 10 + 2

1. 덧셈, 뺼셈만
10 2 + 
10 + 2 - 5
10 2 5 + -
2. 곱셈, 나눗셈
3. 괄호 포함
'''
class CalcListener(CalcPlusListener):
    def __init__(self):
        self.stack = []

    def exitInt(self, ctx:CalcPlusParser.IntContext):
        self.stack.append(int(ctx.INT().getText()))
    
    # def exitParens(self, ctx:CalcPlusParser.ParensContext):
    #     pass
    
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