# Calc5 Test Structure

`test_calc5.py`는 완성 구현 테스트가 아니라 시작 스켈레톤의 기준점이다.

현재 테스트가 확인하는 내용은 다음과 같다.

1. ANTLR 생성 파서가 `program()` 진입점으로 기본 프로그램을 파싱한다.
2. AST 노드 데이터 구조가 최소 형태로 생성된다.
3. AST Builder, Printer, Executor는 아직 명시적 스텁이다.
4. Symbol Table은 Calc4 구현을 재사용할 수 있다.

구현을 시작하면 `NotImplementedError`를 기대하는 계약 테스트를 실제 동작 테스트로 바꾸면 된다.
추천 순서는 expression builder, statement builder, printer, executor 순서다.
