# Calc2 실행 흐름 도식화

이 문서는 `calc2` 프로그램이 파싱되고, `visitor.visit(tree)` 호출 이후 어떤 순서로 실행되는지 설명한다.

기준 파일:

- `CalcPlus.g4`
- `CalcPlusParser.py`
- `calcVisitor.py`
- `test_calc2.py`

## 1. 핵심 개념

`calc2`의 실행은 크게 두 단계로 나뉜다.

1. 입력 문자열을 파싱해서 `Calc2Context` 파스 트리를 만든다.
2. `CalcVisitor`가 그 트리를 방문하면서 문장과 수식을 실제로 실행한다.

즉, 사용자 코드가 곧바로 실행되는 것이 아니라:

```text
문자열 -> 토큰화 -> 파싱 -> 파스 트리 생성 -> visitor로 트리 방문
```

순서로 진행된다.

## 2. `Calc2Context.accept(visitor)`가 하는 일

`parser.calc2()`를 호출하면 루트 노드인 `Calc2Context`가 만들어진다.

이 객체에는 다음과 같은 `accept(visitor)` 메서드가 들어 있다.

```text
accept(visitor)
  -> visitor에 visitCalc2가 있으면 visitor.visitCalc2(self) 호출
  -> 없으면 visitor.visitChildren(self) 호출
```

즉 `accept(visitor)`는 현재 노드 타입에 맞는 방문 메서드로 연결해 주는 디스패치 지점이다.

실제 흐름은 다음처럼 이해하면 된다.

```text
visitor.visit(tree)
  -> tree.accept(visitor)
  -> visitor.visitCalc2(tree)
```

여기서 `tree`는 `Calc2Context`이다.

## 3. 코드 구조 기준 실행 흐름

### 3.1 전체 구조

```text
[프로그램 문자열]
        |
        v
[CalcPlusLexer]
        |
        v
[CommonTokenStream]
        |
        v
[CalcPlusParser.calc2()]
        |
        v
[Calc2Context Parse Tree]
        |
        v
[CalcVisitor.visit(tree)]
        |
        v
[Calc2Context.accept(visitor)]
        |
        v
[visitCalc2]
        |
        +-----------------------------+
        | stmt를 순서대로 하나씩 방문 |
        +-----------------------------+
           |                    |
           v                    v
   [visitExprAssign]       [visitIfElse]
           |                    |
           v                    v
      [visit expr]         [visitCond]
           |                    |
           v                    v
 [Int / Var / AddSub /     [왼쪽 expr]
   MulDiv / Parens]        [오른쪽 expr]
           |                    |
           v                    v
   [memory[var] 저장]      [비교 결과]
                                 |
                      +----------+----------+
                      |                     |
                      v                     v
               [thenBlock 방문]      [elseBlock 방문]
                      |                     |
                      v                     v
                   [visitBlock]
                      |
                      v
             [block 내부 stmt 순차 실행]
                      |
                      v
              [최종 memory 반환]
```

### 3.2 호출 트레이스 형태

```text
visit(tree)
└─ visitCalc2
   ├─ visitExprAssign(...)
   │  └─ visit(expr)
   │     ├─ visitInt(...)
   │     ├─ visitVar(...)
   │     ├─ visitAddSub(...)
   │     ├─ visitMulDiv(...)
   │     └─ visitParens(...)
   │
   ├─ visitIfElse(...)
   │  ├─ visitCond(...)
   │  │  ├─ visit(expr 왼쪽)
   │  │  └─ visit(expr 오른쪽)
   │  └─ visitBlock(...) 또는 elseBlock 방문
   │     └─ 내부 stmt 반복 방문
   │
   └─ return dict(memory)
```

## 4. 예시 코드 기준 실행 흐름

예시 코드:

```c
a = 1;
if (a >= 1) {
    b = a + 2;
    c = b * 3;
} else {
    b = 0;
}
d = c - 4;
```

최종 결과:

```python
{"a": 1, "b": 3, "c": 9, "d": 5}
```

### 4.1 도식화된 흐름

```text
시작
 |
 v
[a = 1]
 |
 v
memory = {a: 1}
 |
 v
[if (a >= 1)]
 |
 v
[a 값 읽기 = 1] ----+
[1 읽기 = 1]       |
 |                |
 v                |
[1 >= 1 = true] <-+
 |
 v
[thenBlock 실행]
 |
 +--> [b = a + 2]
 |         |
 |         v
 |     [a 읽기 = 1]
 |     [2 읽기 = 2]
 |     [1 + 2 = 3]
 |         |
 |         v
 |     memory = {a:1, b:3}
 |
 +--> [c = b * 3]
           |
           v
       [b 읽기 = 3]
       [3 읽기 = 3]
       [3 * 3 = 9]
           |
           v
       memory = {a:1, b:3, c:9}
 |
 v
[d = c - 4]
 |
 v
[c 읽기 = 9]
[4 읽기 = 4]
[9 - 4 = 5]
 |
 v
memory = {a:1, b:3, c:9, d:5}
 |
 v
종료
```

### 4.2 실제 호출 순서 트레이스

