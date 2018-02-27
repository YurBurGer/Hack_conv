import cv2
import numpy as np

VIDEO_SOURCE = 0
TRACKER_TYPE = "KCF"

video = cv2.VideoCapture()
video.open(VIDEO_SOURCE)
if not video.isOpened():
    raise IOError('Camera has not been opened')

while video.isOpened():
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 50)

    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20)

    if circles is not None:
        for circle in circles:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(frame, center, radius, (0,0, 255), 2)
            cv2.circle(frame, center, radius, (0,0, 255), 3)

    cv2.imshow("Image", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
