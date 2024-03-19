# New Functions: cv.putText()

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
blank[:] = 255, 255, 255

# Insert text
cv.putText(blank, 'Computer Vision', (100, 300), cv.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)
# putText(image, text, position, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None, /)
# position: the bottom-left where the text starts

cv.imshow("Show", blank)

cv.waitKey(0)
cv.destroyAllWindows()