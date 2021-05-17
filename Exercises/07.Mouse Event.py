import cv2
import numpy as np

cap = cv2.VideoCapture(0)

circles = []

def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN: # This means clicking the left button of mouse.
        circles.append((x,y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouse) # Takes events when we click the left button of mouse.

while 1:
    ret, frame = cap.read()

    for center in circles:
         cv2.circle(frame, center, 20, (255, 0, 0), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"): # When we press to "h", frames and circle list will clean.
        circles = []

cap.release()
cv2.destroyAllWindows()
