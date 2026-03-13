# Calc4 Implementation Steps

이 문서는 현재 저장소 상태를 기준으로 Calc4를 단계별로 구현하기 위한 가이드다.

중요한 전제는 하나다.

- 파서 골격과 테스트 골격은 이미 있다.

즉, 여기서 말하는 1단계는 "프로젝트 시작 단계"가 아니라 "실제 시맨틱 구현의 첫 단계"다.

## 현재 이미 준비된 것

다음 요소는 이미 파일로 준비되어 있다.

- [`CalcPlus.g4`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/CalcPlus.g4): Calc4 문법
- [`CalcPlusLexer.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/CalcPlusLexer.py), [`CalcPlusParser.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/CalcPlusParser.py): 생성된 파서 코드
- [`calc4_visitor.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/calc4_visitor.py): Visitor 스텁
- [`symbol_table.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/symbol_table.py): SymbolTable 스텁
- [`test_calc4.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/test_calc4.py): 파서/계약 테스트

따라서 지금부터의 구현 시작점은 "심볼 테이블과 Visitor 시맨틱 채우기"다.

## 단계 1. 단일 스코프 심볼 테이블 완성

목표:
블록은 아직 고려하지 않고, 선언된 변수만 읽고 쓸 수 있는 최소 실행 기반을 만든다.

구현 과제:
- [`symbol_table.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/symbol_table.py)에서 `declare`, `lookup`, `assign`를 구현한다.
- 초기 스코프는 이미 `[{}]`로 있으므로, 우선 이 한 개의 스코프만 사용해도 된다.
- `declare(name)`는 현재 스코프에 없는 경우에만 `0`으로 등록한다.
- `lookup(name)`는 현재 스코프에서 값을 가져온다.
- `assign(name, value)`는 현재 스코프에 존재하는 변수만 변경한다.
- 선언 전 사용과 같은 스코프 재선언은 예외로 처리한다.

손대는 지점:
- [`symbol_table.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/symbol_table.py)

아직 하지 않는 것:
- `push_scope`, `pop_scope`
- 내부/외부 블록 탐색
- 섀도잉

완료 기준:
- 선언 후 즉시 조회가 가능하다.
- 선언된 변수에 대입이 가능하다.
- 선언 전 조회/대입은 실패한다.
- 같은 스코프 재선언이 실패한다.

확인 예제:

```c
int a;
a = 3;
write(a);
```

기대 동작:

```text
3
```

오류 예제:

```c
a = 3;
```

## 단계 2. 식 계산과 기본 문장 실행 연결

목표:
선언, 대입, 변수 조회, 사칙연산을 하나의 실행 흐름으로 연결한다.

구현 과제:
- [`calc4_visitor.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/calc4_visitor.py)에서 아래 메서드를 구현한다.
- `visitCalc4`
- `visitDeclare`
- `visitExprAssign`
- `visitVar`
- `visitInt`
- `visitParens`
- `visitMulDiv`
- `visitAddSub`
- `visitWrite`

각 메서드 역할:
- `visitCalc4`: 프로그램의 각 `stmt`를 순서대로 방문
- `visitDeclare`: 선언문 안의 변수들을 하나씩 `declare`
- `visitExprAssign`: 오른쪽 식 계산 후 왼쪽 변수에 `assign`
- `visitVar`: 심볼 테이블에서 변수 값을 읽음
- `visitInt`: 정수 리터럴을 `int`로 반환
- `visitParens`: 내부 식 결과를 그대로 반환
- `visitMulDiv`, `visitAddSub`: 좌우 식을 재귀 계산
- `visitWrite`: 식 결과를 출력 함수로 전달

핵심 포인트:
- Visitor의 expression 메서드는 값을 반환해야 한다.
- statement 메서드는 보통 값을 반환하지 않아도 된다.
- `visitWrite`는 내부 식만 계산하고 반환값은 만들지 않아도 된다.

