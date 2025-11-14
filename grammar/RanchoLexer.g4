lexer grammar RanchoLexer;

// Keywords
LET: 'let';
MUT: 'mut';
FN: 'fn';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
IN: 'in';
BREAK: 'break';
CONTINUE: 'continue';
MATCH: 'match';
STRUCT: 'struct';
ENUM: 'enum';
IMPL: 'impl';
CONST: 'const';
IMPORT: 'import';
AS: 'as';
TRUE: 'true';
FALSE: 'false';
NULL: 'null';

// Operators and punctuation
ARROW: '->';
DOUBLE_COLON: '::';
SPREAD: '...';
RANGE_INCLUSIVE: '..=';
RANGE_EXCLUSIVE: '..';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
STAR_ASSIGN: '*=';
SLASH_ASSIGN: '/=';
PERCENT_ASSIGN: '%=';
AND_ASSIGN: '&=';
OR_ASSIGN: '|=';
XOR_ASSIGN: '^=';
LSHIFT_ASSIGN: '<<=';
RSHIFT_ASSIGN: '>>=';
INCREMENT: '++';
DECREMENT: '--';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
LSHIFT: '<<';
RSHIFT: '>>';
AND_AND: '&&';
OR_OR: '||';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
PERCENT: '%';
ASSIGN: '=';
LESS: '<';
GREATER: '>';
AND: '&';
OR: '|';
XOR: '^';
NOT: '!';
TILDE: '~';
QUESTION: '?';
COLON: ':';
SEMICOLON: ';';
COMMA: ',';
DOT: '.';
AT: '@';
HASH: '#';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';

// Literals
IDENTIFIER: IDENT_START IDENT_CONT*;
INTEGER_LITERAL: DEC_DIGIT+;
HEX_LITERAL: '0' [xX] HEX_DIGIT+;
OCT_LITERAL: '0' [oO] OCT_DIGIT+;
BIN_LITERAL: '0' [bB] BIN_DIGIT+;
FLOAT_LITERAL
  : DEC_DIGIT+ '.' DEC_DIGIT* EXPONENT?
  | '.' DEC_DIGIT+ EXPONENT?
  | DEC_DIGIT+ EXPONENT
  ;
STRING_LITERAL: '"' (ESC_SEQ | ~["\\\r\n])* '"';
CHAR_LITERAL: '\'' (ESC_SEQ | ~['\\\r\n]) '\'';

// Trivia
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

fragment IDENT_START: [a-zA-Z_];
fragment IDENT_CONT: IDENT_START | [0-9];
fragment DEC_DIGIT: [0-9];
fragment HEX_DIGIT: [0-9a-fA-F];
fragment OCT_DIGIT: [0-7];
fragment BIN_DIGIT: [01];
fragment EXPONENT: [eE] [+\-]? DEC_DIGIT+;
fragment ESC_SEQ
  : '\\' [btnr"\'\\]
  | '\\u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
  ;
