import cv2 as cv

img = cv.imread('image.jpg')
cv.imshow('Show Image', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # cvt: convert

# 2. Blurring: Basic Guassian Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.GaussianBlur(image, kernel size)
# Kernel Size: learn later, in simple explanation: the blurring level, must be ODD NUMBERS

# 3. Edge Cascade: Using Canny Edge Detector
canny = cv.Canny(img, 120, 150)
# cv.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None, /)

# 4. Dilating 
dilate = cv.dilate(canny, (5, 5), iterations=2)
# cv.dilate(image, kernel size, iteration=None)

# 5. Eroding 
erode = cv.erode(dilate, (5, 5), iterations=2)
# So dilate and erode are the two contrast methods

# 6. Cropping
# just use array like img = img[100:200, 50:100]

cv.imshow('Eroded Image', erode)
cv.imshow('Blurred Image', blur)
cv.imshow('Gray Image', gray)
cv.imshow('Canny Edges', canny)
cv.imshow('Dilated Image', dilate)
cv.waitKey(0)
cv.destroyAllWindows()