# Syntax Metaprogramming in 1

## Core Concept

In 1, **syntax itself is data**. Programs can declare, manipulate, and transform the syntactic structure of code they process. This enables powerful metaprogramming where compilers, interpreters, and code generators can define custom syntax for domain-specific languages.

## Syntax Variables

Syntax elements are declared as variables that the parser respects:

```1
syntax:
  block_begin: "{"
  block_end: "}"
  statement_separator: ";"
  comment_line: "//"
  comment_block_begin: "/*"
  comment_block_end: "*/"
```

## Example: Block Delimiters

### Traditional 1 (Indentation-based)
```1
function factorial:
  inputs:
    n: Integer
  implementation:
    if n == 0:
      return 1
    else:
      return n * factorial(n - 1)
```

### 1 with C-style Syntax
```1
syntax:
  block_begin: "{"
  block_end: "}"

function factorial:
  inputs:
    n: Integer
  implementation: {
    if n == 0 {
      return 1
    } else {
      return n * factorial(n - 1)
    }
  }
```

### 1 with Pascal-style Syntax
```1
syntax:
  block_begin: "begin"
  block_end: "end"

function factorial:
  inputs:
    n: Integer
  implementation: begin
    if n == 0 begin
      return 1
    end else begin
      return n * factorial(n - 1)
    end
  end
```

## Syntax Contexts

Programs can create **syntax contexts** for different parts of code:

```1
// Compiler can define syntax for the language it compiles
syntax target_lang_syntax:
  block_begin: "{"
  block_end: "}"

syntax compiler_syntax:
  block_begin: ":"
  block_end: ""  // Empty = indentation-based

// Use compiler_syntax for this file
use_syntax: compiler_syntax

function parse_target_code:
  inputs:
    code: String
  implementation:
    // Process code using target_lang_syntax
    with_syntax target_lang_syntax:
      tokens = tokenize(code)
      ast = parse(tokens)
```

## Metaprogramming Applications

### 1. Self-Hosting Compiler
A compiler written in 1 can define the syntax of the language it compiles:

```1
syntax source_language:
  block_begin: "{"
  block_end: "}"

function compile:
  inputs:
    source_code: String
  implementation:
    // Parse source using its syntax
    with_syntax source_language:
      ast = parse_code(source_code)
```

### 2. DSL Creation
Create domain-specific languages with custom syntax:

```1
syntax sql_like:
  statement_separator: ";"
  block_begin: "BEGIN"
  block_end: "END"

syntax json_like:
  block_begin: "{"
  block_end: "}"
  list_begin: "["
  list_end: "]"
```

### 3. Code Generation
Generate code with different syntactic styles:

```1
function generate_c_code:
  implementation:
    with_syntax c_style:
      emit("int main() {")
      emit("  return 0;")
      emit("}")
```

## Syntax Variable Types

### Delimiters
- `block_begin`, `block_end`
- `list_begin`, `list_end`
- `tuple_begin`, `tuple_end`

### Separators
- `statement_separator`
- `parameter_separator`
- `declaration_separator`

### Operators
- `assignment`: "=" | ":=" | "<-"
- `equality`: "==" | "=" | "eq"
- `arrow`: "->" | "=>" | "→"

### Keywords
- `function_keyword`: "function" | "fun" | "def" | "fn"
- `if_keyword`: "if" | "when" | "cond"
- `return_keyword`: "return" | "ret" | "^"

## Implementation

### Syntax Variable Storage
Syntax variables are stored in a `SyntaxContext`:

```1
type SyntaxContext:
  delimiters: Map<String, String>
  keywords: Map<String, String>
  operators: Map<String, String>

  invariant:
    - all values are valid tokens
    - no circular dependencies
```

### Parser Integration
The parser queries the active syntax context:

```1
function Parser.expect_block_begin:
  implementation:
    expected = syntax_context.get("block_begin")
    if match(expected):
      return true
    else:
      error("Expected block delimiter")
```

### Dynamic Syntax Changes
Programs can switch syntax contexts:

```1
function process_embedded_language:
  inputs:
    code: String
    lang_syntax: SyntaxContext
  implementation:
    // Save current syntax
    old_syntax = get_current_syntax()

    // Switch to embedded language syntax
    set_current_syntax(lang_syntax)

    // Process code
    result = parse(code)

    // Restore original syntax
    set_current_syntax(old_syntax)

    return result
```

## Philosophy

**"In 1, code is not just data - syntax itself is data."**

This paradigm enables:
- **Polyglot programming**: Multiple syntactic styles in one program
- **Syntax evolution**: Language syntax can evolve without breaking old code
- **Meta-compilation**: Compilers that understand their own syntax constraints
- **Tool generation**: Automatically generate parsers for custom syntaxes

## Practical Benefits

1. **Bootstrap flexibility**: The bootstrap compiler can use one syntax, while the self-hosting compiler uses another
2. **DSL embedding**: Embed domain-specific languages with natural syntax
3. **Code transformation**: Transform between syntactic styles programmatically
4. **Language experiments**: Try new syntax features without modifying the core language

## Next Steps

- Implement syntax variable declarations in lexer
- Add syntax context switching in parser
- Create standard syntax libraries (C-style, Python-style, etc.)
- Build tools for syntax transformation
- Document best practices for syntax design
