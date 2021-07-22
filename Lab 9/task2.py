import cv2 as cv
import numpy as np

img = cv.imread("urduText.jpg",cv.IMREAD_GRAYSCALE)

structuringElement = np.ones((3,3),np.uint8)


ret, thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

imgDilated = cv.dilate(thresh,structuringElement,iterations=1)
imgClosed = cv.erode(imgDilated,structuringElement,iterations=3)

cv.imwrite("corrected.png",imgClosed)
cv.imwrite("grey.png",img)