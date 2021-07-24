import cv2 as cv
from PIL import Image
import pytesseract as tess


def recoginse_text(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))  # 去除横向细线
    morph1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))  # 去除纵向细线
    morph2 = cv.morphologyEx(morph1, cv.MORPH_OPEN, kernel)
    cv.imshow("Morph", morph2)

    cv.bitwise_not(morph2, morph2)
    textImage = Image.fromarray(morph2)

    # print(img.shape)
    height, width, _ = img.shape
    img_roi = textImage[0:60, width - 125:width - 5]

    text = tess.image_to_string(img_roi, lang='eng')
    print("%s" % text)


def main():
    # 读取需要识别的数字字母图片，并显示读到的原图
    src = cv.imread("answer1.png")
    cv.imshow("src", src)
    print(src.shape)

    # 识别
    recoginse_text(src)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

