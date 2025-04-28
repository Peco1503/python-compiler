grammar BabyDuck;

// Reglas léxicas (tokens)
PROGRAM : 'program';
MAIN : 'main';
END : 'end';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
DO : 'do';
PRINT : 'print';
VOID : 'void';
INT : 'int';
FLOAT : 'float';
VAR : 'var';

// Identificadores
ID : [a-zA-Z][a-zA-Z0-9_]*;

// Constantes numéricas
CTE_INT : [0-9]+;
CTE_FLOAT : [0-9]+ '.' [0-9]+;
CTE_STRING : '"' (~["\r\n])* '"';

// Operadores
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
LT : '<';
GT : '>';
LE : '<=';  // Agregado operador menor o igual
GE : '>=';  // Agregado operador mayor o igual
EQ : '==';  // Agregado operador de igualdad
NE : '!=';
EQUAL : '=';

// Símbolos especiales
SEMICOLON : ';';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
COLON : ':';
COMMA : ',';

// Ignorar espacios en blanco y comentarios
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;

// Reglas sintácticas
// <Programa> -> "program" id ";" <VARS> <FUNCS> "main" <Body> "end"
programa 
    : PROGRAM ID SEMICOLON vars? funcs? MAIN body END
    ;

// <TYPE> -> "int" | "float"
type
    : INT
    | FLOAT
    ;

// <VARS> -> <VAR_DEC_LIST> | ε
// <VAR_DEC_LIST> -> <VAR_DEC> | <VAR_DEC_LIST> <VAR_DEC>
// <VAR_DEC> -> "var" <ID-LIST> ":" <TYPE> ";"
vars
    : VAR varDecList
    ;

varDecList
    : varDec+
    ;

varDec
    : idList COLON type SEMICOLON
    ;

idList
    : ID (COMMA ID)*
    ;

// <Body> -> "{" <STATEMENT_LIST> "}"
body
    : LBRACE statementList? RBRACE
    ;

// <STATEMENT_LIST> -> <STATEMENT> | <STATEMENT_LIST> <STATEMENT> | ε
statementList
    : statement+
    ;

// <STATEMENT> -> <ASSIGN> | <CONDITION> | <CYCLE> | <F_CALL> | <Print>
statement
    : assign
    | condition
    | cycle
    | fcall
    | print
    ;

// <ASSIGN> -> id "=" <EXPRESION> ";"
assign
    : ID EQUAL expresion SEMICOLON
    ;

// <EXPRESION> -> <EXP> | <EXP> ">" <EXP> | <EXP> "<" <EXP> | <EXP> "!=" <EXP>
expresion
    : exp ((GT | LT | NE | LE | GE | EQ) exp)?
    ;

// <EXP> -> <TERMINO> | <TERMINO> "+" <EXP> | <TERMINO> "-" <EXP>
exp
    : termino ((PLUS | MINUS) termino)*
    ;

// <TERMINO> -> <FACTOR> | <FACTOR> "*" <TERMINO> | <FACTOR> "/" <TERMINO>
termino
    : factor ((MULT | DIV) factor)*
    ;

// <FACTOR> -> "(" <EXPRESION> ")" | "+" <FACTOR> | "-" <FACTOR> | id | <CTE>
factor
    : (PLUS | MINUS)? (LPAREN expresion RPAREN | ID | cte)
    ;

// <CTE> -> "cte_int" | "cte_float"
cte
    : CTE_INT
    | CTE_FLOAT
    ;

// <Print> -> "print" "(" <EXP_LIST> ")" ";"
// | "print" "(" <cte_string> ")" ";"
print
    : PRINT LPAREN (CTE_STRING | expresion) RPAREN SEMICOLON
    ;

// <CONDITION> -> "if" "(" <EXPRESION> ")" <Body> ";"
// | "if" "(" <EXPRESION> ")" <Body> "else" <Body> ";"
condition
    : IF LPAREN expresion RPAREN body (ELSE body)? SEMICOLON
    ;

// <CYCLE> -> "while" "(" <EXPRESION> ")" "do" <CUERPO> ";"
// <CUERPO> -> <Body>
cycle
    : WHILE LPAREN expresion RPAREN DO body SEMICOLON
    ;

// <FUNCS> -> <FUNC_LIST> | ε
// <FUNC_LIST> -> <FUNC_DEC> | <FUNC_LIST> <FUNC_DEC>
// <FUNC_DEC> -> "void" id "(" <PARAM_LIST> ")" ";" <VARS> <Body> ";" ";"
funcs
    : funcDec+
    ;

funcDec
    : VOID ID LPAREN paramList? RPAREN SEMICOLON vars? body SEMICOLON
    ;

// <PARAM_LIST> -> <PARAM> | <PARAM_LIST> "," <PARAM> | ε
// <PARAM> -> id ":" <TYPE>
paramList
    : param (COMMA param)*
    ;

param
    : ID COLON type
    ;

// <F_Call> -> id "(" <ARG_LIST> ")" ";"
// <ARG_LIST> -> <EXPRESION> | <ARG_LIST> "," <EXPRESION> | ε
fcall
    : ID LPAREN argList? RPAREN SEMICOLON
    ;

argList
    : expresion (COMMA expresion)*
    ;