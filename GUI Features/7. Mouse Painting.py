# New Function: cv.setMouseCallBack()

import cv2 as cv
import numpy as np

blank = np.zeros((700, 700, 3), dtype='uint8')

cv.imshow('White Board', blank)