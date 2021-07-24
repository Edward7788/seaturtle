import cv2 as cv
from PIL import Image
import pytesseract as tess
import numpy as np

if __name__ == "__main__":
    src = cv.imread("ntt.png")
    cv.imshow("src", src)
    gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))  # 去除横向细線
    morph1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))  # 去除縱向细線
    morph2 = cv.morphologyEx(morph1, cv.MORPH_OPEN, kernel)
    cv.imshow("Morph", morph2)

    cv.bitwise_not(morph2, morph2)
    textImage = np.asarray(morph2)
    print(src.shape)
    height, width, _ = src.shape
    img_roi = textImage[0:847, width - 384:width - 10]
    text = tess.image_to_string(img_roi, lang='eng')
    print(text)

    cv.waitKey(0)
    cv.destroyAllWindows()