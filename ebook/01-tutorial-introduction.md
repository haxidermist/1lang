# Chapter 1: A Tutorial Introduction

Let us begin with a quick introduction to 1. Our aim is to show the essential elements of the language in real programs, but without getting bogged down in details, formalities, and exceptions. At this point, we are not trying to be complete or even precise (except in the examples). We want to get you as quickly as possible to the point where you can write useful programs, and to do that we have to concentrate on the basics: types, functions, control flow, and the distinctive feature of 1—programmable syntax. This chapter is meant to be an introduction, not a reference manual. Subsequent chapters will elaborate on the ideas presented here.

The best way to learn a new programming language is to write programs in it. The typical program to start with is one that prints "Hello, World!" on the screen. In 1, this is:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    println("Hello, World!")
    return 0
  }
```

Just type this into a file named `hello.one`, then compile and run it with:

```bash
python bootstrap/compiler.py hello.one --run
```

The program will print:

```
Hello, World!
```

## 1.1 Getting Started

A 1 program consists of function definitions. The mandatory starting point is the function named `main`. The `main` function specifies its outputs (in this case, an integer exit code), and contains an `implementation` block that defines what the function does.

Every function in 1 declares its inputs and outputs explicitly. Even a simple program like "Hello, World" must specify that it returns an integer exit code. This explicitness is a fundamental design principle of 1.

The statement

```1
println("Hello, World!")
```

calls the built-in function `println`, which prints its argument followed by a newline. The function `println` is one of several built-in functions provided by the 1 environment.

Notice the braces `{ }` around the implementation. These are block delimiters. In 1, blocks can be delimited explicitly with braces, or implicitly through indentation (though the current implementation focuses on explicit braces). We will return to this programmable syntax feature in Chapter 5.

The `return` statement gives back a value to the caller. Here, returning 0 conventionally indicates successful completion.

## 1.2 Variables and Arithmetic

The next program computes and prints a simple arithmetic result:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    x = 10
    y = 20
    sum = x + y
    println(sum)
    return 0
  }
```

This prints `30`. The three lines

```1
x = 10
y = 20
sum = x + y
```

declare and initialize three variables. In 1, you assign values to variables using `=`. The type of each variable is inferred from the value assigned to it. Here, all three variables are integers.

1 provides the usual arithmetic operators: `+` for addition, `-` for subtraction, `*` for multiplication, and `/` for division. These work on integers and floating-point numbers.

The division operator `/` performs integer division when both operands are integers, and floating-point division when either operand is a floating-point number.

## 1.3 The For Statement

Let us write a program to print a table of values. We will use a `while` loop, the basic iteration construct in 1:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    i = 0
    while i < 10: {
      println(i)
      i = i + 1
    }
    return 0
  }
```

This prints the numbers 0 through 9, one per line.

The `while` statement repeatedly executes its body (the statements in braces) as long as the condition `i < 10` is true. The body consists of two statements: one that prints the current value of `i`, and one that increments `i`. After each iteration, the condition is tested again.

## 1.4 Symbolic Constants and Character Strings

In 1, string literals are enclosed in double quotes. We have already seen examples of strings passed to `println`. Strings are a basic data type in 1.

Here is a program that uses several strings:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    greeting = "Hello"
    name = "World"
    combined = str_concat(greeting, str_concat(", ", name))
    println(combined)
    return 0
  }
```

This prints `Hello, World`. The built-in function `str_concat` concatenates two strings. Notice that we must explicitly concatenate strings; 1 does not automatically join adjacent string literals.

## 1.5 A Collection of Useful Programs

We are now going to write a few useful programs to demonstrate more of 1's features. These examples will introduce functions with parameters, recursion, and conditional statements.

### 1.5.1 Factorial

Here is a function that computes the factorial of a number using recursion:

```1
function factorial:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n == 0: {
      return 1
    } else: {
      return n * factorial(n - 1)
    }
  }

function main:
  outputs:
    exit_code: Integer
  implementation: {
    result = factorial(5)
    println(result)
    return 0
  }
```

This program prints `120`, which is 5 factorial (5! = 5 × 4 × 3 × 2 × 1).

