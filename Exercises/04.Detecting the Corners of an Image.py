import cv2
import numpy as np

text = cv2.imread("text.png")
contour = cv2.imread("contour.png")

gray_text = cv2.cvtColor(text,cv2.COLOR_BGR2GRAY)
gray_contour = cv2.cvtColor(contour,cv2.COLOR_BGR2GRAY)

gray_text = np.float32(gray_text)

corners = cv2.goodFeaturesToTrack(gray_text, 50, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(text,(x,y),3,(0,0,255),-1)

cv2.imshow("Text",text)

cv2.waitKey(0)
cv2.destroyAllWindows()
