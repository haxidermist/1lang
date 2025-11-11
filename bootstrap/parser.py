"""
Parser for the 1 programming language bootstrap compiler.
Converts tokens into an Abstract Syntax Tree (AST).
"""

from dataclasses import dataclass, field
from typing import List, Optional, Union, Any
from enum import Enum, auto
from lexer import Token, TokenType, SourceLocation


class ASTNodeType(Enum):
    """Types of AST nodes"""
    # Program structure
    PROGRAM = auto()
    FUNCTION = auto()
    TYPE_DEF = auto()
    MODULE = auto()

    # Declarations
    PARAMETER = auto()
    TYPE_ANNOTATION = auto()
    CONSTRAINT = auto()
    REQUIREMENT = auto()

    # Statements
    BLOCK = auto()
    RETURN = auto()
    IF = auto()
    LOOP = auto()
    WHILE = auto()
    FOR = auto()
    MATCH = auto()
    MATCH_CASE = auto()
    ENSURE = auto()
    ASSIGNMENT = auto()
    EXPRESSION_STMT = auto()
    BREAK = auto()
    CONTINUE = auto()

    # Expressions
    BINARY_OP = auto()
    UNARY_OP = auto()
    CALL = auto()
    INDEX = auto()
    MEMBER = auto()
    LITERAL = auto()
    IDENTIFIER = auto()
    LIST_LITERAL = auto()
    MAP_LITERAL = auto()
    TUPLE_LITERAL = auto()
    LAMBDA = auto()


@dataclass
class ASTNode:
    """Base class for AST nodes"""
    node_type: ASTNodeType
    location: SourceLocation
    metadata: dict = field(default_factory=dict)


@dataclass
class Program(ASTNode):
    """Root program node"""
    declarations: List[ASTNode] = field(default_factory=list)

    def __init__(self, location: SourceLocation):
        super().__init__(ASTNodeType.PROGRAM, location)
        self.declarations = []


class Parameter(ASTNode):
    """Function parameter"""
    def __init__(self, location: SourceLocation, name: str):
        super().__init__(ASTNodeType.PARAMETER, location)
        self.name = name
        self.type_annotation: Optional['TypeAnnotation'] = None
        self.constraint: Optional['Constraint'] = None


class TypeAnnotation(ASTNode):
    """Type annotation"""
    def __init__(self, location: SourceLocation, name: str):
        super().__init__(ASTNodeType.TYPE_ANNOTATION, location)
        self.name = name
        self.type_args: List['TypeAnnotation'] = []


class Constraint(ASTNode):
    """Where clause constraint"""
    def __init__(self, location: SourceLocation, expression: ASTNode):
        super().__init__(ASTNodeType.CONSTRAINT, location)
        self.expression = expression


class Requirement(ASTNode):
    """Function requirement"""
    def __init__(self, location: SourceLocation, description: str):
        super().__init__(ASTNodeType.REQUIREMENT, location)
        self.description = description


class Function(ASTNode):
    """Function declaration"""
    def __init__(self, location: SourceLocation, name: str):
        super().__init__(ASTNodeType.FUNCTION, location)
        self.name = name
        self.inputs: List[Parameter] = []
        self.outputs: List[Parameter] = []
        self.requirements: List[Requirement] = []
        self.body: Optional['Block'] = None


class Block(ASTNode):
    """Block of statements"""
    def __init__(self, location: SourceLocation):
        super().__init__(ASTNodeType.BLOCK, location)
        self.statements: List[ASTNode] = []


class Return(ASTNode):
    """Return statement"""
    def __init__(self, location: SourceLocation, value: Optional[ASTNode] = None):
        super().__init__(ASTNodeType.RETURN, location)
        self.value = value


class If(ASTNode):
    """If statement"""
    def __init__(self, location: SourceLocation, condition: ASTNode, then_block: Block):
        super().__init__(ASTNodeType.IF, location)
        self.condition = condition
        self.then_block = then_block
        self.else_block: Optional[Block] = None


