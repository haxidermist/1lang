# The 1 Programming Language (eBook)

This directory contains the complete book "The 1 Programming Language" in the style of "The C Programming Language" by Kernighan and Ritchie.

## Reading the Book

Start with: **[THE-1-PROGRAMMING-LANGUAGE.md](THE-1-PROGRAMMING-LANGUAGE.md)**

This is the main entry point with the full table of contents and links to all chapters.

## Book Structure

The book consists of:

- **[Preface](00-preface.md)** - Introduction and acknowledgments
- **[Chapter 1](01-tutorial-introduction.md)** - A Tutorial Introduction
- **[Chapter 2](02-types-operators-expressions.md)** - Types, Operators, and Expressions
- **[Chapter 3](03-control-flow.md)** - Control Flow
- **[Chapter 4](04-functions-program-structure.md)** - Functions and Program Structure
- **[Chapter 5](05-programmable-syntax.md)** - Programmable Syntax (Key Innovation!)
- **[Chapter 6](06-self-hosting.md)** - Self-Hosting and Meta-Compilation
- **[Appendix A](appendix-reference.md)** - Language Reference Manual

## Book Features

- **Progressive Examples**: Each chapter builds on previous concepts
- **Complete Code**: All examples are complete, runnable programs
- **Exercises**: Each chapter ends with practice exercises
- **K&R Style**: Clear, concise, practical approach
- **Reference Manual**: Precise language specification

## Running Examples

All code examples in this book can be run:

```bash
cd /path/to/1lang
python bootstrap/compiler.py your_program.one --run
```

## Formats

Currently available in:
- **Markdown** - All chapters as separate .md files
- **Combined** - THE-1-PROGRAMMING-LANGUAGE.md with links

## Future Formats

Planned conversions:
- PDF (via pandoc)
- EPUB (for e-readers)
- HTML (web version)
- LaTeX (for print)

## Generating Other Formats

### PDF (requires pandoc)

```bash
# Combine all chapters
cat 00-preface.md \
    01-tutorial-introduction.md \
    02-types-operators-expressions.md \
    03-control-flow.md \
    04-functions-program-structure.md \
    05-programmable-syntax.md \
    06-self-hosting.md \
    appendix-reference.md > complete-book.md

# Convert to PDF
pandoc complete-book.md -o the-1-programming-language.pdf --toc
```

### EPUB (requires pandoc)

```bash
pandoc complete-book.md -o the-1-programming-language.epub --toc
```

### HTML (requires pandoc)

```bash
pandoc complete-book.md -o the-1-programming-language.html -s --toc
```

## Contributing

Found a typo or error? Suggestions for improvements?

Please open an issue or submit a pull request to the main repository.

## License

This book is released under the MIT License, same as the 1 programming language.

## About the Style

This book follows the style of "The C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie, widely considered one of the best programming language books ever written. Their approach:

- Start with practical examples
- Build concepts progressively
- Include exercises for practice
- Provide a precise reference manual
- Keep explanations clear and concise

## Reading Guide

**For Beginners**: Start with Chapter 1 and work through sequentially. Do the exercises.

**For Experienced Programmers**: Skim Chapter 1, focus on Chapters 5-6 for unique features.

**For Language Implementers**: Read all chapters, study the self-hosting components in `../compiler/`.

## Chapters at a Glance

| Chapter | Topic | Key Concepts |
|---------|-------|--------------|
| 1 | Tutorial | Hello World, Variables, Functions, Recursion |
| 2 | Types & Operators | Integer, String, Arithmetic, Logic |
| 3 | Control Flow | if-else, while, ensure-otherwise |
| 4 | Functions | Parameters, Return Values, Scope |
| 5 | Programmable Syntax | **The Revolutionary Feature** |
| 6 | Self-Hosting | **Compiler Written in 1** |
| Appendix | Reference | Formal Language Specification |

## Page Count Estimate

- Total: ~150-200 pages (printed)
- Chapter 1: ~25 pages
- Chapter 2: ~20 pages
- Chapter 3: ~20 pages
- Chapter 4: ~20 pages
- Chapter 5: ~25 pages
- Chapter 6: ~25 pages
- Appendix: ~20 pages

---

**Enjoy learning the 1 programming language!**

*"In 1, code is data, syntax is data, and now 1 can compile 1."*
