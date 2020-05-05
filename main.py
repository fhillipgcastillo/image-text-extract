try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('bodyparts.jpeg')))
# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='esp'))