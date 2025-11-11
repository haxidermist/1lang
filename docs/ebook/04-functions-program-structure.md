# Chapter 4: Functions and Program Structure

Functions break large computing tasks into smaller ones, and enable people to build on what others have done instead of starting over from scratch. Appropriate functions hide details of operation from parts of the program that don't need to know about them, thus clarifying the whole, and easing the pain of making changes.

1 has been designed to make functions efficient and easy to use; 1 programs generally consist of many small functions rather than a few big ones. A program may reside in one or more source files. Source files may be compiled separately and loaded together. This chapter discusses these aspects of program structure.

## 4.1 Basics of Functions

We have already seen and used many functions. Let us now look at them more systematically. Here is a function that computes the power x^n for positive integer n:

```1
function power:
  inputs:
    base: Integer
    exponent: Integer
  outputs:
    result: Integer
  implementation: {
    p = 1
    i = 0
    while i < exponent: {
      p = p * base
      i = i + 1
    }
    return p
  }
```

A function definition has three parts:

1. **Signature**: The function name (`power`), inputs, and outputs
2. **Inputs section**: Declares the parameters with their types
3. **Outputs section**: Declares the return value(s) with types
4. **Implementation**: The body of the function in braces

The return statement provides the value that the function returns. A function must return a value of the declared output type.

To call this function:

```1
result = power(2, 10)  // result is 1024
```

## 4.2 Functions Returning Non-Integer Values

Functions can return any type. Here is a function that returns a string:

```1
function greet:
  inputs:
    name: String
  outputs:
    message: String
  implementation: {
    hello = "Hello, "
    exclaim = "!"
    message = str_concat(hello, str_concat(name, exclaim))
    return message
  }
```

The output type is `String`, and the function returns a string value.

## 4.3 More on Function Arguments

In 1, all function arguments are passed by value. This means the function receives a copy of the argument value, not the argument itself. Changes to parameters inside the function do not affect the caller's variables.

```1
function try_to_modify:
  inputs:
    x: Integer
  outputs:
    result: Integer
  implementation: {
    x = x + 100
    return x
  }

function main:
  outputs:
    exit_code: Integer
  implementation: {
    a = 5
    b = try_to_modify(a)
    println(a)  // Prints 5 (unchanged)
    println(b)  // Prints 105
    return 0
  }
```

The parameter `x` is a copy of `a`. Modifying `x` does not change `a`.

For efficiency reasons, you might expect that passing large strings or data structures would be expensive. However, the implementation may optimize this by using copy-on-write or other techniques, so passing values is not necessarily inefficient.

## 4.4 External Variables and Scope

The variables declared within a function are local to that function; they come into existence when the function is called and disappear when the function returns. These are called *automatic variables* because they automatically appear and disappear.

It is possible to have variables that are external to all functions, but the current implementation of 1 does not support global variables. All variables must be declared within functions.

However, functions can call other functions, and through their parameters and return values, they can share information:

```1
function compute:
  inputs:
    x: Integer
  outputs:
    result: Integer
  implementation: {
    temp = helper(x)
    return temp * 2
  }

function helper:
  inputs:
    y: Integer
  outputs:
    result: Integer
  implementation: {
    return y + 1
  }
```

## 4.5 Scope Rules

The scope of a name is the part of the program within which the name can be used. For an automatic variable declared in a function, the scope is the function in which the name is declared.

Parameters of a function are in the scope of the function. They act as local variables, initialized by the values passed when the function is called.

Because 1 does not have global variables, there is no ambiguity about which variable a name refers to: it is always the parameter or local variable in the current function.

## 4.6 Header Comments and Documentation

It is good practice to document what each function does, what its parameters mean, and what it returns. This is typically done with comments before the function:

```1
// factorial computes n! for non-negative integers.
// Returns 1 for n = 0.
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
```

Comments in 1 begin with `//` and extend to the end of the line.

The explicit declaration of inputs and outputs makes 1 functions somewhat self-documenting, but additional comments explaining the purpose and any preconditions or post conditions are valuable.

## 4.7 Static Variables

Unlike C, 1 does not have static variables (variables that retain their value between function calls). Each time a function is called, its local variables are initialized fresh.

If you need to maintain state between function calls, you must do so through parameters and return values, or (in a future version of 1) through external state management.

