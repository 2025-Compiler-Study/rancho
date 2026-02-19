# Calc3Visitor 동작 설명

이 문서는 `calc3_visitor.py`의 실행 동작을 `Calc3` 문법 기준으로 설명합니다.

## 1. 상속 구조

- `Calc3Visitor`는 `calcVisitor.py`의 `CalcVisitor`를 상속합니다.
- Calc2에서 이미 구현된 계산/조건/변수 로직(`visitExprAssign`, `visitCond`, `visitMulDiv`, `visitAddSub`, `visitVar` 등)은 그대로 재사용합니다.
- Calc3에서 추가된 것만 `calc3_visitor.py`에 구현합니다:
  - `visitCalc3`
  - `visitReadAssign`
  - `visitWrite`
  - 입력 헬퍼 `_read_int`
  - (조용한 실행을 위한) `visitIfElse` 재정의

## 2. 상태와 의존성

- `self.env`: `self.memory`의 별칭(alias)
- `self.outputs`: `write(expr)`로 출력된 값을 누적 저장하는 리스트
- `read_fn`: 입력 함수 (기본값 `input`)
- `write_fn`: 출력 함수 (기본값 `print`)

테스트에서는 `read_fn`, `write_fn`을 주입해서 표준 입출력 없이도 동작을 검증할 수 있습니다.

## 3. 루트 실행 (`visitCalc3`)

`calc3 : stmt+ EOF` 규칙에 맞게 문장(`stmt`)들을 순서대로 방문합니다.

```python
for stmt_ctx in ctx.stmt():
    self.visit(stmt_ctx)
return dict(self.memory)
```

마지막에 `dict(self.memory)`를 반환하므로 외부에서 내부 상태를 직접 변경하지 못합니다.

## 4. 문장 규칙 처리

- `visitReadAssign`: `VAR = read();`
  - `_read_int()`로 정수 입력 1개를 읽어 변수에 저장합니다.
- `visitIfElse`: `if (cond) thenBlock (else elseBlock)?`
  - 조건이 참이면 `thenBlock`, 거짓이면 `elseBlock`(존재 시)만 실행합니다.
- `visitWrite`: `write(expr);`
  - `expr` 결과를 `outputs`에 추가하고 `write_fn`으로 출력합니다.

`visitExprAssign` 같은 기본 대입/연산 로직은 부모(`CalcVisitor`) 구현을 그대로 사용합니다.

## 5. 입력 실패 정책 (`_read_int`)

아래 경우는 모두 `0`으로 처리합니다.

- `EOFError`
- `None` 입력
- 공백 문자열
- 정수 변환 실패 (`ValueError`)

즉, `read()`는 "정수 1개 읽기, 실패 시 0" 정책입니다.

## 6. 변수 조회 정책 (부모 구현 재사용)

`visitVar`는 부모(`CalcVisitor`) 구현을 사용하며, 변수가 아직 `memory`에 없으면 `0`으로 초기화 후 반환합니다.

```python
if var_name not in self.memory:
    self.memory[var_name] = 0
return self.memory[var_name]
```

이 정책 덕분에 미정의 변수 조회가 런타임 크래시로 이어지지 않습니다.

## 7. Calc2 대비 Calc3 핵심 차이

- `read()/write()` 문장을 Visitor에 추가
- 출력은 `outputs` 버퍼로도 추적 가능
- 입출력 함수 주입(`read_fn`, `write_fn`)으로 테스트 용이성 강화
- 루트 규칙은 `visitCalc3`를 새로 구현하고, 나머지 계산 로직은 `CalcVisitor`를 재사용

현재 구현은 `test_calc3.py`의 스모크/입출력 시나리오(정상 입력, 음수 분기, 잘못된 입력=0)를 만족하도록 작성되어 있습니다.
