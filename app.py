import cv2
import dlib
import os
import os.path
import numpy as np

video_capture = cv2.VideoCapture(0)
face_detector = dlib.get_frontal_face_detector()

current_directory = os.path.dirname(os.path.realpath(__file__))
landmark_file_name = 'shape_predictor_68_face_landmarks.dat'
landmark_file_full_path = os.path.realpath(os.path.join(current_directory, './' + landmark_file_name))

predictor = dlib.shape_predictor(landmark_file_full_path)


def rect_to_bound_box(rect):
    x1 = rect.left()
    x2 = rect.right()
    y1 = rect.top()
    y2 = rect.bottom()

    return x1, y1, x2, y2


def shape_to_np(shape):
    coords = np.zeros((68, 2), 'int')

    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords


def scale_point_back(point, scale):
    (x, y) = point
    x = int(x / scale)
    y = int(y / scale)

    return x, y


while True:
    ret, image = video_capture.read()
    scale = 200 / min(image.shape[0], image.shape[1])
    thumb = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(thumb, cv2.COLOR_BGR2GRAY)
    face_rects = face_detector(gray, 1)

    for i, rect in enumerate(face_rects):
        shape = predictor(gray, face_rects[i])
        shape = shape_to_np(shape)
        for point in shape:
            cv2.circle(image, scale_point_back((point[0], point[1]), scale), 2, (0, 0, 255), 1)

    cv2.imshow('Test', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
