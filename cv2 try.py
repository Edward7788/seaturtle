import cv2
import numpy as np

if __name__ == '__main__':

    img = cv2.imread("ntt.png")

    cv2.namedWindow("ntt", cv2.WINDOW_NORMAL)
    cv2.imshow("ntt", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
