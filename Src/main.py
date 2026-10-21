# AI Assistance Disclosure: Boilerplate code structure generated with AI assistance.
import sys
from lexer import Lexer

def main():
    # Using triple quotes to safely enclose strings containing double quotes
    sample_code = """
    int main_score = 95;
    if (main_score >= 50) {
        print("Pass");
    }
    """
    
    print("Initializing Lexer...")
    lexer = Lexer(sample_code)
    
    try:
        print("Tokenizing source code...\n")
        token_stream = lexer.tokenize()
        
        for t in token_stream:
            print(t)
            
    except Exception as e:
        print(f"Compilation Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()

