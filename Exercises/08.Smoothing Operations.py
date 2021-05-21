import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur   = cv2.blur(img_filter, (5,5))  # (5,5) kısmı sadece pozitif tek sayılar olabilir.
blur_g  = cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)

blur_m = cv2.medianBlur(img_median, 5)

blur_b = cv2.bilateralFilter(img_bilateral,9,75,75)

cv2.imshow("Blur",blur)
cv2.imshow("Blurg",blur_g)

cv2.imshow("Original Median",img_median)
cv2.imshow("Blur-Median",blur_m)

cv2.imshow("Original Bilateral", img_bilateral)
cv2.imshow("Blurred Bilateral", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
