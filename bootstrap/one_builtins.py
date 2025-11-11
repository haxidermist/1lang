"""
Built-in functions for 1 language.
These are available to all 1 programs.
"""

def builtin_len(value):
    """Get length of string or list"""
    return len(value)

def builtin_substr(s, start, end):
    """Get substring from start to end"""
    return s[start:end]

def builtin_char_at(s, index):
    """Get character at index"""
    if index < 0 or index >= len(s):
        return ""
    return s[index]

def builtin_str_concat(a, b):
    """Concatenate two strings"""
    return str(a) + str(b)

def builtin_str_eq(a, b):
    """Compare two strings"""
    return str(a) == str(b)

def builtin_str_to_int(s):
    """Convert string to integer"""
    try:
        return int(s)
    except ValueError:
        return 0

def builtin_int_to_str(n):
    """Convert integer to string"""
    return str(n)

def builtin_is_digit(s):
    """Check if string is a digit"""
    result = len(s) == 1 and s.isdigit()
    return 1 if result else 0

def builtin_is_alpha(s):
    """Check if string is alphabetic"""
    result = len(s) == 1 and s.isalpha()
    return 1 if result else 0

def builtin_is_alnum(s):
    """Check if string is alphanumeric"""
    result = len(s) == 1 and s.isalnum()
    return 1 if result else 0

def builtin_list_append(lst, item):
    """Append item to list (returns new list)"""
    new_list = lst.copy()
    new_list.append(item)
    return new_list

def builtin_list_get(lst, index):
    """Get item from list at index"""
    if index < 0 or index >= len(lst):
        return None
    return lst[index]

def builtin_list_set(lst, index, value):
    """Set item in list (returns new list)"""
    new_list = lst.copy()
    if 0 <= index < len(lst):
        new_list[index] = value
    return new_list

def builtin_exit(code):
    """Exit program with code"""
    import sys
    sys.exit(code)

# Map of built-in function names to implementations
BUILTINS = {
    'len': builtin_len,
    'substr': builtin_substr,
    'char_at': builtin_char_at,
    'str_concat': builtin_str_concat,
    'str_eq': builtin_str_eq,
    'str_to_int': builtin_str_to_int,
    'int_to_str': builtin_int_to_str,
    'is_digit': builtin_is_digit,
    'is_alpha': builtin_is_alpha,
    'is_alnum': builtin_is_alnum,
    'list_append': builtin_list_append,
    'list_get': builtin_list_get,
    'list_set': builtin_list_set,
    'exit': builtin_exit,
}
