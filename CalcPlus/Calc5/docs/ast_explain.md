# AST 정리

## 1. 한눈에 보기

**AST(Abstract Syntax Tree, 추상 구문 트리)**는 소스 코드의 표면적인
문법 표현을 그대로 복사한 트리가 아니다. 컴파일러와 인터프리터의 후속
단계가 사용하기 쉽도록, 프로그램을 구성하는 핵심 요소와 그 관계를 표현한
순서 있는 트리다.

```text
Parse Tree : 이 토큰들이 어떤 문법 규칙으로 인식되었는가?
AST        : 이 프로그램은 어떤 언어 구성 요소로 이루어졌는가?
IR         : 이 프로그램을 어떻게 분석하고 실행할 것인가?
```

`abstract`는 "대충 표현한다"는 뜻이 아니다. 괄호, 세미콜론, 문법을
구현하기 위한 중간 비단말처럼 후속 처리에 불필요한 **구체적 표기법을
추상화한다**는 뜻이다.

엄밀하게는 추상 구문과 AST도 구분할 수 있다.

```text
추상 구문(abstract syntax) = 허용되는 노드 종류와 결합 규칙
AST                         = 특정 프로그램을 그 규칙에 따라 표현한 값
```

예를 들어 다음은 식을 위한 추상 구문 스키마다.

```text
Expr ::= Int(value)
       | Name(identifier)
       | Add(left, right)
       | Mul(left, right)
```

`a + 2 * b`의 AST는 이 스키마의 한 인스턴스다.

```text
Add(Name("a"), Mul(Int(2), Name("b")))
```

---

## 2. Parse Tree와 AST 비교

다음 구체 문법을 사용한다고 가정하자.

```text
expr   -> expr '+' term | term
term   -> term '*' factor | factor
factor -> ID | INT | '(' expr ')'
```

입력은 다음과 같다.

```text
a + (2 * b)
```

### 2.1 Parse Tree

Parse Tree는 적용된 생성 규칙과 문법 기호를 드러낸다.

```text
expr
|-- expr -> term -> factor -> ID(a)
|-- '+'
`-- term -> factor
    |-- '('
    |-- expr -> term
    |   |-- term -> factor -> INT(2)
    |   |-- '*'
    |   `-- factor -> ID(b)
    `-- ')'
```

- 루트는 시작 비단말이다.
- 내부 노드는 `expr`, `term`, `factor` 같은 비단말이다.
- 잎에는 파서가 받은 단말 토큰이 나타난다.
- 괄호와 연산자도 문법 기호로 나타난다.
- 문법이 모호하면 같은 입력에 여러 Parse Tree가 생길 수 있다.

### 2.2 AST

AST는 후속 단계가 필요한 프로그램 구조를 직접 표현한다.

```text
BinaryExpr(+)
|-- VarRef(a)
`-- BinaryExpr(*)
    |-- IntLiteral(2)
    `-- VarRef(b)
```

AST에서는 다음 정보가 트리 구조에 이미 반영되었으므로 생략할 수 있다.

- 우선순위를 구현하기 위한 `expr`, `term`, `factor`
- 그룹화를 위한 `(`와 `)`
- 각 생성 규칙을 거쳤다는 사실

따라서 `a + (2 * b)`와 `a + 2 * b`는 보통 같은 AST가 된다. 반면
`(a + 2) * b`는 다음과 같이 다른 AST가 된다.

```text
BinaryExpr(*)
|-- BinaryExpr(+)
|   |-- VarRef(a)
|   `-- IntLiteral(2)
`-- VarRef(b)
```

### 2.3 차이 표

| 기준 | Parse Tree / CST | AST |
| --- | --- | --- |
| 중심 질문 | 어떤 문법 규칙으로 인식했는가 | 어떤 프로그램 구성 요소인가 |
| 설계 기준 | 구체 문법의 생성 규칙 | 언어와 도구가 정한 추상 구문 |
| 일반적인 노드 | 단말과 비단말 | 선언, 문장, 식, 연산, 이름, 리터럴 |
| 괄호와 세미콜론 | 문법에 있으면 보통 포함 | 구조로 대체되면 보통 생략 |
| 공백과 주석 | lexer와 구현 정책에 따라 다름 | 보통 생략하지만 필요하면 보존 |
| 문법 리팩터링 | 트리 구조가 크게 바뀔 수 있음 | 노드 계약을 유지하면 영향이 작음 |
| 원문 복원 | lossless CST라면 가능 | 일반적으로 불가능 |
| 주 사용처 | 파서 진단, 포매터, 편집기 | 의미 분석, 해석, 정적 분석, 코드 생성 |

`Parse Tree`와 `CST(Concrete Syntax Tree)`는 이론 설명에서는 거의 같은
뜻으로 쓰이지만, 실제 도구의 명칭은 통일되어 있지 않다. 또한 Parse Tree라고
해서 lexer가 버린 공백과 주석까지 자동으로 보존하는 것은 아니다. 원문을
정확히 복원할 수 있는 트리는 별도로 `lossless` 또는 `full-fidelity`라고
부르는 편이 정확하다.

---

## 3. 컴파일 과정에서의 위치

전형적인 컴파일 파이프라인은 다음과 같다.

```text
Source text
    -> Lexing
