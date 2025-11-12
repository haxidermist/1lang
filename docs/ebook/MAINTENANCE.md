# eBook Maintenance Guide

This guide explains how to maintain and update "The 1 Programming Language" ebook.

---

## Table of Contents

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [Editing Chapters](#editing-chapters)
4. [Regenerating HTML](#regenerating-html)
5. [Testing Locally](#testing-locally)
6. [Publishing Updates](#publishing-updates)
7. [Adding New Chapters](#adding-new-chapters)
8. [Troubleshooting](#troubleshooting)

---

## Overview

The ebook uses a static HTML generation system:

- **Source**: Markdown files (`.md`) for each chapter
- **Generator**: Python script (`generate_html.py`)
- **Output**: Static HTML file (`index.html`)
- **Hosting**: GitHub Pages serves from `docs/ebook/`

**Why Static HTML?**

GitHub Pages has restrictions on dynamic JavaScript fetch() calls. The static HTML approach embeds all content in a single file, avoiding CORS issues and ensuring reliable loading.

---

## File Structure

```
ebook/
├── 00-preface.md                    # Source: Preface
├── 01-tutorial-introduction.md      # Source: Chapter 1
├── 02-types-operators-expressions.md # Source: Chapter 2
├── 03-control-flow.md               # Source: Chapter 3
├── 04-functions-program-structure.md # Source: Chapter 4
├── 05-programmable-syntax.md        # Source: Chapter 5
├── 06-self-hosting.md               # Source: Chapter 6
├── appendix-reference.md            # Source: Appendix A
│
├── generate_html.py                 # HTML generator script
├── book.css                         # Stylesheet
├── index.html                       # Generated HTML (93KB)
├── static-book.html                 # Backup copy
├── complete-book.md                 # Combined markdown
│
├── THE-1-PROGRAMMING-LANGUAGE.md    # Markdown TOC
└── README.md                        # This directory's README

docs/ebook/                          # Mirror for GitHub Pages
├── (same markdown files)
├── index.html                       # Generated HTML (copy)
└── book.css                         # Stylesheet (copy)
```

---

## Editing Chapters

### Step 1: Edit the Markdown File

Edit any chapter file in the `ebook/` directory:

```bash
cd C:/work/AI/1lang/ebook

# Edit a chapter (use your preferred editor)
code 01-tutorial-introduction.md
# or
vim 02-types-operators-expressions.md
# or
notepad 03-control-flow.md
```

### Step 2: Follow Markdown Conventions

The generator supports:

**Headers:**
```markdown
# Chapter Title (H1)
## Section Title (H2)
### Subsection Title (H3)
#### Sub-subsection Title (H4)
```

**Code Blocks:**
````markdown
```1
function example:
  outputs:
    result: Integer
  implementation: {
    return 42
  }
```
````

**Inline Code:**
```markdown
Use `variable_name` for inline code.
```

**Emphasis:**
```markdown
*italic text*
**bold text**
```

**Links:**
```markdown
[Link Text](https://example.com)
```

**Lists:**
```markdown
- Item 1
- Item 2
  - Nested item

1. First item
2. Second item
```

**Horizontal Rules:**
```markdown
---
```

**Blockquotes:**
```markdown
> This is a quote
```

---

## Regenerating HTML

### Quick Regeneration

After editing any markdown file(s):

```bash
cd C:/work/AI/1lang/ebook
python3 generate_html.py
```

**Output:**
```
Generated static-book.html
Copied to ../docs/ebook/static-book.html
```

The script:
1. Reads all chapter markdown files in order
2. Converts markdown to HTML
3. Combines into single HTML file
4. Generates table of contents with anchor links
5. Adds navigation buttons between chapters
6. Writes to `index.html` and `docs/ebook/index.html`

### What Gets Generated

- **`ebook/static-book.html`** - Generated HTML (backup)
- **`ebook/index.html`** - Copy of static-book.html
- **`docs/ebook/static-book.html`** - Copy for GitHub Pages
- **`docs/ebook/index.html`** - Copy for GitHub Pages

### Manual Copy (if needed)

If the script doesn't auto-copy to docs:

```bash
cd C:/work/AI/1lang/ebook
cp static-book.html index.html
cp static-book.html ../docs/ebook/index.html
```

---

## Testing Locally

### Before Publishing

Always test locally before pushing to GitHub:

**Method 1: Direct Browser Open**
```bash
cd C:/work/AI/1lang/ebook
start index.html  # Windows
# or
open index.html   # Mac
# or
xdg-open index.html  # Linux
```

**Method 2: Local Web Server (Recommended)**

Python 3:
```bash
cd C:/work/AI/1lang/ebook
python3 -m http.server 8000
```

Then visit: http://localhost:8000/index.html

**Method 3: VS Code Live Server**

If using VS Code:
1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"

### What to Check

- ✅ All chapters appear in table of contents
- ✅ Clicking TOC links jumps to correct chapters
- ✅ Code blocks are properly formatted
- ✅ Navigation buttons work (Previous/Next/Top)
- ✅ Back-to-top button appears when scrolling
- ✅ Styling looks correct (book.css loaded)
- ✅ No broken links or missing images
- ✅ Responsive design works (try mobile view)

---

## Publishing Updates

### Complete Workflow

```bash
# 1. Edit markdown file(s)
cd C:/work/AI/1lang/ebook
vim 01-tutorial-introduction.md

# 2. Regenerate HTML
python3 generate_html.py

# 3. Test locally
start index.html  # Verify changes look correct

# 4. Stage changes
cd ..
git add ebook/ docs/ebook/

# 5. Commit with descriptive message
git commit -m "Update Chapter 1: Add section on recursion examples"

# 6. Push to GitHub
git push origin main

# 7. Wait for GitHub Pages deployment (1-2 minutes)
# 8. Verify at: https://haxidermist.github.io/1lang/ebook/
```

### Quick Update Script

Create a shell script for convenience:

**`ebook/update_book.sh`:**
```bash
#!/bin/bash
cd "$(dirname "$0")"
python3 generate_html.py
git add .
git commit -m "Update ebook: $1"
git push origin main
echo "Book updated and pushed to GitHub"
```

Usage:
```bash
cd C:/work/AI/1lang/ebook
./update_book.sh "Fixed typo in Chapter 2"
```

### Deployment Time

After pushing:
- GitHub Actions triggers automatically
- Deployment takes **1-2 minutes**
- Check progress: https://github.com/haxidermist/1lang/actions
- Green checkmark = deployed successfully

### Verify Deployment

1. Visit: https://haxidermist.github.io/1lang/ebook/
2. Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
3. Check that your changes appear
4. Test on different devices/browsers

---

## Adding New Chapters

### Step 1: Create Markdown File

```bash
cd C:/work/AI/1lang/ebook
touch 07-new-chapter.md
```

### Step 2: Add Chapter Content

```markdown
# Chapter 7: New Chapter Title

Introduction to the new chapter...

## Section 7.1

Content here...

## Exercises

**Exercise 7-1.** Problem description.
```

### Step 3: Update Generator Script

Edit `generate_html.py`:

```python
CHAPTERS = [
    ('00-preface.md', 'Preface', 0),
    ('01-tutorial-introduction.md', 'Chapter 1: A Tutorial Introduction', 1),
    # ... existing chapters ...
    ('07-new-chapter.md', 'Chapter 7: New Chapter Title', 7),  # ADD THIS
    ('appendix-reference.md', 'Appendix A: Language Reference Manual', 8)  # UPDATE INDEX
]
```

### Step 4: Regenerate and Test

```bash
python3 generate_html.py
start index.html  # Verify new chapter appears
```

### Step 5: Update Documentation

Update these files to reference the new chapter:

- `ebook/README.md` - Add to book structure
- `ebook/THE-1-PROGRAMMING-LANGUAGE.md` - Add to TOC
- `README.md` (root) - Update book contents section

### Step 6: Commit and Push

```bash
git add ebook/ docs/ebook/
git commit -m "Add Chapter 7: New Chapter Title"
git push origin main
```

---

## Troubleshooting

### HTML Not Updating After Regeneration

**Problem:** Changes don't appear in browser after regenerating.

**Solution:**
```bash
# Hard refresh in browser
Ctrl+Shift+R  # Windows/Linux
Cmd+Shift+R   # Mac

# Or clear browser cache
# Or open in incognito/private mode
```

### Generator Script Fails

**Problem:** `python3 generate_html.py` produces errors.

**Common Issues:**

1. **File not found**
   ```
   Warning: 01-tutorial-introduction.md not found
   ```
   - Check you're in the `ebook/` directory
   - Verify markdown file exists and has correct name

2. **Python version**
   ```bash
   python3 --version  # Should be 3.7+
   ```
   - If `python3` not found, try `python`

3. **Permission denied**
   ```bash
   chmod +x generate_html.py
   python3 generate_html.py
   ```

### Styling Not Applied

**Problem:** Book appears unstyled (plain HTML).

**Solution:**
1. Verify `book.css` exists in same directory as `index.html`
2. Check CSS link in HTML:
   ```html
   <link rel="stylesheet" href="book.css">
   ```
3. Test locally first to isolate issue

### GitHub Pages Not Updating

**Problem:** Live site doesn't show latest changes after push.

**Troubleshooting Steps:**

1. **Check Actions**
   - Visit: https://github.com/haxidermist/1lang/actions
   - Look for "pages build and deployment"
   - Verify green checkmark (✓)
   - If red X, click to see error details

2. **Verify Files Pushed**
   ```bash
   git status  # Should show nothing to commit
   git log -1  # Should show your latest commit
   ```

3. **Check GitHub Pages Settings**
   - Go to: https://github.com/haxidermist/1lang/settings/pages
   - Verify Source: "Deploy from a branch"
   - Verify Branch: "main" and Folder: "/docs"

4. **Wait Longer**
   - First deployment: 5-10 minutes
   - Subsequent: 1-2 minutes
   - CDN cache may add delay

5. **Force Rebuild**
   - Make a trivial change (add space to README)
   - Commit and push
   - This triggers a new deployment

### Code Blocks Not Formatting

**Problem:** Code appears as plain text without syntax highlighting.

**Cause:** Markdown code fence syntax incorrect.

**Solution:**

Ensure code blocks use triple backticks:

````markdown
```1
function example:
  outputs:
    result: Integer
  implementation: {
    return 42
  }
```
````

NOT:
```markdown
function example:
  outputs:
    result: Integer
```

### Navigation Links Broken

**Problem:** TOC links or navigation buttons don't work.

**Solution:**

1. **Regenerate HTML**
   ```bash
   python3 generate_html.py
   ```

2. **Check Anchor IDs**
   - TOC links use `#chapter-0`, `#chapter-1`, etc.
   - Each chapter div has matching `id="chapter-N"`

3. **Test Locally**
   - Open in browser
   - Check browser console (F12) for errors

---

## Advanced Maintenance

### Custom CSS Changes

To modify styling:

1. Edit `ebook/book.css`
2. Test changes locally
3. Copy to `docs/ebook/book.css`
4. Commit and push

Common customizations:
- Font sizes
- Colors and theme
- Code block styling
- Spacing and margins
- Print styles

### Adding Syntax Highlighting

To add proper syntax highlighting:

1. Include a syntax highlighting library in HTML
2. Modify `generate_html.py` to wrap code in appropriate tags
3. Add syntax-specific CSS rules

Example libraries:
- Highlight.js
- Prism.js
- CodeMirror

### PDF Generation

To create a PDF version:

**Method 1: Browser Print**
1. Open `index.html` in browser
2. Print (Ctrl+P)
3. Save as PDF
4. Use print-friendly CSS (already included)

**Method 2: Pandoc** (if installed)
```bash
pandoc complete-book.md -o book.pdf --toc
```

**Method 3: wkhtmltopdf**
```bash
wkhtmltopdf index.html book.pdf
```

### EPUB Generation

For e-readers:

```bash
pandoc complete-book.md -o book.epub --toc --epub-cover-image=cover.png
```

---

## Best Practices

### Before Editing

1. ✅ Pull latest changes: `git pull origin main`
2. ✅ Create a branch for major changes: `git checkout -b chapter-updates`
3. ✅ Back up current working version

### During Editing

1. ✅ Write clear, concise content
2. ✅ Follow existing formatting conventions
3. ✅ Keep code examples correct and tested
4. ✅ Save frequently

### After Editing

1. ✅ Regenerate HTML
2. ✅ Test locally before pushing
3. ✅ Use descriptive commit messages
4. ✅ Verify deployment on GitHub Pages

### Commit Message Format

Good commit messages:

```
Update Chapter 3: Add while loop examples
Fix typo in Appendix A section on operators
Add Exercise 4-7 to Chapter 4
Improve code formatting in Chapter 5
```

Bad commit messages:
```
Update
Fixed stuff
Changes
asdf
```

---

## Quick Reference

### Common Commands

```bash
# Regenerate HTML
cd C:/work/AI/1lang/ebook && python3 generate_html.py

# Test locally
cd C:/work/AI/1lang/ebook && start index.html

# Full update workflow
cd C:/work/AI/1lang
git pull
cd ebook
# (edit files)
python3 generate_html.py
cd ..
git add ebook/ docs/ebook/
git commit -m "Update: description"
git push origin main

# Check deployment status
# Visit: https://github.com/haxidermist/1lang/actions
```

### File Locations

- **Source Markdown:** `ebook/*.md`
- **Generator:** `ebook/generate_html.py`
- **Stylesheet:** `ebook/book.css`
- **Generated HTML:** `ebook/index.html`
- **GitHub Pages:** `docs/ebook/index.html`
- **Live Site:** https://haxidermist.github.io/1lang/ebook/

---

## Support and Help

If you encounter issues not covered here:

1. **Check GitHub Issues:** https://github.com/haxidermist/1lang/issues
2. **Check GitHub Actions:** Look for failed deployments
3. **Test Locally:** Isolate whether issue is local or on GitHub Pages
4. **Review Git History:** `git log ebook/` to see what changed
5. **Create an Issue:** Document the problem and steps to reproduce

---

## Version History

| Date | Change | Author |
|------|--------|--------|
| 2025-11-12 | Initial ebook with dynamic loading | AI |
| 2025-11-12 | Converted to static HTML generation | AI |
| 2025-11-12 | Added maintenance documentation | AI |

---

**Happy maintaining! Keep "The 1 Programming Language" up to date! 📖✨**