손대는 지점:
- [`calc4_visitor.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/calc4_visitor.py)

완료 기준:
- 선언, 대입, 수식 계산, 출력이 한 번에 동작한다.
- `write(1 + 2 * 3);` 같은 식도 정상 계산된다.
- `int a; a = 1 + 2; write(a);`가 실행된다.

확인 예제:

```c
int a, b;
a = 10;
b = a + 2 * 3;
write(b);
```

기대 동작:

```text
16
```

## 단계 3. 오류 처리 규칙 고정

목표:
Calc4 구현 과제 #1의 실패 규칙을 명확히 고정한다.

구현 과제:
- 선언 전 읽기 시 즉시 실패하도록 정리한다.
- 선언 전 쓰기 시 즉시 실패하도록 정리한다.
- 같은 스코프 재선언 시 즉시 실패하도록 정리한다.
- 예외 타입과 메시지 형식을 일관되게 맞춘다.

실무적으로는 이 단계가 중요한 이유:
- 지금 오류 규칙을 정리하지 않으면, 이후 블록/섀도잉을 넣을 때 실패 위치가 흐려진다.
- "조회 실패"와 "대입 실패"가 같은 규칙을 공유하는지 먼저 결정해야 한다.

권장 방식:
- `SymbolTable`에서 오류를 발생시킨다.
- Visitor는 심볼 테이블 계약을 신뢰하고 로직만 수행한다.

손대는 지점:
- [`symbol_table.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/symbol_table.py)
- 필요하면 [`calc4_visitor.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/calc4_visitor.py)

완료 기준:
- 잘못된 프로그램이 조용히 지나가지 않는다.
- 에러가 발생하면 어떤 이름이 문제인지 알 수 있다.
- 이후 테스트에서 오류 케이스를 분리해 추가할 수 있다.

오류 예제:

```c
int a;
int a;
```

```c
int a;
b = a + 1;
```

## 단계 4. 블록 스코프 도입

목표:
`{ ... }` 블록에 진입하고 빠져나갈 때 변수 유효 범위가 바뀌게 만든다.

구현 과제:
- `push_scope`, `pop_scope`를 구현한다.
- `visitBlock`에서 블록 진입 시 새 스코프를 push하고 종료 시 pop한다.
- `visitStmtBlock`에서 블록 문장을 실제 방문하게 연결한다.
- 블록 안 선언 변수는 블록 밖에서 더 이상 보이지 않게 만든다.

구현 팁:
- `visitBlock`은 `try/finally` 구조로 짜는 편이 안전하다.
- 내부 문장 실행 중 예외가 나도 스코프 정리가 필요하기 때문이다.

손대는 지점:
- [`symbol_table.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/symbol_table.py)
- [`calc4_visitor.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/calc4_visitor.py)

완료 기준:
- 블록 안에서 선언한 변수는 블록 밖에서 조회 실패한다.
- 바깥에서 선언한 변수는 안쪽 블록에서 읽고 쓸 수 있다.
- 중첩 블록에서도 스코프 push/pop이 맞게 동작한다.

확인 예제:

```c
int a;
a = 1;
{
  int b;
  b = a + 2;
  write(b);
}
write(a);
```

기대 동작:

```text
3
1
```

## 단계 5. 섀도잉 구현

목표:
내부 블록에서 같은 이름을 다시 선언했을 때 가장 가까운 선언이 우선되게 만든다.

구현 과제:
- `lookup`은 가장 안쪽 스코프부터 바깥으로 탐색하게 만든다.
- `assign`도 가장 안쪽 스코프부터 바깥으로 탐색하게 만든다.
- `declare`는 현재 스코프만 검사하게 유지한다.
- 내부 블록의 같은 이름 변수가 바깥 변수를 가리도록 만든다.

핵심 규칙:
- 선언: 현재 스코프만 검사
- 조회: 안쪽에서 바깥으로 탐색
- 대입: 안쪽에서 바깥으로 탐색

이 차이를 제대로 지켜야 섀도잉이 맞게 동작한다.

손대는 지점:
- 거의 대부분 [`symbol_table.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/symbol_table.py)

완료 기준:
- 내부 블록에서 `int a;`가 가능하다.
- 내부 블록에서는 바깥 `a`가 아니라 안쪽 `a`를 읽고 쓴다.
- 내부 블록 종료 후 다시 바깥 `a`가 보인다.

확인 예제:

```c
int a;
a = 1;
{
  int a;
  a = 2;
  write(a);
}
write(a);
```

기대 동작:

```text
2
1
```

