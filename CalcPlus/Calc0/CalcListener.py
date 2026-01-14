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
- parseTreeWalker는 깊이 우선(DFS), left-to-right로 내려가고, enter → 자식들 → exit 순서로 호출
- ParseTreeWalker는 전위/중위/후위 중에서 “후위에 해당하는 부분”을 활용
-  exit(후위) 시점에 자식 결과가 다 모여 있으니까 후위표기 만들기엔 딱 좋은 구조
enter 콜백은 전위(pre-order) 시점
exit 콜백은 후위(post-order) 시점
이 리스너에서 후위표기를 만드는 이유는 exit에서 작업
즉, 순회 자체는 DFS이고, enter 시점은 전위, exit 시점은 후위롤 대응
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