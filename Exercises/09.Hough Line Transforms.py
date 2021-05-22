import cv2
import numpy as np

img = cv2.imread("h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 75, 150) # We can change min and max values.

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap= 200) 

# The Maxlinegap value is used to fill the spaces between the lines.
# The value to be given is given experimentally. We tried it like 50, 100, 200.

for line in lines:
    x1,y1,x2,y2 = line[0] # We only reach zero because the starting and ending points are at index 0.
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),  2)

cv2.imshow("Img",img)
cv2.imshow("Gray",gray)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
