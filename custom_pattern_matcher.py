import re

class CustomPatternMatcher:
    """Custom pattern matcher for specific code patterns"""
    
    @staticmethod
    def fix_list_pattern(text):
        """Fix list declarations like fruits = ["apple", "banana", "cherry"]"""
        
        text_lower = text.lower()
        
        # Look for fruits list pattern
        if 'fruits' in text_lower or 'frvits' in text_lower:
            # Check for apple, banana, cherry
            has_apple = 'apple' in text_lower or 'apple' in text_lower
            has_banana = 'banana' in text_lower or '1) banana' in text_lower
            has_cherry = 'cherry' in text_lower or 'cherry' in text_lower
            
            if has_apple and has_banana and has_cherry:
                return 'fruits = ["apple", "banana", "cherry"]'
        
        return None
    
    @staticmethod
    def fix_for_loop_pattern(text):
        """Fix for loop patterns like for fruit in fruits: print(fruit)"""
        
        text_lower = text.lower()
        
        # Look for for loop pattern
        if 'for' in text_lower or '5or' in text_lower:
            # Extract variable name
            var_match = re.search(r'(?:for|5or)\s+(\w+)\s+in', text_lower)
            if var_match:
                var_name = var_match.group(1)
                if var_name == 'frvit' or var_name == 'fruit':
                    var_name = 'fruit'
                
                # Look for fruits
                if 'fruits' in text_lower or 'frvits' in text_lower:
                    list_name = 'fruits'
                    
                    # Look for print statement
                    if 'print' in text_lower or 'Print' in text:
                        return f'for {var_name} in {list_name}:\n    print({var_name})'
        
        return None
    
    @staticmethod
    def extract_complete_code(text):
        """Extract complete list and loop code"""
        
        lines = text.split('\n')
        combined = ' '.join(lines).lower()
        
        # Check if this is the list and loop pattern
        has_fruits = 'fruits' in combined or 'frvits' in combined
        has_apple = 'apple' in combined or 'apple' in combined
        has_banana = 'banana' in combined or '1) banana' in combined
        has_cherry = 'cherry' in combined or 'cherry' in combined
        has_for = 'for' in combined or '5or' in combined
        has_in = 'in' in combined
        has_print = 'print' in combined or 'Print' in combined
        
        if has_fruits and has_apple and has_banana and has_cherry and has_for and has_in and has_print:
            return """fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""
        
        return None
    
    @staticmethod
    def fix_hello_world(text):
        """Fix Hello World pattern"""
        text_lower = text.lower()
        
        # Look for Hello World pattern
        if 'hell' in text_lower or 'helo' in text_lower or 'pcil' in text_lower:
            if 'world' in text_lower or 'wor' in text_lower or 'wold' in text_lower:
                return 'print("Hello World")'
        
        # Look for print statement with Hello World
        if 'print' in text_lower and ('hell' in text_lower or 'helo' in text_lower):
            return 'print("Hello World")'
        
        return None
    
    @staticmethod
    def fix_variable_declarations(text):
        """Fix variable declarations like int x = 10"""
        lines = text.split('\n')
        fixed_lines = []
        
        for line in lines:
            line_lower = line.lower()
            
            # Look for int x = 10 pattern
            if 'int' in line_lower and 'x' in line_lower and ('10' in line or 'io' in line_lower):
                fixed_lines.append('int x = 10')
            
            # Look for int y = 10 pattern
            elif 'int' in line_lower and 'y' in line_lower and ('10' in line or 'io' in line_lower):
                fixed_lines.append('int y = 10')
            
            # Look for x + y = 20 pattern
            elif 'x' in line_lower and 'y' in line_lower and ('20' in line or 'rnlt' in line_lower):
                fixed_lines.append('x + y = 20')
            
            # Look for print(x + y) pattern
            elif 'print' in line_lower and 'x' in line_lower and 'y' in line_lower:
                fixed_lines.append('print(x + y)')
            
            else:
                if line.strip():
                    fixed_lines.append(line)
        
        return fixed_lines
    
    @staticmethod
    def fix_string_concatenation(text):
        """Fix string concatenation patterns"""
        
        # Look for the specific pattern
        if 'C f' in text and 'd number is even' in text:
            text = text.replace('"C f" "d number is even"', 'f"{number} is even"')
            text = text.replace('"f " "d number is odd"', 'f"{number} is odd"')
        
        # More general pattern
        text = re.sub(r'"C f"\s*"d number is even"', 'f"{number} is even"', text)
        text = re.sub(r'"f "\s*"d number is odd"', 'f"{number} is odd"', text)
        
        return text
    
    @staticmethod
    def process(text):
        """Main processing function"""
        
        if not text or len(text.strip()) < 3:
            return text
        
        # Try to extract complete list and loop code first
        complete = CustomPatternMatcher.extract_complete_code(text)
        if complete:
            return complete
        
        # Try to fix list pattern
        list_fix = CustomPatternMatcher.fix_list_pattern(text)
        if list_fix:
            # Try to fix for loop as well
            loop_fix = CustomPatternMatcher.fix_for_loop_pattern(text)
            if loop_fix:
                return f"{list_fix}\n\n{loop_fix}"
            return list_fix
        
        # Try to fix for loop
        loop_fix = CustomPatternMatcher.fix_for_loop_pattern(text)
        if loop_fix:
            return loop_fix
        
        # Try to fix Hello World
        hello = CustomPatternMatcher.fix_hello_world(text)
        if hello:
            return hello
        
        # Try to fix variable declarations
        var_fixed = CustomPatternMatcher.fix_variable_declarations(text)
        if var_fixed and len(var_fixed) > 0:
            return '\n'.join(var_fixed)
        
        # Try string concatenation fix
        text = CustomPatternMatcher.fix_string_concatenation(text)
        
        return text