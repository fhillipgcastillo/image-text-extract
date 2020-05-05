
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

img = Image.open('./images/Screenshot_20200505_085548_com.popular.app.android.jpg')

imgStr = pytesseract.image_to_string(img)
imgData = pytesseract.image_to_data(img)
imgDataFormated = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
imgOut = pytesseract.run_and_get_output(img)
# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='esp'))

# print(imgStr)
# print(imgData)
pp.pprint(imgDataFormated.get("text"))