Token stream
    -> Parsing
Parse Tree / CST
    -> AST construction
AST
    -> Name resolution and type checking
Typed or annotated AST / HIR
    -> Lowering and optimization
IR / CFG / SSA
    -> Code generation
Bytecode or machine code
```

이 순서는 개념적인 구분이다. 모든 구현이 Parse Tree를 실제 객체로 만든 뒤
AST로 변환하는 것은 아니다. 재귀 하강 파서나 parser generator의 semantic
action은 파싱 중에 AST 노드를 바로 만들 수 있다. GNU Bison도 문법 규칙을
인식할 때 부분 식의 semantic value로 더 큰 식을 구성하는 방식을 제공한다.
([GNU Bison semantic actions](https://www.gnu.org/software/bison/manual/html_node/Semantic-Actions.html))

AST가 생성되었다고 프로그램이 의미적으로 올바른 것은 아니다. 다음 검사는
보통 AST 생성 이후에 수행한다.

- 식별자가 선언되었는가?
- 같은 스코프에서 중복 선언되지 않았는가?
- 피연산자 타입이 연산자와 호환되는가?
- 함수 인자의 개수와 타입이 맞는가?
- 모든 실행 경로가 필요한 값을 반환하는가?

따라서 AST는 "프로그램의 의미 그 자체"라기보다 **의미 분석에 적합하게
정리된 구문 구조**라고 표현하는 편이 정확하다.

---

## 4. AST가 필요해진 배경

초기 컴파일러에서는 언어 문법의 인식, 의미 처리, 대상 코드 생성이 서로
강하게 결합되어 있었다. Edgar T. Irons는 1961년 논문에서 초기 컴파일러의
언어 정의와 번역 기능이 구현 안에 뒤섞여 있어 언어를 수정하거나 확장하기
어렵다는 문제를 지적했다.
([A Syntax Directed Compiler for ALGOL 60](https://doi.org/10.1145/366062.366083))

Parse Tree를 그대로 후속 단계의 자료구조로 사용하면 다음 문제가 생긴다.

1. `expr`, `term`, `factor`처럼 파싱 편의를 위해 만든 노드가 모든 단계에 노출된다.
2. 좌재귀 제거와 left factoring처럼 같은 언어의 문법 표현만 바꿔도 후속 코드가 영향을 받는다.
3. 구두점과 중간 비단말 때문에 트리가 크고 방문 코드가 복잡해진다.
4. 구체 표기와 프로그램 구조가 결합되어 다른 표기법이나 프런트엔드를 재사용하기 어렵다.

AST는 파서와 나머지 컴파일러 사이에 다음과 같은 경계를 제공한다.

```text
Parser가 보는 것     : expr, term, factor, '(', ')', ';'
후속 단계가 보는 것 : Add, Assign, Call, If, Function
```

이 경계 덕분에 타입 검사기, 인터프리터, 최적화기, 코드 생성기는 파서가
사용한 구체 문법보다 안정적인 언어 모델을 대상으로 구현될 수 있다.

---

## 5. 유래와 발전 과정

### 5.1 1950년대: 형식 문법과 계층적 구문 분석

Chomsky의 형식 문법 연구와 Backus, Naur의 문법 표기법은 문자열을 계층적인
구조로 분석하는 이론적, 실용적 기반을 마련했다. ALGOL 60은 BNF 계열의
형식 표기법으로 프로그래밍 언어 문법을 기술한 대표적인 초기 사례다.

- [Chomsky, Three Models for the Description of Language, 1956](https://doi.org/10.1109/TIT.1956.1056813)
- [Revised Report on the Algorithmic Language ALGOL 60](https://academic.oup.com/comjnl/article-pdf/5/4/349/899594/050349.pdf)

이 단계의 핵심 관심은 "어떤 문자열이 문법에 속하는가"와 "어떤 생성 규칙으로
유도되는가"였다. 이는 Parse Tree의 직접적인 이론적 기반이다.

### 5.2 1960년: Lisp와 프로그램을 데이터로 다루는 관점

McCarthy의 Lisp는 원자와 재귀적인 순서쌍으로 이루어진 S-expression을
사용했다. AST라는 용어를 사용한 것은 아니지만, 프로그램과 기호식을 중첩된
자료구조로 표현하고 프로그램이 그것을 직접 조작할 수 있음을 보여 주었다.
([Recursive Functions of Symbolic Expressions, 1960](https://www-formal.stanford.edu/jmc/recursive/recursive.html))

### 5.3 1961년: Syntax-directed compilation

Irons의 syntax-directed compiler는 문법 규칙에 번역 동작을 연결하여 언어의
형태와 번역을 체계적으로 기술하려 했다. 이 계열의 접근은 이후 문법 reduction
시 semantic value나 트리 노드를 조립하는 방식으로 발전했다.

### 5.4 1962년 발표, 1963년 출판: Abstract syntax의 명시적 정식화

John McCarthy는 `Towards a Mathematical Science of Computation`에서
`Abstract Syntax of Programming Languages`라는 절을 두고 BNF의 구체적
표기와 다른 추상 구문을 설명했다.

핵심은 `a+b`, `+ab`, `(PLUS A B)`처럼 표기가 달라도 합인지 판별하고 두
피연산자를 추출하고 구성할 수 있다면 같은 추상 구조로 취급할 수 있다는
것이다.
([McCarthy의 Abstract Syntax 절](https://www-formal.stanford.edu/jmc/towards/node12.html),
[IFIP 1962 서지 정보](https://dblp.org/rec/conf/ifip/McCarthy62.html))

주의할 점은 이 글이 `abstract syntax tree`나 `AST`라는 표현을 사용하지
않았다는 사실이다. 따라서 McCarthy를 "AST 약어와 트리 자료구조의 발명자"로
단정하기보다, **표기 독립적인 추상 구문 개념을 명시한 중요한 출발점**으로
보는 것이 정확하다.

### 5.5 1968년 이후: 의미 정보와 트리 처리의 체계화

Knuth의 attribute grammar는 구문 트리 노드에 타입, 값, 심볼 정보 같은
속성을 계산하는 방법을 체계화했다. 이는 AST 자체의 발명과 동일하지는 않지만,
트리를 따라 의미 정보를 계산하는 컴파일러 구조에 큰 영향을 주었다.
([Knuth, Semantics of Context-Free Languages, 1968](https://doi.org/10.1007/BF01692511))

역사상 최초라고 단정할 수는 없지만, `abstract syntax tree`라는 정확한 표현은
늦어도 Franklin L. DeRemer의 1969년 MIT 논문에서 확인된다.
([Practical Translators for LR(k) Languages](https://books.google.com/books/about/Practical_Translators_for_LR_k_Languages.html?id=9ylMAAAAYAAJ))

1970년대 이후 parser generator와 syntax-directed translation이 널리
사용되면서, 문법 규칙을 인식할 때 AST 노드를 만드는 방식이 일반적인
컴파일러 구현 패턴으로 자리 잡았다.

### 5.6 Typed AST, desugaring, 다단계 IR

언어가 커지면서 하나의 AST에 모든 정보를 계속 덧붙이는 방식에는 한계가
생겼다. 현대 컴파일러는 목적에 따라 여러 표현을 둔다.

```text
Parser AST
    -> 이름이 연결된 AST
    -> Typed AST
    -> desugared HIR
    -> 제어 흐름 중심 MIR
    -> SSA 또는 백엔드 IR
