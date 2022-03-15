import numpy as np
from pdf2image import convert_from_path
from PIL import Image
import cv2
import pytesseract

path = r"SDS Files/5_10_SDS.pdf"
poppler_path = r'C:\Program Files\poppler-22.01.0\bin'
temp_path = f'{path}/temp_SDS.jpg'


def convert_pdf_to_image(document, dpi):
    images = []
    images.extend(
        list(
            map(
                lambda image: cv2.cvtColor(
                    np.asarray(image), code=cv2.COLOR_RGB2BGR
                ),
            convert_from_path(path, dpi, poppler_path=poppler_path, grayscale=True),
            )
        )
    )
    return images


def cv_image_scan(path):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = path

    text = pytesseract.image_to_string(image, lang="eng")

    print(text)

cv_image_scan(convert_pdf_to_image(path, 200))