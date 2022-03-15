import os
from PIL import Image
import pytesseract
import PyPDF2
from pdf2image import convert_from_path

import time
poppler_path = r'C:\Program Files\poppler-22.01.0\bin'
temp_path = r'SDS Files/temp_SDS.jpg'

def cv_image_scan(path):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = path

    text = pytesseract.image_to_string(Image.open(image), lang="eng")

    return text

#Comverts PDF to JPEG
def pdf_2_JPEG(path, temp_path):

    pages = convert_from_path(path, 300, poppler_path=poppler_path, grayscale=True)

    results = ''

    for page in pages:
        page.save(temp_path, 'JPEG')
        results = results + cv_image_scan('SDS Files/temp_SDS.jpg')

    return results

start = time.time()

result = pdf_2_JPEG(r"SDS Files/6_10_SDS.pdf", temp_path)

end = time.time()
print(end - start)

print(result)


