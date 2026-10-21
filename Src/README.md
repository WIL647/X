# Mini-Compiler Project - Phase 1: Scanner

## Repository Overview
This repository contains the source code for Phase 1 of our group's multi-phase compiler project.

## Project Structure & File Functionality

1. `lexer.py` (Core Lexical Analyzer Engine)
   - Contains the primary `Lexer` and `Token` classes.
   - Responsible for scanning source text character by character.
   - Handles whitespace skipping, comment filtering (`//`), keyword vs. identifier resolution, number classification (integers and floats), string literal parsing, and multi-character operator recognition (`==`, `!=`, `<=`, `>=`).
   - Implements precise line and column tracking for error reporting.

2. `main.py` (Execution Boilerplate / Sample Runner)
   - Acts as an executable entry point.
   - Supplies sample mini-language code to initialize the `Lexer` and output the resulting token stream to the console.

3. `test_runner.py` (Automated Test Suite & Bug Report Runner)
   - Executes validation tests on both valid code structures and invalid/error-prone source snippets.
   - Verifies correct tokenization and ensures lexical errors are caught and reported cleanly.

4. `bug_report.txt` (Test & Bug Report Documentation)
   - Formally documents the results of the Phase 1 test suite, detailing valid compilation outcomes and error-handling verification.

5. `language_spec.txt` (Lexical Specification)
   - Defines the formal grammar rules, reserved keywords, operators, and literal formats for our mini-language.

---

## How to Run the Project

### Prerequisites
Make sure you have Python 3 installed on your machine. You can verify your installation by running:
```bash
python --version
# or
python3 --version
```

### 1. Running on Linux / macOS
Open your terminal, navigate to the project directory, and execute:

* **To run the main sample scanner:**
  ```bash
  python3 main.py
  ```
* **To run the test suite and generate the bug report:**
  ```bash
  python3 test_runner.py
  ```

### 2. Running on Windows
Open Command Prompt (`cmd`) or PowerShell, navigate to your project folder, and execute:

* **To run the main sample scanner:**
  ```bash
  python main.py
  # If 'python' is not recognized, try:
  py main.py
  ```
* **To run the test suite and generate the bug report:**
  ```bash
  python test_runner.py
  # If 'python' is not recognized, try:
  py test_runner.py
  ```
