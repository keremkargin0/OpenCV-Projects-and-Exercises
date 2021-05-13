import cv2
import numpy as np

img1 = cv2.imread("image.jpeg")
img1 = cv2.resize(img1, (640, 480))

roi = img1[40:410,40:400]

gray1 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1, 5)

circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1,
                           img1.shape[0]/32, param1= 220, param2=8
                           ,minRadius=11 , maxRadius=18)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(roi,
                   (i[0],i[1])
                   ,i[2]
                   ,(0, 255, 0)
                   ,2)

cv2.imshow("Final", roi)

list = circles
print(len(list[0]))

cv2.waitKey(0)
cv2.destroyAllWindows()
