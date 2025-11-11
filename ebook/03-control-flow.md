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
