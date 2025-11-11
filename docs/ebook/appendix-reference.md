# Appendix A: Language Reference Manual

This appendix is a reference manual for the 1 programming language. It describes the syntax and semantics precisely, though the programmable nature of 1 means that syntax can be extended beyond what is described here.

## A.1 Lexical Conventions

### A.1.1 Tokens

There are six classes of tokens: identifiers, keywords, constants, string literals, operators, and other separators. Whitespace (blanks, tabs, newlines) is ignored except as it separates tokens.

### A.1.2 Comments

Comments begin with `//` and extend to the end of the line:

```1
// This is a comment
x = 10  // This is also a comment
```

### A.1.3 Identifiers

An identifier is a sequence of letters, digits, and underscores. The first character must be a letter or underscore. Upper and lower case letters are distinct.

```
identifier:
    letter (letter | digit | underscore)*

letter:
    a-z | A-Z

digit:
    0-9

underscore:
    _
```

### A.1.4 Keywords

The following identifiers are reserved as keywords and may not be used as variable or function names:

```
function    inputs      outputs     implementation
if          else        while       return
ensure      otherwise   break       continue
```

Note: `break` and `continue` are reserved but not currently implemented.

### A.1.5 Constants

Integer constants consist of a sequence of digits:

```
integer-constant:
    digit+
```

Floating-point constants contain a decimal point:

```
float-constant:
    digit+ . digit+
```

### A.1.6 String Literals

A string literal is a sequence of characters enclosed in double quotes:

```
string-literal:
    " string-characters "

string-characters:
    (any character except " or \\ or newline)*
```

Escape sequences:
- `\"` - double quote
- `\\` - backslash
- `\n` - newline

## A.2 Syntax Notation

In the syntax notation used in this reference:

- **Italics** denote syntactic categories
- **Bold** denotes keywords and literal operators
- `{ }` enclose optional items (not block delimiters in this context)
- `...` denotes repetition

## A.3 Types

### A.3.1 Basic Types

The basic data types are:

**Integer**: Whole numbers (implementation-defined range)
**Float**: Floating-point numbers (implementation-defined precision)
**String**: Sequence of characters
**Boolean**: Truth values (represented as Integer: 0 for false, non-zero for true)
**List**: Ordered collection of values

### A.3.2 Type Names

Type names are keywords that denote basic types:

```
type-name:
    Integer
    Float
    String
    Boolean
    List
```

## A.4 Expressions

### A.4.1 Primary Expressions

Primary expressions are:

```
primary-expression:
    identifier
    constant
    string-literal
    ( expression )
```

### A.4.2 Function Calls

```
function-call:
    identifier ( argument-list )

argument-list:
    expression
    argument-list , expression
```

### A.4.3 Unary Operators

```
unary-expression:
    - primary-expression
    ! primary-expression
```

The unary `-` operator negates its operand. The `!` operator returns 1 if the operand is 0, and 0 otherwise.

### A.4.4 Binary Operators

Binary operators group left to right:

```
multiplicative-expression:
    unary-expression
    multiplicative-expression * unary-expression
    multiplicative-expression / unary-expression

additive-expression:
    multiplicative-expression
    additive-expression + multiplicative-expression
    additive-expression - multiplicative-expression

relational-expression:
    additive-expression
    relational-expression < additive-expression
    relational-expression > additive-expression
    relational-expression <= additive-expression
    relational-expression >= additive-expression

equality-expression:
    relational-expression
    equality-expression == relational-expression
    equality-expression != relational-expression

logical-and-expression:
    equality-expression
    logical-and-expression && equality-expression

logical-or-expression:
    logical-and-expression
    logical-or-expression || logical-and-expression
```

### A.4.5 Assignment Expression

```
assignment-expression:
    identifier = expression
```

Assignment evaluates the right-hand expression and stores the result in the variable named by the identifier.

## A.5 Statements

### A.5.1 Expression Statement

```
expression-statement:
    expression
```

### A.5.2 Compound Statement

```
compound-statement:
    { statement-list }

statement-list:
    statement
    statement-list statement
```

### A.5.3 If Statement

```
if-statement:
    if expression : compound-statement
    if expression : compound-statement else : compound-statement
```

### A.5.4 While Statement

```
while-statement:
    while expression : compound-statement
```

### A.5.5 Return Statement

```
return-statement:
    return expression
```

### A.5.6 Ensure-Otherwise Statement

```
ensure-otherwise-statement:
    ensure expression : compound-statement otherwise : compound-statement
```

## A.6 Declarations

### A.6.1 Function Declarations

