grammar CalcPlus;

/*
 * Calc-3 문법 명세
 * 프로그램은 1개 이상의 문장(stmt)으로 구성됩니다.
 */
calc3
    : stmt+ EOF
    ;

/*
 * 문장(stmt)
 * - 변수 할당
 * - read() 입력 후 변수 저장
 * - if-else 분기
 * - write(expr) 출력
 */
stmt
    : VAR '=' expr ';'                      # ExprAssign
    | VAR '=' 'read' '(' ')' ';'            # ReadAssign
    | 'if' '(' cond ')' thenBlock=block
      ('else' elseBlock=block)?             # IfElse
    | 'write' '(' expr ')' ';'              # Write
    ;

/*
 * 조건식(cond): 두 수식을 비교 연산자로 비교
 */
cond
    : expr ('=='|'!='|'>'|'>='|'<'|'<=') expr
    ;

/*
 * 블록(block): 중괄호 내부 문장 0개 이상
 */
block
    : '{' stmt* '}'
    ;

/*
 * 수식(expr): 사칙연산, 변수, 정수, 괄호
 */
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
