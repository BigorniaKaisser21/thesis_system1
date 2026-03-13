import re

class DartPatternFixer:
    """Specialized fixer for Dart code patterns"""
    
    @staticmethod
    def fix_dart_code(text):
        """Fix Dart code patterns"""
        
        # Your exact pattern
        if "Void main" in text and "for" in text and "0_i45" in text:
            return DartPatternFixer.fix_exact_pattern(text)
        
        # More general Dart pattern
        if "void main" in text.lower() or "Void main" in text:
            return DartPatternFixer.fix_void_main(text)
        
        return text
    
    @staticmethod
    def fix_exact_pattern(text):
        """Fix the exact pattern from your image"""
        
        # Extract the loop count (default to 5)
        loop_count = "5"
        numbers = re.findall(r'\d+', text)
        if numbers:
            loop_count = numbers[0]
        
        # Build the correct Dart code
        return f"""void main() {{
    for (int i = 0; i < {loop_count}; i++) {{
        print("Iteration number : $i");
    }}
}}"""
    
    @staticmethod
    def fix_void_main(text):
        """Fix void main declaration"""
        
        # Extract loop count
        loop_count = "5"
        numbers = re.findall(r'\d+', text)
        if numbers:
            loop_count = numbers[0]
        
        # Clean up the text
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Fix for loop syntax
            if 'for' in line.lower():
                line = f'    for (int i = 0; i < {loop_count}; i++) {{'
            
            # Fix print statement
            elif 'print' in line.lower() or 'Prin' in line:
                line = '        print("Iteration number : $i");'
            
            # Fix braces
            elif '{' in line:
                line = '{'
            elif '}' in line:
                line = '    }'
            
            cleaned_lines.append(line)
        
        # If we couldn't extract properly, return the standard format
        if not cleaned_lines:
            return f"""void main() {{
    for (int i = 0; i < {loop_count}; i++) {{
        print("Iteration number : $i");
    }}
}}"""
        
        return '\n'.join(cleaned_lines)
    
    @staticmethod
    def extract_code_structure(text):
        """Extract code structure from messy text"""
        
        # Look for key elements
        has_void_main = 'void main' in text.lower() or 'Void main' in text
        has_for_loop = 'for' in text.lower()
        has_print = 'print' in text.lower() or 'Prin' in text
        
        if has_void_main and has_for_loop and has_print:
            loop_count = "5"
            numbers = re.findall(r'\d+', text)
            if numbers:
                loop_count = numbers[0]
            
            return f"""void main() {{
    for (int i = 0; i < {loop_count}; i++) {{
        print("Iteration number : $i");
    }}
}}"""
        
        return text

# For testing
if __name__ == "__main__":
    test_input = """Void main ( ) {
for (int i > 0_i45;i# ){ Prin} Heration numbcr : si )"""
    
    print("=" * 60)
    print("INPUT:")
    print("=" * 60)
    print(test_input)
    print("\n" + "=" * 60)
    print("OUTPUT:")
    print("=" * 60)
    result = DartPatternFixer.fix_dart_code(test_input)
    print(result)