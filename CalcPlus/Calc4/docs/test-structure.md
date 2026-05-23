# Calc4 Test Structure

## 테스트 실행 방법

가상환경과 의존성이 아직 준비되지 않았다면 먼저 아래 순서로 맞춘다.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

테스트는 프로젝트 루트에서 아래 명령으로 실행한다.

```bash
. .venv/bin/activate
python -m unittest -v test_calc4.py
```

`test_calc4.py`는 구현을 검증하는 완성형 테스트 모음이 아니라, Calc4 시작 시점의 기준점을 고정하는 "골격 테스트"다.

핵심 목적은 세 가지다.

1. ANTLR로 생성한 파서가 Calc4 문법을 정상적으로 읽는지 확인한다.
2. Visitor와 Symbol Table이 아직 미구현 상태라는 사실을 테스트로 명시한다.
3. 이후 구현을 시작할 때 어떤 책임부터 채워야 하는지 순서를 드러낸다.

## 파일 구조

테스트 파일은 크게 네 부분으로 나뉜다.

1. import 준비와 실패 보관
2. 파싱 헬퍼 함수
3. 파서 스모크 테스트
4. 구현 계약 테스트

## 1. import 준비와 실패 보관

`antlr4`, `CalcPlusLexer`, `CalcPlusParser` import를 먼저 시도하고, 실패하면 예외를 `IMPORT_ERROR`에 저장한다.

이 구조의 의도는 다음과 같다.

- 테스트 파일 import 자체가 죽지 않게 한다.
- "생성 파일이 없어서 실패"와 "테스트가 실제로 실패"를 구분한다.
- `unittest.skipIf(...)`와 연결해 준비되지 않은 환경에서는 테스트를 건너뛴다.

즉, 파서 생성 전 단계의 작업자도 테스트 파일을 열고 실패 원인을 바로 이해할 수 있게 만든 구조다.

## 2. `parse_program`

`parse_program(program: str)`는 테스트에서 반복되는 파싱 절차를 한 곳에 모은 헬퍼다.

동작 순서는 다음과 같다.

1. import 실패 여부 확인
2. 문자열 입력을 `InputStream`으로 감싼다.
3. `CalcPlusLexer`로 토큰화한다.
4. `CommonTokenStream`으로 파서 입력 스트림을 만든다.
5. `CalcPlusParser`를 생성한다.
6. 시작 규칙 `calc4()`를 호출한다.
7. `(parser, tree)`를 반환한다.

테스트가 parser와 tree를 같이 받는 이유는 역할이 다르기 때문이다.

- `parser`: 문법 오류 개수 확인
- `tree`: visitor 실행 또는 트리 존재 확인

## 3. `Calc4ParserSmokeTest`

이 클래스는 "시맨틱은 아직 비어 있어도 문법은 읽혀야 한다"는 최소 조건을 검증한다.

### `test_parse_declare_assign_write`

이 테스트는 아래 요소가 함께 파싱되는지 본다.

- 선언문 `int a, b;`
- 대입문 `a = 1 + 2;`
- 출력문 `write(a);`

즉, 가장 기본적인 Calc4 문장 조합이 문법 차원에서 유효한지 확인하는 테스트다.

### `test_parse_nested_blocks_and_if`

이 테스트는 더 복잡한 구조를 한 번에 확인한다.

- 바깥 변수 선언
- 블록 진입
- 내부 같은 이름 변수 선언
- 내부 대입
- `if` 조건문
- 블록 안 `write`

핵심은 "스코프와 제어문이 섞인 형태도 파서가 트리로 만들 수 있어야 한다"는 점이다.

두 테스트 모두 실제 실행 결과는 검증하지 않는다. 오직 아래 두 조건만 본다.

- `parser.getNumberOfSyntaxErrors() == 0`
- `tree is not None`

그래서 이름이 smoke test다. 구현 초기의 최소 생존 여부만 체크한다.

## 4. `Calc4VisitorContractTest`

이 클래스는 Visitor 구현이 아직 비어 있다는 사실을 의도적으로 테스트로 고정한다.

### `_make_visitor`

`calc4_visitor.py`에서 `Calc4Visitor`를 import해 인스턴스를 만든다.  
import 실패 시에는 어떤 파일에서 막혔는지 드러나는 메시지로 `RuntimeError`를 다시 던진다.

### `test_stub_raises_for_program_execution`

간단한 프로그램을 파싱한 뒤 `visitor.visit(tree)`를 호출하고, 현재는 `NotImplementedError`가 나와야 한다고 본다.

이 테스트의 의미는 다음과 같다.

- 아직 실행기 구현이 없다는 사실을 명시한다.
- TODO 상태가 조용히 묻히지 않게 한다.
- 나중에 구현을 시작하면 이 테스트를 먼저 수정하거나 삭제해야 함을 알려준다.

즉, 이 테스트는 기능 검증이 아니라 "현재 단계의 계약"을 검증한다.

## 5. `SymbolTableContractTest`

이 클래스도 같은 목적의 계약 테스트다.  
`SymbolTable`의 주요 메서드가 아직 스텁이라는 점을 고정한다.

현재 확인하는 메서드는 다음과 같다.

- `push_scope()`
- `declare("a")`
- `assign("a", 1)`
- `lookup("a")`

각 메서드가 지금은 `NotImplementedError`를 던져야 테스트를 통과한다.

이 구조는 구현자가 실수로 `pass`나 잘못된 기본값을 남겨두는 일을 막아준다.  
즉, "미구현이라면 명시적으로 실패하라"는 설계다.

## 왜 이런 테스트 구조를 썼는가

Calc4는 구현 범위가 한 번에 넓다.

- 문법
- Visitor 실행
- 심볼 테이블
- 블록 스코프
- 섀도잉
- 조건문
- 입출력

이 모든 것을 처음부터 한 테스트에서 검증하면 어디서 실패했는지 분리하기 어렵다.  
그래서 현재 테스트는 계층을 나눠 둔 상태다.

1. 파서가 되는가
2. Visitor 진입점이 준비됐는가
3. Symbol Table 인터페이스가 준비됐는가

이후 구현이 진행되면 보통 다음 순서로 테스트가 바뀐다.

1. `NotImplementedError` 계약 테스트 제거 또는 수정
2. `SymbolTable` 동작 테스트 추가
3. Visitor 실행 결과 테스트 추가
4. 블록 스코프와 섀도잉 시나리오 테스트 추가
5. 에러 처리 테스트 추가

## 구현자가 읽어야 할 포인트

- 이 테스트 파일은 "정답 검증"보다 "출발선 고정"에 가깝다.
- 현재 통과만으로 Calc4가 구현된 것은 아니다.
- Visitor와 Symbol Table 테스트는 앞으로 깨지도록 설계된 테스트다.
- 실제 구현이 시작되면 가장 먼저 계약 테스트를 기능 테스트로 바꾸는 작업이 필요하다.
