"""
Bytecode generator for 1 language bootstrap compiler.
Generates stack-based bytecode for the 1 VM.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import parser as parser_module
from parser import *


class OpCode(Enum):
    """Bytecode operation codes"""
    # Stack operations
    LOAD_CONST = auto()      # Push constant onto stack
    LOAD_VAR = auto()        # Load variable onto stack
    STORE_VAR = auto()       # Store top of stack to variable
    POP = auto()             # Pop top of stack

    # Arithmetic operations
    ADD = auto()             # a + b
    SUB = auto()             # a - b
    MUL = auto()             # a * b
    DIV = auto()             # a / b
    MOD = auto()             # a % b
    POW = auto()             # a ** b
    NEG = auto()             # -a

    # Comparison operations
    EQ = auto()              # a == b
    NE = auto()              # a != b
    LT = auto()              # a < b
    GT = auto()              # a > b
    LE = auto()              # a <= b
    GE = auto()              # a >= b

    # Logical operations
    AND = auto()             # a and b
    OR = auto()              # a or b
    NOT = auto()             # not a

    # Control flow
    JUMP = auto()            # Unconditional jump
    JUMP_IF_FALSE = auto()   # Jump if top of stack is false
    JUMP_IF_TRUE = auto()    # Jump if top of stack is true

    # Function operations
    CALL = auto()            # Call function
    RETURN = auto()          # Return from function
    HALT = auto()            # Stop execution

    # List operations
    BUILD_LIST = auto()      # Build list from n stack items
    INDEX = auto()           # Index into list/array

    # Built-in functions
    PRINT = auto()           # Print value
    PRINTLN = auto()         # Print value with newline


@dataclass
class Instruction:
    """Single bytecode instruction"""
    opcode: OpCode
    operand: Optional[Any] = None
    location: Optional[SourceLocation] = None

    def __str__(self):
        if self.operand is not None:
            return f"{self.opcode.name} {self.operand}"
        return self.opcode.name


@dataclass
class Function:
    """Compiled function"""
    name: str
    param_count: int
    param_names: List[str] = field(default_factory=list)
    instructions: List[Instruction] = field(default_factory=list)
    constants: List[Any] = field(default_factory=list)


@dataclass
class BytecodeModule:
    """Compiled module containing bytecode"""
    functions: Dict[str, Function] = field(default_factory=dict)
    constants: List[Any] = field(default_factory=list)
    entry_point: str = "main"


class CodeGenerator:
    """Generates bytecode from AST"""

    def __init__(self):
        self.module = BytecodeModule()
        self.current_function: Optional[Function] = None
        self.label_counter = 0
        self.loop_stack: List[tuple] = []  # Stack of (break_label, continue_label)

    def generate(self, program: Program) -> BytecodeModule:
        """Generate bytecode for entire program"""
        # Generate code for each function
        for decl in program.declarations:
            if isinstance(decl, parser_module.Function):
                self.generate_function(decl)

        return self.module

    def generate_function(self, func: parser_module.Function):
        """Generate bytecode for a function"""
        # Extract parameter names
        param_names = [param.name for param in func.inputs]

        compiled_func = Function(
            name=func.name,
            param_count=len(func.inputs),
            param_names=param_names
        )

        self.current_function = compiled_func

        # Generate function body
        if func.body:
            self.generate_block(func.body)

        # Add implicit return if not present
        if not compiled_func.instructions or \
           compiled_func.instructions[-1].opcode != OpCode.RETURN:
            self.emit(OpCode.LOAD_CONST, None)  # Return None/void
            self.emit(OpCode.RETURN)

        # Add function to module
        self.module.functions[func.name] = compiled_func
        self.current_function = None

    def generate_block(self, block: Block):
        """Generate bytecode for a block"""
        for stmt in block.statements:
            self.generate_statement(stmt)

    def generate_statement(self, stmt: ASTNode):
        """Generate bytecode for a statement"""
        if isinstance(stmt, Return):
            self.generate_return(stmt)
        elif isinstance(stmt, If):
            self.generate_if(stmt)
        elif isinstance(stmt, While):
            self.generate_while(stmt)
        elif isinstance(stmt, Ensure):
            self.generate_ensure(stmt)
        elif isinstance(stmt, Assignment):
            self.generate_assignment(stmt)
        elif stmt.node_type == ASTNodeType.BREAK:
            self.generate_break()
        elif stmt.node_type == ASTNodeType.CONTINUE:
            self.generate_continue()
        else:
            # Expression statement - evaluate and pop result
            self.generate_expression(stmt)
            self.emit(OpCode.POP)

    def generate_return(self, ret: Return):
        """Generate return statement"""
        if ret.value:
            self.generate_expression(ret.value)
        else:
            self.emit(OpCode.LOAD_CONST, None)

        self.emit(OpCode.RETURN)

    def generate_if(self, if_stmt: If):
        """Generate if statement"""
        # Generate condition
        self.generate_expression(if_stmt.condition)

        # Jump to else/end if false
        else_label = self.new_label()
        end_label = self.new_label()

        self.emit(OpCode.JUMP_IF_FALSE, else_label)

        # Generate then block
        self.generate_block(if_stmt.then_block)
        self.emit(OpCode.JUMP, end_label)

        # Generate else block
        self.patch_label(else_label)
        if if_stmt.else_block:
            self.generate_block(if_stmt.else_block)

        self.patch_label(end_label)

    def generate_while(self, while_stmt: While):
        """Generate while loop"""
        end_label = self.new_label()

        # Record loop start position
        start_pos = len(self.current_function.instructions)

        # Push loop labels for break/continue
        self.loop_stack.append((end_label, start_pos))

        # Generate condition
        self.generate_expression(while_stmt.condition)
        self.emit(OpCode.JUMP_IF_FALSE, end_label)

        # Generate body
        self.generate_block(while_stmt.body)

        # Jump back to start position
        self.emit(OpCode.JUMP, start_pos)

        # Loop end
        self.patch_label(end_label)

        # Pop loop labels
        self.loop_stack.pop()

    def generate_ensure(self, ensure_stmt: Ensure):
        """Generate ensure/otherwise statement"""
        # Similar to if statement
        self.generate_expression(ensure_stmt.condition)

        else_label = self.new_label()
        end_label = self.new_label()

        self.emit(OpCode.JUMP_IF_FALSE, else_label)

        # Generate then block
        self.generate_block(ensure_stmt.then_block)
        self.emit(OpCode.JUMP, end_label)

        # Generate else block
        self.patch_label(else_label)
        if ensure_stmt.else_block:
            self.generate_block(ensure_stmt.else_block)

        self.patch_label(end_label)

    def generate_assignment(self, assign: Assignment):
        """Generate assignment"""
        # Generate value
        self.generate_expression(assign.value)

        # Store to target
        if isinstance(assign.target, Identifier):
            # Handle compound assignment
            if assign.operator != '=':
                # Load current value
                self.emit(OpCode.LOAD_VAR, assign.target.name)

                # Apply operation
                if assign.operator == '+=':
                    self.emit(OpCode.ADD)
                elif assign.operator == '-=':
                    self.emit(OpCode.SUB)
                elif assign.operator == '*=':
                    self.emit(OpCode.MUL)
                elif assign.operator == '/=':
                    self.emit(OpCode.DIV)

            self.emit(OpCode.STORE_VAR, assign.target.name)

    def generate_break(self):
        """Generate break statement"""
        if not self.loop_stack:
            raise Exception("break outside of loop")

        break_label, _ = self.loop_stack[-1]
        self.emit(OpCode.JUMP, break_label)

    def generate_continue(self):
        """Generate continue statement"""
        if not self.loop_stack:
            raise Exception("continue outside of loop")

        _, continue_label = self.loop_stack[-1]
        self.emit(OpCode.JUMP, continue_label)

    def generate_expression(self, expr: ASTNode):
        """Generate bytecode for expression"""
        if isinstance(expr, Literal):
            self.generate_literal(expr)
        elif isinstance(expr, Identifier):
            self.generate_identifier(expr)
        elif isinstance(expr, BinaryOp):
            self.generate_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            self.generate_unary_op(expr)
        elif isinstance(expr, Call):
            self.generate_call(expr)
        elif isinstance(expr, Index):
            self.generate_index(expr)
        elif isinstance(expr, ListLiteral):
            self.generate_list_literal(expr)
        else:
            # Unknown expression - push null
            self.emit(OpCode.LOAD_CONST, None)

    def generate_literal(self, lit: Literal):
        """Generate literal value"""
        self.emit(OpCode.LOAD_CONST, lit.value)

    def generate_identifier(self, ident: Identifier):
        """Generate identifier reference"""
        self.emit(OpCode.LOAD_VAR, ident.name)

    def generate_binary_op(self, binop: BinaryOp):
        """Generate binary operation"""
        # Generate left and right operands
        self.generate_expression(binop.left)
        self.generate_expression(binop.right)

        # Generate operation
        op_map = {
            '+': OpCode.ADD,
            '-': OpCode.SUB,
            '*': OpCode.MUL,
            '/': OpCode.DIV,
            '%': OpCode.MOD,
            '**': OpCode.POW,
            '==': OpCode.EQ,
            '!=': OpCode.NE,
            '<': OpCode.LT,
            '>': OpCode.GT,
            '<=': OpCode.LE,
            '>=': OpCode.GE,
            'and': OpCode.AND,
            'or': OpCode.OR,
        }

        opcode = op_map.get(binop.operator)
        if opcode:
            self.emit(opcode)
        else:
            raise Exception(f"Unknown binary operator: {binop.operator}")

    def generate_unary_op(self, unop: UnaryOp):
        """Generate unary operation"""
        self.generate_expression(unop.operand)

        if unop.operator == '-':
            self.emit(OpCode.NEG)
        elif unop.operator == 'not':
            self.emit(OpCode.NOT)
        else:
            raise Exception(f"Unknown unary operator: {unop.operator}")

    def generate_call(self, call: Call):
        """Generate function call"""
        # Generate arguments (in order)
        for arg in call.arguments:
            self.generate_expression(arg)

        # Get function name
        if isinstance(call.function, Identifier):
            func_name = call.function.name

            # Check for built-in functions
            if func_name == "print":
                self.emit(OpCode.PRINT)
            elif func_name == "println":
                self.emit(OpCode.PRINTLN)
            else:
                # Regular function call
                self.emit(OpCode.CALL, (func_name, len(call.arguments)))
        else:
            raise Exception("Only simple function calls supported in bootstrap")

    def generate_index(self, index: Index):
        """Generate index access"""
        self.generate_expression(index.object)
        self.generate_expression(index.index)
        self.emit(OpCode.INDEX)

    def generate_list_literal(self, lst: ListLiteral):
        """Generate list literal"""
        # Generate each element
        for elem in lst.elements:
            self.generate_expression(elem)

        # Build list from n elements
        self.emit(OpCode.BUILD_LIST, len(lst.elements))

    def emit(self, opcode: OpCode, operand: Any = None, location: SourceLocation = None):
        """Emit an instruction"""
        inst = Instruction(opcode, operand, location)
        self.current_function.instructions.append(inst)

    def new_label(self) -> str:
        """Create a new label"""
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def patch_label(self, label: str):
        """Patch a label to current position"""
        pos = len(self.current_function.instructions)

        # Replace all references to this label with the actual position
        for inst in self.current_function.instructions:
            if inst.operand == label:
                inst.operand = pos


def generate_bytecode(program: Program) -> BytecodeModule:
    """Generate bytecode from AST"""
    generator = CodeGenerator()
    return generator.generate(program)


def disassemble_function(func: Function) -> str:
    """Disassemble a function for debugging"""
    lines = [f"Function {func.name} ({func.param_count} params):"]

    for i, inst in enumerate(func.instructions):
        lines.append(f"  {i:4d}: {inst}")

    return "\n".join(lines)


def disassemble_module(module: BytecodeModule) -> str:
    """Disassemble entire module"""
    lines = ["Bytecode Module:"]
    lines.append(f"Entry point: {module.entry_point}")
    lines.append("")

    for func_name, func in module.functions.items():
        lines.append(disassemble_function(func))
        lines.append("")

    return "\n".join(lines)
