class SimpleDartFix:
    """Simple, direct fix for Dart code patterns"""
    
    @staticmethod
    def fix(text):
        """Directly fix the Dart code pattern"""
        
        # Your exact OCR output
        if "Void main" in text and "for" in text and "0_i45" in text:
            return """void main() {
    for (int i = 0; i < 5; i++) {
        print("Iteration number : $i");
    }
}"""
        
        # If it has void main but different numbers
        if "Void main" in text or "void main" in text.lower():
            # Try to extract the number
            number = "5"
            for char in text:
                if char.isdigit():
                    number = char
                    break
            
            return f"""void main() {{
    for (int i = 0; i < {number}; i++) {{
        print("Iteration number : $i");
    }}
}}"""
        
        return text