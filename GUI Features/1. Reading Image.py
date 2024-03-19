import cv2
img = cv2.imread('/home/bachnd05/Documents/OpenCV/Lesson/image.jpg', 1) 
    # -1: cv2.IMREAD_COLOR: Default: Load a color image
    # 0: cv2.IMREAD_GRAYSCALE: Load image in gray modetrash:///Lesson.2/image.jpg
    # 1: cv2.IMREAD_UNCHANGED: Load image as such including alpha channel
new_img = cv2.resize(img, (600, 600))

cv2.imshow("Image", img)
cv2.imshow("New Image", new_img)
cv2.imwrite("Image.jpg", new_img)
print(img.shape)

cv2.waitKey(0) 
# if waitKey(1000) => display 1 sec until a key is pressed
# if waitKey(0) => display indefinitely until a key is pressed

cv2.destroyAllWindows() # close all windows that were created