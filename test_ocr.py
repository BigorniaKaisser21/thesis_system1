import sys
sys.path.append('.')
from trocr_processor import get_trocr_processor
from PIL import Image
import pytesseract
import cv2

# Test TrOCR
print("=== TrOCR Test ===")
trocr = get_trocr_processor()
if trocr.model is not None:
    img = cv2.imread('temp_handwriting.png')
    cv2.imwrite('test_trocr.png', img)
    text = trocr.extract_text('test_trocr.png')
    print(f"TrOCR: {text}")
else:
    print("TrOCR model failed to load")

# Test Tesseract
print("\n=== Tesseract Test ===")
if pytesseract.pytesseract.tesseract_cmd:
    try:
        text = pytesseract.image_to_string(Image.open('temp_handwriting.png'), config='--psm 6')
        print(f"Tesseract: {text}")
        print(f"Version: {pytesseract.get_tesseract_version()}")
    except Exception as e:
        print(f"Tesseract error: {e}")
else:
    print("Tesseract path not set")
