from paddleocr import PaddleOCR
import requests
import numpy as np
from PIL import Image
from io import BytesIO

def convert_from_url(img_url):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    response = requests.get(img_url)
    image = np.array(Image.open(BytesIO(response.content)))
    result = ocr.ocr(image, cls=True)
    text = [line[1][0] for line in result]
    return " ".join(text)
