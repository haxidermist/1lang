# Chapter 5: Programmable Syntax

Most programming languages fix their syntax at design time. Once the language is defined, programmers must work within the constraints of that syntax. The 1 programming language breaks this tradition with a revolutionary feature: **programmable syntax**. In 1, syntax itself is data that programs can manipulate.

This chapter introduces the concept of programmable syntax, shows how it works in practice, and explores its implications for language design and program development.

## 5.1 The Problem with Fixed Syntax

Traditional programming languages make a fundamental assumption: the notation in which programs are written is fixed. Programmers adapt their thinking to the language's syntax. While this provides consistency, it also creates limitations:

1. **Domain mismatch**: The language's syntax may not match the problem domain
2. **Evolution constraints**: Adding new syntax features requires changing the compiler
3. **Notation rigidity**: Programmers cannot choose the most natural notation for their problem

Consider a simple example: block delimiters. Some languages use braces `{ }`, others use `begin/end`, and still others use indentation. Each choice has advocates, but programmers must accept the language designer's decision.

## 5.2 Syntax as Data

The key insight of 1 is that syntax elements—such as block delimiters, keywords, and operators—can be treated as data. Just as a program can manipulate strings, integers, and lists, a program can manipulate its own syntax.

In 1, block delimiters are not hardcoded into the parser. Instead, they are configurable:

```1
// Current default: braces for blocks
function example:
  outputs:
    result: Integer
  implementation: {
    x = 10
    return x
  }
```

The braces `{` and `}` are the current block delimiters, but these could be changed:

```
// Hypothetical: using begin/end
function example:
  outputs:
    result: Integer
  implementation: begin
    x = 10
    return x
  end
```

The parser treats block delimiters as parameters, not as fixed tokens.

## 5.3 Block Delimiters

The current implementation of 1 uses braces `{` and `}` as block delimiters. This choice was made to enable rapid development and to work around limitations in indentation-based parsing.

Braces provide several advantages:

1. **Explicit boundaries**: No ambiguity about where a block begins and ends
2. **Nesting clarity**: Easy to see nested structures
3. **Machine-friendly**: Simple to parse programmatically
4. **Editor-independent**: No dependence on tab/space settings

Example with nested blocks:

```1
function absolute_value:
  inputs:
    x: Integer
  outputs:
    result: Integer
  implementation: {
    if x >= 0: {
      return x
    } else: {
      return -x
    }
  }
```

The braces make the nesting structure explicit.

## 5.4 Alternative Syntaxes

While the current implementation uses braces, the design of 1 allows for alternative syntaxes. A future version might support:

**Indentation-based blocks:**
```1
function example:
  outputs:
    result: Integer
  implementation:
    x = 10
    return x
```

**Keyword-based blocks:**
```1
function example:
  outputs:
    result: Integer
  implementation:
    begin
      x = 10
      return x
    end
```

**Custom delimiters:**
```1
function example:
  outputs:
    result: Integer
  implementation: [
    x = 10
    return x
  ]
```

The key is that the syntax is not fixed in the language definition. It can be specified and changed.

## 5.5 Syntax Variables (Future Feature)

The full vision of programmable syntax includes syntax variables—identifiers that hold syntax rules. A future version of 1 might include:

```1
syntax block_delimiters: {
  open: "{"
  close: "}"
}

syntax keywords: {
  function: "function"
  if: "if"
  while: "while"
  return: "return"
}
```

With these declarations, programs could modify their own syntax:

```1
syntax block_delimiters: {
  open: "begin"
  close: "end"
}

// Now use the new syntax
function example:
  outputs:
    result: Integer
  implementation: begin
    x = 10
    return x
  end
```

This is not yet implemented, but it demonstrates the direction of the language.

## 5.6 With-Syntax Blocks (Future Feature)

To enable localized syntax changes, 1 might support `with_syntax` blocks:

```1
with_syntax block_delimiters = indent_based:
  function example:
    outputs:
      result: Integer
    implementation:
      x = 10
      return x
```

Inside the `with_syntax` block, the specified syntax rules apply. Outside, the default syntax is restored.

This allows different parts of a program to use different syntaxes, or even different programs to collaborate with different notational preferences.

## 5.7 Parsing Programs in 1

One of the most powerful applications of programmable syntax is that 1 programs can parse and manipulate other 1 programs. The self-hosting compiler demonstrates this:

```1
// From compiler/tokenizer.one
function tokenize:
  inputs:
    source: String
  outputs:
    token_count: Integer
  implementation: {
    pos = 0
    tokens = 0
    source_len = len(source)

    while pos < source_len: {
      c = char_at(source, pos)
      // Recognize tokens based on syntax rules...
      tokens = tokens + 1
      pos = pos + 1
    }

    return tokens
  }
```

This function, written in 1, can tokenize 1 source code. Because syntax is data, the tokenizer can access and use the same syntax rules that the parser uses.

## 5.8 Implications of Programmable Syntax

Programmable syntax has profound implications:

