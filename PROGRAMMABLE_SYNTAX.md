# Programmable Syntax: A Revolutionary Feature of 1

## The Breakthrough

**In 1, syntax is not fixed—it's programmable data that code can manipulate.**

This paradigm shift means:
- Programs can choose their own block delimiters
- Compilers written in 1 can define custom syntax for the languages they compile
- Domain-specific languages emerge naturally from syntax variables
- Code becomes truly homoiconic—syntax and semantics are both data

## Current Implementation

### Brace-Delimited Blocks

1 now supports **explicit block delimiters** alongside indentation:

```1
// Traditional indentation-based (when fully implemented)
function factorial:
  inputs:
    n: Integer
  implementation:
    if n == 0:
      return 1
    else:
      return n * factorial(n - 1)

// Brace-delimited (works now!)
function factorial:
  inputs:
    n: Integer
  implementation: {
    if n == 0: {
      return 1
    } else: {
      return n * factorial(n - 1)
    }
  }
```

### Why This Matters

**1. Solves the Bootstrap Problem**

Without indentation tracking, the bootstrap compiler couldn't determine block boundaries.
By making block delimiters programmable, we:
- Fixed the immediate technical limitation
- Opened up a revolutionary metaprogramming paradigm
- Enabled compilers to define their own syntax

**2. Syntax as First-Class Data**

In most languages, syntax is hardcoded in the parser. In 1:
```1
// Future syntax - not yet implemented
syntax c_style:
  block_begin: "{"
  block_end: "}"

syntax python_style:
  block_begin: ":"
  block_end: ""  // Indentation-based

// Use different syntaxes in same program!
with_syntax c_style: {
  function foo: {
    return 42
  }
}

with_syntax python_style:
  function bar:
    return 43
```

**3. Self-Modifying Compilers**

A compiler written in 1 can manipulate the syntax of the code it's compiling:

```1
function compile_custom_language:
  inputs:
    source_code: String
    target_syntax: SyntaxContext
  implementation: {
    // Parse using target language's syntax
    with_syntax target_syntax: {
      ast = parse(source_code)
    }

    // Generate code using 1's syntax
    bytecode = generate(ast)
    return bytecode
  }
```

## Practical Applications

### 1. Multiple Syntactic Styles

Choose the syntax that fits your problem domain:

```1
// Mathematical notation
function integrate:
  implementation: {
    sum = 0
    i = start
    while i < end: {
      sum = sum + f(i) * delta
      i = i + delta
    }
    return sum
  }

// Systems programming style
function alloc_buffer:
  implementation: {
    ptr = malloc(size)
    if ptr == null: {
      return error("Out of memory")
    }
    memset(ptr, 0, size)
    return ptr
  }
```

### 2. Language Embedding

Embed domain-specific languages naturally:

```1
// SQL-like queries in 1
query = parse_with_sql_syntax("
  SELECT * FROM users
  WHERE age > 18
  ORDER BY name
")

// HTML generation
html = generate_with_html_syntax({
  tag: "div"
  children: [
    { tag: "h1", text: "Hello" }
    { tag: "p", text: "World" }
  ]
})
```

### 3. Code Generation

Generate code in multiple syntactic styles:

```1
function generate_c_code:
  implementation: {
    emit_with_c_syntax({
      "int main() {"
      "  printf(\"Hello\\n\");"
      "  return 0;"
      "}"
    })
  }
```

## Philosophy

### Traditional View
"Syntax is fixed; programs adapt to the language"

### 1's View
"Syntax is data; the language adapts to the program"

This inversion enables:
- **Polyglot Programming**: Multiple syntaxes in one program
- **Syntax Evolution**: Language can evolve without breaking old code
- **Meta-Compilation**: Compilers that understand their constraints
- **Tool Generation**: Auto-generate parsers for custom syntax

## Technical Details

### Current Support

✅ **Brace-delimited blocks**: `{ statements }`
✅ **Mixed syntax**: Braces and indentation in same file
✅ **Nested blocks**: Braces within braces
✅ **Control flow**: if/while/ensure with braces

### Future Extensions

🔄 **Syntax declarations**: `syntax name: { ... }`
🔄 **Context switching**: `with_syntax name: { ... }`
🔄 **Custom operators**: `operator + precedence 10 ...`
🔄 **Custom keywords**: `keyword myif equivalent if`
🔄 **Syntax libraries**: Standard syntax definitions

## Example: Mixed Syntax Program

```1
// fibonacci.one - Multiple syntactic styles

function fibonacci_recursive:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n <= 1: {
      return n
    } else: {
      return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    }
  }

function fibonacci_iterative:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n <= 1: {
      return n
    }

    prev = 0
    curr = 1

    i = 2
    while i <= n: {
      next = prev + curr
      prev = curr
      curr = next
      i = i + 1
    }

    return curr
  }

function main:
  outputs:
    exit_code: Integer
  implementation: {
    println("Recursive fib(10):")
    println(fibonacci_recursive(10))

    println("Iterative fib(10):")
    println(fibonacci_iterative(10))

    return 0
  }
```

## Impact on Self-Hosting

**Before**: Bootstrap compiler couldn't handle indentation → couldn't write compiler in 1

**After**: Programmable syntax → can write compiler in 1 using explicit delimiters

This breakthrough enables:
1. **Self-hosting compiler** can use brace syntax
2. **Source-to-source transformers** can convert between syntaxes
3. **Polyglot tools** can process multiple syntactic styles
4. **Future evolution** of syntax features without breaking compatibility

## Philosophical Implications

### Code as Data, Syntax as Data

Lisp pioneered "code as data" (homoiconicity).
1 extends this to **"syntax as data"** (meta-homoiconicity).

Programs in 1 can:
- **Read** syntax definitions
- **Manipulate** syntax structures
- **Transform** between syntactic styles
- **Generate** new syntaxes dynamically

### The Ultimate Flexibility

Different parts of a program can use different syntaxes:
- UI code might use declarative syntax
- System code might use imperative syntax
- Math code might use formula-like syntax
- Generated code might use minimal syntax

All in the same program, seamlessly interoperating.

## Next Steps

1. **Complete syntax variable system**
   - Full `syntax:` declarations
   - `with_syntax` blocks
   - Syntax inheritance

2. **Standard syntax library**
   - `syntax.c_style`
   - `syntax.python_style`
   - `syntax.lisp_style`
   - `syntax.forth_style`

3. **Syntax transformation tools**
   - Convert between styles
   - Validate syntax definitions
   - Generate parsers from syntax specs

4. **IDE integration**
   - Syntax-aware highlighting
   - Multi-syntax editing
   - Syntax refactoring

## Conclusion

By making syntax programmable, 1 becomes a **meta-language**—a language for creating languages.

This isn't just a workaround for a technical limitation. It's a fundamental rethinking of what programming languages can be: not fixed notations, but flexible systems where syntax itself becomes a tool for expression.

**In 1, you don't just write in the language—you write the language itself.**
