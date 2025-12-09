lexer grammar deliverable1_lexer;

EQ: '=';
VAR: [a-zA-Z_]+[0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
CHAR: '"'([0-9]|[a-zA-Z]|' ')+'"' |
    '\''([0-9]|[a-zA-Z]|' ')+'\'';
BOOL: 'True' | 'False';

//OP: '+' | '-' | '/' | '*';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

REMAINDER: '%';
WS: [\t\n\r ]+ -> skip;
ARRAY: '['(INT(', 'INT)*|
    CHAR(', 'CHAR)*|
    FLOAT(', 'FLOAT)*)']';
LPAREN: '(';    
RPAREN: ')';      