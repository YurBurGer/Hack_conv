import cv2
import numpy as np
import math

HSV_CONTROL_WINDOW = "Control"
TRACKING_IMAGE_WINDOW = "Tracking"
HSV_IMAGE_WINDOW = "HSV"
FILTERED_IMAGE_WINDOW = "HSV (Filtered)"
VIDEO_SOURCE = 1

TRACKER_TYPE = "KCF"

video = cv2.VideoCapture()
video.open(1)
if not video.isOpened():
    raise IOError('Camera has not been opened')

cv2.namedWindow(HSV_CONTROL_WINDOW, cv2.WINDOW_AUTOSIZE)


class Params:
    def __init__(self):
        self.lowH = 179
        self.highH = 179
        self.lowS = 133
        self.highS = 255
        self.lowV = 22
        self.highV = 128


params = Params()


def onLowHChanged(value):
    params.lowH = value


def onHighHChanged(value):
    params.highH = value


def onLowSChanged(value):
    params.lowS = value


def onHighSChanged(value):
    params.highS = value


def onLowVChanged(value):
    params.lowV = value


def onHighVChanged(value):
    params.HighV = value


cv2.createTrackbar("LowH", HSV_CONTROL_WINDOW, params.lowH, 179, onLowHChanged)
cv2.createTrackbar("HighH", HSV_CONTROL_WINDOW, params.highH, 179, onHighHChanged)
cv2.createTrackbar("LowS", HSV_CONTROL_WINDOW, params.lowS, 255, onLowSChanged)
cv2.createTrackbar("HighS", HSV_CONTROL_WINDOW, params.highS, 255, onHighSChanged)
cv2.createTrackbar("LowV", HSV_CONTROL_WINDOW, params.lowV, 255, onLowVChanged)
cv2.createTrackbar("HighV", HSV_CONTROL_WINDOW, params.highV, 255, onHighVChanged)

while video.isOpened():
    ret, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresholded = cv2.inRange(hsv, np.array([params.lowH, params.lowS, params.lowV]),
                              np.array([params.highH, params.highS, params.highV]))

    thresholded = cv2.dilate(thresholded, None, iterations=5)
    thresholded = cv2.erode(thresholded, None, iterations=5)

    moments = cv2.moments(thresholded)

    if moments['m00'] > 10000:
        posX = int(moments['m10'] / moments['m00'])
        posY = int(moments['m01'] / moments['m00'])
        cv2.circle(frame, (posX, posY), 5, np.array([0, 0, 255]), -1)

    n = cv2.countNonZero(thresholded)
    cv2.imshow(TRACKING_IMAGE_WINDOW, frame)
    cv2.imshow(FILTERED_IMAGE_WINDOW, thresholded)
    # print(n)
    if cv2.waitKey(1) == 27:
        break


    def get_coordinanes():
        return [posX, posY]

    if cv2.waitKey(1) == 27:
        break

    def get_turn():
        if posX >= 640:
            print('Right')
        else:
            print('Left')
    # get_turn()

    def get_distance():
        if n > 1000:
            # print -11.0576 * math.log(4.28264 * 0.000001 * n)
            print -12.8 * math.log(3.51703 * 0.000001 * n)
        else:
            print 'too low distance'
    get_distance()

video.release()
cv2.destroyAllWindows()
