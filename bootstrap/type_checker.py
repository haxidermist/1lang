"""
Basic type checker for 1 language bootstrap compiler.
This is a simplified version - no complex constraint solving.
"""

from typing import Dict, Optional, List
from dataclasses import dataclass
from parser import *


class Type:
    """Base type class"""
    pass


@dataclass
class PrimitiveType(Type):
    """Primitive type (Integer, Float, String, Boolean)"""
    name: str

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, PrimitiveType) and self.name == other.name


@dataclass
class FunctionType(Type):
    """Function type"""
    param_types: List[Type]
    return_type: Type

    def __str__(self):
        params = ", ".join(str(t) for t in self.param_types)
        return f"({params}) -> {self.return_type}"


@dataclass
class ListType(Type):
    """List type"""
    element_type: Type

    def __str__(self):
        return f"List<{self.element_type}>"


@dataclass
class VoidType(Type):
    """Void/Unit type"""
    def __str__(self):
        return "Void"


# Built-in types
INTEGER_TYPE = PrimitiveType("Integer")
FLOAT_TYPE = PrimitiveType("Float")
STRING_TYPE = PrimitiveType("String")
BOOLEAN_TYPE = PrimitiveType("Boolean")
VOID_TYPE = VoidType()


class TypeCheckError(Exception):
    """Type checking error"""
    def __init__(self, message: str, location: SourceLocation):
        self.message = message
        self.location = location
        super().__init__(f"{location}: {message}")


