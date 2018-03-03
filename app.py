import cv2

video_capture = cv2.VideoCapture(0)

ret, image = video_capture.read()
cv2.imshow('Test', image)

cv2.waitKey()