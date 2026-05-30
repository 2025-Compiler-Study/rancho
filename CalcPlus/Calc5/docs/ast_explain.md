# AST(Abstract Syntax Tree, 추상 구문 트리) 설명

## AST란?

**AST(Abstract Syntax Tree, 추상 구문 트리)**는 소스 코드를 컴파일러나 인터프리터가 다루기 쉽게 **트리 구조로 표현한 것**입니다.

소스 코드는 사람이 읽기 위한 문자열입니다.

```c
x = 1 + 2 * 3;
```

하지만 컴파일러는 문자열 그대로 코드를 이해하지 않습니다. 먼저 코드를 분석해서 다음과 같이 구조화합니다.

> 이 코드는 대입문이고, 오른쪽에는 덧셈이 있으며, 덧셈의 오른쪽에는 곱셈이 있다.

이렇게 코드의 구조를 트리 형태로 나타낸 결과가 바로 AST입니다.

---

## 예시

다음 코드를 예로 들어보겠습니다.

```c
x = 1 + 2 * 3;
```

이 코드는 AST로 대략 다음과 같이 표현할 수 있습니다.

```text
Assignment
├── Identifier: x
└── BinaryExpression: +
    ├── Number: 1
    └── BinaryExpression: *
        ├── Number: 2
        └── Number: 3
```

여기서 중요한 점은 AST가 **연산자 우선순위**를 구조로 반영한다는 것입니다.

즉,

```c
1 + 2 * 3
```

은 다음과 같이 해석됩니다.

```c
1 + (2 * 3)
```

따라서 `*` 노드가 `+` 노드보다 아래에 위치합니다.

---

## AST의 “추상”이란 무슨 뜻인가?

AST는 코드의 모든 문법적 세부사항을 그대로 보존하지 않습니다. 핵심적인 의미 구조만 남깁니다.

예를 들어 다음 두 코드는 표면적으로는 다릅니다.

```c
x = 1 + 2;
```

```c
x=(1+2);
```

공백, 괄호, 세미콜론 위치 같은 세부사항은 다르지만 의미는 거의 같습니다. AST에서는 이런 불필요한 문법 요소를 생략하고 다음처럼 표현할 수 있습니다.

```text
Assignment
├── Identifier: x
└── BinaryExpression: +
    ├── Number: 1
    └── Number: 2
```

그래서 **추상 구문 트리**라고 부릅니다.

---

## AST가 만들어지는 과정

컴파일러의 일반적인 흐름은 다음과 같습니다.

```text
소스 코드
  ↓
Lexical Analysis, 토큰화
  ↓
Parsing, 구문 분석
  ↓
AST 생성
  ↓
Semantic Analysis, 의미 분석
  ↓
Optimization, 최적화
  ↓
Code Generation, 코드 생성
```

예를 들어 코드가 다음과 같다면,

```c
x = 1 + 2;
```

먼저 토큰으로 나뉩니다.

```text
Identifier(x)
Equals(=)
Number(1)
Plus(+)
Number(2)
Semicolon(;)
```

그다음 파서가 이 토큰들을 읽고 AST를 만듭니다.

```text
Assignment
├── Identifier: x
└── BinaryExpression: +
    ├── Number: 1
    └── Number: 2
```

---

## Parse Tree와 AST의 차이

AST를 이해할 때 자주 헷갈리는 것이 **Parse Tree**, 즉 구문 분석 트리입니다.

### Parse Tree

Parse Tree는 문법 규칙을 아주 자세하게 반영합니다.

예를 들어 문법이 다음과 같다고 가정해봅시다.

```text
Expression → Expression + Term
Term → Number
```

Parse Tree에는 `Expression`, `Term`, 괄호, 세미콜론 같은 문법 요소들이 많이 포함될 수 있습니다.

### AST

AST는 그중에서 실제 의미 분석과 코드 생성에 필요한 핵심 구조만 남깁니다.

예를 들어,

```c
1 + 2
```

의 AST는 단순히 다음처럼 표현됩니다.

```text
BinaryExpression: +
├── Number: 1
└── Number: 2
```

정리하면 다음과 같습니다.

```text
Parse Tree = 문법 규칙을 자세히 표현한 트리
AST        = 코드의 의미 구조를 간결하게 표현한 트리
```

---

## AST는 왜 필요한가?

AST는 컴파일러가 코드를 이해하고 처리하기 위한 중간 표현입니다.

### 1. 의미 분석

예를 들어 다음 코드가 있다고 합시다.

```c
x = y + 1;
```

AST를 보면 컴파일러는 다음 질문들을 검사할 수 있습니다.

```text
x가 선언되어 있는가?
y가 선언되어 있는가?
y의 타입은 숫자인가?
x에 오른쪽 값을 대입할 수 있는가?
```

---

### 2. 최적화

예를 들어 다음 코드가 있습니다.

```c
x = 1 + 2 * 3;
```

AST를 보면 컴파일러는 `2 * 3`을 먼저 계산하고, 그다음 `1 + 6`을 계산할 수 있습니다. 그래서 컴파일 시점에 다음처럼 바꿀 수 있습니다.

```c
x = 7;
```

이런 최적화를 **상수 접기(constant folding)**라고 합니다.

---

### 3. 코드 생성

AST는 최종적으로 기계어, 바이트코드, LLVM IR, JavaScript 코드 등으로 변환될 수 있습니다.

예를 들어 AST가 다음과 같다면,

```text
BinaryExpression: +
├── Number: 1
└── Number: 2
```

가상의 스택 기반 바이트코드로는 다음처럼 만들 수 있습니다.

```text
PUSH 1
PUSH 2
ADD
```

---

## AST 노드 예시

프로그래밍 언어의 AST에는 보통 이런 노드들이 있습니다.

```text
Program
FunctionDeclaration
VariableDeclaration
Assignment
IfStatement
WhileStatement
ReturnStatement
BinaryExpression
UnaryExpression
CallExpression
Identifier
Literal
```

예를 들어 다음 JavaScript 코드가 있다고 합시다.

```js
function add(a, b) {
  return a + b;
}
```

AST는 대략 이렇게 됩니다.

```text
FunctionDeclaration
├── name: add
├── parameters
│   ├── Identifier: a
│   └── Identifier: b
└── body
    └── ReturnStatement
        └── BinaryExpression: +
            ├── Identifier: a
            └── Identifier: b
```

---

## 핵심 요약

AST는 소스 코드를 컴파일러가 다루기 쉽게 만든 **트리 형태의 의미 구조**입니다.

```text
코드:
x = 1 + 2 * 3;

AST:
Assignment
├── x
└── +
    ├── 1
    └── *
        ├── 2
        └── 3
```

AST는 공백, 괄호, 세미콜론 같은 불필요한 문법 세부사항은 줄이고, 변수 선언, 함수 호출, 연산, 조건문, 반복문 같은 중요한 구조를 표현합니다.

컴파일러에서는 AST를 기반으로 **타입 검사, 의미 분석, 최적화, 코드 생성**을 수행합니다.
