#!/bin/bash
# publish_to_github.sh - Script to publish 1 language to GitHub
# Usage: ./publish_to_github.sh YOUR_GITHUB_USERNAME

if [ -z "$1" ]; then
    echo "Error: Please provide your GitHub username"
    echo "Usage: ./publish_to_github.sh YOUR_GITHUB_USERNAME"
    exit 1
fi

GITHUB_USERNAME="$1"
REPO_NAME="1lang"

echo "========================================="
echo "Publishing 1 Programming Language"
echo "========================================="
echo ""
echo "GitHub Username: $GITHUB_USERNAME"
echo "Repository: $REPO_NAME"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: git is not installed"
    exit 1
fi

echo "Step 1: Initializing git repository..."
git init

echo ""
echo "Step 2: Adding all files..."
git add .

echo ""
echo "Step 3: Creating initial commit..."
git commit -m "Initial commit: 1 Programming Language with self-hosting achieved

- Bootstrap compiler in Python (lexer, parser, type checker, codegen, VM)
- Self-hosting compiler components written in 1
- Programmable syntax paradigm implementation
- Complete documentation and examples
- Self-hosting demonstration working

🎉 SELF-HOSTING ACHIEVED! 🎉"

echo ""
echo "Step 4: Renaming branch to main..."
git branch -M main

echo ""
echo "Step 5: Adding remote repository..."
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

echo ""
echo "Step 6: Ready to push to GitHub!"
echo ""
echo "IMPORTANT: Make sure you have created the repository on GitHub first:"
echo "  https://github.com/new"
echo ""
echo "To push, run:"
echo "  git push -u origin main"
echo ""
echo "You may need to authenticate with your GitHub credentials."
echo "If password doesn't work, use a Personal Access Token from:"
echo "  https://github.com/settings/tokens"
echo ""
echo "========================================="
echo "Ready for publication!"
echo "========================================="
