# calcVisitor.py

from CalcPlusParser import CalcPlusParser
from CalcPlusVisitor import CalcPlusVisitor

class CalcVisitor(CalcPlusVisitor):

    def __init__(self):
        # 인터프리터 실행 중 변수 값을 저장한다.
        self.memory: dict[str, int] = {}
    
    # 오버라이드
    '''# TODO: visit() 오버라이드 없이 재구현
    '''
    # def visit(self, ctx):
    #     # 방어 코드: 컨텍스트가 없으면 평가할 대상이 없다.
    #     if ctx is None:
    #         return None
    #     # 파스 트리 노드가 아닌 객체는 안전하게 건너뛴다.
    #     if not hasattr(ctx, "getChildCount") and not hasattr(ctx, "getChildren"):
    #         return None
    #     # 컨텍스트 타입으로 방문 메서드 이름을 만든다. 예: IfElseContext -> visitIfElseContext
    #     type_name = type(ctx).__name__
    #     ## 루트 노드일 때 => "Calc2Context"
    #     method_name = f"visit{type_name}"
    #     # 먼저 정확히 일치하는 핸들러를 찾는다.
    #     method = getattr(self, method_name, None)
    #     # ANTLR 컨텍스트는 보통 "Context"로 끝나므로 이를 제거한 이름도 시도한다. 예: visitIfElse
    #     if method is None and type_name.endswith("Context"):
    #         method = getattr(self, f"visit{type_name[:-7]}", None)
    #     # 전용 핸들러가 없으면 자식 노드를 순회한다.
    #     if method is None:
    #         return self.visitChildren(ctx)
    #     # 찾은 핸들러를 실행한다.
    #     return method(ctx)

    # def visitChildren(self, ctx):
    #     # 자식 방문 결과 중 마지막 값을 반환한다(ANTLR Visitor 관례).
    #     result = None
    #     if hasattr(ctx, "getChildren"):
    #         for child in ctx.getChildren():
    #             result = self.visit(child)
    #     else:
    #         for i in range(ctx.getChildCount()):
    #             result = self.visit(ctx.getChild(i))
    #     return result
    
    def visitCalc2(self, ctx: CalcPlusParser.Calc2Context):
        # 프로그램 내 문장을 순서대로 실행한다.
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        # 외부에서 내부 상태를 실수로 바꾸지 않도록 복사본을 반환한다.
        return dict(self.memory)
    
    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        # 대입문의 좌변에서 변수 이름을 읽는다.
        var_name = ctx.VAR().getText()
        # 우변 수식을 먼저 계산한다.
        value = self.visit(ctx.expr())
        # 계산 값을 메모리에 저장한다.
        self.memory[var_name] = value
        return  value
    
    def visitIfElse(self, ctx):
        # 조건식을 먼저 평가한다.
        condition = self.visit(ctx.cond())
        print(f"{condition=},\t{ctx.getText()}")
        # 조건 결과에 따라 선택된 분기만 실행한다.
        if condition:
            # 문법 라벨이 thenBlock이므로 참 분기를 실행한다.
            # print(f"{ctx.thenBlock=}")
            self.visit(ctx.thenBlock)
        elif ctx.elseBlock is not None:
            # else 분기는 선택 사항이므로 존재 여부를 확인한다.
            self.visit(ctx.elseBlock)
        return None

    def visitBlock(self, ctx: CalcPlusParser.BlockContext):
        # 블록은 문장을 순서대로 담는 컨테이너다.
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        return None

    def visitCond(self, ctx: CalcPlusParser.CondContext):
        # 두 수식을 계산한 뒤 비교 연산을 수행한다.
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # 비교 연산자는 expr(0)과 expr(1) 사이 토큰이다.
        op = ctx.getChild(1).getText()
        if op == "==":
            return left == right
        elif op == "!=":
            return left != right
        elif op == ">":
            return left > right
        elif op == ">=":
            return left >= right
        elif op == "<":
            return left < right
        elif op == "<=":
            return left <= right
        raise ValueError(f"Unknown comparison operator: {op}")

    def visitVar(self, ctx: CalcPlusParser.VarContext):
        # 정의되지 않은 변수는 첫 조회 시 0으로 초기화한다.
        var_name = ctx.VAR().getText()
        if var_name not in self.memory:
            self.memory[var_name] = 0
        return self.memory[var_name]

    def visitInt(self, ctx: CalcPlusParser.IntContext):
        # 정수 토큰 문자열을 Python int로 변환한다.
        return int(ctx.INT().getText())

    def visitParens(self, ctx: CalcPlusParser.ParensContext):
        # 괄호식은 내부 수식 평가 결과를 그대로 사용한다.
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: CalcPlusParser.MulDivContext):
        # 이항 연산: 좌우 피연산자를 먼저 계산한다.
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        # 이 규칙에서는 연산자가 '*' 또는 '/'만 온다.
        return left * right if op == "*" else left / right

    def visitAddSub(self, ctx: CalcPlusParser.AddSubContext):
        # 이항 연산: 좌우 피연산자를 먼저 계산한다.
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        # 이 규칙에서는 연산자가 '+' 또는 '-'만 온다.
        return left + right if op == "+" else left - right
