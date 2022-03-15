import os
from PIL import Image
import pytesseract
import PyPDF2
from pdf2image import convert_from_path

import time

#Path to input files
folder = r"SDS Files/"

#Temp path to save temp image file for scanning (can be deleted if needed)
temp_path = f'{folder}/temp_SDS.jpg'

#path to poppler to run pdf2image(required to run for windows)
poppler_path = r'C:\Program Files\poppler-22.01.0\bin'

#Copies and pastes text from a PDF (Currently not being used)
def copy_paste_pdf(path):
    fhandle = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(fhandle)

    count = pdfReader.numPages

    result = []

    for i in range(count):
        # print("----------------------------New Page----------------------------------")
        page = pdfReader.getPage(i)
        result = str(result) + f'{page.extractText()}'
    return result

#If not using the Copy and paste feature use tesseract to read to file
def cv_image_scan(path):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = path

    text = pytesseract.image_to_string(Image.open(image), lang="eng")

    return text

#Comverts PDF to JPEG
def pdf_2_JPEG(path, temp_path):

    pages = convert_from_path(path, 100, poppler_path=poppler_path, grayscale=True)

    results = ''

    for page in pages:
        page.save(temp_path, 'JPEG')
        results = results + cv_image_scan('SDS Files/temp_SDS.jpg')

    return results

#Api to run the correct funcion
def api(path, temp_path):
    if path.endswith('.pdf'):

        result = copy_paste_pdf(path)

        if len(result) > 50:
            print('Copy Paste===============')
            #return result
        else:
            pdf_2_JPEG(path, temp_path)
            print('pdf 2 JPEG===============')
    else:
        cv_image_scan(path)
        print('Computer Vision===============')

directory = os.fsencode(folder)

start = time.time()
for file in os.listdir(directory):
    item_start = time.time()

    i = os.fsdecode(file)
    print(i)
    print(api(f'{folder}{i}', temp_path))

    item_end = time.time()
    print(item_end - item_start)

    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

end = time.time()
print(end - start)