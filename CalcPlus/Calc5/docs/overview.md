# Calc5 Overview

Calc5는 Calc4의 언어 스펙을 유지하면서 실행 구조를 바꾸는 단계다.
Calc4까지는 ANTLR Parse Tree를 Visitor가 바로 실행했지만, Calc5에서는 Parse Tree를 먼저 AST로 변환하고 그 AST를 실행한다.

## 목표

Calc5의 핵심 목표는 다음 네 가지다.

1. 프로그램 진입 규칙을 `program`으로 통일한다.
2. Parse Tree에서 의미 중심 AST를 구성한다.
3. AST 구조를 출력해서 변환 결과를 확인할 수 있게 한다.
4. Parse Tree가 아니라 AST Executor가 프로그램을 실행하게 한다.

## 실행 흐름

```text
source code
    -> ANTLR Lexer / Parser
    -> Parse Tree
    -> AstBuilder
    -> AST
    -> AstPrinter 또는 AstExecutor
```

이 구조로 나누면 문법 분석, 의미 구조 생성, 실행 책임이 분리된다.
다음 단계에서 문법이나 실행 모델이 커져도 Parse Tree 직접 실행보다 확장하기 쉽다.

## Calc4와의 차이

| 구분 | Calc4 | Calc5 |
| --- | --- | --- |
| 진입 규칙 | `calc4` | `program` |
| 실행 방식 | Parse Tree Visitor가 즉시 실행 | AST 생성 후 Executor가 실행 |
| 주요 구현 대상 | Visitor, SymbolTable | AstBuilder, AstPrinter, AstExecutor |
| 변수 관리 | SymbolTable 직접 사용 | Executor에서 SymbolTable 재사용 |
| 디버깅 대상 | Parse Tree / 실행 결과 | AST 출력 + 실행 결과 |

## 문법 요약

Calc5의 언어 문법은 Calc4와 거의 같다.
변수 선언, 대입, `read`, `write`, `if/else`, 블록, 사칙연산, 비교 조건을 사용한다.

```antlrv4
program : (stmt)+ EOF;

stmt    : 'int' VAR (',' VAR)* ';'
        | VAR '=' expr ';'
        | VAR '=' 'read' '(' ')' ';'
        | 'write' '(' expr ')' ';'
        | 'if' '(' cond ')' thenBlock=block ('else' elseBlock=block)?
        | block
        ;
```

중요한 변경점은 문법 기능이 아니라 진입 규칙 이름과 실행 구조다.

## AST 노드 구성

현재 스켈레톤의 AST 노드는 `ast_nodes.py`에 정의되어 있다.

- `Program`: 전체 statement 목록
- `Declare`: 변수 선언
- `Assign`: 변수 대입
- `Write`: 출력 문장
- `Block`: 블록 statement 목록
- `IfElse`: 조건문
- `IntLiteral`: 정수 리터럴
- `VarRef`: 변수 참조
- `ReadCall`: 입력 호출
- `BinaryExpr`: 산술 연산 또는 비교 연산

문법상 `int a, b;`는 하나의 statement지만, AST에서는 `Declare("a")`, `Declare("b")`처럼 나누는 편이 실행하기 쉽다.
괄호는 AST 노드로 남기지 않고 내부 expression의 트리 구조에 반영한다.

## 파일 역할

| 파일 | 역할 |
| --- | --- |
| `CalcPlus.g4` | Calc5 문법, `program` 진입 규칙 정의 |
| `ast_nodes.py` | AST 노드 데이터 구조 |
| `ast_builder.py` | Parse Tree를 AST로 변환하는 Visitor 스텁 |
| `ast_printer.py` | AST 출력기 스텁 |
| `ast_executor.py` | AST 실행기 스텁 |
| `symbol_table.py` | Calc4 방식의 스코프 기반 변수 테이블 |
| `test_calc5.py` | 파서, AST 노드, 스텁 계약 테스트 |
| `docs/implementation-steps.md` | 구현 순서 |
| `docs/problem-explanation.md` | 과제 해설 |
| `docs/test-structure.md` | 테스트 구조 설명 |

## 구현 순서

1. `ast_nodes.py`의 노드 구조를 과제 요구에 맞게 확정한다.
2. `ast_builder.py`에서 `Int`, `Var`, `BinaryExpr` 등 expression 변환부터 구현한다.
3. 선언, 대입, read/write, block, if/else statement 변환을 구현한다.
4. `ast_printer.py`에서 JSON, LISP, 들여쓰기 방식 중 하나로 AST를 출력한다.
5. `ast_executor.py`에서 AST를 순서대로 실행한다.
6. Builder 단계에서 선언 전 사용, 중복 선언 같은 의미 오류 수집 방식을 정한다.

## 현재 상태

현재 Calc5는 구현 시작용 스켈레톤이다.
AST 관련 핵심 메서드는 의도적으로 `NotImplementedError`를 발생시킨다.
테스트도 이 상태를 계약으로 고정해 두었다.

즉, 지금 단계의 목표는 완성된 실행기가 아니라 다음 구현을 시작할 수 있는 구조를 준비하는 것이다.

## 테스트

```bash
python3 -m unittest -v test_calc5.py
```

ANTLR 런타임이 설치되지 않은 환경에서는 파서 관련 테스트가 skip된다.
전체 파서 테스트까지 실행하려면 다음 의존성이 필요하다.

```bash
pip install -r requirements.txt
```

파서를 다시 생성하려면 ANTLR tool과 Java가 필요하다.

```bash
antlr4 -Dlanguage=Python3 -visitor -listener CalcPlus.g4
```
