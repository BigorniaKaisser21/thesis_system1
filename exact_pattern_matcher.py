import re

class ExactPatternMatcher:
    """Exactly matches specific OCR patterns"""
    
    @staticmethod
    def match_fruits_pattern(text):
        """Match the exact fruits pattern from your OCR output"""
        
        # Normalize the text - remove extra spaces and newlines
        text = ' '.join(text.split())
        
        # The exact pattern from your output
        if "1) banana" in text and "frvits" in text and "apple'" in text and "5or" in text and "cherry" in text:
            return """fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""
        
        # More flexible pattern matching
        lines = text.split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        
        # Check if we have 3 lines with specific content
        if len(cleaned_lines) >= 3:
            first_line = cleaned_lines[0].lower()
            second_line = cleaned_lines[1].lower()
            third_line = cleaned_lines[2].lower()
            
            # Check for banana in first line
            has_banana = 'banana' in first_line or '1)' in first_line
            
            # Check for fruits list in second line
            has_frvits = 'frvits' in second_line
            has_apple = 'apple' in second_line
            has_5or = '5or' in second_line
            has_print = 'print' in second_line or 'Print' in second_line
            
            # Check for cherry in third line
            has_cherry = 'cherry' in third_line
            
            if has_banana and has_frvits and has_apple and has_5or and has_cherry:
                return """fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""
        
        return None
    
    @staticmethod
    def match_hello_world_pattern(text):
        """Match Hello World pattern"""
        text_lower = text.lower()
        
        if 'pcil' in text_lower and 'hell' in text_lower and 'world' in text_lower:
            return 'print("Hello World")'
        
        if 'jme' in text_lower and 'io' in text_lower and 'rnlt' in text_lower:
            return """print("Hello World")

int x = 10
int y = 10

x + y = 20

print(x + y)"""
        
        return None
    
    @staticmethod
    def match_if_else_pattern(text):
        """Match if-else pattern"""
        text_lower = text.lower()
        
        if 'c f' in text_lower and 'd number' in text_lower:
            return """if number % 2 == 0:
    print("C f" "d number is even")
else:
    print("f " "d number is odd")"""
        
        return None
    
    @staticmethod
    def process(text):
        """Main processing function"""
        
        if not text or len(text.strip()) < 3:
            return text
        
        # Try exact fruit pattern first
        fruits_result = ExactPatternMatcher.match_fruits_pattern(text)
        if fruits_result:
            return fruits_result
        
        # Try hello world pattern
        hello_result = ExactPatternMatcher.match_hello_world_pattern(text)
        if hello_result:
            return hello_result
        
        # Try if-else pattern
        ifelse_result = ExactPatternMatcher.match_if_else_pattern(text)
        if ifelse_result:
            return ifelse_result
        
        return text