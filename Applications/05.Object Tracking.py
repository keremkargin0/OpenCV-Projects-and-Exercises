import cv2
from tracker import *

# Create Tracker Object

tracker = EuclideanDistTracker()

# Object Detection for Substracted Video

vid = cv2.VideoCapture("highway.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50) # Takes only moving objects.

while True:
    ret, frame = vid.read()


    # Extract Region of Interest

    roi = frame[340:720, 500:800]

    # Object Detection
    mask = object_detector.apply(roi)

    # We want to see only white object after mask operation. Don't want grays.
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:

        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)

        if area > 100:
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)

            # Drawing rectangle around the objects
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x+w, y+h), (0,255,0), 2)

            detections.append([x,y,w,h])

    # Object Tracking

    boxes_ids = tracker.update(detections)
    # Thus, we can access the counts of vehicles.

    for box_id in boxes_ids:
        x,y,w,h,id = box_id
        cv2.putText(roi,  str(id), (x,y-15), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0),3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Roi", roi)
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()
