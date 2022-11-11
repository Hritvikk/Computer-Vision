import cv2
import numpy as np

# read the image
th = cv2.imread("Task_2.jpg", 0)
 
# define the kernel
kernel = np.ones((3, 3), np.int)
 
# Erosion
erosion = cv2.erode(th, kernel,iterations=1)

# Dilation
dilation = cv2.dilate(th, kernel,iterations=2)

# Opening 
opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
#or opening = cv2.dilate(erosion, dilate_kernel,iterations=1)

# Closing
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
#or closing = cv2.erode(dilation, kernel,iterations=1)

 
# print the output
cv2.imshow("Original Image", th)
cv2.imshow("Eroded Image", erosion)
cv2.imshow("Dilated Image", dilation)
cv2.imshow("Opened Image", opening)
cv2.imshow("Closed Image", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()