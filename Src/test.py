import cv2
import pytesseract
import numpy as np
import re


def do_ocr(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow('img_gray.png', img_gray)
    cv2.imshow('money-test.png', thresh_img)

    cv2.imwrite('money-test.png', thresh_img)

    custom_config = r'--oem 1 -l digits -c tessedit_char_whitelist=0123456789'
    ocr_output = pytesseract.image_to_string(img_gray, config=custom_config)

    print(ocr_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Return output text from OCR
    return ocr_output


screenRGB = cv2.imread('money.png')
cropped = screenRGB
do_ocr(cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Load icon
img = cv2.imread('test.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgSrc = f'icons/refresh_button.png'
template = cv2.imread(imgSrc, 0)
# Compare images
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
icon_found = len(loc[0]) > 0

print(f'icon_found {icon_found}')
