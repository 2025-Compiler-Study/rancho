# Calc3 설명

## 1. 개요
`Calc3`는 `Calc2`(수식, 변수, `if/else`)에 입출력 기능인 `read()`와 `write(expr)`를 추가한 인터프리터 단계다.

- 목적: 기존 계산/분기 기능을 유지하면서 파일 입력 + stdin/stdout 기반 실행까지 연결
- 핵심 구현: ANTLR 문법(`CalcPlus.g4`) + Visitor 실행기(`calc3_visitor.py`)

## 2. 문법 요약
프로그램 루트는 `calc3 : stmt+ EOF` 이며, 문장(`stmt`)은 다음 4종을 지원한다.

1. 변수 할당: `VAR = expr;`
2. 입력 할당: `VAR = read();`
3. 분기: `if (cond) { ... } else { ... }` (`else` 생략 가능)
4. 출력: `write(expr);`

조건식은 `==`, `!=`, `<`, `>`, `<=`, `>=` 비교를 지원하고, 수식은 사칙연산/괄호/변수/정수를 지원한다.

## 3. 실행 구조
실행 흐름은 다음과 같다.

1. 소스 문자열을 `InputStream`으로 생성
2. `CalcPlusLexer`로 토큰화
3. `CalcPlusParser.calc3()`로 파스 트리 생성
4. `Calc3Visitor.visit(tree)`로 해석 실행

`Calc3Visitor`는 `CalcVisitor`를 상속해 Calc2 동작을 재사용하고, Calc3에서 필요한 입출력 문장만 확장한다.

## 4. I/O 정책

### `read()`
- `visitReadAssign`에서 stdin 입력을 읽어 변수에 저장
- EOF, `None`, 공백 문자열, 비정수 입력은 모두 `0`으로 처리

### `write(expr)`
- 수식을 계산한 값을 stdout으로 출력
- 동시에 `outputs` 버퍼에도 값을 누적해 테스트 검증에 사용

## 5. 메모리/평가 규칙
- 변수 저장소는 전역 딕셔너리(`memory`)를 사용
- 미정의 변수 참조 시 기본값 `0`으로 자동 초기화
- 조건/사칙연산은 부모 Visitor 구현(`visitCond`, `visitMulDiv`, `visitAddSub`)을 통해 처리
- 프로그램 실행 결과는 최종 메모리 사본(`dict(self.memory)`)으로 반환

## 6. 테스트 상태
`test_calc3.py`에는 파서 스모크 테스트와 Visitor 동작 테스트가 준비되어 있다.

- 파서: 기본 대입, `read/write/if-else` 파싱
- Visitor: 기본 실행, 음수 입력 분기, 비정수 입력의 `0` 처리

현재 환경에서는 ANTLR Python runtime/import가 준비되지 않아 테스트가 skip 상태로 실행된다.
