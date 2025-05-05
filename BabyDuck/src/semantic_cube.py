# Definiciono de tipos
INT = 0
FLOAT = 1
ERROR = -1

# Defincion de operadores
PLUS = '+'
MINUS = '-'
MULT = '*'
DIV = '/'
LT = '<'
GT = '>'
LE = '<='
GE = '>='
EQ = '=='
NE = '!='
ASSIGN = '='

# Cubo semantico como un diccionario de tres dimensiones: [tipo1][tipo2][operador]
SEMANTIC_CUBE = {
    INT: {
        INT: {
            PLUS: INT,
            MINUS: INT,
            MULT: INT,
            DIV: FLOAT, # Division de enteros da float
            LT: INT, # Las comparaciones devuelven 1 o 0 (falso o verdadero)
            GT: INT,
            LE: INT,
            GE: INT,
            EQ: INT,
            NE: INT,
            ASSIGN: INT # Asignacion de int a int
        },
        FLOAT: {
            PLUS: FLOAT,
            MINUS: FLOAT,
            MULT: FLOAT,
            DIV: FLOAT,
            LT: INT,
            GT: INT,
            LE: INT,
            GE: INT,
            EQ: INT,
            NE: INT,
            ASSIGN: ERROR # No se puede asignar un float a un int sin conversion
        }
    },
    FLOAT: {
        INT: {
            PLUS: FLOAT,
            MINUS: FLOAT,
            MULT: FLOAT,
            DIV: FLOAT,
            LT: INT,
            GT: INT,
            LE: INT,
            GE: INT,
            EQ: INT,
            NE: INT,
            ASSIGN: FLOAT # No se puede asignar un int a un float sin conversion
        },
        FLOAT: {
            PLUS: FLOAT,
            MINUS: FLOAT,
            MULT: FLOAT,
            DIV: FLOAT,
            LT: INT,
            GT: INT,
            LE: INT,
            GE: INT,
            EQ: INT,
            NE: INT,
            ASSIGN: FLOAT # Asignacion de float a float
        }
    }
}

def get_result_type(left_type, right_type, operator):
    """
    Funcion para obtener el tipo de resultante de una operacion
    
    Args: 
        left_type: Tipo del operador izquierdo
        right_type: Tipo del operador derecho
        operator: Operador a evaluar (operador de la operacion)
    Returns:
        Tipo resultante de la operacion o ERROR si no es válida
    """

    try: 
        return SEMANTIC_CUBE[left_type][right_type][operator]
    except KeyError:
        return ERROR
