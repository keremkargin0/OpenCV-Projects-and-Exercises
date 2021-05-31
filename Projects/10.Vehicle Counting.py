import cv2
import numpy as np

vid = cv2.VideoCapture("traffic.avi")
backsub = cv2.createBackgroundSubtractorMOG2()

# Counter for counting vehicles
counter = 0

while True:
    ret, frame = vid.read()

    if ret:
        fgmask = backsub.apply(frame)

        cv2.line(frame, (50,0), (50,300), (255,255,0), 2)
        cv2.line(frame, (70, 0), (70, 300), (255, 255, 0), 2)

        contours,hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        try: hierarchy = hierarchy[0]
        except:hierarchy = []

        for contour,hier in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 40 & h > 40:
                cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),3)

                if x > 50 & x < 70:
                    counter +=1
        cv2.putText(frame,"Car count:" + str(counter),(90,100), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow("Car Counter",frame)
        cv2.imshow("Fgmask", fgmask)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

vid.release()
cv2.destroyAllWindows()
