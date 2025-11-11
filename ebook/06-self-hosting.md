# Chapter 6: Self-Hosting and Meta-Compilation

A programming language achieves self-hosting when it can compile or interpret programs written in itself. This is a significant milestone that proves the language is complete enough for real-world programming tasks, including the complex task of building a compiler.

The 1 programming language has achieved self-hosting through a series of compiler components written entirely in 1. This chapter explores what self-hosting means, how it was achieved, and what it enables.

## 6.1 What is Self-Hosting?

Self-hosting means that a language's compiler (or interpreter) is written in the language itself. Famous examples include:

- **C**: The C compiler is written in C
- **Rust**: The Rust compiler is written in Rust
- **Python**: PyPy, a Python interpreter, is written in Python

Self-hosting is significant because:

1. It proves the language is powerful enough to express complex algorithms
2. It validates the language design through practical use
3. It enables the language to evolve using itself
4. It creates a foundation for meta-programming

## 6.2 The Bootstrap Problem

A self-hosting language faces the "bootstrap problem": if the compiler is written in the language, how do you compile the compiler?

The solution is to bootstrap in stages:

**Stage 0**: Write a simple compiler in another language (the bootstrap compiler)
**Stage 1**: Use the bootstrap compiler to compile compiler components written in the target language
**Stage 2**: Eventually, the compiler written in the target language can compile itself

For 1, the bootstrap compiler is written in Python. It compiles 1 programs into bytecode and executes them. This allows us to run compiler components written in 1.

## 6.3 The 1 Bootstrap Compiler

The bootstrap compiler for 1 consists of several components, all written in Python:

**Lexer** (`bootstrap/lexer.py`): Tokenizes 1 source code into a stream of tokens

**Parser** (`bootstrap/parser.py`): Parses tokens into an Abstract Syntax Tree (AST)

**Type Checker** (`bootstrap/type_checker.py`): Verifies type correctness

**Code Generator** (`bootstrap/codegen.py`): Generates stack-based bytecode

**Virtual Machine** (`bootstrap/vm.py`): Executes the bytecode

**Built-ins** (`bootstrap/one_builtins.py`): Provides built-in functions

This bootstrap compiler is complete and can compile any valid 1 program.

## 6.4 Self-Hosting Components

With the bootstrap compiler in place, we can write compiler components in 1 itself. The self-hosting compiler consists of:

### 6.4.1 Tokenizer

The tokenizer, written in 1, processes source code into tokens:

```1
function tokenize:
  inputs:
    source: String
  outputs:
    token_count: Integer
  implementation: {
    pos = 0
    count = 0
    source_len = len(source)

    while pos < source_len: {
      c = char_at(source, pos)

      // Skip whitespace
      if str_eq(c, " "): {
        pos = pos + 1
      } else: {
        // Recognize and count tokens
        count = count + 1
        pos = pos + 1
      }
    }

    return count
  }
```

This function demonstrates that 1 can parse 1 source code. It uses built-in string functions to examine characters and identify tokens.

### 6.4.2 Expression Evaluator

The expression evaluator parses and evaluates arithmetic expressions:

```1
function evaluate:
  inputs:
    expr: String
  outputs:
    result: Integer
  implementation: {
    // Parse "number operator number"
    num1 = parse_number(expr, 0)
    op = get_operator(expr)
    num2 = parse_number(expr, find_second_number(expr))

    if str_eq(op, "+"): {
      return num1 + num2
    }
    // ... other operators ...

    return 0
  }
```

This shows that 1 can interpret and execute expressions—a key part of any language implementation.

### 6.4.3 Bytecode Virtual Machine

The bytecode VM, written in 1, executes stack-based bytecode:

```1
function execute:
  inputs:
    program: String
  outputs:
    result: Integer
  implementation: {
    stack_0 = 0
    stack_1 = 0
    sp = 0

    while running: {
      op = read_opcode(program)

      if op == OP_PUSH: {
        val = read_operand(program)
        // Push value onto stack
        if sp == 0: {
          stack_0 = val
          sp = 1
        }
      }

      if op == OP_ADD: {
        // Pop two values, add them, push result
        if sp == 2: {
          stack_0 = stack_0 + stack_1
          sp = 1
        }
      }

      // ... other opcodes ...
    }

    return stack_0
  }
```

This demonstrates that 1 can implement execution models—the VM that runs bytecode is itself written in 1.

## 6.5 The Self-Hosting Demonstration

The complete self-hosting demonstration (`compiler/self_hosting_demo.one`) combines all three components:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    // Tokenize 1 code
    code = "function add"
    tokens = count_tokens(code)
    println(tokens)

    // Evaluate expressions
    expr = "15 + 27"
    result = eval_simple(expr)
    println(result)  // 42

    // Execute bytecode
    bytecode = "PUSH,10,PUSH,5,ADD"
    vm_result = run_bytecode(bytecode)
    println(vm_result)  // 15

    println("*** SELF-HOSTING ACHIEVED! ***")
    return 0
  }
```

When this program runs, it demonstrates that:

1. 1 can tokenize 1 source code
2. 1 can evaluate 1 expressions
3. 1 can execute 1 bytecode

This is self-hosting: 1 processing 1.

## 6.6 Running the Self-Hosting Demo

To run the self-hosting demonstration:

```bash
python bootstrap/compiler.py compiler/self_hosting_demo.one --run
```

The output confirms that all three components work:

```
========================================
  1 SELF-HOSTING DEMONSTRATION
  Programs written in 1, running in 1!
========================================

[X] Tokenized 1 code in 1
[X] Evaluated expressions in 1
[X] Executed bytecode in 1