```

예를 들어 Rust 컴파일러는 대략 `AST -> HIR -> THIR -> MIR -> LLVM IR`
단계를 사용한다. HIR에서는 괄호처럼 분석에 불필요한 구조를 제거하고 `for`를
더 단순한 표현으로 낮춘다. THIR에서는 타입과 암시적 연산을 더 명시적으로
나타낸다.
([rustc compiler overview](https://rustc-dev-guide.rust-lang.org/overview.html),
[AST to HIR lowering](https://rustc-dev-guide.rust-lang.org/hir/lowering.html))

### 5.7 현대: IDE를 위한 구체 정보의 재도입

전통적인 AST는 공백, 주석, 정확한 괄호 위치를 버려도 컴파일에는 문제가
없었다. 하지만 IDE, 리팩터링, 포매터는 원문의 정확한 형태와 입력 중인 잘못된
코드도 다뤄야 한다. 그 결과 현대 도구는 AST와 CST 사이의 여러 절충점을
사용한다.

- Clang AST는 리팩터링 지원을 위해 `ParenExpr`과 축약되지 않은 일부 소스 구조를 보존한다. ([Clang AST](https://clang.llvm.org/docs/IntroductionToTheClangAST.html))
- Roslyn은 토큰, 공백, 주석, 전처리 지시문, 누락된 토큰을 보존하는 immutable full-fidelity syntax tree를 사용한다. ([Roslyn syntax model](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/work-with-syntax))
- Tree-sitter는 편집할 때 효율적으로 갱신되며 오류가 있는 코드에도 유용한 incremental CST를 만든다. ([Tree-sitter](https://tree-sitter.github.io/tree-sitter/index.html))

따라서 현대에는 이름만 보고 AST인지 CST인지 판단하기보다 다음 속성을
확인하는 것이 정확하다.

- 문법 규칙과 노드가 얼마나 직접 대응하는가?
- 구두점, 공백, 주석을 보존하는가?
- 원문을 손실 없이 재생성할 수 있는가?
- 타입과 심볼 같은 의미 정보를 포함하는가?
- 전체 파일을 다시 파싱하지 않고 증분 갱신할 수 있는가?

---

## 6. AST를 정의하는 RFC나 표준이 있는가?

### 6.1 결론

**모든 프로그래밍 언어와 도구가 따라야 하는 AST 구조를 정의한 단일 IETF
RFC는 없다.** AST의 노드 종류와 추상화 수준은 언어 문법, 컴파일러 단계,
도구의 목적에 따라 달라지기 때문이다.

IETF RFC에서 AST라는 용어가 등장할 수는 있다. 예를 들어
[RFC 9239](https://www.rfc-editor.org/rfc/rfc9239.html)는 JavaScript의
`Script`와 `Module`을 AST의 최상위 goal로 언급한다. 그러나 이 RFC의 목적은
JavaScript media type 등록이며 AST 노드 형식을 표준화하는 것이 아니다.

`RFC`를 넓은 의미의 기술 제안 절차로 사용하면 언어별 관련 문서는 존재한다.
다만 이들도 범용 AST 표준은 아니다.

### 6.2 RFC와 표준에 가까운 문서

| 문서 | 성격 | AST와의 관계 |
| --- | --- | --- |
| [OMG ASTM 1.0](https://www.omg.org/spec/ASTM/About-ASTM) | OMG 공식 표준, 2011 | 여러 언어의 분석 도구가 교환할 수 있는 AST 메타모델을 정의한다. 범용 표준에 가장 가깝지만 IETF RFC는 아니다. |
| [ESTree](https://github.com/estree/estree) | JavaScript 생태계의 사실상 표준 | JavaScript 도구가 교환할 AST 노드 인터페이스를 정의한다. ECMAScript 공식 표준 자체는 아니다. |
| [ECMA-262](https://262.ecma-international.org/16.0/#sec-syntactic-grammar) | ECMAScript 언어 표준 | 문법과 Parse Node를 정의하지만 구현체가 같은 트리 자료구조를 사용할 것을 요구하지 않는다. |
| [PEP 339](https://peps.python.org/pep-0339/) | Python의 withdrawn informational PEP | CPython의 `Parse Tree -> AST -> CFG -> bytecode` 설계를 역사적으로 설명한다. 규범적 AST 표준은 아니다. |
| [Rust RFC 1211](https://rust-lang.github.io/rfcs/1211-mir.html) | Rust 컴파일러 설계 RFC | 하나의 AST만 사용하던 구조에서 MIR로 lowering해야 하는 이유를 설명한다. AST 형식 자체를 표준화하지 않는다. |

상호 운용 가능한 AST 포맷이 필요하다면 "AST의 RFC"를 찾기보다 대상에 따라
다음 중 하나를 선택해야 한다.

1. 특정 언어 생태계의 노드 규격을 따른다. 예: JavaScript의 ESTree.
2. 컴파일러가 제공하는 공식 API를 따른다. 예: Clang AST, Python `ast`.
3. 여러 언어 사이의 분석 모델 교환이 목적이면 OMG ASTM이나 KDM을 검토한다.
4. 프로젝트 내부 계약이라면 별도의 AST 스키마와 버전 정책을 문서화한다.

---

## 7. AST와 IR은 어떻게 다른가?

AST도 넓은 의미에서는 고수준 중간 표현이다. 하지만 일반적으로 AST는 소스
언어의 선언, 문장, 식 구조를 유지하고, 하위 IR은 실행과 분석을 쉽게 만들기
위해 그 구조를 낮춘다.

예를 들어 다음 소스가 있다고 하자.

```c
if (a && b) {
    x = 1;
}
```

AST는 `If`, `LogicalAnd`, `Assign` 관계를 보존한다. 제어 흐름 IR은 이를
조건 분기와 basic block으로 바꾼다.

```text
entry:
    branch a, check_b, exit

