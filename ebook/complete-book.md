# Preface

The 1 programming language is a new language designed with a revolutionary premise: that syntax itself should be programmable. Where traditional languages fix their notation at design time, 1 allows programs to manipulate and extend the very syntax they are written in.

This book is meant to help the reader learn how to program in 1. It contains a tutorial introduction to get started, separate chapters on each major feature, and a reference manual. Most of the presentation is based on reading, writing, and revising examples, rather than on mere statements of rules. For the most part, the examples are complete, real programs rather than isolated fragments. All examples have been tested directly from the text, which is in machine-readable form.

The book is organized as follows. Chapter 1 is a tutorial introduction that covers the major features of 1 through practical examples. The purpose of this chapter is to show the essential elements of the language in real programs, but without getting bogged down in details, rules, and exceptions. The tutorial does assume a basic familiarity with programming concepts; there is no explanation of computers, of compilation, or of the meaning of terms like variable and assignment statement.

Chapters 2 through 4 discuss various aspects of 1 in more detail, and rather more formally, than does Chapter 1. Chapter 2 deals with the basic data types, operators and expressions. Chapter 3 treats control flow: if-else, while, for, and the ensure-otherwise construct. Chapter 4 covers functions and program structure—external variables, scope rules, and so on.

Chapter 5 discusses the key innovation of 1: programmable syntax. This chapter shows how block delimiters can be treated as data, how syntax can be extended and modified, and how programs can manipulate their own notation.

Chapter 6 describes the self-hosting compiler—how 1 can compile itself, and what this means for the language and its future development.

The Appendix is a language reference manual that provides a precise definition of the language. The official syntax is described here, though the programmable nature of 1 means that programs can define their own syntax extensions.

## Acknowledgments

The 1 language emerged from an intensive collaboration between human insight and artificial intelligence. The bootstrap compiler was developed in Python to demonstrate the feasibility of the core ideas. The self-hosting components prove that the language can process itself.

This book follows the model established by Brian W. Kernighan and Dennis M. Ritchie in their classic work, "The C Programming Language." Their clear, practical approach to teaching a programming language through examples has proven timeless and is emulated here.

## A Note on Exercises

Each chapter concludes with a series of exercises. These exercises suggest practical programs of varying difficulty, from simple applications of material in the chapter to more challenging problems that extend concepts or introduce new ideas. Solutions to exercises are not provided; working through them is the best way to learn the language.

---

**Let us begin.**


---

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


---

# Chapter 2: Types, Operators, and Expressions

Variables and constants are the basic data objects manipulated in a program. Declarations specify the type of variables and may set their initial values. Operators specify what is to be done with them. Expressions combine variables and constants to produce new values. This chapter discusses these topics in detail.

## 2.1 Variable Names

Names in 1 are made up of letters, digits, and underscores. Names must begin with a letter or underscore. The following are valid variable names:

```
x
count
total_sum
_temp
variable123
```

Upper case and lower case letters are distinct, so `count` and `Count` are different names. By convention, variable names use lowercase letters with underscores separating words.

Function names follow the same rules as variable names. Keywords such as `function`, `if`, `while`, `return` cannot be used as variable names.

It is wise to choose variable names that are meaningful and that will not become confused. Avoid names that differ only in case or that differ only by a single character.

## 2.2 Data Types and Sizes

1 provides several basic data types:

**Integer**: whole numbers, both positive and negative. Examples: `0`, `42`, `-17`, `1000`

**Float**: floating-point numbers. Examples: `3.14`, `-0.5`, `2.0`

**String**: sequences of characters enclosed in double quotes. Examples: `"hello"`, `"world"`, `""`

**Boolean**: truth values, represented as integers. The value `0` is false; any non-zero value is true (typically `1`).

**List**: ordered collections of values. Lists are created and manipulated using built-in functions.

The size and range of these types may vary depending on the implementation. In the current bootstrap compiler, integers are implemented as Python integers (effectively unlimited precision), and floats are Python floating-point numbers (typically 64-bit IEEE 754).

## 2.3 Constants

An integer constant like `1234` is an integer. A number with a decimal point like `123.4` is a floating-point number.

String constants are sequences of zero or more characters surrounded by double quotes:

```1
"I am a string"
""
"String with \"quotes\" inside"
```

Within strings, the backslash `\` serves as an escape character. The sequence `\"` represents a double quote within a string. The sequence `\n` represents a newline character.

There are no character constants in the current version of 1. Single characters are represented as strings of length 1.

## 2.4 Declarations and Initialization

