parser grammar deliverable2_parser;
options { tokenVocab=deliverable2_lexer; }

start:
    //allows for new lines at top or bottom
    (NEWLINE | statement)* EOF;

// STATEMENTS
statement:
    comment
    | assStatement //assignment
    | condStatement //if/elif/else block
    | loopStatement;

// COMMENTS
comment:
    COMMENT | LONGCOMM;

// ASSIGNMENT STATEMENTS
assStatement:
    VAR EQ expr
    | VAR PLUSEQ expr
    | VAR MINUSEQ expr
    | VAR MULTEQ expr
    | VAR DIVEQ expr;

// EXPRESSIONS
//ensures precedence between operators
expr:
    opExpr;

// LOW PRECEDENCE EXPRESSIONS
opExpr:
    hiOpExpr ((PLUS | MINUS) hiOpExpr)*;
   
// HIGHER PRECEDENCE EXPRESSIONS
hiOpExpr:
    primary ((MULT | DIV | REMAINDER) primary)*;

// PRIMARY (smallest evaluable units)
primary:
    INT
    | FLOAT
    | VAR
    | STR
    | BOOL
    | array
    | NOT primary
    //can use parentheses in if statements & arithmetic
    | LPAR boolExpr RPAR
    | LPAR expr RPAR;

array: LBRACK (INT | FLOAT | STR | BOOL)?
    (COMMA (INT | FLOAT | STR | BOOL))* RBRACK;

// CONDITIONAL STATEMENTS
condStatement:
    ifBlock
    (elifBlock)*
    (elseBlock)?;
    //block forces logic after if/else statements
    //IF stateBlock
    //(ELIF stateBlock)*
    // can have any number of elif statements
    //(ELSE elseBlock)?; // optional else statement

ifBlock:
    IF stateBlock;

elifBlock:
    ELIF stateBlock;

stateBlock:
    boolExpr COLON block;
    
elseBlock:
    ELSE COLON block;

// LOGICAL BLOCK
//must be a new line + an indentation
block:
    NEWLINE INDENT statement //at least 1 statement in block
    (NEWLINE INDENT statement)* //can have multiple statements in block
    (NEWLINE (INDENT)?)*; //allows blank/non-indented lines in block

// BOOLEAN EXPRESSION
//one or more comparisons with optional and/ors
boolExpr:
    comp (conj comp)*;

// COMPARISON
//comparison can be just primary or primary < primary
comp:
    primary (compOp primary)?;

// COMPARISON OPERATORS
compOp:
    LESS | GRTR | LESSEQ
    | GRTREQ | EQEQ | NOTEQ;

// CONJUNCTION OPERATORS
conj:
    AND | OR;

forBlock:
    VAR IN (primary | function) COLON block;

function:
    VAR LPAR arguments RPAR;

loopStatement:
    WHILE stateBlock
    | FOR forBlock;

arguments:
    primary(COMMA primary)*;
    