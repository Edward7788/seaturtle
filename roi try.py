import cv2
import imutils
import joblib

pts = []

img = cv2.imread("paper.png")
img = imutils.resize(img, width=500)

roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi

cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
cv2.imshow("roi", img)
cv2.waitKey(0)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    if key == ord("s"):
        saved_data = {
            "ROI": pts
        }
        joblib.dump(value=saved_data, filename="config.pkl")
        print("[INFO] ROI座標已保存到本地.")
        break
cv2.destroyAllWindows()
