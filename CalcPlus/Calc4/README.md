# Calc4 Start Setup

이 디렉터리는 `Calc4` 구현 시작용 골격만 남긴 상태다.

포함 내용:

- `CalcPlus.g4`: Calc4 기준 문법
- `calc4_visitor.py`: 구현할 Visitor 스텁
- `symbol_table.py`: 스코프 기반 심볼 테이블 스텁
- `test_calc4.py`: 파서 스모크 테스트와 구현 계약 테스트
- `docs/test-structure.md`: `test_calc4.py` 구조 해설
- `docs/problem-explanation.md`: Calc4 문제 해설
- `docs/implementation-steps.md`: Calc4 단계별 구현 가이드

현재 의도:

- 파서는 생성되고 테스트가 돌아가야 한다.
- 시맨틱 구현은 아직 비워 둔다.
- 구현 전 테스트 기준점만 먼저 고정한다.

## regenerate

```bash
antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4
```

## run tests

```bash
python3 -m unittest -v test_calc4.py
```

## test guide

테스트 구조 설명은 [`docs/test-structure.md`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/docs/test-structure.md)에 정리했다.

## problem guide

Calc4 문제 해설은 [`docs/problem-explanation.md`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/docs/problem-explanation.md)에 정리했다.

## implementation guide

Calc4 단계별 구현 순서는 [`docs/implementation-steps.md`](/home/jake/project/CS/compiler/rancho/CalcPlus/Calc4/docs/implementation-steps.md)에 정리했다.

## next implementation order

1. `symbol_table.py`에 scope stack 구현
2. `Declare`, `ExprAssign`, `Var`부터 처리
3. 선언 전 사용/중복 선언 오류 처리
4. `StmtBlock`과 `block` 진입/탈출 처리
5. `if/else`, `read`, `write` 연결