check_b:
    branch b, assign_x, exit

assign_x:
    x = 1
    jump exit
```

| 표현 | 주된 관심사 |
| --- | --- |
| AST | 소스 언어 구성 요소와 중첩 구조 |
| Typed AST / HIR | 타입, 심볼, 일부 desugaring을 포함한 고수준 분석 |
| CFG / MIR | 실행 순서와 제어 흐름 |
| SSA / LLVM IR | 데이터 흐름, 최적화, 코드 생성 |

---

## 8. 자주 생기는 오해

### "파서는 반드시 Parse Tree를 만든 뒤 AST로 변환한다"

아니다. Parse Tree를 실제 객체로 만들지 않고 파싱 중 AST를 바로 생성할 수
있다. Calc5처럼 ANTLR Parse Tree를 명시적으로 AST로 변환하는 구조도 있다.

### "AST는 언어마다 하나로 정해져 있다"

아니다. 같은 언어라도 컴파일러, IDE, linter, 포매터가 서로 다른 AST 또는
syntax tree를 사용할 수 있다.

### "AST에는 괄호나 토큰이 절대 들어가면 안 된다"

아니다. 보통 생략할 뿐이다. Clang처럼 원본 소스와의 대응이 중요하면 괄호나
암시적 변환 노드를 유지할 수 있다.

### "AST가 있으면 원본 코드를 그대로 복원할 수 있다"

일반적으로 불가능하다. 주석, 공백, 선택적 괄호, 세미콜론 같은 정보를
제거했기 때문이다. 정확한 복원이 필요하면 lossless CST나 별도 token stream이
필요하다.

### "AST는 항상 엄밀한 트리다"

기본적인 부모-자식 구조는 트리지만, 이름이 심볼 테이블 엔트리를 참조하거나
타입 객체와 공통 하위 구조를 공유하면 전체 내부 표현은 그래프에 가까워질 수
있다. `AST`라는 이름은 주된 구문 소유 구조를 가리키는 관례다.

---

## 9. Calc5에 적용

Calc5의 목표 구조는 다음과 같다.

```text
CalcPlus.g4
    -> generated lexer and parser
    -> ANTLR Parse Tree
    -> ast_builder.py
    -> ast_nodes.py의 AST
    -> ast_printer.py 또는 ast_executor.py
