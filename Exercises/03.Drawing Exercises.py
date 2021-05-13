import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype = np.uint8) + 255

# Drawing simple lines.
cv2.line(canvas, (50,50),(512,512), (255,0,0),thickness= 5)
cv2.line(canvas, (50,50),(512,50), (123,10,220),thickness= 5)


# Drawing simple rectangles.
cv2.rectangle(canvas, (50,50), (200,200), (24,24,24),thickness= 2)
cv2.rectangle(canvas, (25,25), (125,125), (122,122,122),thickness= 6)

# Drawing simple circle.
cv2.circle(canvas,(325,325), 100, (25,25,25), thickness= -1)

# OpenCV doesn't have a function for drawing triangles.
# Drawing simple triangle manually.
p1 = (100,200)
p2 = (50,50)
p3 = (300,100)

cv2.line(canvas, p1,p2, (10,10,10), thickness= 2)
cv2.line(canvas, p2,p3, (10,10,10), thickness= 2)
cv2.line(canvas, p1,p3, (10,10,10), thickness= 2)


# Drawing simple quadrangle.
points = np.array([[[110,200],[330,200],[290,220],[220,250]]], np.int32)

cv2.polylines(canvas, [points], True, (20,20,20), thickness= 3)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
