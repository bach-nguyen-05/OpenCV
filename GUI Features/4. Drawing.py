# New functions
# numpy: np.zeros(shape, dtype=)
# cv.rectangle(), cv.circle(), cv.line(), cv.ellipse()

import cv2 as cv
import numpy as np

# Creating a blank image
blank = np.zeros((500, 500, 3), dtype= 'uint8')
# np.zeros is a numpy function to create an array with a given shape and type

# 1. Paint an image a certain color
blank [:] = 255, 255, 255
blank[200:300, 300:400] = 255, 180, 180 # OpenCV Standard: BGR (Blue, Green, Red)

# 2. Draw a circle cv.circle(image, center, radius, thickness)
# if thickness == -1, shaded circle
cv.circle(blank, (300, 200), 150, (90, 90, 90), 3)

# 3. Draw an rectangle
cv.rectangle(blank, (50, 150), (100, 300), (100, 150, 150), thickness=2)
cv.rectangle(blank,(0, 0), (blank.shape[1] // 2, blank.shape[0]), (150, 0, 150), -1)
# cv.rectangle(image, pt1, pt2, color, thickness=None, lineType=None, shift=None, /)
# a // b means int floor division

# 4. Draw a line (explicit parameter is kinda like a rectangle)
cv.line(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 0, 0), 4)

# 5. Draw an ellipse and polygon: more complicated => Read Document

cv.imshow("New Color", blank)
cv.waitKey(0)
cv.destroyAllWindows()