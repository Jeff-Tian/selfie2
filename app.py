import cv2
import dlib
import os.path
import numpy as np

video_capture = cv2.VideoCapture(0)
face_detector = dlib.get_frontal_face_detector()

current_directory = os.path.dirname(os.path.realpath(__file__))
landmark_file_name = 'shape_predictor_68_face_landmarks.dat'
landmark_file_full_path = os.path.realpath(os.path.join(current_directory, './' + landmark_file_name))

predictor = dlib.shape_predictor(landmark_file_full_path)

sun_glasses_full_path = os.path.realpath(os.path.join(current_directory, './images/sunglasses.png'))


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


def add_sun_glasses_effect(image, center_point, width):
    sun_glasses = cv2.imread(sun_glasses_full_path)
    height = int(width * (sun_glasses.shape[0] / sun_glasses.shape[1]))

    center_x, center_y = center_point
    start_x = int(center_x - width / 2)
    start_y = int(center_y - height / 2)

    sun_glasses = cv2.resize(sun_glasses, (width, height), interpolation=cv2.INTER_AREA)

    gray_sun_glasses = cv2.cvtColor(sun_glasses, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_sun_glasses, 200, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    glass_area = image[start_y:start_y + height, start_x:start_x + width]
    glass_area_mask = cv2.bitwise_and(glass_area, glass_area, mask=mask_inv)
    sun_glasses_mask = cv2.bitwise_and(sun_glasses, sun_glasses, mask=mask)

    merged = cv2.add(glass_area_mask, sun_glasses_mask)

    image[start_y:start_y + height, start_x:start_x + width] = merged


while True:
    ret, image = video_capture.read()
    scale = 200 / min(image.shape[0], image.shape[1])
    thumb = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(thumb, cv2.COLOR_BGR2GRAY)
    face_rects = face_detector(gray)

    for i, rect in enumerate(face_rects):
        shape = predictor(gray, face_rects[i])
        shape = shape_to_np(shape)

        width = int(abs(shape[17][0] - shape[26][0]) / scale)
        add_sun_glasses_effect(image, scale_point_back((shape[27][0], shape[27][1]), scale), width + 38)

    cv2.imshow('Test', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
