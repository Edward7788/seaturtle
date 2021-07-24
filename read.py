import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

if __name__ == '__main__':

    image = cv2.imread('paper2.png', cv2. IMREAD_COLOR)
    res_img = cv2.resize(image, (300, 300), interpolation=cv2.INTER_CUBIC)
    gray_img = cv2.cvtColor(res_img, cv2.COLOR_RGB2GRAY)
    sim_inv = cv2.threshold(gray_img, 110, 255, cv2.THRESH_BINARY_INV)[1]
    blur = cv2.medianBlur(sim_inv, 3)
    kernel = np.ones((2, 2), np.uint8)
    open_img = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)

    custom_config = r'--oem 3 --psm 6'
    #height, width, _ = image.shape
    #open_img = image[0:60, width - 80:width - 5]
    print(pytesseract.image_to_string(open_img, lang='eng', config=custom_config))