class While(ASTNode):
    """While loop"""
    def __init__(self, location: SourceLocation, condition: ASTNode, body: Block):
        super().__init__(ASTNodeType.WHILE, location)
        self.condition = condition
        self.body = body


class Ensure(ASTNode):
    """Ensure/otherwise statement"""
    def __init__(self, location: SourceLocation, condition: ASTNode, then_block: Block):
        super().__init__(ASTNodeType.ENSURE, location)
        self.condition = condition
        self.then_block = then_block
        self.else_block: Optional[Block] = None


class Assignment(ASTNode):
    """Assignment statement"""
    def __init__(self, location: SourceLocation, target: ASTNode, value: ASTNode, operator: str = "="):
        super().__init__(ASTNodeType.ASSIGNMENT, location)
        self.target = target
        self.value = value
        self.operator = operator


class BinaryOp(ASTNode):
    """Binary operation"""
    def __init__(self, location: SourceLocation, left: ASTNode, operator: str, right: ASTNode):
        super().__init__(ASTNodeType.BINARY_OP, location)
        self.left = left
        self.operator = operator
        self.right = right


class UnaryOp(ASTNode):
    """Unary operation"""
    def __init__(self, location: SourceLocation, operator: str, operand: ASTNode):
        super().__init__(ASTNodeType.UNARY_OP, location)
        self.operator = operator
        self.operand = operand


class Call(ASTNode):
    """Function call"""
    def __init__(self, location: SourceLocation, function: ASTNode):
        super().__init__(ASTNodeType.CALL, location)
        self.function = function
        self.arguments: List[ASTNode] = []


class Member(ASTNode):
    """Member access (obj.member)"""
    def __init__(self, location: SourceLocation, object: ASTNode, member: str):
        super().__init__(ASTNodeType.MEMBER, location)
        self.object = object
        self.member = member


class Index(ASTNode):
    """Index access (obj[index])"""
    def __init__(self, location: SourceLocation, object: ASTNode, index: ASTNode):
        super().__init__(ASTNodeType.INDEX, location)
        self.object = object
        self.index = index


class Literal(ASTNode):
    """Literal value"""
    def __init__(self, location: SourceLocation, value: Any):
        super().__init__(ASTNodeType.LITERAL, location)
        self.value = value


class Identifier(ASTNode):
    """Identifier"""
    def __init__(self, location: SourceLocation, name: str):
        super().__init__(ASTNodeType.IDENTIFIER, location)
        self.name = name


class ListLiteral(ASTNode):
    """List literal [a, b, c]"""
    def __init__(self, location: SourceLocation):
        super().__init__(ASTNodeType.LIST_LITERAL, location)
        self.elements: List[ASTNode] = []


class ParseError(Exception):
    """Parsing error"""
    def __init__(self, message: str, location: SourceLocation):
        self.message = message
        self.location = location
        super().__init__(f"{location}: {message}")


