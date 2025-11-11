"""
Main compiler for the 1 programming language bootstrap.
Ties together all compilation stages.
"""

import sys
import argparse
from pathlib import Path

from lexer import lex_file, lex_string, LexerError
from parser import parse_file, parse_string, ParseError, Program
from type_checker import type_check_program, TypeCheckError
from codegen import generate_bytecode, disassemble_module, BytecodeModule
from vm import run_bytecode, VM
import pickle


class CompilationError(Exception):
    """Compilation error"""
    pass


class Compiler:
    """Main compiler class"""

    def __init__(self, verbose: bool = False, debug: bool = False):
        self.verbose = verbose
        self.debug = debug

    def compile_file(self, filename: str) -> BytecodeModule:
        """Compile a file"""
        if self.verbose:
            print(f"Compiling {filename}...")

        try:
            # Stage 1: Lexical analysis
            if self.verbose:
                print("  Stage 1: Lexical analysis...")

            tokens = lex_file(filename)

            if self.debug:
                print("\n=== Tokens ===")
                for token in tokens[:20]:  # Show first 20 tokens
                    print(f"  {token}")
                if len(tokens) > 20:
                    print(f"  ... and {len(tokens) - 20} more")
                print()

            # Stage 2: Parsing
            if self.verbose:
                print("  Stage 2: Parsing...")

            from parser import Parser
            parser = Parser(tokens)
            ast = parser.parse()

            if self.debug:
                print("\n=== AST ===")
                self.print_ast(ast, indent=2)
                print()

            # Stage 3: Type checking
            if self.verbose:
                print("  Stage 3: Type checking...")

            if not type_check_program(ast):
                raise CompilationError("Type checking failed")

            # Stage 4: Code generation
            if self.verbose:
                print("  Stage 4: Code generation...")

            bytecode = generate_bytecode(ast)

            if self.debug:
                print("\n=== Bytecode ===")
                print(disassemble_module(bytecode))

            if self.verbose:
                print("  Compilation successful!")

            return bytecode

        except LexerError as e:
            raise CompilationError(f"Lexical error: {e}")
        except ParseError as e:
            raise CompilationError(f"Parse error: {e}")
        except TypeCheckError as e:
            raise CompilationError(f"Type error: {e}")
        except Exception as e:
            raise CompilationError(f"Compilation error: {e}")

    def compile_string(self, source: str, filename: str = "<input>") -> BytecodeModule:
        """Compile a string"""
        try:
            # Stage 1: Lexical analysis
            tokens = lex_string(source, filename)

            # Stage 2: Parsing
            from parser import Parser
            parser = Parser(tokens)
            ast = parser.parse()

            # Stage 3: Type checking
            if not type_check_program(ast):
                raise CompilationError("Type checking failed")

            # Stage 4: Code generation
            bytecode = generate_bytecode(ast)

            return bytecode

        except Exception as e:
            raise CompilationError(str(e))

    def print_ast(self, node, indent: int = 0):
        """Pretty print AST for debugging"""
        prefix = " " * indent

        if isinstance(node, Program):
            print(f"{prefix}Program:")
            for decl in node.declarations:
                self.print_ast(decl, indent + 2)

        elif hasattr(node, '__class__'):
            print(f"{prefix}{node.__class__.__name__}")
            if hasattr(node, '__dict__'):
                for key, value in node.__dict__.items():
                    if key in ['location', 'metadata', 'node_type']:
                        continue
                    if isinstance(value, list):
                        if value:
                            print(f"{prefix}  {key}:")
                            for item in value:
                                self.print_ast(item, indent + 4)
                    elif hasattr(value, '__class__') and hasattr(value, '__dict__'):
                        print(f"{prefix}  {key}:")
                        self.print_ast(value, indent + 4)
                    elif value is not None:
                        print(f"{prefix}  {key}: {value}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="1 language bootstrap compiler")

    parser.add_argument("input", help="Input .one file")
    parser.add_argument("-o", "--output", help="Output bytecode file (.1bc)")
    parser.add_argument("-r", "--run", action="store_true", help="Run after compiling")
    parser.add_argument("-d", "--debug", action="store_true", help="Debug mode")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-t", "--disassemble", action="store_true", help="Disassemble bytecode")

    args = parser.parse_args()

    try:
        # Create compiler
        compiler = Compiler(verbose=args.verbose, debug=args.debug)

        # Compile
        bytecode = compiler.compile_file(args.input)

        # Save bytecode if requested
        if args.output:
            with open(args.output, 'wb') as f:
                pickle.dump(bytecode, f)
            if args.verbose:
                print(f"Bytecode saved to {args.output}")

        # Disassemble if requested
        if args.disassemble:
            print("\n=== Disassembly ===")
            print(disassemble_module(bytecode))

        # Run if requested
        if args.run:
            if args.verbose:
                print("\n=== Running ===\n")

            result = run_bytecode(bytecode, debug=args.debug)

            if args.verbose:
                print(f"\n=== Program exited with: {result} ===")

    except CompilationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Internal error: {e}", file=sys.stderr)
        if args.debug:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
