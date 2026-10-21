# Test harness and error reporting
import sys
from lexer import Lexer, Token

def run_test(test_name, source_code, expect_success=True):
    print(f"==================================================")
    print(f"RUNNING TEST: {test_name}")
    print(f"--------------------------------------------------")
    print("Source Code:\n" + source_code.strip())
    print(f"--------------------------------------------------")
    
    lexer = Lexer(source_code)
    try:
        tokens = lexer.tokenize()
        if not expect_success:
            print(f"❌ TEST FAILED: Expected a lexical error, but code tokenized successfully.")
            return False
        
        print("✅ TEST PASSED: Successfully generated token stream:")
        for t in tokens:
            print(f"   {t}")
        return True

    except SyntaxError as e:
        if expect_success:
            print(f"❌ TEST FAILED: Unexpected lexical error caught:\n   {e}")
            return False
        else:
            print(f"✅ TEST PASSED (Expected Error Caught Successfully):")
            print(f"   {e}")
            return True
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        return false

def main():
    print("🚀 STARTING COMPILER PHASE 1: SCANNER TEST SUITE\n")
    
    # Test Case 1: Valid Source Code
    valid_code = """
    int score = 95;
    float rate = 3.14;
    if (score >= 50) {
        print("Passed successfully!");
    }
    """
    
    # Test Case 2: Invalid Source Code (Lexical Errors)
    # Contains an unexpected symbol '@' and an unterminated string literal
    invalid_code = """
    int total = 100 @ 50;
    string msg = "unterminated string;
    """
    
    # Run tests
    test_1_passed = run_test("Test 01 - Valid Syntax & Tokenization", valid_code, expect_success=True)
    print("\n")
    test_2_passed = run_test("Test 02 - Invalid Syntax & Lexical Error Handling", invalid_code, expect_success=False)
    
    print(f"\n==================================================")
    print("📊 FINAL TEST REPORT SUMMARY")
    print(f"--------------------------------------------------")
    print(f"Test 01 (Valid Code):   {'PASSED' if test_1_passed else 'FAILED'}")
    print(f"Test 02 (Error Check):  {'PASSED' if test_2_passed else 'FAILED'}")
    print(f"==================================================")

if __name__ == "__main__":
    main()
