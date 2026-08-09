"""Calc5의 식(expression)을 표현하는 AST 노드들.

AST(Abstract Syntax Tree)는 소스 코드의 의미를 트리 형태로 보관한다.
예를 들어 ``5 + a``는 ``BinaryExpr("+", IntLiteral(5), VarRef("a"))``로
표현할 수 있다.

이 파일의 클래스명은 CapWords, 객체의 필드명은 lowercase_with_underscores
규칙을 따른다. 근거는 docs/ast-conventions.md에 기록되어 있다.
"""

'''
# 사칙연산 예제
- 5 * 3 + a * (5 - 9 / 3)
- 5 * 3 + a

- 우선순위 역전
- 트리과정
=> visualizer
'''

class AstNode:
    """모든 AST 노드의 공통 부모 클래스.

    현재는 공통 데이터나 기능이 없지만, 모든 노드가 같은 종류라는 것을
    표현하기 위해 둔다. 나중에 소스 코드 위치 정보 등을 여기에 추가할 수 있다.
    """

    def children(self) -> tuple["AstNode", ...]:
        """이 노드에 직접 연결된 자식 노드를 반환한다.

        리터럴과 변수 참조는 더 작은 식을 포함하지 않으므로 기본값은 빈 튜플이다.
        트리 출력기나 AST 순회 코드는 이 메서드로 하위 노드를 공통 방식으로
        방문할 수 있다.
        """
        return ()

    def __eq__(self, other: object) -> bool:
        """같은 종류이고 저장한 필드 값도 같을 때 두 노드를 같다고 판단한다."""
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        """노드의 클래스명과 필드 값을 보여 주는 디버그용 문자열을 만든다."""
        fields = ", ".join(
            f"{name}={value!r}" for name, value in self.__dict__.items()
        )
        return f"{type(self).__name__}({fields})"


class Expr(AstNode):
    """계산하면 하나의 값이 나오는 AST 노드의 공통 부모 클래스.

    IntLiteral, VarRef, BinaryExpr는 모두 Expr를 상속한다. 따라서 연산의
    왼쪽과 오른쪽에는 어떤 종류의 식 노드든 넣을 수 있다.
    """


class IntLiteral(Expr):
    """소스 코드에 직접 쓴 정수 리터럴을 나타낸다. 예: ``5``, ``-3``."""

    def __init__(self, value: int):
        # 실제 정수값을 저장한다. 예: IntLiteral(5)의 value는 5이다.
        self.value: int = value


class VarRef(Expr):
    """변수 사용을 나타낸다. 예: 식 ``a + 1`` 안의 ``a``."""

    def __init__(self, name: str):
        # 변수를 선언할 때 사용한 이름을 저장한다. 예: VarRef("a").
        self.name: str = name


class BinaryExpr(Expr):
    """피연산자 두 개를 갖는 연산식을 나타낸다. 예: ``left + right``.

    ``+``, ``-``, ``*``, ``/``처럼 왼쪽 값과 오른쪽 값이 필요한 연산을
    하나의 노드 형태로 통일해 표현한다.
    """

    def __init__(self, op: str, left: Expr, right: Expr):
        # 연산자 문자열이다. 예: "+", "-", "*", "/".
        self.op: str = op

        # 연산자의 왼쪽 식이다. 숫자, 변수, 또 다른 BinaryExpr가 될 수 있다.
        self.left: Expr = left

        # 연산자의 오른쪽 식이다. 숫자, 변수, 또 다른 BinaryExpr가 될 수 있다.
        self.right: Expr = right

    '''
    # TODO: 점검, 변경가능 
    - 의도가 어떻게 되는가
      - 해석 순서
        - 정렬
    '''
    def children(self) -> tuple[Expr, Expr]:
        """연산자의 왼쪽·오른쪽 피연산자를 순서대로 반환한다."""
        return (self.left, self.right)
