# Calc-3 Subject

Calc-3는 Calc-2(수식, 변수, if/else)에 입출력 내장 함수 `read`, `write`를 추가한 단계다.
핵심은 문법 자체보다 **실행기와 I/O 연결(파일 입력 + stdin/stdout)** 이다.

## 목표
1. `read()`와 `write(expr)`를 지원하는 인터프리터를 구현한다.
2. 기존 Calc-2 동작(수식/변수/분기)은 그대로 유지한다.
3. CLI 형태로 소스 파일을 실행할 수 있게 한다.

## 언어 스펙
1. 프로그램은 1개 이상의 문장(`stmt`)으로 구성된다.
2. 변수 할당: `변수 = 수식;`
3. 입력: `변수 = read();`
4. 출력: `write(수식);`
5. 분기: `if (cond) { ... } else { ... }` (`else` 생략 가능)
6. 비교 연산: `==`, `!=`, `<`, `>`, `<=`, `>=`
7. 변수 스코프는 블록 분리 없이 전역 메모리로 처리한다.
8. 미정의 변수는 `0`으로 취급한다.

## 문법(ANTLR4)
```antlrv4
grammar CalcPlus;

calc3
    : stmt+ EOF
    ;

stmt
    : VAR '=' expr ';'                      # ExprAssign
    | VAR '=' 'read' '(' ')' ';'            # ReadAssign
    | 'if' '(' cond ')' thenBlock=block
      ('else' elseBlock=block)?             # IfElse
    | 'write' '(' expr ')' ';'              # Write
    ;

cond
    : expr ('=='|'!='|'>'|'>='|'<'|'<=') expr
    ;

block
    : '{' stmt* '}'
    ;

expr
    : expr ('*'|'/') expr                   # MulDiv
    | expr ('+'|'-') expr                   # AddSub
    | INT                                   # Int
    | VAR                                   # Var
    | '(' expr ')'                          # Parens
    ;

WS  : [ \t\r\n]+ -> skip;
INT : [0-9]+;
VAR : [A-Za-z]+;
```

## 구현 과제

### 과제 1: I/O 중심 최소 실행기
1. 고정값 출력 프로그램을 실행할 수 있어야 한다. (`write(42);`)
2. Echo 프로그램을 실행할 수 있어야 한다. (`a = read(); write(a);`)
3. Calc-3 인터프리터를 CLI 스크립트/실행 파일로 제공한다.
4. 실행 예시는 `calc3 sample.cp` 형식을 따른다.
5. `read()` 입력은 stdin에서 받는다.
6. `write()` 출력은 stdout으로 보낸다.
7. `read()` 실패(EOF, 숫자 아님) 시 정책을 정해 일관되게 처리한다.

### 과제 2: Calc-2 기능과 완전 연동
1. 사칙연산/괄호/변수 참조가 I/O와 함께 동작해야 한다.
2. `if/else` 내부에서도 `read`/`write`가 의도대로 실행되어야 한다.
3. 프로그램 종료 후 변수 최종 상태를 확인할 수 있어야 한다.

## 테스트 권장 항목
1. `write(1+2*3);` 결과 확인
2. `a=read(); if (a>0){write(a);} else {write(0);}` 분기 확인
3. 입력 실패 케이스(EOF/비정수) 확인
4. Calc-2 회귀 케이스 확인(입출력 없는 프로그램)
