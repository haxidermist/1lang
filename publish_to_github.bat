@echo off
REM publish_to_github.bat - Script to publish 1 language to GitHub
REM Usage: publish_to_github.bat YOUR_GITHUB_USERNAME

if "%1"=="" (
    echo Error: Please provide your GitHub username
    echo Usage: publish_to_github.bat YOUR_GITHUB_USERNAME
    exit /b 1
)

set GITHUB_USERNAME=%1
set REPO_NAME=1lang

echo =========================================
echo Publishing 1 Programming Language
echo =========================================
echo.
echo GitHub Username: %GITHUB_USERNAME%
echo Repository: %REPO_NAME%
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Error: git is not installed
    exit /b 1
)

echo Step 1: Initializing git repository...
git init

echo.
echo Step 2: Adding all files...
git add .

echo.
echo Step 3: Creating initial commit...
git commit -m "Initial commit: 1 Programming Language with self-hosting achieved" -m "" -m "- Bootstrap compiler in Python (lexer, parser, type checker, codegen, VM)" -m "- Self-hosting compiler components written in 1" -m "- Programmable syntax paradigm implementation" -m "- Complete documentation and examples" -m "- Self-hosting demonstration working" -m "" -m "🎉 SELF-HOSTING ACHIEVED! 🎉"

echo.
echo Step 4: Renaming branch to main...
git branch -M main

echo.
echo Step 5: Adding remote repository...
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git

echo.
echo Step 6: Ready to push to GitHub!
echo.
echo IMPORTANT: Make sure you have created the repository on GitHub first:
echo   https://github.com/new
echo.
echo To push, run:
echo   git push -u origin main
echo.
echo You may need to authenticate with your GitHub credentials.
echo If password doesn't work, use a Personal Access Token from:
echo   https://github.com/settings/tokens
echo.
echo =========================================
echo Ready for publication!
echo =========================================
