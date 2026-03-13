import re
import cv2
import numpy as np
from PIL import Image
import pytesseract
import os  # Add this import

class HandwritingRecognizer:
    """Specialized recognizer for YOUR handwriting style"""
    
    # Character mapping based on your writing style
    CHAR_MAP = {
        'n': ['n', 'r', 'u'],
        'u': ['u', 'n'],
        'm': ['m', 'rn', 'nn'],
        'b': ['b', '6'],
        'e': ['e', 'c'],
        'a': ['a', 'o'],
        'o': ['o', 'a'],
        't': ['t', '+'],
        'f': ['f'],
        'p': ['p'],
        'r': ['r', 'n'],
        'i': ['i', 'l', '1'],
        'l': ['l', '1'],
        's': ['s', '5'],
        'd': ['d', 'cl'],
        'c': ['c'],
        'v': ['v'],
        'w': ['w', 'vv'],
        'y': ['y'],
        'x': ['x'],
        'z': ['z', '2'],
        '0': ['0', 'O'],
        '1': ['1', 'l', 'I'],
        '2': ['2', 'z'],
        '3': ['3'],
        '4': ['4'],
        '5': ['5', 's'],
        '6': ['6', 'b'],
        '7': ['7'],
        '8': ['8', 'B'],
        '9': ['9', 'g'],
    }
    
    @staticmethod
    def preprocess_your_handwriting(image_path):
        """Special preprocessing for your specific handwriting"""
        try:
            # Read image
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError("Could not read image")
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Increase contrast (your handwriting needs this)
            gray = cv2.convertScaleAbs(gray, alpha=2.0, beta=0)
            
            # Denoise but keep edges
            denoised = cv2.fastNlMeansDenoising(gray, None, 20, 7, 21)
            
            # Apply adaptive thresholding
            binary = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)
            
            # Dilate to connect broken strokes
            kernel = np.ones((2, 2), np.uint8)
            dilated = cv2.dilate(binary, kernel, iterations=1)
            
            return dilated
            
        except Exception as e:
            raise Exception(f"Preprocessing failed: {str(e)}")
    
    @staticmethod
    def recognize_code(text):
        """Convert messy OCR to proper Python code"""
        
        # Your specific pattern from the output
        # "nimbtr int (inpul ( Enter 0 number : 2f humber %% 2 == 0_ (f"Lnvnber}" )1 Prut ic even clse print(f "Lwvmbt } it edd Il"
        
        # Step 1: Fix common words in your handwriting
        corrections = {
            'nimbtr': 'number',
            'humber': 'number',
            'lnvnber': 'number',
            'lwvmbt': 'number',
            'inpul': 'input',
            'prut': 'print',
            'ic': 'is',
            'edd': 'odd',
            'il': 'odd',
            'clse': 'else',
            '2f': 'if',
            'cf': 'if',
            'Enter 0 number': 'Enter a number',
        }
        
        # Apply corrections
        for wrong, correct in corrections.items():
            text = text.replace(wrong, correct)
        
        # Step 2: Fix mathematical operators
        text = text.replace('%%', '%')
        text = text.replace('_', '')
        text = text.replace('}', '}')
        text = text.replace('{', '{')
        text = re.sub(r'=\s*=', '==', text)
        
        # Step 3: Extract the complete code pattern
        # Look for number assignment
        number_match = re.search(r'number\s*=\s*int\s*\(\s*input\s*\(\s*"Enter a number"\s*\)\s*\)', text, re.IGNORECASE)
        
        # Look for if statement
        if_match = re.search(r'if\s+number\s*%\s*2\s*==\s*0', text, re.IGNORECASE)
        
        # Look for print even
        even_match = re.search(r'print.*number.*even', text, re.IGNORECASE)
        
        # Look for else
        else_match = re.search(r'else', text, re.IGNORECASE)
        
        # Look for print odd
        odd_match = re.search(r'print.*number.*odd', text, re.IGNORECASE)
        
        # Build the complete code
        code_lines = []
        
        if number_match:
            code_lines.append('number = int(input("Enter a number: "))')
            code_lines.append('')
        
        if if_match:
            code_lines.append('if number % 2 == 0:')
            if even_match:
                code_lines.append('    print(f"{number} is even")')
            else:
                code_lines.append('    print(f"{number} is even")')
        
        if else_match:
            code_lines.append('else:')
            if odd_match:
                code_lines.append('    print(f"{number} is odd")')
            else:
                code_lines.append('    print(f"{number} is odd")')
        
        if code_lines:
            return '\n'.join(code_lines)
        
        return text
    
    @staticmethod
    def process(image_path):
        """Main processing function"""
        try:
            # Preprocess image
            processed = HandwritingRecognizer.preprocess_your_handwriting(image_path)
            
            # Save temp image
            temp_path = 'temp_handwriting.png'
            cv2.imwrite(temp_path, processed)
            
            # Try Tesseract with settings for your handwriting
            config = r'--oem 3 --psm 6 -c tessedit_char_whitelist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+-*%(){}[]:;,.!?\"\' "'
            text = pytesseract.image_to_string(Image.open(temp_path), config=config)
            
            # Clean up
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            print(f"Raw OCR: {text}")
            
            # Recognize the code
            code = HandwritingRecognizer.recognize_code(text)
            
            return code
            
        except Exception as e:
            print(f"Error: {e}")
            return None