```

현재 AST 노드는 다음과 같이 언어의 핵심 구성 요소를 직접 표현한다.

```text
Program
|-- Declare
|-- Assign
|-- Write
|-- Block
|-- IfElse
`-- Expr
    |-- IntLiteral
    |-- VarRef
    |-- ReadCall
    `-- BinaryExpr
```

구현할 때 중요한 기준은 다음과 같다.

1. 괄호 Parse Tree 노드는 별도 AST 노드로 만들지 않고 내부 식을 반환할 수 있다.
2. `int a, b;`처럼 문법상 하나인 선언을 `Declare("a")`, `Declare("b")`로 나눌 수 있다.
3. 연산자의 우선순위와 결합 방향은 `BinaryExpr`의 중첩 구조로 보존해야 한다.
4. `ast_executor.py`는 ANTLR context가 아니라 AST 노드에만 의존해야 한다.
5. 향후 진단 품질이 필요하면 AST 노드에 source span을 추가할 수 있다.

이처럼 Parse Tree에서 AST로 변환할 때 노드 수가 반드시 줄어드는 것은 아니다.
구두점과 문법 중간 노드는 사라지지만, 하나의 선언을 여러 `Declare`로 나누거나
암시적 변환 노드를 추가하면 AST 노드가 더 많아질 수도 있다.

---

## 10. 최종 요약

```text
Parse Tree
    문법의 유도 구조
    구체 문법에 강하게 의존

AST
    프로그램 구성 요소의 구조
    의미 분석과 실행에 적합

Typed AST / HIR
    타입, 심볼, desugaring이 반영된 고수준 표현

IR / CFG / SSA
    제어 흐름, 데이터 흐름, 최적화와 코드 생성에 적합한 표현
```

AST의 핵심 가치는 단순히 "트리라서"가 아니다. 구체 문법과 후속 컴파일 단계
사이에 목적에 맞는 안정적인 경계를 제공한다는 데 있다.
