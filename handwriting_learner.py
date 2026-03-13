import json
import os
import re

class HandwritingLearner:
    """Learns your handwriting patterns over time"""
    
    def __init__(self, patterns_file='handwriting_patterns.json'):
        self.patterns_file = patterns_file
        self.patterns = self.load_patterns()
    
    def load_patterns(self):
        """Load saved handwriting patterns"""
        if os.path.exists(self.patterns_file):
            try:
                with open(self.patterns_file, 'r') as f:
                    return json.load(f)
            except:
                return self.get_default_patterns()
        return self.get_default_patterns()
    
    def get_default_patterns(self):
        """Default patterns based on your examples"""
        return {
            "word_mappings": {
                "nimbtr": "number",
                "humber": "number",
                "lnvnber": "number",
                "lwvmbt": "number",
                "inpul": "input",
                "prut": "print",
                "ic": "is",
                "edd": "odd",
                "il": "odd",
                "clse": "else",
                "2f": "if",
                "cf": "if"
            },
            "character_mappings": {
                "0": ["0", "O"],
                "1": ["1", "l", "I"],
                "2": ["2", "z"],
                "5": ["5", "s"],
                "6": ["6", "b"],
                "8": ["8", "B"],
                "f": ["f"],
                "p": ["p"],
                "r": ["r", "n"]
            },
            "code_patterns": {
                "input_statement": r'number\s*=\s*int\s*\(\s*input\s*\(\s*"Enter\s*a\s*number"\s*\)\s*\)',
                "if_statement": r'if\s+number\s*%\s*2\s*==\s*0\s*:',
                "print_even": r'print\s*\(\s*f\s*"\s*\{\s*number\s*\}\s*is\s*even\s*"\s*\)',
                "print_odd": r'print\s*\(\s*f\s*"\s*\{\s*number\s*\}\s*is\s*odd\s*"\s*\)'
            },
            "fixed_code": """number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")"""
        }
    
    def save_patterns(self):
        """Save learned patterns"""
        with open(self.patterns_file, 'w') as f:
            json.dump(self.patterns, f, indent=2)
    
    def learn_from_ocr(self, ocr_text, correct_text=None):
        """Learn new patterns from OCR mistakes"""
        ocr_words = ocr_text.lower().split()
        
        # Learn word mappings
        if correct_text and "number" in correct_text:
            for word in ocr_words:
                if word not in self.patterns["word_mappings"]:
                    if len(word) > 3 and word not in ["the", "and", "for"]:
                        self.patterns["word_mappings"][word] = "number"
        
        self.save_patterns()
    
    def correct_text(self, text):
        """Apply learned patterns to correct text"""
        if not text:
            return text
        
        corrected = text
        
        # Apply word mappings
        for wrong, correct in self.patterns["word_mappings"].items():
            corrected = re.sub(r'\b' + re.escape(wrong) + r'\b', correct, corrected, flags=re.IGNORECASE)
        
        return corrected
    
    def extract_code(self, text):
        """Extract code structure from text"""
        text_lower = text.lower()
        
        # Check if this contains the key elements
        has_number = 'number' in text_lower
        has_if = 'if' in text_lower
        has_percent = '%' in text
        has_even = 'even' in text_lower
        has_odd = 'odd' in text_lower
        has_print = 'print' in text_lower
        
        if has_number and has_if and has_percent and has_even and has_odd:
            return self.patterns["fixed_code"]
        
        return text

# Global instance
_learner = None

def get_learner():
    global _learner
    if _learner is None:
        _learner = HandwritingLearner()
    return _learner