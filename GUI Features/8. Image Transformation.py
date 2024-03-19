# Translation: shifting an image along x and y-axis
# So we can move the image up, down, left, and right

import cv2 as cv
import numpy as np

img = cv.imread('image.jpg')

def translate(img, x, y):
    # x, y: number of pixels to be translated along the x-axis and y-axis respectively
    transMat = np.float32()
    # Create a translation matrix

cv.imshow('Translated Image', img)
cv.waitKey(0)
cv.destroyAllWindows()