The `factorial` function demonstrates several features:

1. **Function parameters**: The `inputs:` section declares that `factorial` takes one parameter, `n`, which must be an integer.

2. **Function return values**: The `outputs:` section declares that the function returns an integer called `result`.

3. **Conditional execution**: The `if-else` statement tests whether `n == 0`. If so, it returns 1 (the base case). Otherwise, it computes `n * factorial(n - 1)` recursively.

4. **Recursion**: The function calls itself with a smaller argument.

### 1.5.2 Fibonacci

Here is a function that computes Fibonacci numbers:

```1
function fibonacci:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n == 0: {
      return 0
    } else: {
      if n == 1: {
        return 1
      } else: {
        return fibonacci(n - 1) + fibonacci(n - 2)
      }
    }
  }

function main:
  outputs:
    exit_code: Integer
  implementation: {
    result = fibonacci(8)
    println(result)
    return 0
  }
```

This prints `21`, the 8th Fibonacci number.

Notice how we can nest `if-else` statements. The function has three cases: if `n` is 0, return 0; if `n` is 1, return 1; otherwise, return the sum of the two previous Fibonacci numbers.

## 1.6 Arguments—Call by Value

In 1, function arguments are passed by value. This means that when a function is called, each argument expression is evaluated, and its value is copied to the corresponding parameter. Changes to parameters inside a function do not affect the arguments in the caller.

For example:

```1
function increment:
  inputs:
    x: Integer
  outputs:
    result: Integer
  implementation: {
    x = x + 1
    return x
  }

function main:
  outputs:
    exit_code: Integer
  implementation: {
    a = 10
    b = increment(a)
    println(a)  // Prints 10
    println(b)  // Prints 11
    return 0
  }
```

The variable `a` is not changed by the call to `increment`; only the parameter `x` (a copy of `a`) is incremented.

## 1.7 Character Arrays and String Manipulation

1 provides several built-in functions for working with strings:

- `len(s)` - returns the length of string `s`
- `substr(s, start, end)` - returns a substring from position `start` to `end`
- `char_at(s, index)` - returns the character at position `index`
- `str_concat(s1, s2)` - concatenates two strings
- `str_eq(s1, s2)` - tests if two strings are equal

Here is a program that uses these functions:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    text = "Hello, World!"
    length = len(text)
    println(length)  // Prints 13

    first_five = substr(text, 0, 5)
    println(first_five)  // Prints "Hello"

    first_char = char_at(text, 0)
    println(first_char)  // Prints "H"

    return 0
  }
```

String indices start at 0, as in most modern programming languages.

## 1.8 External Variables and Scope

In the examples so far, all variables have been local to the functions in which they are declared. Such variables come into existence when the function is called and disappear when the function returns.

Functions can also access variables declared at the global scope (outside of any function), but the current implementation of 1 does not yet support global variables. All variables must be declared within functions.

Within a function, variables can be declared anywhere. A variable exists from the point of its first assignment to the end of the block containing that assignment.

## 1.9 Summary

This chapter has covered the basic elements of 1:

- Functions with explicit inputs and outputs
- Basic data types: integers, strings
- Arithmetic and comparison operators
- Control flow: `if-else` and `while`
- Recursion
- Built-in functions for I/O and string manipulation
- Block delimiters using braces

We have not covered all the features of 1, but we have seen enough to write useful programs. The following chapters will fill in the details.

## Exercises

**Exercise 1-1.** Write a program that prints the numbers 1 through 100, one per line.

**Exercise 1-2.** Write a function `power` that computes x raised to the power n (x^n) for non-negative integer n.

**Exercise 1-3.** Write a function to compute the greatest common divisor (GCD) of two integers using Euclid's algorithm.

**Exercise 1-4.** Write a program that prints a multiplication table for the numbers 1 through 10.

**Exercise 1-5.** Write a function `is_prime` that tests whether a given integer is prime.

**Exercise 1-6.** Write a function that reverses a string by using `substr` and `str_concat` to build up the reversed string.

**Exercise 1-7.** Write a function `count_chars` that counts the number of times a given character appears in a string.

**Exercise 1-8.** Write an iterative (non-recursive) version of the factorial function.
