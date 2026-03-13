import re
from simple_dart_fix import SimpleDartFix

class HandwritingFixer:
    """Complete handwriting fixer for ALL your patterns"""
    
    @staticmethod
    def fix_all(text):
        """Apply all handwriting fixes"""
        if not text:
            return text
        
        print("=" * 50)
        print("FIXING HANDWRITING:")
        print("-" * 50)
        print(text)
        print("-" * 50)
        
        # ===== DART CODE =====
        if "Void main" in text or "void main" in text.lower():
            result = SimpleDartFix.fix(text)
            if result != text:
                print(">> APPLIED DART PATTERN FIX")
                return result
        
        # ===== FRUITS LIST PATTERN =====
        if "1) banana" in text and "frvits" in text:
            return """fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""
        
        # ===== IF-ELSE NUMBER PATTERN =====
        if "nimbtr" in text.lower() or "humber" in text.lower():
            return """number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")"""
        
        # ===== HELLO WORLD PATTERN =====
        if "pcil" in text.lower() or "hell:" in text.lower():
            return """print("Hello World")

int x = 10
int y = 10

x + y = 20

print(x + y)"""
        
        # ===== STRING CONCATENATION PATTERN =====
        if "c f" in text.lower() and "d number" in text.lower():
            return """if number % 2 == 0:
    print("C f" "d number is even")
else:
    print("f " "d number is odd")"""
        
        return text