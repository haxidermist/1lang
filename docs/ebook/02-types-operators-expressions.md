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
