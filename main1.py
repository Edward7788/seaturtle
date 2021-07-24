import cv2
import pytesseract
import imutils
from PIL import Image

if __name__ == '__main__':
    img = cv2.imread("answer1.png")
    # img = imutils.resize(img, width=500)

    # roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
    # x, y, w, h = roi

    # cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
    print(img.shape)
    height, width, _ = img.shape
    img_roi = img[0:847, width - 400:width - 10]
    text = pytesseract.image_to_string(img_roi, lang='eng')
    print(text)
    cv2.imshow("result", img)

    cv2.waitKey(0)
