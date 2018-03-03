import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, image = video_capture.read()
    cv2.imshow('Test', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
