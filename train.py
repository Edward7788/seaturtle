import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
tessdata_dir_config = r'--tessdata-dir "/usr/local/bin/tesseract"'

if __name__ == '__main__':

    img = cv2.imread('paper.png', cv2. IMREAD_COLOR)

    print(img.shape)
    height, width, _ = img.shape
    img_roi = img[0:60, width-125:width-5]

    text = pytesseract.image_to_string(img_roi, lang='eng', config=tessdata_dir_config)
    print("%s" % text)

    cv2.namedWindow("roi")
    cv2.imshow("roi", img_roi)
    cv2.waitKey(0)
    cv2.destroyAllWindow()
