## first install requirements 
* pip install -r requirements.txt 

## install tesseract 
https://github.com/tesseract-ocr/tesseract

## configure your file with the corresponding tesseract exec file
* pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
* Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

## documentation info:
https://tesseract-ocr.github.io/tessdoc/