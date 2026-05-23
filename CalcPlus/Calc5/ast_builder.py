"""Parse Tree to AST builder skeleton for Calc5."""

from CalcPlusParser import CalcPlusParser
from CalcPlusVisitor import CalcPlusVisitor


class AstBuilder(CalcPlusVisitor):
    """Converts ANTLR parse-tree contexts into Calc5 AST nodes."""

    def _var_name(self, token) -> str:
        return token.getText()

    def visitProgram(self, ctx: CalcPlusParser.ProgramContext):
        raise NotImplementedError("Parse Tree를 AST Program으로 변환하세요.")

    def visitDeclare(self, ctx: CalcPlusParser.DeclareContext):
        raise NotImplementedError("선언문을 Declare 노드 목록으로 변환하세요.")

    def visitExprAssign(self, ctx: CalcPlusParser.ExprAssignContext):
        raise NotImplementedError("대입문을 Assign 노드로 변환하세요.")

    def visitReadAssign(self, ctx: CalcPlusParser.ReadAssignContext):
        raise NotImplementedError("read() 대입문을 Assign + ReadCall 형태로 변환하세요.")

    def visitWrite(self, ctx: CalcPlusParser.WriteContext):
        raise NotImplementedError("write 문장을 AST 노드로 변환하세요.")

    def visitIfElse(self, ctx: CalcPlusParser.IfElseContext):
        raise NotImplementedError("if/else 문장을 IfElse 노드로 변환하세요.")

    def visitStmtBlock(self, ctx: CalcPlusParser.StmtBlockContext):
        raise NotImplementedError("문장 위치의 block을 Block 노드로 변환하세요.")

    def visitBlock(self, ctx: CalcPlusParser.BlockContext):
        raise NotImplementedError("block 내부 statement 목록을 Block 노드로 변환하세요.")

    def visitCond(self, ctx: CalcPlusParser.CondContext):
        raise NotImplementedError("조건 비교를 BinaryExpr 또는 별도 조건 노드로 변환하세요.")

    def visitVar(self, ctx: CalcPlusParser.VarContext):
        raise NotImplementedError("변수 참조를 VarRef 노드로 변환하세요.")

    def visitInt(self, ctx: CalcPlusParser.IntContext):
        raise NotImplementedError("정수 리터럴을 IntLiteral 노드로 변환하세요.")

    def visitParens(self, ctx: CalcPlusParser.ParensContext):
        raise NotImplementedError("괄호는 AST에서 제거하고 내부 expression을 반환하세요.")

    def visitMulDiv(self, ctx: CalcPlusParser.MulDivContext):
        raise NotImplementedError("곱셈/나눗셈 expression을 BinaryExpr로 변환하세요.")

    def visitAddSub(self, ctx: CalcPlusParser.AddSubContext):
        raise NotImplementedError("덧셈/뺄셈 expression을 BinaryExpr로 변환하세요.")