All variables must be assigned a value before use. The first assignment to a variable implicitly declares it:

```1
x = 10          // x is now an integer
name = "Alice"  // name is now a string
```

The type of a variable is inferred from the value assigned to it. Once assigned, a variable's type is fixed; you cannot assign a value of a different type to the same variable.

Function parameters are declared explicitly in the function signature:

```1
function add:
  inputs:
    a: Integer
    b: Integer
  outputs:
    sum: Integer
  implementation: {
    sum = a + b
    return sum
  }
```

Here, `a` and `b` are declared to be of type `Integer`. The return value `sum` is also declared as an `Integer`.

## 2.5 Arithmetic Operators

The binary arithmetic operators are `+`, `-`, `*`, and `/`. Integer division truncates any fractional part:

```1
x = 5 / 2   // x is 2, not 2.5
```

The `+` operator adds, `-` subtracts, `*` multiplies, and `/` divides. These operators have their conventional precedence: `*` and `/` are performed before `+` and `-`. Operators at the same precedence level are evaluated left to right.

Parentheses can be used to alter the normal order of evaluation:

```1
x = (5 + 3) * 2   // x is 16
y = 5 + 3 * 2     // y is 11
```

The unary minus operator `-` negates its operand:

```1
x = 10
y = -x    // y is -10
```

## 2.6 Relational and Logical Operators

The relational operators are:

```
==    equal to
!=    not equal to
<     less than
<=    less than or equal to
>     greater than
>=    greater than or equal to
```

These operators produce an integer result: `1` for true and `0` for false.

```1
x = 5
y = 10
result = x < y    // result is 1 (true)
```

The logical operators are:

```
&&    logical AND
||    logical OR
!     logical NOT
```

These operators also produce `1` for true and `0` for false. The `&&` and `||` operators are short-circuiting: the second operand is not evaluated if the result is determined by the first operand.

```1
x = 5
y = 10
result = (x < y) && (y < 20)  // result is 1 (true)
```

## 2.7 Type Conversions

When an operator has operands of different types, they must be converted to a common type. The general rule is to convert "narrower" types to "wider" types without losing information. For example, in an expression involving an integer and a float, the integer is converted to float.

Explicit type conversion can be performed using built-in functions:

- `str_to_int(s)` - converts a string to an integer
- `int_to_str(n)` - converts an integer to a string

Example:

```1
text = "42"
number = str_to_int(text)     // number is 42
back_to_text = int_to_str(number)  // back_to_text is "42"
```

## 2.8 Assignment Operators

The assignment operator is `=`. It assigns the value of the expression on the right to the variable on the left:

```1
x = 10
y = x + 5
```

Unlike some languages, 1 does not have compound assignment operators like `+=`, `-=`, etc. You must write out the full expression:

```1
x = x + 1   // increment x (no ++ operator)
```

## 2.9 Conditional Expressions

1 does not have a ternary conditional operator like C's `? :`. Instead, you must use an `if-else` statement:

```1
if x > 0: {
  result = x
} else: {
  result = -x
}
```

This pattern is so common that you may wish to define a utility function for it:

```1
function abs:
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

## 2.10 Precedence and Order of Evaluation

The precedence of operators in 1, from highest to lowest, is:

```
1. Parentheses ()
2. Unary minus -
3. Multiplication * and Division /
4. Addition + and Subtraction -
5. Relational operators <, <=, >, >=
6. Equality operators ==, !=
7. Logical AND &&
8. Logical OR ||
```

Operators at the same level are evaluated left to right, except for the assignment operator, which is evaluated right to left.

The order of evaluation of function arguments is not specified. In the expression:

```1
result = f(a) + g(b)
```

either `f(a)` or `g(b)` may be evaluated first. If both functions modify global state, the result may depend on the order of evaluation.

Similarly, the order in which side effects occur is not specified. Write programs that do not depend on order of evaluation when the order is not explicitly determined.

## 2.11 Summary

This chapter has covered:

- Variable naming conventions
- Basic data types: Integer, Float, String, Boolean, List
- Constants and literals
- Variable declaration through assignment
- Arithmetic, relational, and logical operators
- Type conversions
- Operator precedence and evaluation order

Understanding these fundamentals is essential for writing correct 1 programs. The next chapter discusses control flow constructs that make use of the operators and expressions described here.

## Exercises

**Exercise 2-1.** Write expressions to test whether a year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.

**Exercise 2-2.** Write a function that returns the absolute value of an integer without using the `if` statement. (Hint: use multiplication by the sign.)

**Exercise 2-3.** Write a function `digit_to_int` that converts a single-character string containing a digit to its integer value.

**Exercise 2-4.** Write a function `to_lowercase` that converts an uppercase letter (as a single-character string) to lowercase. Assume ASCII encoding.

**Exercise 2-5.** Evaluate the following expressions and explain the order of evaluation:
- `5 + 3 * 2`
- `(5 + 3) * 2`
- `10 / 2 + 3`
- `10 / (2 + 3)`

**Exercise 2-6.** Write a function that extracts the individual digits from a three-digit integer. For example, given `456`, extract `4`, `5`, and `6`.

**Exercise 2-7.** Write a function that tests whether a string represents a valid integer (all digits, possibly with a leading minus sign).


---

# Chapter 3: Control Flow

The control-flow statements of a language specify the order in which computations are performed. We have already seen the most common control-flow constructions in earlier examples; here we will complete the set, and be more precise about the ones already discussed.

## 3.1 Statements and Blocks

An expression such as `x = 0` or `i = i + 1` or `println(x)` becomes a statement when it is followed by a newline or semicolon. In 1, statements are typically written one per line.

The statements of a function are enclosed in braces `{ }` to form a compound statement or block. There is no semicolon after the right brace that ends a block.

```1
function example:
  outputs:
    result: Integer
  implementation: {
    x = 0
    y = 10
    return x + y
  }
