import cv2
import numpy as np
import pytesseract as pt
import imutils

plate = cv2.imread("licence_plate.jpg")

plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(plate_gray, 5, 250, 250) # değerleri değiştirdikçe yumuşatma oranı değişir.
edged = cv2.Canny(filtered, 30, 200) # min, max threshold u değiştirdikçe köşe bulma oranları değişir.
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(contours)
cnts = sorted(cnts, key= cv2.contourArea, reverse= True)[:10]

screen = None

for c in cnts:
    epsilon = 0.018*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        screen = approx
        break

mask = np.zeros(plate_gray.shape, np.uint8)

new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)
new_img = cv2.bitwise_and(plate, plate, mask= mask)

(x,y) = np.where(mask == 255)

(topx, topy) = (np.min(x),np.min(y))
(bottomx, bottomy) = (np.max(x),np.max(y))

croped = plate_gray[topx:bottomx + 1, topy:bottomy + 1]

plate_text = pt.image_to_string(croped, lang= "tur")
print(plate_text)

cv2.imshow("Croped", croped)
cv2.imshow("Plate", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