class Parser:
    """Parses tokens into AST"""

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def is_at_end(self) -> bool:
        """Check if at end of tokens"""
        return self.peek().type == TokenType.EOF

    def peek(self, offset: int = 0) -> Token:
        """Look ahead at token"""
        pos = self.current + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]  # Return EOF
        return self.tokens[pos]

    def previous(self) -> Token:
        """Get previous token"""
        return self.tokens[self.current - 1]

    def advance(self) -> Token:
        """Consume current token"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def check(self, token_type: TokenType) -> bool:
        """Check if current token matches type"""
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def match(self, *token_types: TokenType) -> bool:
        """Check and consume if token matches any type"""
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type: TokenType, message: str) -> Token:
        """Consume token or error"""
        if self.check(token_type):
            return self.advance()
        raise ParseError(message, self.peek().location)

    def skip_newlines(self):
        """Skip newline tokens"""
        while self.match(TokenType.NEWLINE):
            pass

    def error(self, message: str) -> ParseError:
        """Create parse error at current location"""
        return ParseError(message, self.peek().location)

    def parse(self) -> Program:
        """Parse entire program"""
        program = Program(SourceLocation("<program>", 1, 1))

        self.skip_newlines()

        while not self.is_at_end():
            decl = self.declaration()
            if decl:
                program.declarations.append(decl)
            self.skip_newlines()

        return program

    def declaration(self) -> Optional[ASTNode]:
        """Parse top-level declaration"""
        if self.match(TokenType.FUNCTION):
            return self.function_declaration()

        # For now, only support function declarations in bootstrap
        raise self.error(f"Unexpected token: {self.peek().lexeme}")

    def function_declaration(self) -> Function:
        """Parse function declaration"""
        location = self.previous().location

        name_token = self.consume(TokenType.IDENTIFIER, "Expected function name")
        function = Function(location, name_token.lexeme)

        self.consume(TokenType.COLON, "Expected ':' after function name")
        self.skip_newlines()

        # Parse inputs
        if self.match(TokenType.INPUTS):
            self.consume(TokenType.COLON, "Expected ':' after 'inputs'")
            self.skip_newlines()
            function.inputs = self.parameter_list()
            self.skip_newlines()

        # Parse outputs
        if self.match(TokenType.OUTPUTS):
            self.consume(TokenType.COLON, "Expected ':' after 'outputs'")
            self.skip_newlines()
            function.outputs = self.parameter_list()
            self.skip_newlines()

        # Parse requirements (optional for bootstrap)
        if self.match(TokenType.REQUIREMENTS):
            self.consume(TokenType.COLON, "Expected ':' after 'requirements'")
            self.skip_newlines()
            function.requirements = self.requirement_list()
            self.skip_newlines()

        # Parse implementation
        self.consume(TokenType.IMPLEMENTATION, "Expected 'implementation'")
        self.consume(TokenType.COLON, "Expected ':' after 'implementation'")
        self.skip_newlines()

        function.body = self.block()

        return function

    def parameter_list(self) -> List[Parameter]:
        """Parse parameter list"""
        params = []

        while not self.check(TokenType.OUTPUTS) and \
              not self.check(TokenType.REQUIREMENTS) and \
              not self.check(TokenType.IMPLEMENTATION) and \
              not self.is_at_end():

            if self.check(TokenType.NEWLINE):
                self.skip_newlines()
                if not self.check(TokenType.IDENTIFIER):
                    break

            param = self.parameter()
            params.append(param)

            if not self.match(TokenType.NEWLINE):
                break

        return params

    def parameter(self) -> Parameter:
        """Parse single parameter"""
        name_token = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
        param = Parameter(name_token.location, name_token.lexeme)

        # Parse type annotation
        if self.match(TokenType.COLON):
            param.type_annotation = self.type_annotation()

        return param

    def type_annotation(self) -> TypeAnnotation:
        """Parse type annotation"""
        name_token = self.consume(TokenType.IDENTIFIER, "Expected type name")
        type_ann = TypeAnnotation(name_token.location, name_token.lexeme)

        # Parse generic type arguments
        if self.match(TokenType.LT):
            while True:
                type_ann.type_args.append(self.type_annotation())
                if not self.match(TokenType.COMMA):
                    break
            self.consume(TokenType.GT, "Expected '>' after type arguments")

        # Parse where constraint
        # (simplified for bootstrap - just skip for now)
        if self.check(TokenType.WHERE):
            # Skip where clause in bootstrap version
            pass

        return type_ann

    def requirement_list(self) -> List[Requirement]:
        """Parse requirement list"""
        requirements = []

        while not self.check(TokenType.IMPLEMENTATION) and not self.is_at_end():
            if self.check(TokenType.NEWLINE):
                self.skip_newlines()
                if not self.check(TokenType.MINUS):
                    break

            if self.match(TokenType.MINUS):
                # Read requirement description (simplified)
                # Just consume until newline for now
                desc_tokens = []
                while not self.check(TokenType.NEWLINE) and not self.is_at_end():
                    desc_tokens.append(self.advance().lexeme)

                desc = " ".join(desc_tokens)
                req = Requirement(self.previous().location, desc)
                requirements.append(req)

        return requirements

    def block(self) -> Block:
        """Parse block of statements"""
        location = self.peek().location
        block = Block(location)

        # Check for explicit brace-delimited block
        if self.match(TokenType.LBRACE):
            # Brace-delimited block - parse until RBRACE
            while not self.is_at_end():
                self.skip_newlines()

                if self.check(TokenType.RBRACE):
                    break

                stmt = self.statement()
                if stmt:
                    block.statements.append(stmt)

            self.consume(TokenType.RBRACE, "Expected '}' after block")
            return block

        # Indentation-based block (original logic)
        while not self.is_at_end():
            self.skip_newlines()

            if self.is_at_end():
                break

            # Stop at top-level keywords (FUNCTION starts a new declaration)
            if self.check(TokenType.FUNCTION):
                break

            # Check if we're at a keyword that ends this block
            # ELSE and OTHERWISE should end the block when they appear
            if self.check(TokenType.ELSE) or self.check(TokenType.OTHERWISE):
                break

            stmt = self.statement()
            if stmt:
                block.statements.append(stmt)

        return block

    def statement(self) -> Optional[ASTNode]:
        """Parse statement"""
        self.skip_newlines()

        if self.match(TokenType.RETURN):
            return self.return_statement()

        if self.match(TokenType.IF):
            return self.if_statement()

        if self.match(TokenType.WHILE):
            return self.while_statement()

        if self.match(TokenType.ENSURE):
            return self.ensure_statement()

        if self.match(TokenType.BREAK):
            return ASTNode(ASTNodeType.BREAK, self.previous().location)

        if self.match(TokenType.CONTINUE):
            return ASTNode(ASTNodeType.CONTINUE, self.previous().location)

        # Try assignment or expression
        return self.assignment_or_expression()

    def return_statement(self) -> Return:
        """Parse return statement"""
        location = self.previous().location

        value = None
        if not self.check(TokenType.NEWLINE) and not self.is_at_end():
            value = self.expression()

        return Return(location, value)

    def if_statement(self) -> If:
        """Parse if statement"""
        location = self.previous().location

        condition = self.expression()
        self.consume(TokenType.COLON, "Expected ':' after if condition")
        self.skip_newlines()

        then_block = self.block()

        if_stmt = If(location, condition, then_block)

        if self.match(TokenType.ELSE):
            self.consume(TokenType.COLON, "Expected ':' after else")
            self.skip_newlines()
            if_stmt.else_block = self.block()

        return if_stmt

    def while_statement(self) -> While:
        """Parse while loop"""
        location = self.previous().location

        condition = self.expression()
        self.consume(TokenType.COLON, "Expected ':' after while condition")
        self.skip_newlines()

        body = self.block()

        return While(location, condition, body)

    def ensure_statement(self) -> Ensure:
        """Parse ensure/otherwise statement"""
        location = self.previous().location

        condition = self.expression()
        self.consume(TokenType.COLON, "Expected ':' after ensure condition")
        self.skip_newlines()

        then_block = self.block()

        ensure_stmt = Ensure(location, condition, then_block)

        self.skip_newlines()
        if self.match(TokenType.OTHERWISE):
            self.consume(TokenType.COLON, "Expected ':' after otherwise")
            self.skip_newlines()
            ensure_stmt.else_block = self.block()

        return ensure_stmt

    def assignment_or_expression(self) -> ASTNode:
        """Parse assignment or expression statement"""
        expr = self.expression()

        # Check for assignment operators
        if self.match(TokenType.ASSIGN, TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN,
                     TokenType.STAR_ASSIGN, TokenType.SLASH_ASSIGN):
            operator = self.previous().lexeme
            value = self.expression()
            return Assignment(expr.location, expr, value, operator)

        return expr

    def expression(self) -> ASTNode:
        """Parse expression"""
        return self.or_expression()

    def or_expression(self) -> ASTNode:
        """Parse or expression"""
        left = self.and_expression()

        while self.match(TokenType.OR):
            operator = self.previous().lexeme
            right = self.and_expression()
            left = BinaryOp(left.location, left, operator, right)

        return left

    def and_expression(self) -> ASTNode:
        """Parse and expression"""
        left = self.equality()

        while self.match(TokenType.AND):
            operator = self.previous().lexeme
            right = self.equality()
            left = BinaryOp(left.location, left, operator, right)

        return left

    def equality(self) -> ASTNode:
        """Parse equality expression"""
        left = self.comparison()

        while self.match(TokenType.EQ, TokenType.NE):
            operator = self.previous().lexeme
            right = self.comparison()
            left = BinaryOp(left.location, left, operator, right)

        return left

    def comparison(self) -> ASTNode:
        """Parse comparison expression"""
        left = self.addition()

        while self.match(TokenType.LT, TokenType.GT, TokenType.LE, TokenType.GE):
            operator = self.previous().lexeme
            right = self.addition()
            left = BinaryOp(left.location, left, operator, right)

        return left

    def addition(self) -> ASTNode:
        """Parse addition expression"""
        left = self.multiplication()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous().lexeme
            right = self.multiplication()
            left = BinaryOp(left.location, left, operator, right)

        return left

    def multiplication(self) -> ASTNode:
        """Parse multiplication expression"""
        left = self.unary()

        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            operator = self.previous().lexeme
            right = self.unary()
            left = BinaryOp(left.location, left, operator, right)

        return left

    def unary(self) -> ASTNode:
        """Parse unary expression"""
        if self.match(TokenType.MINUS, TokenType.NOT, TokenType.TILDE):
            operator = self.previous().lexeme
            operand = self.unary()
            return UnaryOp(self.previous().location, operator, operand)

        return self.postfix()

    def postfix(self) -> ASTNode:
        """Parse postfix expression (calls, member access, indexing)"""
        expr = self.primary()

        while True:
            if self.match(TokenType.LPAREN):
                # Function call
                call = Call(expr.location, expr)

                if not self.check(TokenType.RPAREN):
                    while True:
                        call.arguments.append(self.expression())
                        if not self.match(TokenType.COMMA):
                            break

                self.consume(TokenType.RPAREN, "Expected ')' after arguments")
                expr = call

            elif self.match(TokenType.DOT):
                # Member access
                member_token = self.consume(TokenType.IDENTIFIER, "Expected member name")
                expr = Member(expr.location, expr, member_token.lexeme)

            elif self.match(TokenType.LBRACKET):
                # Index access
                index = self.expression()
                self.consume(TokenType.RBRACKET, "Expected ']' after index")
                expr = Index(expr.location, expr, index)

            else:
                break

        return expr

    def primary(self) -> ASTNode:
        """Parse primary expression"""
        # Literals
        if self.match(TokenType.TRUE, TokenType.FALSE, TokenType.NULL):
            return Literal(self.previous().location, self.previous().literal)

        if self.match(TokenType.INTEGER, TokenType.FLOAT):
            return Literal(self.previous().location, self.previous().literal)

        if self.match(TokenType.STRING):
            return Literal(self.previous().location, self.previous().literal)

        # Identifier
        if self.match(TokenType.IDENTIFIER):
            return Identifier(self.previous().location, self.previous().lexeme)

        # Parenthesized expression
        if self.match(TokenType.LPAREN):
            expr = self.expression()
            self.consume(TokenType.RPAREN, "Expected ')' after expression")
            return expr

        # List literal
        if self.match(TokenType.LBRACKET):
            list_lit = ListLiteral(self.previous().location)

            if not self.check(TokenType.RBRACKET):
                while True:
                    list_lit.elements.append(self.expression())
                    if not self.match(TokenType.COMMA):
                        break

            self.consume(TokenType.RBRACKET, "Expected ']' after list elements")
            return list_lit

        raise self.error(f"Unexpected token: {self.peek().lexeme}")


def parse_file(filename: str) -> Program:
    """Parse a file"""
    from lexer import lex_file
    tokens = lex_file(filename)
    parser = Parser(tokens)
    return parser.parse()


def parse_string(source: str, filename: str = "<input>") -> Program:
    """Parse a string"""
    from lexer import lex_string
    tokens = lex_string(source, filename)
    parser = Parser(tokens)
    return parser.parse()