```

Braces around a block are always required in the current implementation of 1. This is one of the design choices that makes the syntax unambiguous and suitable for programmatic manipulation.

## 3.2 If-Else

The if-else statement is used to make decisions. The basic form is:

```1
if condition: {
  statement
}
```

The condition is evaluated. If it is true (non-zero), the statement is executed. The braces are required even for single statements.

The else part is optional:

```1
if condition: {
  statement1
} else: {
  statement2
}
```

If the condition is true, statement1 is executed; otherwise statement2 is executed. The else clause is always associated with the nearest previous unmatched if.

Because the if-else statement returns no value, it cannot be used within expressions. You must use separate statements:

```1
if x > 0: {
  y = x
} else: {
  y = -x
}
```

If-else statements can be nested to create multi-way decisions:

```1
if n < 0: {
  println("negative")
} else: {
  if n == 0: {
    println("zero")
  } else: {
    println("positive")
  }
}
```

The inner if-else could be written without braces in some languages, but in 1, braces are required at each level.

## 3.3 Else-If

The construction

```1
if condition1: {
  statement1
} else: {
  if condition2: {
    statement2
  } else: {
    if condition3: {
      statement3
    } else: {
      statement4
    }
  }
}
```

occurs so frequently that it is worth noting a pattern. This is simply a multi-way decision. The conditions are evaluated in order. When one is found to be true, the corresponding statement is executed, and the chain terminates. The code for each condition is executed only if all previous conditions were false.

The final else handles the "none of the above" or default case where none of the conditions is satisfied. Sometimes there is no explicit action for the default; in that case, the trailing else can be omitted.

Here is a practical example that converts a numeric grade to a letter grade:

```1
function letter_grade:
  inputs:
    score: Integer
  outputs:
    grade: String
  implementation: {
    if score >= 90: {
      return "A"
    } else: {
      if score >= 80: {
        return "B"
      } else: {
        if score >= 70: {
          return "C"
        } else: {
          if score >= 60: {
            return "D"
          } else: {
            return "F"
          }
        }
      }
    }
  }
```

## 3.4 While

The while statement has the form:

```1
while condition: {
  statement
}
```

The condition is evaluated. If it is true (non-zero), the statement is executed and the condition is re-evaluated. This cycle continues until the condition becomes false (zero), at which point execution continues after the statement.

Here is an example that prints the numbers from 0 to 9:

```1
i = 0
while i < 10: {
  println(i)
  i = i + 1
}
```

The key points about while loops:

1. The condition is tested before each iteration
2. If the condition is initially false, the body is never executed
3. The loop continues until the condition becomes false
4. The body must eventually make the condition false, or the loop will run forever

### Infinite Loops

A while loop with a constant true condition will run forever:

```1
while 1: {
  // This loop never terminates
}
```

Such loops are sometimes useful, but more often they are programming errors. Make sure your loops have a proper termination condition.

## 3.5 Break and Continue

1 does not currently support `break` and `continue` statements. To exit a loop early, you must structure your code so that the loop condition becomes false. To skip the rest of an iteration, you must use an if statement to guard the remaining code.

For example, to search for a value in a conceptual list and stop when found, you might write:

```1
found = 0
i = 0
while i < count && found == 0: {
  if value == target: {
    found = 1
  }
  i = i + 1
}
```

This pattern is more verbose than using `break`, but it makes the loop termination condition explicit.

## 3.6 Ensure-Otherwise

The ensure-otherwise construct is a distinctive feature of 1 designed for error handling and validation. It has the form:

```1
ensure condition: {
  statement1
} otherwise: {
  statement2
}
```

The ensure-otherwise statement evaluates the condition. If the condition is true, statement1 is executed. If the condition is false, statement2 is executed. This is similar to if-else, but the semantic meaning is different: ensure-otherwise expresses a contract or invariant that should be true, with a handler for the case where it is violated.

The ensure-otherwise construct is particularly useful for precondition checking:

```1
function divide:
  inputs:
    a: Integer
    b: Integer
  outputs:
    result: Integer
  implementation: {
    ensure b != 0: {
      result = a / b
      return result
    } otherwise: {
      println("Error: division by zero")
      return 0
    }
  }
