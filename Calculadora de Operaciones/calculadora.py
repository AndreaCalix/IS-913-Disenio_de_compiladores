
import ply.lex as lex
import ply.yacc as yacc
import sys
import re

#contiene 3 partes un lexer, una analizador y un generador de codigo
#lo primero es crear los tokens, para poder saber cuales con validos y cuales no
# creamos una lista para agregar algunos tokens

tokens = [
    'INT', #enteros
    'FLOAT' #decimales
    'NOMBRES'#cadenas
    'SUMA',
    'MENOS',
    'DIVISION',
    'MULTIPLICACION',
    'ASIGNACION',
    'DPARENTESIS', #parentesis derecha 
    'IPARENTESIS', #parentesis izquierda
]
#DEBEN HABER MAS OPERADORES PERO POR MOTIVO DE PRUEBA ESTAN HECHOS SEGUN VIDEO
#La lista de tokens sera lo que nuestra gramatica utilizara para determinar si la regla gramatical es correcta o no

T_SUMA = r'\+' #estamos indicando que se reconoza un signo +
T_MENOS = r'\-' #estamos indicando que se reconoza un signo -
T_MULTIPLICACION = r'\*' #estamos indicando que se reconoza un signo *
T_DIVISION = r'\/' #estamos indicando que se reconoza un signo /
T_ASIGNACION = r'\=' #estamos indicando que se reconoza un signo =
T_DPAREN = r'\(' #parentesis derecha
T_IPAREN = r'\)' #parentesis izquierda
t_ignore = r' ' #identifica los espacios para ignorarlos ej. 2 + 3

#funcion para enteros 
def t_INT(t):
    #estamos conviertiendo el token a un numero para que python pueda realizar operaciones con el 
    r'\d+'
    t.value = int(t.value)
    return t

#funcion para decimales
def  t_FLOAT(t):
    r'\d+\.\d+'   #identifica cualquier numero seguido de un punto
    t.value = float(t.value)
    return t

#funcion para identificar nombres
def t_NOMBRES(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #cualquier caracter entre mayusculas y minusculas
    t.type = 'NOMBRES'
    return t

#detectar errores en idenificacion de tokens
def t_error(t):
    print('Caracter no valido !!!')
    t.lexer.skip(1) #saltamos un token hacia adelante

#ignorar saltos de linea
def t_ignore_linea(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
lexer = lex.lex()

## ------------ ejecucion de prueba ----------
lexer.input("1+2")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

