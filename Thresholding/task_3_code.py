import cv2
import numpy as np

# read the image into grayscale and resize to fit in current screen
im = cv2.imread("Task_3.jpg", 0)
img = cv2.resize(im, (800, 866))
# or : img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Simple Thresholding (Global) 
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# Adaptive Thresholding : Divides into sub images
thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)
thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 5)

# print the output
cv2.imshow('Original Grayscaled Image', img)
cv2.imshow('Binary Thresholding', thresh1)
cv2.imshow('Binary Thresholding Inverted', thresh2)
cv2.imshow('Truncated Thresholding', thresh3)
cv2.imshow('Set to 0 Thresholding', thresh4)
cv2.imshow('Set to 0 Inverted Thresholding', thresh5)
cv2.imshow('Adaptive Mean Thresholding', thresh6)
cv2.imshow('Adaptive Gaussian Thresholding', thresh7)

cv2.waitKey(0)
cv2.destroyAllWindows()