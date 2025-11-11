# The 1 Programming Language

**A Revolutionary Language with Programmable Syntax**

---

## About This Book

This book describes the 1 programming language, a revolutionary language where syntax itself is programmable. Just as programs manipulate data, 1 programs can manipulate their own notation.

The book follows the model of "The C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie, combining tutorial material with precise reference documentation.

---

## Table of Contents

### [Preface](00-preface.md)

### [Chapter 1: A Tutorial Introduction](01-tutorial-introduction.md)
1.1 Getting Started
1.2 Variables and Arithmetic
1.3 The For Statement
1.4 Symbolic Constants and Character Strings
1.5 A Collection of Useful Programs
- 1.5.1 Factorial
- 1.5.2 Fibonacci
1.6 Arguments—Call by Value
1.7 Character Arrays and String Manipulation
1.8 External Variables and Scope
1.9 Summary
- Exercises

### [Chapter 2: Types, Operators, and Expressions](02-types-operators-expressions.md)
2.1 Variable Names
2.2 Data Types and Sizes
2.3 Constants
2.4 Declarations and Initialization
2.5 Arithmetic Operators
2.6 Relational and Logical Operators
2.7 Type Conversions
2.8 Assignment Operators
2.9 Conditional Expressions
2.10 Precedence and Order of Evaluation
2.11 Summary
- Exercises

### [Chapter 3: Control Flow](03-control-flow.md)
3.1 Statements and Blocks
3.2 If-Else
3.3 Else-If
3.4 While
3.5 Break and Continue
3.6 Ensure-Otherwise
3.7 Loops—A Closer Look
3.8 Recursion as Control Flow
3.9 Summary
- Exercises

### [Chapter 4: Functions and Program Structure](04-functions-program-structure.md)
4.1 Basics of Functions
4.2 Functions Returning Non-Integer Values
4.3 More on Function Arguments
4.4 External Variables and Scope
4.5 Scope Rules
4.6 Header Comments and Documentation
4.7 Static Variables
4.8 Recursion
4.9 The Main Function
4.10 Program Organization
4.11 Built-in Functions
4.12 Summary
- Exercises

### [Chapter 5: Programmable Syntax](05-programmable-syntax.md)
5.1 The Problem with Fixed Syntax
5.2 Syntax as Data
5.3 Block Delimiters
5.4 Alternative Syntaxes
5.5 Syntax Variables (Future Feature)
5.6 With-Syntax Blocks (Future Feature)
5.7 Parsing Programs in 1
5.8 Implications of Programmable Syntax
5.9 Syntax Transformations
5.10 Current Limitations
5.11 Design Principles
5.12 Comparison with Other Languages
5.13 Practical Applications
5.14 Summary
- Exercises

### [Chapter 6: Self-Hosting and Meta-Compilation](06-self-hosting.md)
6.1 What is Self-Hosting?
6.2 The Bootstrap Problem
6.3 The 1 Bootstrap Compiler
6.4 Self-Hosting Components
- 6.4.1 Tokenizer
- 6.4.2 Expression Evaluator
- 6.4.3 Bytecode Virtual Machine
6.5 The Self-Hosting Demonstration
6.6 Running the Self-Hosting Demo
6.7 Implications of Self-Hosting
6.8 Toward a Full Self-Hosting Compiler
6.9 The Fixpoint Test
6.10 Comparison with Other Languages
6.11 Future Directions
6.12 Meta-Circular Evaluation
6.13 Summary
- Exercises

### [Appendix A: Language Reference Manual](appendix-reference.md)
A.1 Lexical Conventions
A.2 Syntax Notation
A.3 Types
A.4 Expressions
A.5 Statements
A.6 Declarations
A.7 Program Structure
A.8 Scope Rules
A.9 Operator Precedence
A.10 Built-in Functions
A.11 Compilation and Execution
A.12 Undefined Behavior
A.13 Implementation-Defined Behavior
A.14 Differences from Previous Versions
A.15 Summary

---

## About the 1 Language

The 1 programming language represents a fundamental shift in language design:

- **Syntax is Programmable**: Programs can manipulate their own notation
- **Self-Hosting**: 1 can compile and execute 1 programs
- **Explicitly Typed**: All inputs and outputs are declared
- **Verification-Friendly**: Designed for formal verification
- **AI-Ready**: Optimized for AI code generation

### Key Innovations

1. **Programmable Syntax**: Block delimiters and syntax rules are data, not fixed design decisions
2. **Rapid Self-Hosting**: Achieved self-hosting in one intensive development session
3. **Meta-Homoiconicity**: Not just "code is data" but "syntax is data"

### Current Status

✅ **Bootstrap compiler complete** (Python implementation)
✅ **Self-hosting demonstrated** (core components in 1)
✅ **All examples working** (factorial, fibonacci, string manipulation, etc.)
✅ **Documentation comprehensive** (this book!)

---

## How to Read This Book

**If you are new to programming:**
Start with Chapter 1 and work through the examples. Type them in and run them. Do the exercises.

**If you are an experienced programmer:**
Skim Chapter 1, then focus on Chapters 5 and 6 which describe 1's unique features. Use the appendix as a reference.

**If you want to extend the language:**
Read all chapters, paying special attention to Chapter 6 on self-hosting. Study the self-hosting compiler components in the `compiler/` directory.

---

## Running the Examples

All examples in this book can be run using the bootstrap compiler:

```bash
# Run an example from the book
python bootstrap/compiler.py your_program.one --run

# Run with verbose output
python bootstrap/compiler.py your_program.one --run --verbose

# Disassemble bytecode
python bootstrap/compiler.py your_program.one --disassemble
```

---

## Repository Contents

```
1lang/
├── bootstrap/              # Bootstrap compiler (Python)
├── compiler/              # Self-hosting compiler (1 language!)
├── examples/              # Example programs
├── ebook/                 # This book
└── docs/                  # Additional documentation
```

---

## Contributing

The 1 language is open source and contributions are welcome. Areas for contribution include:

- Language features (pattern matching, modules, etc.)
- Standard library expansion
- Optimization passes
- Documentation and examples
- Tools (IDE support, debugger, REPL)

See `CONTRIBUTING.md` in the repository root.

---

## License

The 1 programming language is released under the MIT License.

---

## Acknowledgments

The 1 language was developed through an intensive collaboration between human insight and artificial intelligence. The bootstrap compiler is implemented in Python. The self-hosting components prove that 1 can process itself.

This book follows the model of "The C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie, whose clear and practical approach to teaching programming languages has been an inspiration.

---

## Status

**Version**: 1.0
**Date**: 2025
**Status**: Self-hosting achieved

The 1 programming language is ready for:
- Writing real programs
- Self-compilation
- Further development
- Research and experimentation

---

**Welcome to the future of programmable syntax.**

---

*For the latest version of this book and the 1 language, visit:*
*https://github.com/haxidermist/1lang*