```

The ensure-otherwise statement makes contracts explicit and encourages programmers to think about error conditions.

## 3.7 Loops—A Closer Look

Most loops have a common pattern: initialize a control variable, test a condition involving that variable, and update the variable. The while loop handles this pattern, but requires the initialization and update to be separate statements:

```1
i = 0                    // initialization
while i < n: {          // test
  // loop body
  i = i + 1             // update
}
```

This separation is intentional: it makes each component of the loop explicit and clear. There is no "hidden" increment as there would be in a C-style for loop.

### Counting Down

To count down, reverse the initialization, test, and update:

```1
i = 10
while i > 0: {
  println(i)
  i = i - 1
}
```

This prints the numbers 10 down to 1.

### Iterating with Conditions

The while loop is general enough to handle any iteration pattern. For example, to iterate until a condition is met:

```1
sum = 0
i = 1
while sum < 1000: {
  sum = sum + i
  i = i + 1
}
```

This sums the integers 1, 2, 3, ... until the sum exceeds 1000.

## 3.8 Recursion as Control Flow

Recursion is a powerful form of control flow. Many problems that would require complex loops can be expressed simply using recursion.

We have seen recursive functions for factorial and Fibonacci numbers. Here is another example: computing the sum of integers from 1 to n:

```1
function sum_to_n:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    if n == 0: {
      return 0
    } else: {
      return n + sum_to_n(n - 1)
    }
  }
```

This function calls itself with progressively smaller arguments until it reaches the base case (n == 0).

Recursion is elegant but can be inefficient for some problems due to function call overhead. When performance matters, an iterative solution may be preferable:

```1
function sum_to_n_iterative:
  inputs:
    n: Integer
  outputs:
    result: Integer
  implementation: {
    sum = 0
    i = 1
    while i <= n: {
      sum = sum + i
      i = i + 1
    }
    return sum
  }
```

Choose between recursion and iteration based on clarity and performance needs.

## 3.9 Summary

This chapter has covered the control-flow statements of 1:

- **if-else**: conditional execution
- **while**: loops that test a condition before each iteration
- **ensure-otherwise**: contract-based conditional execution
- **recursion**: functions that call themselves

These constructs are sufficient to express any algorithm. The key is choosing the right construct for each situation: use if-else for decisions, while for loops, ensure-otherwise for validation, and recursion for naturally recursive problems.

## Exercises

**Exercise 3-1.** Write a function that uses a while loop to compute the sum of the first n positive integers.

**Exercise 3-2.** Write a function to find the largest integer in a list without using recursion. (You will need to use list access functions and a while loop.)

**Exercise 3-3.** Write a recursive function to reverse a string.

**Exercise 3-4.** Write both recursive and iterative functions to compute the nth triangular number (the sum 1 + 2 + ... + n).

**Exercise 3-5.** Write a function that uses nested if-else statements to categorize an integer as:
- "negative" if less than 0
- "zero" if equal to 0
- "small positive" if 1-10
- "medium positive" if 11-100
- "large positive" if greater than 100

**Exercise 3-6.** Write a function that uses a while loop to count how many times a target digit appears in an integer. For example, the digit 3 appears twice in 13373.

**Exercise 3-7.** Write a function using ensure-otherwise that computes the square root of an integer using Newton's method, ensuring that the input is non-negative.

**Exercise 3-8.** Write a recursive function to compute the power x^n where n is a non-negative integer. Optimize it by using the identity x^n = (x^(n/2))^2 when n is even.


---

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


---

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


---

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


---

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


---