## 단계 6. `if`, `read`, `write`까지 Calc4 문장 전체 연결

목표:
남은 문장들을 모두 Visitor 실행 흐름에 연결해 Calc4 전체를 완성한다.

구현 과제:
- `visitCond` 구현
- `visitIfElse` 구현
- `visitReadAssign` 구현
- `write_fn`, `read_fn` 주입 방식 정리
- 필요하면 기본 입출력 동작 정의

세부 내용:
- `visitCond`는 좌우 식을 계산한 뒤 비교 연산 결과를 반환한다.
- `visitIfElse`는 조건값에 따라 `thenBlock` 또는 `elseBlock`만 실행한다.
- `visitReadAssign`는 입력을 받아 정수로 변환한 뒤 해당 변수에 대입한다.
- `visitWrite`는 이미 2단계에서 붙였더라도 이 단계에서 전체 IO 흐름 기준으로 정리한다.

주의할 점:
- `if`의 각 블록은 일반 블록처럼 독립 스코프를 가져야 한다.
- `read()`는 수식의 일부가 아니라 대입문 형태로만 나온다.

손대는 지점:
- [`calc4_visitor.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/calc4_visitor.py)

완료 기준:
- 조건문이 참/거짓에 따라 올바른 블록만 실행된다.
- `read()` 값이 변수에 들어간다.
- 출력이 기대와 맞는다.

확인 예제:

```c
int a;
a = 1;
if (a > 0) {
  write(a);
} else {
  write(0);
}
```

기대 동작:

```text
1
```

## 단계 7. 테스트를 골격에서 기능 검증으로 전환

목표:
현재의 "스텁 확인 테스트"를 실제 기능 검증 테스트로 바꾼다.

구현 과제:
- [`test_calc4.py`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/test_calc4.py)의 `NotImplementedError` 기대 테스트를 제거하거나 수정한다.
- `SymbolTable` 단위 테스트를 추가한다.
- Visitor 실행 결과 테스트를 추가한다.
- 블록 스코프, 섀도잉, 오류 케이스 테스트를 추가한다.

추천 테스트 추가 순서:
- 선언/조회/대입
- 재선언 오류
- 선언 전 사용 오류
- 블록 진입/종료
- 섀도잉
- 조건문 실행
- read/write

완료 기준:
- 테스트가 "미구현 확인"이 아니라 "동작 보장" 역할을 한다.
- Calc4 핵심 규칙이 회귀 테스트로 남는다.

## 추천 작업 순서 요약

실제로 손을 대는 순서는 아래가 가장 안전하다.

1. `SymbolTable`의 `declare`, `lookup`, `assign`
2. `Calc4Visitor`의 선언/식/대입/출력
3. 오류 처리 정리
4. `push_scope`, `pop_scope`
5. 블록 방문
6. 섀도잉 검증
7. `if`, `read`
8. 테스트 전환

## 각 단계에서 스스로 확인할 질문

### 단계 1을 끝냈다면

- 선언 직후 값이 0인가
- 선언 전 변수 접근이 막히는가
- 같은 스코프 재선언이 막히는가

### 단계 2를 끝냈다면

- 식 계산 결과가 올바른가
- 변수 값이 수식에 반영되는가
- `write`가 실제 계산 결과를 출력하는가

### 단계 4를 끝냈다면

- 블록 종료 후 내부 변수가 사라지는가
- 바깥 변수는 안쪽에서 계속 보이는가

### 단계 5를 끝냈다면

- 내부 같은 이름 변수가 바깥 변수를 가리는가
- 내부 블록 종료 후 원래 변수가 복구되는가

### 단계 6을 끝냈다면

- `if`에서 한 쪽 블록만 실행되는가
- `read`와 `write`가 문법 의도대로 연결되는가

## 결론

현재 저장소 기준으로 실질적인 첫 구현 단계는 "단일 스코프 심볼 테이블"이다.  
그 다음은 "식 계산과 대입 연결", 그 다음이 "블록 스코프와 섀도잉"이다.

즉, Calc4를 푸는 핵심 축은 아래 세 개다.

1. 선언 강제
2. 스코프 스택
3. 가장 안쪽 선언 우선

이 세 가지를 단계적으로 붙이면 Calc4 전체 구현이 자연스럽게 완성된다.
