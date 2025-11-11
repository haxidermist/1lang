"""
Lexer for the 1 programming language bootstrap compiler.
Converts source code into tokens.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional


class TokenType(Enum):
    # Keywords
    FUNCTION = auto()
    TYPE = auto()
    MODULE = auto()
    IMPORT = auto()
    EXPORT = auto()
    INPUTS = auto()
    OUTPUTS = auto()
    REQUIREMENTS = auto()
    IMPLEMENTATION = auto()
    WHERE = auto()
    INVARIANT = auto()
    ENSURE = auto()
    OTHERWISE = auto()
    MATCH = auto()
    IF = auto()
    ELSE = auto()
    LOOP = auto()
    WHILE = auto()
    FOR = auto()
    IN = auto()
    RETURN = auto()
    BREAK = auto()
    CONTINUE = auto()
    CONST = auto()
    LET = auto()
    VAR = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    SYNTAX = auto()
    WITH_SYNTAX = auto()
    USE_SYNTAX = auto()

    # Identifiers and literals
    IDENTIFIER = auto()
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    POWER = auto()
    EQ = auto()
    NE = auto()
    LT = auto()
    GT = auto()
    LE = auto()
    GE = auto()
    ASSIGN = auto()
    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    STAR_ASSIGN = auto()
    SLASH_ASSIGN = auto()
    AMPERSAND = auto()
    PIPE = auto()
    CARET = auto()
    TILDE = auto()
    LSHIFT = auto()
    RSHIFT = auto()
    ARROW = auto()
    FAT_ARROW = auto()

    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    COLON = auto()
    SEMICOLON = auto()
    DOT = auto()
    QUESTION = auto()

    # Special
    NEWLINE = auto()
    EOF = auto()
    COMMENT = auto()


@dataclass
class SourceLocation:
    """Location in source code"""
    filename: str
    line: int
    column: int

    def __str__(self):
        return f"{self.filename}:{self.line}:{self.column}"


@dataclass
class Token:
    """A lexical token"""
    type: TokenType
    lexeme: str
    location: SourceLocation
    literal: Optional[any] = None

    def __str__(self):
        return f"{self.type.name}({self.lexeme}) at {self.location}"


class LexerError(Exception):
    """Lexical analysis error"""
    def __init__(self, message: str, location: SourceLocation):
        self.message = message
        self.location = location
        super().__init__(f"{location}: {message}")


class Lexer:
    """Tokenizes 1 source code"""

    KEYWORDS = {
        'function': TokenType.FUNCTION,
        'type': TokenType.TYPE,
        'module': TokenType.MODULE,
        'import': TokenType.IMPORT,
        'export': TokenType.EXPORT,
        'inputs': TokenType.INPUTS,
        'outputs': TokenType.OUTPUTS,
        'requirements': TokenType.REQUIREMENTS,
        'implementation': TokenType.IMPLEMENTATION,
        'where': TokenType.WHERE,
        'invariant': TokenType.INVARIANT,
        'ensure': TokenType.ENSURE,
        'otherwise': TokenType.OTHERWISE,
        'match': TokenType.MATCH,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'loop': TokenType.LOOP,
        'while': TokenType.WHILE,
        'for': TokenType.FOR,
        'in': TokenType.IN,
        'return': TokenType.RETURN,
        'break': TokenType.BREAK,
        'continue': TokenType.CONTINUE,
        'const': TokenType.CONST,
        'let': TokenType.LET,
        'var': TokenType.VAR,
        'true': TokenType.TRUE,
        'false': TokenType.FALSE,
        'null': TokenType.NULL,
        'and': TokenType.AND,
        'or': TokenType.OR,
        'not': TokenType.NOT,
        'syntax': TokenType.SYNTAX,
        'with_syntax': TokenType.WITH_SYNTAX,
        'use_syntax': TokenType.USE_SYNTAX,
    }

    def __init__(self, source: str, filename: str = "<input>"):
        self.source = source
        self.filename = filename
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def current_location(self) -> SourceLocation:
        """Get current source location"""
        return SourceLocation(self.filename, self.line, self.column)

    def is_at_end(self) -> bool:
        """Check if at end of source"""
        return self.pos >= len(self.source)

    def peek(self, offset: int = 0) -> Optional[str]:
        """Look ahead at character without consuming"""
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]

    def advance(self) -> str:
        """Consume and return current character"""
        if self.is_at_end():
            return '\0'

        char = self.source[self.pos]
        self.pos += 1

        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def match(self, expected: str) -> bool:
        """Consume character if it matches expected"""
        if self.is_at_end():
            return False
        if self.source[self.pos] != expected:
            return False
        self.advance()
        return True

    def skip_whitespace(self):
        """Skip whitespace except newlines"""
        while not self.is_at_end():
            char = self.peek()
            if char in ' \t\r':
                self.advance()
            else:
                break

    def skip_line_comment(self):
        """Skip // comment"""
        while not self.is_at_end() and self.peek() != '\n':
            self.advance()

    def skip_block_comment(self):
        """Skip /* */ comment"""
        self.advance()  # consume *

        while not self.is_at_end():
            if self.peek() == '*' and self.peek(1) == '/':
                self.advance()  # consume *
                self.advance()  # consume /
                return
            self.advance()

        raise LexerError("Unterminated block comment", self.current_location())

    def tokenize_string(self) -> Token:
        """Tokenize string literal"""
        location = self.current_location()
        self.advance()  # consume opening "

        value = ""
        while not self.is_at_end() and self.peek() != '"':
            if self.peek() == '\\':
                self.advance()
                # Handle escape sequences
                escaped = self.peek()
                if escaped == 'n':
                    value += '\n'
                elif escaped == 't':
                    value += '\t'
                elif escaped == 'r':
                    value += '\r'
                elif escaped == '\\':
                    value += '\\'
                elif escaped == '"':
                    value += '"'
                else:
                    raise LexerError(f"Unknown escape sequence: \\{escaped}", self.current_location())
                self.advance()
            else:
                value += self.advance()

        if self.is_at_end():
            raise LexerError("Unterminated string literal", location)

        self.advance()  # consume closing "

        return Token(TokenType.STRING, f'"{value}"', location, value)

    def tokenize_number(self) -> Token:
        """Tokenize number (integer or float)"""
        location = self.current_location()
        lexeme = ""

        # Read digits
        while not self.is_at_end() and self.peek().isdigit():
            lexeme += self.advance()

        # Check for decimal point
        if not self.is_at_end() and self.peek() == '.' and self.peek(1) and self.peek(1).isdigit():
            lexeme += self.advance()  # consume .

            while not self.is_at_end() and self.peek().isdigit():
                lexeme += self.advance()

            return Token(TokenType.FLOAT, lexeme, location, float(lexeme))

        return Token(TokenType.INTEGER, lexeme, location, int(lexeme))

    def tokenize_identifier(self) -> Token:
        """Tokenize identifier or keyword"""
        location = self.current_location()
        lexeme = ""

        while not self.is_at_end() and (self.peek().isalnum() or self.peek() == '_'):
            lexeme += self.advance()

        # Check if it's a keyword
        token_type = self.KEYWORDS.get(lexeme, TokenType.IDENTIFIER)

        # Set literal value for boolean keywords
        literal = None
        if token_type == TokenType.TRUE:
            literal = True
        elif token_type == TokenType.FALSE:
            literal = False
        elif token_type == TokenType.NULL:
            literal = None

        return Token(token_type, lexeme, location, literal)

    def add_token(self, token_type: TokenType, lexeme: str = None, literal: any = None):
        """Add a token to the list"""
        if lexeme is None:
            lexeme = token_type.name
        token = Token(token_type, lexeme, self.current_location(), literal)
        self.tokens.append(token)

    def tokenize(self) -> List[Token]:
        """Tokenize entire source code"""
        while not self.is_at_end():
            self.skip_whitespace()

            if self.is_at_end():
                break

            location = self.current_location()
            char = self.peek()

            # Comments
            if char == '/' and self.peek(1) == '/':
                self.skip_line_comment()
                continue

            if char == '/' and self.peek(1) == '*':
                self.advance()  # consume /
                self.skip_block_comment()
                continue

            # Newlines (significant in 1)
            if char == '\n':
                self.advance()
                self.tokens.append(Token(TokenType.NEWLINE, '\\n', location))
                continue

            # String literals
            if char == '"':
                self.tokens.append(self.tokenize_string())
                continue

            # Numbers
            if char.isdigit():
                self.tokens.append(self.tokenize_number())
                continue

            # Identifiers and keywords
            if char.isalpha() or char == '_':
                self.tokens.append(self.tokenize_identifier())
                continue

            # Two-character operators
            if char == '=' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.EQ, '==', location))
                continue

            if char == '!' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.NE, '!=', location))
                continue

            if char == '<' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.LE, '<=', location))
                continue

            if char == '>' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.GE, '>=', location))
                continue

            if char == '<' and self.peek(1) == '<':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.LSHIFT, '<<', location))
                continue

            if char == '>' and self.peek(1) == '>':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.RSHIFT, '>>', location))
                continue

            if char == '+' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.PLUS_ASSIGN, '+=', location))
                continue

            if char == '-' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.MINUS_ASSIGN, '-=', location))
                continue

            if char == '*' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.STAR_ASSIGN, '*=', location))
                continue

            if char == '/' and self.peek(1) == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.SLASH_ASSIGN, '/=', location))
                continue

            if char == '-' and self.peek(1) == '>':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.ARROW, '->', location))
                continue

            if char == '=' and self.peek(1) == '>':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.FAT_ARROW, '=>', location))
                continue

            if char == '*' and self.peek(1) == '*':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.POWER, '**', location))
                continue

            # Single-character tokens
            single_char_tokens = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.STAR,
                '/': TokenType.SLASH,
                '%': TokenType.PERCENT,
                '<': TokenType.LT,
                '>': TokenType.GT,
                '=': TokenType.ASSIGN,
                '&': TokenType.AMPERSAND,
                '|': TokenType.PIPE,
                '^': TokenType.CARET,
                '~': TokenType.TILDE,
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                '{': TokenType.LBRACE,
                '}': TokenType.RBRACE,
                '[': TokenType.LBRACKET,
                ']': TokenType.RBRACKET,
                ',': TokenType.COMMA,
                ':': TokenType.COLON,
                ';': TokenType.SEMICOLON,
                '.': TokenType.DOT,
                '?': TokenType.QUESTION,
            }

            if char in single_char_tokens:
                self.advance()
                self.tokens.append(Token(single_char_tokens[char], char, location))
                continue

            # Unknown character
            raise LexerError(f"Unexpected character: '{char}'", location)

        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, '', self.current_location()))

        return self.tokens


def lex_file(filename: str) -> List[Token]:
    """Tokenize a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        source = f.read()

    lexer = Lexer(source, filename)
    return lexer.tokenize()


def lex_string(source: str, filename: str = "<input>") -> List[Token]:
    """Tokenize a string"""
    lexer = Lexer(source, filename)
    return lexer.tokenize()
