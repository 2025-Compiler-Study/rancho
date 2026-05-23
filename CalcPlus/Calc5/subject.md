## Calc5

이번 단계에서는 언어 스펙은 크게 건드리지 않는다.
기존처럼 Parse Tree를 순회하면서 바로 실행하지 않고, AST를 먼저 구성한 뒤 AST를 실행한다.

```antlrv4
grammar CalcPlus;

program :   (stmt)+ EOF;

stmt    :   'int' VAR (',' VAR)* ';'            # Declare
        |   VAR '=' expr ';'                    # ExprAssign
        |   VAR '=' 'read' '(' ')' ';'          # ReadAssign
        |   'write' '(' expr ')' ';'            # Write
        |   'if' '(' cond ')' thenBlock=block
            ('else' elseBlock=block)?           # IfElse
        |   block                               # StmtBlock
        ;

expr    :   expr ('*'|'/') expr # MulDiv
        |   expr ('+'|'-') expr # AddSub
        |   INT                 # Int
        |   VAR                 # Var
        |   '(' expr ')'        # Parens
        ;

cond    :   expr ('=='|'!='|'>'|'>='|'<'|'<=') expr ;
block   :   '{' (stmt)* '}' ;
```

핵심 변화:

- 진입 문법은 `program`으로 통일한다.
- Parse Tree의 문법용 노드를 의미 중심 AST 노드로 줄인다.
- AST를 사람이 확인할 수 있게 출력한다.
- Parse Tree가 아니라 AST를 실행한다.
- 실행 단계의 변수 관리는 Calc4의 Symbol Table을 재사용한다.
