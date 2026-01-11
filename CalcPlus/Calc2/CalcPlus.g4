grammar CalcPlus;

/*
 * Calc-2 문법 명세
 * 프로그램은 한 개 이상의 문장(stmt)으로 구성됩니다.
 */
program : stmt+ EOF;

/*
 * 문장(stmt)은 변수 할당문 또는 if-else 분기문으로 구성됩니다.
 * # 뒤의 이름은 생성되는 Visitor/Listener에서 사용할 Label입니다.
 */
stmt
    : VAR '=' expr ';'                      # ExprAssign
    | 'if' '(' cond ')' thenBlock=block
      ('else' elseBlock=block)?             # IfElse
    ;

/*
 * 조건(cond)은 if문의 조건부에 사용되며, 두 수식(expr)을 비교 연산자로 비교합니다.
 */
cond
    : expr ('=='|'!='|'>'|'>='|'<'|'<=') expr
    ;

/*
 * 블록(block)은 '{'와 '}' 사이에 0개 이상의 문장(stmt)을 포함할 수 있습니다.
 */
block
    : '{' stmt* '}'
    ;

/*
 * 수식(expr)은 재귀적으로 정의되며, 사칙연산, 정수, 변수, 괄호를 포함합니다.
 * 재귀 규칙의 순서에 따라 곱셈/나눗셈이 덧셈/뺄셈보다 우선순위가 높습니다.
 */
expr
    : expr ('*'|'/') expr                   # MulDiv
    | expr ('+'|'-') expr                   # AddSub
    | INT                                   # Int
    | VAR                                   # Var
    | '(' expr ')'                          # Parens
    ;

/*
 * Lexer 규칙들
 */
WS:   [ \t\r\n]+ -> skip; // 공백, 탭, 개행문자는 무시합니다.
INT:  [0-9]+;           // 정수는 0-9 사이의 숫자 1개 이상으로 구성됩니다.
VAR:  [A-Za-z]+;        // 변수는 알파벳 대소문자 1개 이상으로 구성됩니다.