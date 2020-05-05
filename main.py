try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(Image.open('bodyparts.jpeg')))
# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='esp'))