```text
1. parse_program(program)
2. parser.calc2()
3. Calc2Context tree 생성
4. visitor.visit(tree)
5. tree.accept(visitor)
6. visitor.visitCalc2(ctx)

7. 첫 번째 stmt 방문: "a = 1;"
8. visitor.visitExprAssign(ctx)
9.   ctx.VAR().getText() -> "a"
10.  visitor.visit(ctx.expr())
11.  visitor.visitInt(ctx)
12.    int("1") -> 1 반환
13.  memory["a"] = 1

14. 두 번째 stmt 방문: "if (a >= 1) { ... } else { ... }"
15. visitor.visitIfElse(ctx)
16.   visitor.visit(ctx.cond())
17.   visitor.visitCond(ctx)
18.     visitor.visit(ctx.expr(0))
19.     visitor.visitVar(ctx)
20.       memory["a"] 조회 -> 1 반환
21.     visitor.visit(ctx.expr(1))
22.     visitor.visitInt(ctx)
23.       int("1") -> 1 반환
24.     op = ">="
25.     1 >= 1 -> True 반환
26.   condition == True
27.   visitor.visit(ctx.thenBlock)
28.   visitor.visitBlock(ctx)

29. block stmt 1 방문: "b = a + 2;"
30. visitor.visitExprAssign(ctx)
31.   var_name = "b"
32.   visitor.visit(ctx.expr())
33.   visitor.visitAddSub(ctx)
34.     visitor.visit(ctx.expr(0))
35.     visitor.visitVar(ctx)
36.       memory["a"] 조회 -> 1 반환
37.     visitor.visit(ctx.expr(1))
38.     visitor.visitInt(ctx)
39.       int("2") -> 2 반환
40.     op = "+"
41.     1 + 2 -> 3 반환
42.   memory["b"] = 3

43. block stmt 2 방문: "c = b * 3;"
44. visitor.visitExprAssign(ctx)
45.   var_name = "c"
46.   visitor.visit(ctx.expr())
47.   visitor.visitMulDiv(ctx)
48.     visitor.visit(ctx.expr(0))
49.     visitor.visitVar(ctx)
50.       memory["b"] 조회 -> 3 반환
51.     visitor.visit(ctx.expr(1))
52.     visitor.visitInt(ctx)
53.       int("3") -> 3 반환
54.     op = "*"
55.     3 * 3 -> 9 반환
56.   memory["c"] = 9

57. visitIfElse() 종료

58. 세 번째 stmt 방문: "d = c - 4;"
59. visitor.visitExprAssign(ctx)
60.   var_name = "d"
61.   visitor.visit(ctx.expr())
62.   visitor.visitAddSub(ctx)
63.     visitor.visit(ctx.expr(0))
64.     visitor.visitVar(ctx)
65.       memory["c"] 조회 -> 9 반환
66.     visitor.visit(ctx.expr(1))
67.     visitor.visitInt(ctx)
68.       int("4") -> 4 반환
69.     op = "-"
70.     9 - 4 -> 5 반환
71.   memory["d"] = 5

72. visitCalc2() 종료
73. dict(self.memory) 반환
74. 최종 결과: {"a": 1, "b": 3, "c": 9, "d": 5}
```

### 4.3 트리 모양으로 본 호출 흐름

```text
visit(tree)
└─ visitCalc2
   ├─ visitExprAssign(a = 1)
   │  └─ visitInt(1)
   │     └─ memory[a] = 1
   │
   ├─ visitIfElse(if a >= 1)
   │  ├─ visitCond(a >= 1)
   │  │  ├─ visitVar(a) -> 1
   │  │  └─ visitInt(1) -> 1
   │  │     └─ result: true
   │  │
   │  └─ visitBlock(thenBlock)
   │     ├─ visitExprAssign(b = a + 2)
   │     │  └─ visitAddSub
   │     │     ├─ visitVar(a) -> 1
   │     │     └─ visitInt(2) -> 2
   │     │        └─ memory[b] = 3
   │     │
   │     └─ visitExprAssign(c = b * 3)
   │        └─ visitMulDiv
   │           ├─ visitVar(b) -> 3
   │           └─ visitInt(3) -> 3
   │              └─ memory[c] = 9
   │
   └─ visitExprAssign(d = c - 4)
      └─ visitAddSub
         ├─ visitVar(c) -> 9
         └─ visitInt(4) -> 4
            └─ memory[d] = 5
```

## 5. 이 프로젝트 안의 비슷한 파일

완전히 같은 목적의 문서는 없지만, 일부 내용이 겹치는 파일은 있다.

- `calcVisitor-explanation.md`
  - `visit` 동작, `visitCalc2`, `visitIfElse`, `thenBlock`, `memory` 반환 이유를 설명한다.
  - 다만 전체 실행 흐름을 도식화해서 정리한 문서는 아니다.
- `approach.md`
  - Calc2를 어떻게 구현할지에 대한 접근 가이드다.
  - 실행 결과를 따라가는 트레이스 문서는 아니다.
- `calc2-learning-checklist.md`
  - 학습용 체크리스트다.
  - 도식화나 호출 흐름 설명은 없다.

즉, 이 문서는 기존 문서의 일부 설명을 보완하면서:

- `accept(visitor)` 의미
- 전체 구조 흐름
- 예시 기반 흐름
- 실제 호출 트레이스

를 한 번에 볼 수 있게 정리한 최종본이다.
