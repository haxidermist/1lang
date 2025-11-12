#!/usr/bin/env python3
"""
Generate static HTML book from markdown files
"""
import os
import re

# Chapter files in order
CHAPTERS = [
    ('00-preface.md', 'Preface', 0),
    ('01-tutorial-introduction.md', 'Chapter 1: A Tutorial Introduction', 1),
    ('02-types-operators-expressions.md', 'Chapter 2: Types, Operators, and Expressions', 2),
    ('03-control-flow.md', 'Chapter 3: Control Flow', 3),
    ('04-functions-program-structure.md', 'Chapter 4: Functions and Program Structure', 4),
    ('05-programmable-syntax.md', 'Chapter 5: Programmable Syntax', 5),
    ('06-self-hosting.md', 'Chapter 6: Self-Hosting and Meta-Compilation', 6),
    ('appendix-reference.md', 'Appendix A: Language Reference Manual', 7)
]

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The 1 Programming Language - Complete Book</title>
    <link rel="stylesheet" href="book.css">
</head>
<body>
    <div id="top" class="book-header">
        <h1 class="book-title">The 1 Programming Language</h1>
        <p class="book-subtitle">A Revolutionary Language with Programmable Syntax</p>
        <p class="book-meta">In the style of "The C Programming Language" by Kernighan & Ritchie</p>
    </div>

    <div class="toc">
        <h2>Table of Contents</h2>
        <ul>
{toc}
        </ul>
    </div>

{content}

    <hr>
    <div style="text-align: center; padding: 2em; color: #888;">
        <p><strong>The 1 Programming Language</strong></p>
        <p>Version 1.0 • 2025</p>
        <p><a href="https://github.com/haxidermist/1lang">GitHub Repository</a></p>
        <p style="margin-top: 1em; font-style: italic;">"In 1, code is data, syntax is data, and now 1 can compile 1."</p>
    </div>

    <a href="#top" class="back-to-top" id="backToTop" style="display:none;">↑</a>

    <script>
        // Show back-to-top button on scroll
        window.addEventListener('scroll', function() {{
            const backToTop = document.getElementById('backToTop');
            if (window.pageYOffset > 300) {{
                backToTop.style.display = 'block';
            }} else {{
                backToTop.style.display = 'none';
            }}
        }});
    </script>
</body>
</html>
'''

def escape_html(text):
    """Escape HTML special characters"""
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;'))

def convert_md_to_html(md_text):
    """Basic markdown to HTML conversion"""
    lines = md_text.split('\n')
    html_lines = []
    in_code_block = False
    code_lang = ''
    in_list = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_lang = line[3:].strip()
                html_lines.append('<pre><code>')
            else:
                in_code_block = False
                html_lines.append('</code></pre>')
            i += 1
            continue

        if in_code_block:
            html_lines.append(escape_html(line))
            i += 1
            continue

        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4>{line[5:]}</h4>')
        # Horizontal rule
        elif line.strip() == '---':
            html_lines.append('<hr>')
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{process_inline(line[2:])}</li>')
        elif line.startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
            # Simple numbered list detection
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            content = re.sub(r'^\d+\.\s+', '', line)
            html_lines.append(f'<li>{process_inline(content)}</li>')
        # Blockquote
        elif line.startswith('> '):
            html_lines.append(f'<blockquote>{process_inline(line[2:])}</blockquote>')
        # Empty line
        elif line.strip() == '':
            if in_list:
                html_lines.append('</ul>' if html_lines[-1].endswith('</li>') else '</ol>')
                in_list = False
            html_lines.append('')
        # Regular paragraph
        else:
            if in_list:
                html_lines.append('</ul>' if html_lines[-1].endswith('</li>') else '</ol>')
                in_list = False
            html_lines.append(f'<p>{process_inline(line)}</p>')

        i += 1

    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)

def process_inline(text):
    """Process inline markdown (bold, italic, code, links)"""
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def generate_html_book():
    """Generate the complete HTML book"""
    toc_items = []
    content_sections = []

    for filename, title, idx in CHAPTERS:
        if not os.path.exists(filename):
            print(f"Warning: {filename} not found")
            continue

        # Read markdown
        with open(filename, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert to HTML
        html_content = convert_md_to_html(md_content)

        # Add to TOC
        toc_items.append(f'            <li><a href="#chapter-{idx}">{title}</a></li>')

        # Add chapter section
        nav_prev = f'<a href="#chapter-{idx-1}" class="nav-button">← Previous</a>' if idx > 0 else '<span></span>'
        nav_next = f'<a href="#chapter-{idx+1}" class="nav-button">Next →</a>' if idx < len(CHAPTERS) - 1 else '<span></span>'

        section = f'''
    <div class="chapter" id="chapter-{idx}">
{html_content}
    </div>

    <div class="nav-buttons">
        {nav_prev}
        <a href="#top" class="nav-button">↑ Top</a>
        {nav_next}
    </div>
'''
        content_sections.append(section)

    # Generate final HTML
    toc_html = '\n'.join(toc_items)
    content_html = '\n'.join(content_sections)

    final_html = HTML_TEMPLATE.format(
        toc=toc_html,
        content=content_html
    )

    # Write to file
    with open('static-book.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Generated static-book.html")

    # Also copy to docs
    docs_path = '../docs/ebook/static-book.html'
    if os.path.exists('../docs/ebook'):
        with open(docs_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Copied to {docs_path}")

if __name__ == '__main__':
    generate_html_book()