## 4.8 Recursion

A function may call itself either directly or indirectly. We have seen several examples of direct recursion. Here is an example of indirect recursion:

```1
function is_even:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n == 0: {
      return 1
    } else: {
      return is_odd(n - 1)
    }
  }

function is_odd:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n == 0: {
      return 0
    } else: {
      return is_even(n - 1)
    }
  }
```

These two functions call each other recursively to determine whether a number is even or odd (assuming non-negative integers).

Recursion is a powerful technique, but it has costs: each recursive call uses stack space, and function call overhead can make recursion slower than iteration. Use recursion when it makes the code clearer, but be aware of the performance implications.

## 4.9 The Main Function

Every 1 program must have a function named `main`. This is where execution begins. The `main` function should return an integer exit code:

```1
function main:
  outputs:
    exit_code: Integer
  implementation: {
    // Program logic here
    return 0
  }
```

By convention, returning 0 indicates successful execution, and returning non-zero indicates an error.

The main function can call any other functions, read input, produce output, and perform any computations needed.

## 4.10 Program Organization

A 1 program consists of one or more functions. These functions are typically organized in a single source file, but could be split across multiple files (in a future version with a module system).

Functions should be ordered so that each function is defined before it is called, or all functions should be declared before they are used (in a future version with forward declarations).

The typical organization is:

1. Comments describing the program
2. Helper functions (in order of dependency)
3. Main function

For example:

```1
// Program to compute combinations C(n,k) = n! / (k! * (n-k)!)

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

function combination:
  inputs:
    n: Integer
    k: Integer
  outputs:
    result: Integer
  implementation: {
    nfact = factorial(n)
    kfact = factorial(k)
    nkfact = factorial(n - k)
    return nfact / (kfact * nkfact)
  }

function main:
  outputs:
    exit_code: Integer
  implementation: {
    result = combination(5, 2)  // C(5,2) = 10
    println(result)
    return 0
  }
```

## 4.11 Built-in Functions

1 provides a set of built-in functions for common operations. These functions are always available without any import or declaration.

**String functions:**
- `len(s)` - length of string s
- `substr(s, start, end)` - substring from start to end
- `char_at(s, index)` - character at position index
- `str_concat(s1, s2)` - concatenate two strings
- `str_eq(s1, s2)` - test string equality
- `str_to_int(s)` - convert string to integer
- `int_to_str(n)` - convert integer to string

**Character testing:**
- `is_digit(c)` - returns 1 if c is a digit
- `is_alpha(c)` - returns 1 if c is a letter
- `is_alnum(c)` - returns 1 if c is alphanumeric

**List functions:**
- `list_append(list, item)` - append item to list
- `list_get(list, index)` - get item at index
- `list_set(list, index, value)` - set item at index

**I/O functions:**
- `print(s)` - print string without newline
- `println(s)` - print string with newline

These built-in functions are implemented by the runtime system and provide essential functionality.

## 4.12 Summary

Functions are the building blocks of 1 programs. This chapter has covered:

- Function definition syntax with explicit inputs and outputs
- Pass-by-value parameter passing
- Local variables and scope
- Recursion
- The main function
- Built-in functions
- Program organization

Well-designed functions make programs easier to understand, test, and modify. Each function should have a single, well-defined purpose, and its interface (inputs and outputs) should be clear.

## Exercises

**Exercise 4-1.** Write a function `swap` that takes two integers as input and returns them in opposite order (requires returning multiple values, which is not yet supported; for now, just document how you would design this).

**Exercise 4-2.** Write a function `min` that returns the smaller of two integers, and a function `max` that returns the larger.

**Exercise 4-3.** Write a function `min_of_three` that returns the smallest of three integers using the `min` function from the previous exercise.

**Exercise 4-4.** Write a recursive function to compute the sum of the digits of a non-negative integer.

**Exercise 4-5.** Write a function `str_reverse` that reverses a string using recursion. Compare it with an iterative version.

**Exercise 4-6.** Write a function `count_substring` that counts how many times a substring appears in a string.

**Exercise 4-7.** Write mutually recursive functions to implement a simple parser for nested parentheses.

**Exercise 4-8.** Organize a program with multiple functions to compute the first n prime numbers. Use helper functions for testing primality and generating candidates.