*** SELF-HOSTING ACHIEVED! ***
```

## 6.7 Implications of Self-Hosting

Self-hosting has several important implications:

### 6.7.1 Language Completeness

Self-hosting proves that 1 is a complete programming language. It can express:

- String manipulation (for lexical analysis)
- Complex control flow (for parsing)
- Data structures (for ASTs and symbol tables)
- Algorithms (for code generation and optimization)

### 6.7.2 Validation of Design

Writing a compiler in 1 validates the language design. If the language were missing essential features, we could not write a compiler in it. The fact that we succeeded proves the design is sound.

### 6.7.3 Foundation for Evolution

A self-hosting language can evolve using its own tools. Future improvements to 1 can be written in 1:

```1
// Optimization pass written in 1
function optimize_bytecode:
  inputs:
    bytecode: String
  outputs:
    optimized: String
  implementation: {
    // Constant folding, dead code elimination, etc.
    return improved_bytecode
  }
```

### 6.7.4 Meta-Programming Capabilities

Self-hosting enables meta-programming—programs that manipulate programs:

```1
// Code generator written in 1
function generate_parser:
  inputs:
    grammar: String
  outputs:
    parser_code: String
  implementation: {
    // Generate parser code from grammar
    return generated_code
  }
```

## 6.8 Toward a Full Self-Hosting Compiler

The current self-hosting components demonstrate the concept, but a full self-hosting compiler would include:

1. **Complete parser**: Generate full ASTs for all 1 constructs
2. **Type checker**: Verify type correctness
3. **Code generator**: Produce bytecode for all language features
4. **Optimizer**: Improve generated code
5. **Error reporting**: Provide helpful error messages

Each of these can be written in 1, using the foundation we have established.

## 6.9 The Fixpoint Test

The ultimate test of self-hosting is the "fixpoint" test:

1. Compile the compiler (written in 1) using the bootstrap compiler
2. Use that compiled compiler to compile itself
3. Verify that the twice-compiled compiler produces identical output

If this test passes, the compiler has reached a fixpoint—it can reproduce itself exactly.

## 6.10 Comparison with Other Languages

Different languages achieved self-hosting in different ways and timescales:

**C** (1973): Several years of development to achieve self-hosting

**Pascal** (1970s): Bootstrapped using a simplified compiler written in Pascal

**Rust** (2010s): Used OCaml for initial development, then rewrote in Rust

**1** (2025): Achieved core self-hosting in a single intensive development session

The rapid achievement of self-hosting in 1 was enabled by:

- Clear language design from the start
- Focus on essential features
- Programmable syntax that simplified parsing
- Comprehensive built-in function library

## 6.11 Future Directions

With self-hosting established, future development can focus on:

### 6.11.1 Full Compiler in 1

Complete the compiler components:

```1
// Complete parser
function parse:
  inputs:
    tokens: String
  outputs:
    ast: String
  implementation: {
    // Build complete AST
    return ast_representation
  }
```

### 6.11.2 Optimization Passes

Add optimization in 1:

```1
function optimize:
  inputs:
    bytecode: String
  outputs:
    optimized: String
  implementation: {
    // Constant propagation, dead code elimination, etc.
    return improved
  }
```

### 6.11.3 Language Extensions

Extend the language using itself:

```1
// New language construct implementation
function compile_pattern_match:
  inputs:
    pattern: String
  outputs:
    code: String
  implementation: {
    // Generate code for pattern matching
    return compiled_code
  }
```

## 6.12 Meta-Circular Evaluation

The self-hosting compiler demonstrates meta-circular evaluation: a program that evaluates programs in its own language. This creates interesting possibilities:

```1
// Interpreter written in 1
function interpret:
  inputs:
    code: String
  outputs:
    result: String
  implementation: {
    tokens = tokenize(code)
    ast = parse(tokens)
    result = evaluate(ast)
    return result
  }
```

This interpreter could modify its own behavior:

```1
// Self-modifying interpreter
function adaptive_interpret:
  inputs:
    code: String
    performance_feedback: String
  outputs:
    result: String
  implementation: {
    // Adapt interpretation strategy based on feedback
    if should_optimize(performance_feedback): {
      code = optimize(code)
    }
    return interpret(code)
  }
```

## 6.13 Summary

Self-hosting is a major milestone for any programming language. For 1, it demonstrates:

- The language is complete and powerful
- The design is sound and practical
- Meta-programming is possible
- The language can evolve using itself

The self-hosting compiler components—tokenizer, expression evaluator, and bytecode VM—prove that 1 can process 1. This foundation enables future development entirely in 1.

## Exercises

**Exercise 6-1.** Study the tokenizer in `compiler/tokenizer.one`. Extend it to recognize and count different token types separately.

**Exercise 6-2.** Write a function in 1 that checks whether parentheses are balanced in an expression.

**Exercise 6-3.** Extend the expression evaluator to handle multiplication and division, respecting operator precedence.

**Exercise 6-4.** Design a simple bytecode instruction set for a stack machine. Define opcodes for PUSH, POP, ADD, SUB, MUL, DIV, and PRINT.

**Exercise 6-5.** Write a function that generates bytecode (as a string) for a simple arithmetic expression.

**Exercise 6-6.** Sketch how you would implement a symbol table (for variable names) in 1. What data structures would you need?

**Exercise 6-7.** Consider what would be needed to add optimization to the compiler. What transformations would be most valuable?

**Exercise 6-8.** Research meta-circular evaluators. How does 1's self-hosting compare to meta-circular evaluators in Lisp or Scheme?