```
function-declaration:
    function identifier : inputs-section outputs-section implementation-section

inputs-section:
    inputs : parameter-list

parameter-list:
    parameter-declaration
    parameter-list parameter-declaration

parameter-declaration:
    identifier : type-name

outputs-section:
    outputs : result-list

result-list:
    result-declaration
    result-list result-declaration

result-declaration:
    identifier : type-name

implementation-section:
    implementation : compound-statement
```

Example:

```1
function example:
  inputs:
    x: Integer
    y: Integer
  outputs:
    result: Integer
  implementation: {
    result = x + y
    return result
  }
```

### A.6.2 Variable Declarations

Variables are declared implicitly by assignment:

```
variable-declaration:
    identifier = expression
```

The type of the variable is inferred from the type of the expression.

## A.7 Program Structure

A 1 program consists of a sequence of function declarations:

```
program:
    function-declaration-list

function-declaration-list:
    function-declaration
    function-declaration-list function-declaration
```

One function must be named `main`:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    // program body
    return 0
  }
```

## A.8 Scope Rules

The scope of a function parameter or local variable is the function in which it is declared.

Function names are in scope throughout the program (subject to ordering constraints in the current implementation).

## A.9 Operator Precedence

Operators are listed in order of decreasing precedence:

| Precedence | Operators | Associativity |
|------------|-----------|---------------|
| 1 (highest) | `( )` | - |
| 2 | `-` (unary), `!` | right to left |
| 3 | `*`, `/` | left to right |
| 4 | `+`, `-` | left to right |
| 5 | `<`, `<=`, `>`, `>=` | left to right |
| 6 | `==`, `!=` | left to right |
| 7 | `&&` | left to right |
| 8 | `||` | left to right |
| 9 (lowest) | `=` | right to left |

## A.10 Built-in Functions

The following functions are provided by the runtime environment:

### A.10.1 String Functions

**len(s: String) -> Integer**
Returns the length of string s.

**substr(s: String, start: Integer, end: Integer) -> String**
Returns the substring of s from index start (inclusive) to end (exclusive).

**char_at(s: String, index: Integer) -> String**
Returns the character at position index as a single-character string.

**str_concat(s1: String, s2: String) -> String**
Returns the concatenation of s1 and s2.

**str_eq(s1: String, s2: String) -> Integer**
Returns 1 if s1 and s2 are equal, 0 otherwise.

**str_to_int(s: String) -> Integer**
Converts a string to an integer.

**int_to_str(n: Integer) -> String**
Converts an integer to a string.

### A.10.2 Character Testing Functions

**is_digit(c: String) -> Integer**
Returns 1 if c is a single-character string containing a digit, 0 otherwise.

**is_alpha(c: String) -> Integer**
Returns 1 if c is a single-character string containing a letter, 0 otherwise.

**is_alnum(c: String) -> Integer**
Returns 1 if c is a single-character string containing a letter or digit, 0 otherwise.

### A.10.3 List Functions

**list_append(list: List, item: Any) -> List**
Appends item to list and returns the modified list.

**list_get(list: List, index: Integer) -> Any**
Returns the item at position index in list.

**list_set(list: List, index: Integer, value: Any) -> List**
Sets the item at position index to value and returns the modified list.

### A.10.4 I/O Functions

**print(s: String) -> Integer**
Prints string s without a newline. Returns 0.

**println(s: String) -> Integer**
Prints string s followed by a newline. Returns 0.

**println(n: Integer) -> Integer**
Prints integer n followed by a newline. Returns 0.

## A.11 Compilation and Execution

A 1 program is compiled to stack-based bytecode and executed by a virtual machine.

To compile and run a program:

```bash
python bootstrap/compiler.py program.one --run
```

To compile without running:

```bash
python bootstrap/compiler.py program.one -o program.1bc
```

To disassemble bytecode:

```bash
python bootstrap/compiler.py program.one --disassemble
```

## A.12 Undefined Behavior

The following behaviors are undefined:

- Division by zero
- Array/string index out of bounds
- Type errors (attempting to use a value as the wrong type)
- Calling a function with the wrong number of arguments
- Infinite recursion leading to stack overflow

## A.13 Implementation-Defined Behavior

The following behaviors are implementation-defined:

- Range and precision of Integer and Float types
- Maximum string length
- Maximum recursion depth
- Maximum program size

## A.14 Differences from Previous Versions

This is the initial version of the 1 language. Future versions may include:

- Module system
- Global variables
- Multiple return values
- Pattern matching
- Syntax variable declarations
- With-syntax blocks
- Additional control flow constructs

## A.15 Summary

This reference manual has defined:

- Lexical structure (tokens, keywords, constants)
- Types (Integer, Float, String, Boolean, List)
- Expressions and operators
- Statements (if, while, ensure-otherwise, return)
- Function declarations
- Program structure
- Built-in functions

For examples and explanations, see Chapters 1-6 of this book.
