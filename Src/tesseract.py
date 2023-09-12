# Import OpenCV
import cv2
# Import tesseract OCR
import pytesseract
import numpy as np


def do_ocr(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)

    cv2.imwrite('money.png', thresh_img)
    custom_config = r'--oem 1 --psm 7 -l grobold -c tessedit_char_whitelist=0123456789'
    ocr_output = pytesseract.image_to_string(thresh_img, config=custom_config)
    # Return output text from OCR
    return ocr_output
