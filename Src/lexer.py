import enum

class TokenType(enum.Enum):
    KEYWORD        = 'KEYWORD'
    IDENTIFIER     = 'IDENTIFIER'
    INT_LITERAL    = 'INT_LITERAL'
    FLOAT_LITERAL  = 'FLOAT_LITERAL'
    STRING_LITERAL = 'STRING_LITERAL'
    OPERATOR       = 'OPERATOR'
    PUNCTUATION    = 'PUNCTUATION'
    EOF            = 'EOF'

class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    def __repr__(self):
        return f"Token({self.type.name:15}, {repr(self.value):15}, Line: {self.line}, Col: {self.column})"

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.keywords = {'int', 'float', 'bool', 'string', 'if', 'else', 'while', 'return', 'print'}
        self.two_char_ops = {'==', '!=', '<=', '>='}

    def error(self, message):
        raise SyntaxError(f"Lexical error: {message} at line {self.line}, column {self.column}")

    def advance(self):
        if self.position < len(self.source):
            if self.source[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1

    def peek(self, offset=0):
        pos = self.position + offset
        return self.source[pos] if pos < len(self.source) else None

    def tokenize(self):
        tokens = []
        while self.position < len(self.source):
            ch = self.peek()
            if ch.isspace():
                self.advance()
                continue
            if ch == '/' and self.peek(1) == '/':
                while self.peek() and self.peek() != '\n':
                    self.advance()
                continue
            if ch.isalpha() or ch == '_':
                start_col = self.column
                val = ''
                while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
                    val += self.peek()
                    self.advance()
                tokens.append(Token(TokenType.KEYWORD if val in self.keywords else TokenType.IDENTIFIER, val, self.line, start_col))
                continue
            if ch.isdigit():
                start_col = self.column
                val = ''
                has_dot = False
                while self.peek() and (self.peek().isdigit() or (self.peek() == '.' and not has_dot)):
                    if self.peek() == '.': has_dot = True
                    val += self.peek()
                    self.advance()
                tokens.append(Token(TokenType.FLOAT_LITERAL if has_dot else TokenType.INT_LITERAL, val, self.line, start_col))
                continue
            if ch == '"':
                start_col = self.column
                val = ''
                self.advance()
                while self.peek() and self.peek() != '"':
                    val += self.peek()
                    self.advance()
                self.advance()
                tokens.append(Token(TokenType.STRING_LITERAL, val, self.line, start_col))
                continue
            next_two = ch + (self.peek(1) or '')
            if next_two in self.two_char_ops:
                start_col = self.column
                tokens.append(Token(TokenType.OPERATOR, next_two, self.line, start_col))
                self.advance(); self.advance()
                continue
            if ch in "+-*/=<>;,(){}":
                start_col = self.column
                tokens.append(Token(TokenType.OPERATOR if ch in "+-*/=" else TokenType.PUNCTUATION, ch, self.line, start_col))
                self.advance()
                continue
            self.error(f"Unexpected character '{ch}'")
        tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return tokens
