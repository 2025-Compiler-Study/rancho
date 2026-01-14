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

'''
listener의 특징
이미 후위연산자로 되어있는 것인가?
왜 연산자나 괄호 등 숫자가 인ㄴ 것들은 append하는 것이 없던 것인가?
'''
class CalcListenerPostfix(CalcPlusListener):
    def __init__(self):
        self.stack = []
    
    def exitInt(self, ctx:CalcPlusParser.IntContext):
        # print(f"self.stack[-1] : {self.stack[-1]}")
        self.stack.append(ctx.INT().getText())
        print(f"self.stack : {self.stack}")

    def exitMulDiv(self, ctx:CalcPlusParser.MulDivContext):
        right = self.stack.pop()
        left = self.stack.pop()
        # (0)이 아닌 (1)인 이유 => expr ('*'|'/') expr 3개 중 가운데 연산자 선택
        op = ctx.getChild(1).getText()
        self.stack.append(f"{left} {right} {op}")
        print(f"self.stack : {self.stack}")

    def exitAddSub(self, ctx:CalcPlusParser.AddSubContext):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(f"{left} {right} {op}")
        print(f"self.stack : {self.stack}")

    def result(self):
        return self.stack[-1] if self.stack else None