
#constante para los digitos
DIGITS = '0123456789'

# ------------------ Errores ----------------------
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Caracter Ilegal', details)

# --------- posicision -----------
class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)
        
#definir constantes para los diferentes tipos de tokens
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_SUMA = 'SUMA'
TT_RESTA = 'RESTA'
TT_MULT = 'MULT'
TT_DIV = 'DIV'
TT_DPAREN = 'DPAREN'
TT_IPAREN = 'IPAREN'

# ---------------------- crear una clase TOKENS -------------------------------
class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

# ---------------------- crear una clase LEXER -------------------------------
class Lexer:
    def __init__(self, fn, text): #en el metodo de inicializacion debemos tomar el texto que estemos procesando
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text) #realizar un seguimiento de la posicion en donde estamos 
        self.current_char = None #caracter actual
        self.advance()
    
    #metoddo que avanzara al siguiente caracter
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char =  self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    #metodo para la creacion de tokens
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t': #ignorar caracteres con espacios y tabulaciones
                self.advance() #si hay caracteres con espacio o tabulaciones se llama la funcion advance para avanzar a otro caracter
            #identifcar si el caracter actual esta en digitos
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+': #identificar el caracter de suma
                tokens.append(Token(TT_SUMA))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_RESTA))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MULT))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_IPAREN))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_DPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'" )

        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

# ----------- correr -------------
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    return tokens, error

        