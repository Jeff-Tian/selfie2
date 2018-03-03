import cv2
import dlib

video_capture = cv2.VideoCapture(0)
face_detector = dlib.get_frontal_face_detector()

while True:
    ret, image = video_capture.read()
    scale = 0.5
    thumb = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(thumb, cv2.COLOR_BGR2GRAY)
    face_rects = face_detector(gray, 1)
    cv2.rectangle(gray, (face_rects[0].left(), face_rects[0].top()), (face_rects[0].right(), face_rects[0].bottom()), (0, 255, 0), 2)
    cv2.imshow('Test', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
