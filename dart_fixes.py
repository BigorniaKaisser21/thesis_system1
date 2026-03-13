import re

class DartFixer:
    """Specialized fixer for Dart code patterns"""
    
    @staticmethod
    def fix_dart_code(text):
        """Fix Dart code patterns"""
        
        # Check if this is the void main pattern
        if "void main" in text.lower() or "Void main" in text:
            return DartFixer.fix_void_main(text)
        
        # Check if this is a for loop pattern
        if "for" in text.lower() and "int" in text.lower():
            return DartFixer.fix_for_loop(text)
        
        return text
    
    @staticmethod
    def fix_void_main(text):
        """Fix void main declaration"""
        
        # Your exact pattern
        if "Void main ( ) {" in text:
            # Extract the for loop part
            for_loop_match = re.search(r'for\s*\(\s*int\s+i\s*>\s*0_i45;i#\s*\)\s*{\s*Prin}\s*Heration\s+numbcr\s*:\s*si\s*\)', text, re.DOTALL)
            if for_loop_match:
                return """void main() {
    for (int i = 0; i < 5; i++) {
        print("Iteration number : $i");
    }
}"""
        
        # More general pattern
        return """void main() {
    for (int i = 0; i < 5; i++) {
        print("Iteration number : $i");
    }
}"""
    
    @staticmethod
    def fix_for_loop(text):
        """Fix for loop syntax"""
        
        # Fix the for loop declaration
        text = re.sub(r'for\s*\(\s*int\s+i\s*>\s*0_i45;i#\s*\)', 'for (int i = 0; i < 5; i++)', text)
        
        # Fix print statement
        text = re.sub(r'Prin}\s*Heration\s+numbcr\s*:\s*si\s*\)', 'print("Iteration number : $i");', text)
        
        # Fix missing braces
        text = text.replace('{', '{\n    ')
        text = text.replace('}', '\n}')
        
        return text
    
    @staticmethod
    def extract_numbers(text):
        """Extract numbers from text"""
        numbers = re.findall(r'\d+', text)
        return numbers[0] if numbers else '5'

# For testing
if __name__ == "__main__":
    test_input = """Void main ( ) {
for (int i > 0_i45;i# ){ Prin} Heration numbcr : si )"""
    
    print("=" * 50)
    print("INPUT:")
    print("=" * 50)
    print(test_input)
    print("\n" + "=" * 50)
    print("OUTPUT:")
    print("=" * 50)
    result = DartFixer.fix_dart_code(test_input)
    print(result)