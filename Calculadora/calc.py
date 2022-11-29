import ply.lex as lex
import ply.yacc as yacc
import sys 

##########################  A. LEXICO   ############################

#TOKENS
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'PLEFT',
    'PRIGHT',
    'CLEFT',
    'CRIGHT'
]

#EXPRESIONES REGULARES
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
T_ignore =r' '
t_PLEFT = r'\('
t_PRIGHT = r'\)'
t_CLEFT = r'\['
t_CRIGHT = r'\]'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int (t.value)
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z+_0-9]*'
    t.type= 'NAME'
    return t

def t_error(t):
    print ("Caracteres incorrectos")
    t.lexer.skip(1)

##########################  A. SINTACTICO   ############################

lexer=lex.lex()

precedence =(
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)

def p_calc(p): #calculo es una expresion o asignacion de variable 
    '''
    calc : expression
         | var_assign
         | empty
    '''
    print(run(p[1]))

def p_var_assign(p): #asignacion de variable es una cadena  seguido del '=' mas una expresion
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])

def p_group_expression(p): #expresion es un parentesis/corchete apertura
                            # seguido de una expresion seguido de un parentesis/corchete de cierre
    '''
    expression  : PLEFT expression PRIGHT
                | CLEFT expression CRIGHT
    '''
    p[0] = p[2]

def p_expression(p): #expresion es una expresion mas un operando seguido de una expresion
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''
    p[0]=(p[2], p[1], p[3])

def p_expression_int_float(p): #expresion es un numero entero o un flotante
    '''
    expression : INT
               | FLOAT
    '''
    p[0]=p[1]
   

def p_expression_var(p): #expresion es un identificador
    '''
    expression : NAME
    '''
    p[0]=('var',p[1])

def p_error(p):
    print("Error de sintaxis")

def p_empty(p):
    '''
    empty : 
    '''
    p[0]= None

parser = yacc.yacc()
env = {}

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Se encontro una variable no declarada'
            return env[p[1]]

    else:
        return p

while True:
    try:
        s= input('>> ')
    except EOFError:
        break
    parser.parse(s)


