grammar CalcPlus;
calc0   :   expr EOF ;
expr    :   expr ('*'|'/') expr # MulDiv
        |   expr ('+'|'-') expr # AddSub
        |   INT                 # Int
        |   '(' expr ')'        # Parens
        ;
WS  : [ \t\r\n]+ -> skip;
INT : [0-9]+ ;
