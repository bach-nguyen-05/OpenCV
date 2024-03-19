# Video Capture

import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit('No Camera!')
while True:
    ret, frame = cap.read()
    # cap.read() return the video frame by frame and a boolean whether the frame is successfully read or not
    
    img = np.zeros(frame.shape, np.uint8)

    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.65, fy = 0.7)
    canny = cv2.Canny(smaller_frame, 80, 250)

    cv2.imshow('Canny Edges', canny)
    cv2.imshow('Frame', smaller_frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()