# Calc5 Start Setup

이 디렉터리는 Calc5 구현 시작용 스켈레톤이다.

Calc5의 목표는 언어 문법을 크게 바꾸지 않고, Parse Tree를 바로 실행하던 흐름을 다음 구조로 바꾸는 것이다.

1. ANTLR Parse Tree 생성
2. Parse Tree를 AST로 변환
3. AST를 출력하거나 시각화
4. AST Executor로 실행

포함 내용:

- `CalcPlus.g4`: Calc5 기준 문법. 진입 규칙은 `program`이다.
- `ast_nodes.py`: AST 노드 데이터 구조 골격
- `ast_builder.py`: Parse Tree에서 AST를 만드는 Visitor 스텁
- `ast_printer.py`: AST 출력기 스텁
- `ast_executor.py`: AST 실행기 스텁
- `symbol_table.py`: Calc4에서 쓰던 스코프 기반 심볼 테이블
- `test_calc5.py`: 파서 스모크 테스트와 스켈레톤 계약 테스트
- `docs/overview.md`: Calc5 전체 구조 요약
- `docs/`: Calc5 문제 해설과 구현 순서

현재 의도:

- 파서는 `program()` 진입점으로 생성되어야 한다.
- AST 관련 구현은 아직 비워 두고 `NotImplementedError`로 드러낸다.
- Symbol Table은 Calc4 구현을 재사용해 Calc5의 초점을 AST에 둔다.

## venv setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

현재 코드 실행에 필요한 최소 외부 의존성은 `antlr4-python3-runtime` 하나다.
이 저장소의 생성 파일은 현재 `ANTLR 4.9.2` 기준이므로 런타임도 같은 버전으로 맞춘다.

## run tests

```bash
. .venv/bin/activate
python -m unittest -v test_calc5.py
```

## regenerate parser

```bash
antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4
```

`CalcPlus.g4`로 생성 파일을 다시 만들려면 ANTLR tool과 Java가 필요하다.
이미 생성된 `CalcPlusLexer.py`, `CalcPlusParser.py`, `CalcPlusVisitor.py`, `CalcPlusListener.py`가 유효하면 테스트 실행만으로는 Java가 없어도 된다.

## next implementation order

1. `ast_nodes.py`의 노드 종류가 과제 요구를 담는지 확인
2. `ast_builder.py`에서 expression 노드부터 변환
3. 선언, 대입, read/write, block, if 노드 변환
4. `ast_printer.py`로 AST 구조 확인
5. `ast_executor.py`에서 AST 실행 연결
6. Builder 단계의 의미 오류 수집 정책 추가
