# Contributing to 1 Programming Language

Thank you for your interest in contributing to the 1 programming language! This guide will help you get started.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Areas for Contribution](#areas-for-contribution)

---

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/1lang.git
   cd 1lang
   ```
3. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Development Setup

### Requirements
- Python 3.7 or higher
- No external dependencies required

### Testing Your Setup
```bash
# Run the self-hosting demo
python bootstrap/compiler.py compiler/self_hosting_demo.one --run

# Run example programs
python bootstrap/compiler.py examples/hello.one --run
python bootstrap/compiler.py examples/factorial.one --run
```

If these run successfully, your setup is complete!

---

## How to Contribute

### Reporting Bugs

Open an issue with:
- **Clear title** describing the problem
- **Steps to reproduce** the bug
- **Expected behavior** vs **actual behavior**
- **1 code sample** that demonstrates the issue
- **Environment**: OS, Python version

### Suggesting Features

Open an issue with:
- **Clear description** of the feature
- **Use cases** - why is this useful?
- **Example code** showing how it would work
- **Implementation ideas** (if you have any)

### Contributing Code

1. Check existing issues for something to work on
2. Comment on the issue to let others know you're working on it
3. Fork and create a branch
4. Make your changes
5. Test thoroughly
6. Submit a pull request

---

## Code Style

### Python Code (Bootstrap Compiler)

- **PEP 8** style guide
- **Type hints** where appropriate
- **Docstrings** for all functions and classes
- **Comments** for complex logic

Example:
```python
def parse_expression(self) -> Expression:
    """Parse an arithmetic expression.

    Returns:
        Expression AST node
    """
    # Implementation...
```

### 1 Language Code

Follow the style in existing examples:
```1
function example:
  inputs:
    param: Integer
  outputs:
    result: Integer
  implementation: {
    // Clear comments
    result = param + 1
    return result
  }
```

---

## Testing

### Running Tests

```bash
# Run all examples
python bootstrap/compiler.py examples/hello.one --run
python bootstrap/compiler.py examples/factorial.one --run
python bootstrap/compiler.py examples/arithmetic.one --run

# Run self-hosting components
python bootstrap/compiler.py compiler/tokenizer.one --run
python bootstrap/compiler.py compiler/calculator.one --run
python bootstrap/compiler.py compiler/mini_vm.one --run

# Run complete demo
python bootstrap/compiler.py compiler/self_hosting_demo.one --run
```

### Adding Tests

When adding features:
1. Add example program in `examples/`
2. Add test case in self-hosting components if applicable
3. Document expected output

---

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Ensure all tests pass**
4. **Update README.md** if adding user-facing features
5. **Write clear commit messages**:
   ```
   Add feature: programmable block delimiters

   - Implemented brace-delimited blocks
   - Added syntax variable support
   - Updated parser to handle both styles

   Closes #123
   ```
6. **Submit PR** with:
   - Clear description of changes
   - Reference to related issues
   - Example usage if applicable

---

## Areas for Contribution

### High Priority

1. **Full Parser in 1**
   - Complete AST generation in 1 language
   - Type checking in 1
   - Full language support

2. **Optimization**
   - Bytecode optimization passes
   - Constant folding
   - Dead code elimination

3. **Standard Library**
   - More built-in functions
   - String manipulation
   - Data structures

4. **Error Messages**
   - Better error reporting
   - Line/column information
   - Helpful suggestions

### Medium Priority

1. **Language Features**
   - Pattern matching
   - Module system
   - Structs/records
   - Generics

2. **Tools**
   - Syntax highlighter
   - LSP server
   - Debugger
   - REPL

3. **Documentation**
   - Language tutorial
   - API reference
   - More examples
   - Video walkthroughs

### Research Areas

1. **Syntax Evolution**
   - Programs that modify syntax
   - Domain-specific syntaxes
   - Syntax transformation tools

2. **Verification**
   - Formal verification support
   - Constraint solving
   - Proof checking

3. **Performance**
   - JIT compilation
   - Native code generation
   - Optimization strategies

---

## Code of Conduct

- **Be respectful** and inclusive
- **Be constructive** in feedback
- **Focus on ideas**, not people
- **Help others** learn and grow

---

## Questions?

- Open an issue for questions
- Tag with `question` label
- We're here to help!

---

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to the future of programmable syntax!**

🎉 Together we're building something revolutionary! 🎉
