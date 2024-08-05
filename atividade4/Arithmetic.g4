grammar Arithmetic;

// Regras do Lexer
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
INT     : [0-9]+ ;
LPAREN  : '(' ;
RPAREN  : ')' ;
VAR     : [a-zA-Z]+ ;
ASSIGN  : '=' ;
WS      : [ \t\r\n]+ -> skip ;

// Regras do Parser
program     : statement+ ;
statement   : assignment | expr ;
assignment  : VAR ASSIGN expr ;
expr        : term ( (PLUS | MINUS) term )* ;
term        : factor ( (MUL | DIV) factor )* ;
factor      : INT | VAR | LPAREN expr RPAREN ;
