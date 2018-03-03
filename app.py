import cv2
import dlib

video_capture = cv2.VideoCapture(0)
face_detector = dlib.get_frontal_face_detector()


def rect_to_bound_box(rect):
    x1 = rect.left()
    x2 = rect.right()
    y1 = rect.top()
    y2 = rect.bottom()

    return x1, y1, x2, y2


def sacle_back(bounding_box, scale):
    (x1, y1, x2, y2) = bounding_box
    x1 = int(x1 / scale)
    y1 = int(y1 / scale)
    x2 = int(x2 / scale)
    y2 = int(y2 / scale)
    return x1, y1, x2, y2


while True:
    ret, image = video_capture.read()
    scale = 200 / min(image.shape[0], image.shape[1])
    thumb = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(thumb, cv2.COLOR_BGR2GRAY)
    face_rects = face_detector(gray, 1)

    for i, rect in enumerate(face_rects):
        (x1, y1, x2, y2) = rect_to_bound_box(face_rects[i])
        (x1, y1, x2, y2) = sacle_back((x1, y1, x2, y2), scale)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('Test', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
