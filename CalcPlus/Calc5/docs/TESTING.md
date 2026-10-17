# Calc5 테스트 방법

## 목적

Calc5의 AST 구조, 시각화, expression 평가, 그리고 과제 #3 Executor를
재현 가능하게 검증한다. Executor 테스트는 Parse Tree를 순회하지 않고
Python 코드로 직접 구성한 `Program` AST만 실행한다.

## 사전 준비

프로젝트 루트에서 가상환경과 의존성을 준비한다.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

## 전체 자동 테스트

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest -v
```

`PYTHONDONTWRITEBYTECODE=1`은 테스트 실행으로 `__pycache__` 파일이
생기지 않게 한다.

## 과제 #3 Executor 테스트만 실행

선언, 대입, `read`, `write`, block scope, 문맥 오류 즉시 종료를 확인한다.

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest -v test_calc5.AstExecutorTest
```

이 테스트 그룹이 확인하는 동작은 다음과 같다.

| 검증 항목 | 기대 결과 |
| --- | --- |
| `a = 1 + 2 * 3` | expression을 재귀 평가해 `a`에 `7` 저장 |
| `read()`와 `write()` | 주입한 입력값을 계산에 사용하고 계산값을 출력 |
| block 내부 선언 | block 종료 뒤 지역 변수 접근 시 오류 |
| 바깥 변수 수정 | block 안에서 바깥 scope의 변수값 수정 가능 |
| 같은 scope 재선언 | `DuplicateDeclarationError`, 이후 문장 미실행 |
| 미선언 변수 읽기/대입 | `UndefinedVariableError`, 이후 문장 미실행 |

## 수동 실행 확인

아래 명령은 `read()`에 10을 제공한다. 따라서 `a = 1`, `b = 10`,
`c = a + b`가 되어 `11`을 출력한다.

```bash
.venv/bin/python -c "from calc5_ast import AstExecutor, build_program; program = build_program('int a, b; a = 1; b = read(); { int c; c = a + b; write(c); } b = 0;'); AstExecutor(read_fn=lambda: 10).execute(program)"
```

## #2 비주얼라이저로 AST 구조 확인

Executor의 계산 결과가 예상과 다르면 먼저 AST 모양을 확인한다. 특히
`Assign`의 value, `BinaryExpr`의 left/right, `Block`의 statement 순서를 본다.

```bash
.venv/bin/python ast_visualizer.py --program $'int a;\na = 1 + 2 * 3;\nwrite(a);'
```

시각화된 트리는 아래의 의미 구조를 보여야 한다.

```text
Program
├── Declare(a)
├── Assign(a)
│   └── BinaryExpr(+)
│       ├── IntLiteral(1)
│       └── BinaryExpr(*)
│           ├── IntLiteral(2)
│           └── IntLiteral(3)
└── Write
    └── VarRef(a)
```

비주얼라이저는 모든 `children()`을 표시하지만, Executor는 statement 의미에
따라 실행한다. 예를 들어 `Assign`은 value만 평가한 뒤 target에 저장한다.