class TypeEnvironment:
    """Type environment for tracking variable types"""

    def __init__(self, parent: Optional['TypeEnvironment'] = None):
        self.parent = parent
        self.bindings: Dict[str, Type] = {}

    def define(self, name: str, typ: Type):
        """Define a variable"""
        self.bindings[name] = typ

    def lookup(self, name: str) -> Optional[Type]:
        """Look up a variable type"""
        if name in self.bindings:
            return self.bindings[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

    def child(self) -> 'TypeEnvironment':
        """Create child environment"""
        return TypeEnvironment(self)


class TypeChecker:
    """Type checks AST"""

    def __init__(self):
        self.global_env = TypeEnvironment()
        self.current_env = self.global_env
        self.errors: List[TypeCheckError] = []

        # Built-in functions
        self.define_builtins()

    def define_builtins(self):
        """Define built-in functions"""
        # I/O functions
        self.global_env.define("print", FunctionType([STRING_TYPE], VOID_TYPE))
        self.global_env.define("println", FunctionType([STRING_TYPE], VOID_TYPE))

        # String functions
        self.global_env.define("len", FunctionType([STRING_TYPE], INTEGER_TYPE))
        self.global_env.define("substr", FunctionType([STRING_TYPE, INTEGER_TYPE, INTEGER_TYPE], STRING_TYPE))
        self.global_env.define("char_at", FunctionType([STRING_TYPE, INTEGER_TYPE], STRING_TYPE))
        self.global_env.define("str_concat", FunctionType([STRING_TYPE, STRING_TYPE], STRING_TYPE))
        self.global_env.define("str_eq", FunctionType([STRING_TYPE, STRING_TYPE], BOOLEAN_TYPE))
        self.global_env.define("str_to_int", FunctionType([STRING_TYPE], INTEGER_TYPE))
        self.global_env.define("int_to_str", FunctionType([INTEGER_TYPE], STRING_TYPE))
        self.global_env.define("is_digit", FunctionType([STRING_TYPE], BOOLEAN_TYPE))
        self.global_env.define("is_alpha", FunctionType([STRING_TYPE], BOOLEAN_TYPE))
        self.global_env.define("is_alnum", FunctionType([STRING_TYPE], BOOLEAN_TYPE))

        # List functions (simplified - treat as Integer for now)
        self.global_env.define("list_append", FunctionType([INTEGER_TYPE, INTEGER_TYPE], INTEGER_TYPE))
        self.global_env.define("list_get", FunctionType([INTEGER_TYPE, INTEGER_TYPE], INTEGER_TYPE))
        self.global_env.define("list_set", FunctionType([INTEGER_TYPE, INTEGER_TYPE, INTEGER_TYPE], INTEGER_TYPE))

        # System functions
        self.global_env.define("exit", FunctionType([INTEGER_TYPE], VOID_TYPE))

    def error(self, message: str, location: SourceLocation):
        """Record type error"""
        error = TypeCheckError(message, location)
        self.errors.append(error)
        return error

    def resolve_type_annotation(self, annotation: Optional[TypeAnnotation]) -> Type:
        """Resolve a type annotation to a Type"""
        if annotation is None:
            return VOID_TYPE

        name = annotation.name

        # Primitive types
        if name == "Integer":
            return INTEGER_TYPE
        elif name == "Float":
            return FLOAT_TYPE
        elif name == "String":
            return STRING_TYPE
        elif name == "Boolean":
            return BOOLEAN_TYPE
        elif name == "List":
            if annotation.type_args:
                elem_type = self.resolve_type_annotation(annotation.type_args[0])
                return ListType(elem_type)
            return ListType(INTEGER_TYPE)  # Default to Integer
        else:
            # Unknown type - for bootstrap, just treat as Integer
            return INTEGER_TYPE

    def check_program(self, program: Program) -> bool:
        """Type check entire program"""
        self.errors = []

        # First pass: collect function declarations
        for decl in program.declarations:
            if isinstance(decl, Function):
                param_types = []
                for param in decl.inputs:
                    param_types.append(self.resolve_type_annotation(param.type_annotation))

                return_type = VOID_TYPE
                if decl.outputs:
                    return_type = self.resolve_type_annotation(decl.outputs[0].type_annotation)

                func_type = FunctionType(param_types, return_type)
                self.global_env.define(decl.name, func_type)

        # Second pass: check function bodies
        for decl in program.declarations:
            if isinstance(decl, Function):
                self.check_function(decl)

        return len(self.errors) == 0

    def check_function(self, func: Function):
        """Type check a function"""
        # Create new environment for function
        self.current_env = self.global_env.child()

        # Add parameters to environment
        for param in func.inputs:
            param_type = self.resolve_type_annotation(param.type_annotation)
            self.current_env.define(param.name, param_type)

        # Check function body
        if func.body:
            self.check_block(func.body)

        # Restore environment
        self.current_env = self.global_env

    def check_block(self, block: Block) -> Type:
        """Type check a block"""
        last_type = VOID_TYPE

        for stmt in block.statements:
            last_type = self.check_statement(stmt)

        return last_type

    def check_statement(self, stmt: ASTNode) -> Type:
        """Type check a statement"""
        if isinstance(stmt, Return):
            return self.check_return(stmt)
        elif isinstance(stmt, If):
            return self.check_if(stmt)
        elif isinstance(stmt, While):
            return self.check_while(stmt)
        elif isinstance(stmt, Ensure):
            return self.check_ensure(stmt)
        elif isinstance(stmt, Assignment):
            return self.check_assignment(stmt)
        elif stmt.node_type == ASTNodeType.BREAK or stmt.node_type == ASTNodeType.CONTINUE:
            return VOID_TYPE
        else:
            # Expression statement
            return self.check_expression(stmt)

    def check_return(self, ret: Return) -> Type:
        """Type check return statement"""
        if ret.value:
            return self.check_expression(ret.value)
        return VOID_TYPE

    def check_if(self, if_stmt: If) -> Type:
        """Type check if statement"""
        cond_type = self.check_expression(if_stmt.condition)

        # Condition should be boolean (but we're lenient in bootstrap)

        self.current_env = self.current_env.child()
        then_type = self.check_block(if_stmt.then_block)
        self.current_env = self.current_env.parent

        if if_stmt.else_block:
            self.current_env = self.current_env.child()
            else_type = self.check_block(if_stmt.else_block)
            self.current_env = self.current_env.parent

        return VOID_TYPE

    def check_while(self, while_stmt: While) -> Type:
        """Type check while loop"""
        cond_type = self.check_expression(while_stmt.condition)

        self.current_env = self.current_env.child()
        self.check_block(while_stmt.body)
        self.current_env = self.current_env.parent

        return VOID_TYPE

    def check_ensure(self, ensure_stmt: Ensure) -> Type:
        """Type check ensure statement"""
        cond_type = self.check_expression(ensure_stmt.condition)

        self.current_env = self.current_env.child()
        self.check_block(ensure_stmt.then_block)
        self.current_env = self.current_env.parent

        if ensure_stmt.else_block:
            self.current_env = self.current_env.child()
            self.check_block(ensure_stmt.else_block)
            self.current_env = self.current_env.parent

        return VOID_TYPE

    def check_assignment(self, assign: Assignment) -> Type:
        """Type check assignment"""
        value_type = self.check_expression(assign.value)

        # For identifiers, define or update in environment
        if isinstance(assign.target, Identifier):
            self.current_env.define(assign.target.name, value_type)

        return value_type

    def check_expression(self, expr: ASTNode) -> Type:
        """Type check expression"""
        if isinstance(expr, Literal):
            return self.check_literal(expr)
        elif isinstance(expr, Identifier):
            return self.check_identifier(expr)
        elif isinstance(expr, BinaryOp):
            return self.check_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            return self.check_unary_op(expr)
        elif isinstance(expr, Call):
            return self.check_call(expr)
        elif isinstance(expr, Member):
            return self.check_member(expr)
        elif isinstance(expr, Index):
            return self.check_index(expr)
        elif isinstance(expr, ListLiteral):
            return self.check_list_literal(expr)
        else:
            # Unknown expression type
            return INTEGER_TYPE

    def check_literal(self, lit: Literal) -> Type:
        """Type check literal"""
        value = lit.value

        if isinstance(value, int):
            return INTEGER_TYPE
        elif isinstance(value, float):
            return FLOAT_TYPE
        elif isinstance(value, str):
            return STRING_TYPE
        elif isinstance(value, bool):
            return BOOLEAN_TYPE
        else:
            return VOID_TYPE

    def check_identifier(self, ident: Identifier) -> Type:
        """Type check identifier"""
        typ = self.current_env.lookup(ident.name)

        if typ is None:
            self.error(f"Undefined variable: {ident.name}", ident.location)
            return INTEGER_TYPE

        return typ

    def check_binary_op(self, binop: BinaryOp) -> Type:
        """Type check binary operation"""
        left_type = self.check_expression(binop.left)
        right_type = self.check_expression(binop.right)

        # Arithmetic operators
        if binop.operator in ['+', '-', '*', '/', '%', '**']:
            # For bootstrap, allow mixed numeric types
            if isinstance(left_type, PrimitiveType) and left_type.name in ['Integer', 'Float']:
                if isinstance(right_type, PrimitiveType) and right_type.name in ['Integer', 'Float']:
                    # If either is Float, result is Float
                    if left_type.name == 'Float' or right_type.name == 'Float':
                        return FLOAT_TYPE
                    return INTEGER_TYPE

            return INTEGER_TYPE

        # Comparison operators
        elif binop.operator in ['<', '>', '<=', '>=', '==', '!=']:
            return BOOLEAN_TYPE

        # Logical operators
        elif binop.operator in ['and', 'or']:
            return BOOLEAN_TYPE

        else:
            return INTEGER_TYPE

    def check_unary_op(self, unop: UnaryOp) -> Type:
        """Type check unary operation"""
        operand_type = self.check_expression(unop.operand)

        if unop.operator == '-':
            return operand_type
        elif unop.operator == 'not':
            return BOOLEAN_TYPE
        else:
            return INTEGER_TYPE

    def check_call(self, call: Call) -> Type:
        """Type check function call"""
        func_type = self.check_expression(call.function)

        # Check arguments
        for arg in call.arguments:
            self.check_expression(arg)

        # If it's a function type, return the return type
        if isinstance(func_type, FunctionType):
            return func_type.return_type

        return VOID_TYPE

    def check_member(self, member: Member) -> Type:
        """Type check member access"""
        obj_type = self.check_expression(member.object)

        # For bootstrap, just return Integer
        return INTEGER_TYPE

    def check_index(self, index: Index) -> Type:
        """Type check index access"""
        obj_type = self.check_expression(index.object)
        index_type = self.check_expression(index.index)

        # If object is a list, return element type
        if isinstance(obj_type, ListType):
            return obj_type.element_type

        return INTEGER_TYPE

    def check_list_literal(self, lst: ListLiteral) -> Type:
        """Type check list literal"""
        if not lst.elements:
            return ListType(INTEGER_TYPE)

        # Check first element to determine type
        first_type = self.check_expression(lst.elements[0])

        # Check remaining elements
        for elem in lst.elements[1:]:
            self.check_expression(elem)

        return ListType(first_type)


def type_check_program(program: Program) -> bool:
    """Type check a program"""
    checker = TypeChecker()
    success = checker.check_program(program)

    if not success:
        for error in checker.errors:
            print(f"Type error: {error}")

    return success
