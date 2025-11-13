//this is where deliverable 1 will be
parser grammar deliverable1_parser;
options { tokenVocab=deliverable1_lexer; }

// program has one or more statements
start: statement+ EOF;

// statements handle regular & compound assignments
statement: VAR EQ expr
    | VAR PLUS EQ expr
    | VAR MINUS EQ expr
    | VAR MULT EQ expr
    | VAR DIV EQ expr;

expr: additiveExpr;

// lowest precedence for addition & subtraction
additiveExpr:
    multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
    ;

// higher precedence (evaluated before add/sub)
multiplicativeExpr:
    primary ((MULT | DIV | REMAINDER) primary)*;

// highest precedence
primary: INT
    | FLOAT
    | VAR
    | CHAR
    | BOOL
    | ARRAY
    | LPAREN expr RPAREN;