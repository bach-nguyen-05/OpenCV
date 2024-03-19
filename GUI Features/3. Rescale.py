import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0)

def frame_resize (frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # (a, b, c) : (height, width, channel)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
    # interpolation

if not cap.isOpened():
    sys.exit("Error")

while True:
    read, frame = cap.read()
    frame = frame_resize(frame, 0.8)
    new_frame = frame_resize(frame, 0.5)
    new_frame = cv.cvtColor(new_frame, cv.COLOR_BGR2GRAY) 
    # convert color to gray
    
    print(new_frame)
    if not read:
        sys.exit("Can't read frame")
    cv.imshow("Resized video", new_frame)
    cv.imshow("Show video", frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()