### 1. Domain-Specific Languages

Programmers can define syntax that matches their problem domain:

```1
// Mathematical notation
syntax operators: {
  "∀": "forall"
  "∃": "exists"
  "∈": "element_of"
}

// Now use mathematical symbols in code
```

### 2. Language Evolution

The language can evolve without breaking existing code:

```1
// Old syntax still works
function old_style: { ... }

// New syntax also works
function new_style: begin ... end
```

### 3. Multi-Paradigm Support

Different programming paradigms can coexist with their natural syntax:

```1
// Functional style with one syntax
// Imperative style with another syntax
// Logic programming with yet another
```

### 4. Meta-Programming

Programs can generate and manipulate programs:

```1
function generate_parser:
  inputs:
    syntax_rules: String
  outputs:
    parser_code: String
  implementation: {
    // Generate a parser based on syntax rules
    return generated_code
  }
```

## 5.9 Syntax Transformations

With programmable syntax, transformations between syntactic styles become first-class operations:

```1
function transform_syntax:
  inputs:
    code: String
    from_syntax: String
    to_syntax: String
  outputs:
    transformed: String
  implementation: {
    // Parse code using from_syntax
    // Generate code using to_syntax
    return result
  }
```

This could enable automatic translation between different coding styles, or adaptation of code to different contexts.

## 5.10 Current Limitations

The current implementation of 1 does not yet fully realize the vision of programmable syntax. Current limitations include:

1. **Fixed block delimiters**: Braces are required; indentation-based syntax is not yet supported
2. **No syntax variables**: Cannot declare or modify syntax rules
3. **No with-syntax blocks**: Cannot localize syntax changes
4. **Limited token types**: The parser recognizes a fixed set of token types

These limitations will be addressed in future versions as the language evolves.

## 5.11 Design Principles

The design of programmable syntax follows several principles:

1. **Explicitness**: Syntax rules should be declared explicitly, not inferred
2. **Locality**: Syntax changes should be scoped to avoid action-at-a-distance
3. **Compatibility**: Different syntax styles should be able to coexist
4. **Simplicity**: The mechanism for specifying syntax should itself be simple

These principles ensure that programmable syntax enhances rather than complicates the language.

## 5.12 Comparison with Other Languages

Other languages have approached syntax flexibility in different ways:

**Lisp**: Homoiconic (code is data), but syntax is uniform S-expressions
**Racket**: #lang mechanism allows different languages in same file
**Scala/Kotlin**: Operator overloading and DSL support
**Template Haskell**: Compile-time metaprogramming

1's approach is unique: syntax itself (not just code structure) is data that can be manipulated. This is **meta-homoiconicity**—not just "code is data" but "syntax is data."

## 5.13 Practical Applications

Even with current limitations, programmable syntax enables practical applications:

### 1. Code Generation

Generate 1 code with the desired syntax style:

```1
function generate_function:
  inputs:
    name: String
    use_braces: Integer
  outputs:
    code: String
  implementation: {
    if use_braces == 1: {
      return code_with_braces
    } else: {
      return code_with_indents
    }
  }
```

### 2. Syntax Checking

Verify that code follows a particular syntax style:

```1
function check_syntax_style:
  inputs:
    code: String
    required_style: String
  outputs:
    compliant: Integer
  implementation: {
    // Parse and verify syntax style
    return result
  }
```

### 3. Transpilation

Convert between different syntax styles:

```1
function convert_to_braces:
  inputs:
    indented_code: String
  outputs:
    braced_code: String
  implementation: {
    // Transform indentation to braces
    return result
  }
```

## 5.14 Summary

Programmable syntax is the defining feature of the 1 programming language. While the current implementation provides a foundation through explicit block delimiters, the full vision includes:

- Syntax rules as first-class data
- Localized syntax modifications
- Multiple syntax styles coexisting
- Programs that manipulate syntax

This chapter has introduced the concept and shown its current state and future direction. The next chapter explores how programmable syntax enables self-hosting—the ability of 1 to compile itself.

## Exercises

**Exercise 5-1.** Write a function that converts a simple expression from infix notation (a + b) to prefix notation (+ a b).

**Exercise 5-2.** Design a syntax rule structure for a hypothetical future version of 1 that supports syntax variables. What fields would it need?

**Exercise 5-3.** Write a function that checks whether a string of braces is balanced (every `{` has a matching `}`).

**Exercise 5-4.** Sketch how you would implement a parser that could use either braces or begin/end keywords based on a parameter.

**Exercise 5-5.** Consider the implications of allowing programs to modify their own syntax at runtime. What problems might this create? How could they be prevented?

**Exercise 5-6.** Design a notation for mathematical expressions and describe how you would implement a parser for it in 1.

**Exercise 5-7.** Write a function that takes code in one style (braced) and adds indentation to make the structure more visible.

**Exercise 5-8.** Research homoiconicity in Lisp. How does 1's programmable syntax differ from Lisp's homoiconicity? What can each approach do that the other cannot?
