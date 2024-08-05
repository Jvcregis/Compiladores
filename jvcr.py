import enum
import sys

class Lexer:
    def __init__(self, input):
        self.source = input + '\n' #código-fonte (entrada)
        self.curChar = '' #caractere atual dentro do código-fonte
        self.curPos = -1
        self.nextChar()
        pass

    # Processa o proximo caractere
    def nextChar(self):
        self.curPos = self.curPos + 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]

    # Retorna o caractere seguinte (ainda não lido).
    def peek(self):
        if self.curPos+1 >= len(self.source):
            return '\0'
        else: 
            return self.source[self.curPos+1]

    # Token inválido encontrado, método usado para imprimir mensagem de erro e encerrar.
    def abort(self, message):
        sys.exit("Erro léxico! " + message)
		
    # Pular espaço em branco
    def skipWhitespace(self):
        while self.curChar==' ' or self.curChar=='\n' or self.curChar=='\t' or self.curChar=='\r' or self.curChar=='\f':
            self.nextChar()
		
    # Pular comentários.
    def skipComment(self):
        if self.curChar == '/':
            if self.peek() == '/':
                while self.peek() != '\n' and self.peek() != '\0':
                    self.nextChar()
                self.nextChar() # Pulando o último caracter do comentário
            elif self.peek() == '*':
                while self.curChar != '\0':
                    if self.curChar == '*' and self.peek() == '/':
                        self.nextChar()  # Pula o '*'
                        self.nextChar()  # Pula o '/'
                        break
                    else:
                        self.nextChar()
            else:
                self.abort("O caracter '/' foi utilizado de forma inválida.")

    # Return o próximo token --> Implementar esta função e as funções de skip acima 
    # Atualmente esta função retorna um token de tipo TEST para cada caractere do programa até alcançar EOF
    def getToken(self):
        while True:
            self.skipWhitespace()
            if self.curChar == '/':
                self.skipComment()
                continue  # Após pular o comentário, continua verificando por espaços em branco ou mais comentários
            break  # Sai do loop quando encontrar um caractere que não é espaço em branco ou início de comentário
        token = None
        
        if self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)

        elif self.curChar == '&':
            if self.peek() == '&':
                self.nextChar()
                token = Token("&&", TokenType.AND)
            else:
                self.abort("O caracter '&' foi utilizado de forma inválida.")

        elif self.curChar == '<':
            if self.peek() == '=':
                self.nextChar()
                token = Token('<=', TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)

        elif self.curChar == '>':
            if self.peek() == '=':
                self.nextChar()
                token = Token('>=', TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)

        elif self.curChar == '=':
            if self.peek() == '=':
                self.nextChar()
                token = Token("==", TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == '!':
            if self.peek() == '=':
                self.nextChar()
                token = Token("!=", TokenType.NOTEQ)
            else:
                token = Token("=", TokenType.EQ)

        elif self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)

        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.MULT)

        elif self.curChar == ';':
            token = Token(self.curChar, TokenType.SEMICOLON)

        elif self.curChar == '.':
            token = Token(self.curChar, TokenType.DOT)

        elif self.curChar == ',':
            token = Token(self.curChar, TokenType.COMMA)

        elif self.curChar == '(':
            token = Token(self.curChar, TokenType.L_PAREN)

        elif self.curChar == ')':
            token = Token(self.curChar, TokenType.R_PAREN)

        elif self.curChar == '{':
            token = Token(self.curChar, TokenType.L_BRACK)
        
        elif self.curChar == '}':
            token = Token(self.curChar, TokenType.R_BRACK)
        
        elif self.curChar == '[':
            token = Token(self.curChar, TokenType.L_SQBRACK)

        elif self.curChar == ']':
            token = Token(self.curChar, TokenType.R_SQBRACK)

        elif self.curChar.isalpha() or self.curChar == '_':
            initial_position = self.curPos
            while self.peek().isalnum() or self.peek() == '_':
                self.nextChar()
            lexema = self.source[initial_position : self.curPos + 1]
            if lexema == 'System' and self.peek() == '.':
                temp = self.source[initial_position : initial_position + 18]
                if temp == 'System.out.println':
                    lexema = 'System_out_println'
                    while self.peek().isalnum() or self.peek() == '.':
                        self.nextChar()
            tipoToken = Token.checkIfKeyword(lexema)
            if tipoToken is None:
                token = Token(lexema, TokenType.IDENT)
            else:
                token = Token(lexema, tipoToken)

        elif self.curChar.isnumeric():
            initial_position = self.curPos
            while self.peek().isnumeric():
                self.nextChar()
            numero = self.source[initial_position : self.curPos + 1]
            token = Token(numero, TokenType.NUMBER)

        elif self.curChar == '"':
            initial_position = self.curPos
            while self.curChar != '"':
                self.nextChar()
                if self.curChar == '\0':
                    self.abort("Arquivo terminou sem a string terminar.")
            string = self.source[initial_position : self.curPos + 1]
            token = Token(string, TokenType.LITERAL)

        else: 
            self.abort(f"Caracter não reconhecido. Caracter: {self.curChar}")
        
        self.nextChar()
        return token

class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText #lexema, a instância específica encontrada
        self.kind = tokenKind # o tipo de token (TokenType) classificado
    
    @staticmethod
    def checkIfKeyword(word):
        for kind in TokenType:
            if kind.name == word.upper() and kind.value > 100 and kind.value < 200:
                return kind
        return None

class TokenType(enum.Enum):
    EOF = -1
    NUMBER = 1 #NUMERO done
    IDENT = 2 #IDENTIFICADOR done
    LITERAL = 3 #STRING "alasdlasdal"
    #PALAVRAS RESERVADAS
    BOOLEAN = 101
    CLASS = 102
    PUBLIC = 103
    EXTENDS = 104
    STATIC = 105
    VOID = 106
    MAIN = 107
    STRING = 108
    INT = 109
    WHILE = 110
    IF = 111
    ELSE = 112
    RETURN = 113
    LENGTH = 114
    TRUE = 115
    FALSE = 116
    THIS = 117
    NEW = 118
    SYSTEM_OUT_PRINTLN = 119
    FOR = 120
    BREAK = 121
    #OPERADORES
    AND = 201   # && done
    LT = 202    # < done
    EQEQ = 203  # == done
    NOTEQ = 204 # != done
    PLUS = 205  # + done
    MINUS = 206 # - done
    MULT = 207  # * done
    NOT = 208   # ! done
    GT = 209    # > done
    GTEQ = 210  # >= done
    LTEQ = 211  # <= done
    #DELIMITADORES
    SEMICOLON = 251   # ; done
    DOT = 252    # . done
    COMMA = 253  # , done
    EQ = 254 # = done
    L_PAREN = 255  # ( done
    R_PAREN = 256  # ) done
    L_BRACK = 257  # { done
    R_BRACK = 258  # } done
    L_SQBRACK = 259  # [ done
    R_SQBRACK = 260  # ] done