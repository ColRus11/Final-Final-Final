grammar ColRus;

program: statement* EOF;

statement
    : expressionStmt
    | printStmt
    | defStmt
    | forStmt
    | repeatStmt
    | ifStmt
    | whileStmt
    | mlpStmt
    | kmeansStmt
    | functionCallStmt
    | returnStmt
    | graficarStmt
    ;

expressionStmt: ID (LBRACK expression RBRACK)? EQUALS (expression | functionCall) SEMI;

printStmt: 'muestre' expression (COMMA expression)* SEMI;

defStmt: 'definir' ID LPAREN params? RPAREN block;

forStmt: 'para' ID 'desde' expression 'hasta' expression block;

repeatStmt: 'repetir' ID 'desde' expression 'hasta' expression block;

ifStmt: 'si' expression block ('sino' block)?;

whileStmt: 'mientras' expression block;

mlpStmt
    : ID CREAR_MLP LPAREN expression? RPAREN SEMI
    | ID ENTRENAR_MLP LPAREN expression COMMA expression COMMA expression COMMA expression RPAREN SEMI
    | ID EQUALS ID PREDECIR_MLP LPAREN expression RPAREN SEMI
    | ID PREDECIR_MLP LPAREN expression RPAREN SEMI
    ;

kmeansStmt: ID EQUALS 'kmeans' LPAREN expression COMMA expression RPAREN SEMI;

functionCallStmt: functionCall SEMI;

returnStmt: 'retorne' expression SEMI;

block: LBRACE statement* RBRACE;

params: ID (COMMA ID)*;

expression: relationalExpr;

relationalExpr
    : additiveExpr (('<' | '>' | '<=' | '>=' | '==' | '!=') additiveExpr)?
    ;

additiveExpr
    : multiplicativeExpr (('+' | '-') multiplicativeExpr)*
    ;

multiplicativeExpr
    : powerExpr (('*' | '/' | '%') powerExpr)*
    ;

powerExpr
    : unaryExpr ('^' unaryExpr)*
    ;

unaryExpr
    : (SUB | BANG) unaryExpr
    | primaryExpr
    ;

primaryExpr
    : atom
    | functionCall
    | memberAccess
    ;

atom
    : INT
    | FLOAT
    | STRING
    | ID (LBRACK expression RBRACK)?
    | matrixExpr
    | LPAREN expression RPAREN
    | memberAccess
    ;

memberAccess
    : ID DOT ID (LPAREN args RPAREN)?
    ;

functionCall
    : ID (LPAREN args RPAREN)?
    ;

args
    : expression (COMMA expression)*
    ;

matrixExpr
    : LBRACK matrix RBRACK
    ;

matrix
    : row (COMMA row)*
    | expression (COMMA expression)*
    ;

row
    : LBRACK expression (COMMA expression)* RBRACK
    ;

graficarStmt
    : GRAFANA ID (COMMA ID)* (COMMA STRING)? LPAREN RPAREN SEMI
    ;
    
// Tokens
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
SEMI: ';';
DOT: '.';
EQUALS: '=';
SUB: '-';
ADD: '+';
MUL: '*';
DIV: '/';
MOD: '%';
BANG: '!';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
EQ: '==';
NE: '!=';
CREAR_MLP: 'crear_mlp';
ENTRENAR_MLP: 'entrenar_mlp';
PREDECIR_MLP: 'predecir_mlp';
GRAFANA: 'graficar';
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;