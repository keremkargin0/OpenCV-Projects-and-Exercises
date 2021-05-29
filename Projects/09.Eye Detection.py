import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("frontalface.xml")
eye_cascade = cv2.CascadeClassifier("eye.xml")


while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (50, 70, 80), 6)

    roi_frame = frame[y:y+h, x:x+w]
    roi_gray = frame_gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3 , 8)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_frame, (ex,ey), (ex + ew, ey + eh), (30, 50, 255), 2)


    cv2.imshow("Video", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
