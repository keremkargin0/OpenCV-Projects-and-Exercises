import numpy as np
import cv2
import pyautogui

# Take a Screenshot Using Pyautogui
image = pyautogui.screenshot()

# Since the pyautogui takes as a PIL(pillow) and in RGB we need to convert it to numpy array and BGR
# So we can write it to the disk

image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

#writing it to the disk using opencv
cv2.imwrite("test.png",image)
