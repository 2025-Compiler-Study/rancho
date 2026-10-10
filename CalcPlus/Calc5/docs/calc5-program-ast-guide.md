# Calc5 Program AST: 과제 1 예제 2

이번 단계는 기존 expression AST를 유지한 채 프로그램 구조까지 확장한다. 지원 범위는 선언, 대입, `read()`, `write()`, `{ ... }` block이다. `if/else`와 조건식은 다음 단계다.

## 예제와 AST

입력 프로그램:

```text
int a, b;
a = 1;
b = read();
{
    int c;
    c = a + b;
    write(c);
}
b = 0;
```

의미 중심 AST는 다음 구조다.

```text
Program
├── Declare("a")
├── Declare("b")
├── Assign("a", IntLiteral(1))
├── Assign("b", ReadCall())
├── Block
│   ├── Declare("c")
│   ├── Assign("c", BinaryExpr("+", VarRef("a"), VarRef("b")))
│   └── Write(VarRef("c"))
└── Assign("b", IntLiteral(0))
```

`int a, b;`는 실행·심볼 테이블의 단위에 맞추어 `Declare` 두 개가 된다. `Assign`의 대상 이름은 문자열 속성이고, 계산해야 하는 오른쪽 값만 AST 자식이다. `Program`과 `Block`은 여러 statement 자식을 가지므로 전체 트리는 더 이상 이진 트리가 아니라 일반 트리다. 단, `BinaryExpr` 부분은 여전히 left/right 자식 둘을 가진 이진 트리다.

## 파일 역할

| 파일 | 역할 |
| --- | --- |
| `calc5_ast.py` | 노드, ANTLR Builder, `format_ast`, expression 계산, `AstExecutor` |
| `symbol_table.py` | 선언 여부와 block scope의 변수값 관리 |
| `ast_visualizer.py` | `children()`을 따라 터미널 트리·방문 순서·DOT 생성 |
| `test_calc5.py` | 노드, Builder, 실행과 scope의 TDD 테스트 |
| `test_ast_visualizer.py` | Program 시각화 연결 테스트 |

ANTLR 생성 파일은 수정하지 않았다. `CalcPlus.g4`에 이미 필요한 program 문법이 있었기 때문이다.

## 실행과 검증

가상환경이 없다면 먼저 만든다.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

전체 테스트:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest -v
```

예제 2 AST를 직접 확인한다. Bash의 `$'...'`는 줄바꿈을 포함한 하나의 인자로 넘긴다.

```bash
.venv/bin/python ast_visualizer.py --program $'int a, b;\na = 1;\nb = read();\n{\n  int c;\n  c = a + b;\n  write(c);\n}\nb = 0;'
```

실행 결과도 입력을 고정해 재현할 수 있다.

```bash
.venv/bin/python -c "from calc5_ast import AstExecutor, build_program; p = build_program('int a, b; a = 1; b = read(); { int c; c = a + b; write(c); } b = 0;'); AstExecutor(read_fn=lambda: 10).execute(p)"
```

위 명령은 `11`을 출력한다. `read_fn=lambda: 10`이 `read()`의 값이고, `c = 1 + 10` 뒤 `write(c)`가 실행되기 때문이다.

## 과제 3: Executor의 오류 처리

`AstExecutor`는 Parse Tree를 다시 보지 않고, 수동으로 만든 `Program` AST만 실행한다. 변수 관련 판단은 `SymbolTable`에 위임하며 문맥 오류는 즉시 예외로 끝난다.

| 상황 | 발생 예외 | 이후 문장 |
| --- | --- | --- |
| 같은 scope에서 `int a; int a;` | `DuplicateDeclarationError` | 실행하지 않음 |
| 선언 없이 `a = 1;` | `UndefinedVariableError` | 실행하지 않음 |
| 선언 없이 `write(a);` | `UndefinedVariableError` | 실행하지 않음 |
| block 종료 뒤 `c` 사용 | `UndefinedVariableError` | 실행하지 않음 |

안쪽 block은 바깥 scope를 읽고 수정할 수 있다. 반대로 block 안에서 선언한 `c`는 block 종료 시 제거된다. 이 동작은 `test_calc5.py`의 `AstExecutorTest`가 검증한다.

## 구현 순서(TDD)

1. Program/statement 노드의 `children()` 구조를 테스트한다.
2. 예제 2의 수동 AST와 `format_ast()`를 테스트한다.
3. `AstExecutor`의 입출력·block scope 테스트를 통과시킨다.
4. `build_program()`이 ANTLR Parse Tree에서 같은 AST를 만드는지 검증한다.
5. 비주얼라이저가 같은 `children()` 구조를 표시하는지 검증한다.
6. Executor가 재선언·미선언 오류에서 다음 statement를 실행하지 않는지 검증한다.
