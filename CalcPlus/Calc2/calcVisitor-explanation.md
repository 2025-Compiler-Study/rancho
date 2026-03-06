# CalcVisitor 동작 및 수정 노트

이 문서는 현재 `calcVisitor.py`가 왜 정상 동작하는지, 그리고 각 수정이 왜 필요했는지를 설명합니다.

## 1. 테스트 실패의 근본 원인

첫 번째 크래시는 `visit`의 잘못된 조건문 때문에 발생했습니다.

- 잘못된 코드: `if ctx in None:`
- 올바른 코드: `if ctx is None:`

`in` 연산자는 오른쪽에 순회 가능한 객체가 필요하지만 `None`은 순회할 수 없으므로, Python에서 다음 예외가 발생합니다.

- `TypeError: argument of type 'NoneType' is not iterable`

`visit`는 모든 노드 방문의 시작점이므로, 이 한 가지 버그로 전체 테스트가 모두 깨졌습니다.

## 2. 동적 디스패치를 사용하는 이유

ANTLR 파스 트리는 다음과 같은 여러 컨텍스트 클래스를 제공합니다.

- `Calc2Context`
- `ExprAssignContext`
- `IfElseContext`

Visitor는 각 컨텍스트 타입을 동적으로 메서드 이름에 매핑합니다.

1. 컨텍스트에서 타입 이름을 가져옵니다.
2. `visit<TypeName>` 메서드를 먼저 시도합니다.
3. 클래스 이름이 `Context`로 끝나면, 이를 제거한 형태(예: `visitIfElse`)도 시도합니다.
4. 해당 메서드가 없으면 자식 노드를 재귀적으로 방문합니다.

이 방식은 Visitor를 범용적으로 유지하고, 긴 수동 `if/elif` 체인을 피하게 해줍니다.

## 3. `thenBlock`이 필요한 이유 (`theBlock`이 아님)

`CalcPlus.g4` 문법에서 참 분기는 다음과 같이 라벨링되어 있습니다.

- `thenBlock=block`

따라서 ANTLR이 생성하는 필드는 `ctx.thenBlock`입니다. `ctx.theBlock`에 접근하면 다음 예외가 납니다.

- `AttributeError: 'IfElseContext' object has no attribute 'theBlock'`

그래서 `ctx.thenBlock`을 사용하도록 수정해야 합니다.

## 4. `self.memory`를 복사해서 반환하는 이유

`visitCalc2`는 `self.memory`를 직접 반환하지 않고 `dict(self.memory)`를 반환합니다.

이렇게 하면 최종 변수 상태의 스냅샷을 반환하게 되고, 외부에서 인터프리터 내부 상태를 실수로 변경하는 일을 막을 수 있습니다.

## 5. 미정의 변수 처리 방식

`visitVar`는 변수가 처음 읽힐 때 값이 없으면 `0`으로 초기화합니다.

이는 의도된 동작이며 테스트와도 일치합니다. (예: `e`나 `b`를 할당 전에 읽어도 크래시가 나면 안 됨)

## 6. 수식 및 조건식 평가

- `visitExprAssign`: 우변(RHS)을 먼저 평가한 뒤, 좌변(LHS) 변수에 대입합니다.
- `visitMulDiv` / `visitAddSub`: 좌우 수식을 평가한 뒤 연산자 토큰을 적용합니다.
- `visitCond`: 두 수식을 평가하고 `== != > >= < <=` 중 하나를 적용합니다.

이로써 조건식과 할당문 내부에서 산술 연산이 일관되게 동작합니다.

## 7. 동작을 바꾼 오타 수정 요약

- `ctx in None` -> `ctx is None`
- `__nane__` -> `__name__`
- `self.memmory` -> `self.memory`
- `self.visis(...)` -> `self.visit(...)`
- `ctx.theBlock` -> `ctx.thenBlock`

이 수정들을 반영한 뒤 `test_calc2.py` 전체 테스트가 통과합니다.
