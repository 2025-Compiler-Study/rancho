# Calc5 과제 #3: 이번 수정 사항만 해설

## 결론

첫 변경은 이미 구현되어 있던 `AstExecutor`와 `SymbolTable`이 과제 #3의 "문맥 오류 시 즉시 종료" 요구를 만족하는지 **테스트로 증명하고 문서화**한 작업이었다. 이후 과제 #3의 실행 범위를 문법의 조건문까지 확장해 `CompareExpr`, `IfElse`, 조건 실행을 실제로 구현했다.

수정된 파일은 다음 두 개다.

```text
calc5_ast.py
ast_visualizer.py
test_calc5.py
test_ast_visualizer.py
docs/calc5-program-ast-guide.md
```

`symbol_table.py`는 수정하지 않았다. 기존 scope·재선언·미선언 오류 처리를 그대로 재사용한다.

## 조건문 실행 구현

`calc5_ast.py`에 다음 노드를 추가했다.

```python
CompareExpr(op, left, right)
IfElse(condition, then_block, else_block=None)
```

Builder는 ANTLR의 `cond`와 `IfElse` Parse Tree를 위 노드로 변환한다. Executor는 `eval_condition()`에서 `==`, `!=`, `>`, `>=`, `<`, `<=`를 계산하고, 참이면 then block만 거짓이면 else block만 실행한다.

`ast_visualizer.py`도 `condition`, `then`, `else`, `left`, `right` 관계 이름을 표시하도록 확장했다.

## 1. `test_calc5.py` 변경

### 추가한 import

```python
from symbol_table import DuplicateDeclarationError, UndefinedVariableError
```

기존에는 `RuntimeError`처럼 넓은 범위의 오류만 확인할 수 있었다. 이제는 재선언 오류와 미선언 변수 오류를 구체적인 예외 타입으로 검증한다.

### 재선언 즉시 종료 테스트

```python
program = Program([
    Declare("a"),
    Declare("a"),
    Write(IntLiteral(99)),
])
```

실행 순서:

```text
Declare("a")  -> 선언 성공
Declare("a")  -> DuplicateDeclarationError
Write(99)      -> 실행되지 않음
```

테스트에서 `output == []`를 확인한다. 따라서 예외만 났다는 사실뿐 아니라 오류 이후 statement가 실행되지 않았음도 확인한다.

### 미선언 변수 대입 즉시 종료 테스트

```python
program = Program([
    Assign("a", IntLiteral(1)),
    Write(IntLiteral(99)),
])
```

`a`가 선언된 적 없으므로 `SymbolTable.assign()`이 `UndefinedVariableError`를 발생시킨다. 뒤의 `Write(99)`는 실행되지 않는다.

### 미선언 변수 읽기 테스트

```python
program = Program([Write(VarRef("a"))])
```

`Write`는 먼저 `VarRef("a")`를 계산한다. 이때 `SymbolTable.lookup("a")`가 실패하므로 `UndefinedVariableError`가 발생한다.

### block의 바깥 변수 수정 테스트

```python
Program([
    Declare("a"),
    Block([Assign("a", IntLiteral(3))]),
    Write(VarRef("a")),
])
```

안쪽 block에 `a`가 없으면 Symbol Table은 바깥 scope를 역순으로 찾아 전역 `a`를 수정한다. 따라서 출력은 `3`이다. block 내부에서 선언한 새 변수는 block 종료와 함께 제거되지만, 바깥 변수의 수정은 유지된다.

## 2. `docs/calc5-program-ast-guide.md` 변경

`과제 3: Executor의 오류 처리` 절을 추가했다.

- 재선언, 미선언 대입, 미선언 읽기, block 밖 지역 변수 사용의 결과를 표로 정리했다.
- 오류가 발생하면 이후 statement를 실행하지 않는다는 정책을 명시했다.
- TDD 순서에 Executor 오류 즉시 종료 검증 단계를 추가했다.

## 동작 근거: 기존 구현

오류를 실제로 발생시키는 코드는 이미 `symbol_table.py`에 있었다.

```python
if name in scope:
    raise DuplicateDeclarationError(...)

if scope is None:
    raise UndefinedVariableError(...)
```

`AstExecutor.execute()`는 이 예외를 잡아서 계속 실행하지 않는다.

```python
for statement in program.statements:
    self.execute_stmt(statement)
```

따라서 `execute_stmt()` 중 예외가 발생하면 반복문도 즉시 중단된다. 이것이 과제 #3의 "즉시 종료" 요구를 만족하는 이유다.

## 검증 명령

전체 테스트:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest -v
```

Executor 테스트만 실행:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest -v test_calc5.AstExecutorTest
```

이번 변경 후 전체 테스트 결과는 29개 통과다.
