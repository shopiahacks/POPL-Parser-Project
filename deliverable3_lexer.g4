lexer grammar deliverable2_lexer;

// Comments:
COMMENT: '#' ~[\r\n]* -> skip;
LONGCOMM: '\'\'\''(.)*?'\'\'\'' -> skip;

// Keywords:
IF: 'if';
ELIF: 'elif';
ELSE: 'else';

WHILE: 'while';
FOR: 'for';

IN: 'in';

OR: 'or';
NOT: 'not';
AND: 'and';

BOOL: 'True' | 'False';

// Operators:
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
REMAINDER: '%';

PLUSEQ: '+=';
MINUSEQ: '-=';
MULTEQ: '*=';
DIVEQ: '/=';

EQ: '=';

// Comparative Operators:
LESS: '<';
GRTR: '>';
LESSEQ: '<=';
GRTREQ: '>=';
EQEQ: '==';
NOTEQ: '!=';

// Symbols:
COLON: ':';
LPAR: '(';
RPAR: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';

// Literals:
VAR: ('-')?[a-zA-Z_]+[0-9]*;
INT: ('-')?[0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
STR: '"'([0-9]|[a-zA-Z]|' '|'.'|'\'')*'"'
    | '\''([0-9]|[a-zA-Z]|' '|'.'|'\'')+'\'';


// Whitespace:
INDENT: ('    ')+ | ('\t')+;
NEWLINE: '\r'? '\n';
WS: [ ]+ -> skip;

