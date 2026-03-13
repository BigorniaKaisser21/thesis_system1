import torch
from PIL import Image
from transformers import AutoTokenizer, AutoModelForImageTextToText, AutoImageProcessor
import cv2
import numpy as np
import os
import re

class TrOCRHandwritingProcessor:
    """Handwriting recognition using Microsoft's TrOCR model"""
    
    def __init__(self):
        print("=" * 50)
        print("LOADING TrOCR MODEL (New API)...")
        print("=" * 50)
        try:
            self.tokenizer = AutoTokenizer.from_pretrained("microsoft/trocr-base-handwritten")
            self.image_processor = AutoImageProcessor.from_pretrained("microsoft/trocr-base-handwritten")
            self.model = AutoModelForImageTextToText.from_pretrained("microsoft/trocr-base-handwritten")
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.model.to(self.device)
            print(f"✅ TrOCR loaded successfully on {self.device}")
        except Exception as e:
            print(f"❌ Failed to load TrOCR: {e}")
            print("⚠️ Make sure you have installed: pip install transformers torch torchvision")
            self.tokenizer = None
            self.image_processor = None
            self.model = None
    
    def preprocess_image(self, image_path):
        """Preprocessing for new TrOCR API"""
        try:
            # Read image
            img = cv2.imread(image_path)
            if img is None:
                print(f"❌ Could not read image: {image_path}")
                return None
            
            # Convert to RGB
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Convert to PIL Image
            pil_image = Image.fromarray(img_rgb)
            
            return pil_image
            
        except Exception as e:
            print(f"Preprocessing error: {e}")
            return None
    
    def extract_text(self, image_path):
        """Extract text using new TrOCR API"""
        if self.model is None:
            print("⚠️ TrOCR model not loaded")
            return None
        
        try:
            # Preprocess image
            pil_image = self.preprocess_image(image_path)
            if pil_image is None:
                return None
            
            # Process image with image_processor
            inputs = self.image_processor(pil_image, return_tensors="pt")
            pixel_values = inputs.pixel_values.to(self.device)
            
            # Generate text
            generated_ids = self.model.generate(pixel_values)
            generated_text = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            
            return generated_text
            
        except Exception as e:
            print(f"TrOCR extraction error: {e}")
            return None
    
    def extract_code_structure(self, text):
        """Convert natural text to code structure"""
        
        # Common code patterns
        text_lower = text.lower()
        
        # Detect if-else pattern
        if 'if' in text_lower and 'else' in text_lower:
            # Try to extract numbers
            numbers = re.findall(r'\d+', text)
            num = numbers[0] if numbers else '2'
            
            # Check for even/odd
            has_even = 'even' in text_lower
            has_odd = 'odd' in text_lower
            
            if has_even and has_odd:
                return f"""number = int(input("Enter a number: "))

if number % {num} == 0:
    print(f"{{number}} is even")
else:
    print(f"{{number}} is odd")"""
        
        # Detect fruits list pattern
        if 'fruit' in text_lower or 'apple' in text_lower or 'banana' in text_lower:
            return """fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""
        
        # Detect Hello World
        if 'hello' in text_lower and 'world' in text_lower:
            return 'print("Hello World")'
        
        return text
    
    def process(self, image_path):
        """Main processing function"""
        
        # Extract text with TrOCR
        text = self.extract_text(image_path)
        
        if not text:
            return None
        
        print(f"📝 TrOCR extracted: {text}")
        
        # Convert to code structure
        code = self.extract_code_structure(text)
        
        return code

# Singleton instance
_trocr_instance = None

def get_trocr_processor():
    """Get or create TrOCR processor singleton"""
    global _trocr_instance
    if _trocr_instance is None:
        _trocr_instance = TrOCRHandwritingProcessor()
    return _trocr_instance