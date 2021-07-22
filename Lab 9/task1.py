import cv2 as cv
import numpy as np

img = cv.imread("signature.png",cv.IMREAD_GRAYSCALE)

structuringElement = np.ones((3,3),np.uint8)

imgEroded = cv.erode(img,structuringElement,iterations=10)
imgDialated = cv.dilate(img,structuringElement,iterations=10)


cv.imwrite("imgEroded.png",cv.bitwise_not(imgEroded))
cv.imwrite("imgDialated.png",cv.bitwise_not(imgDialated))

imgErodedThenDialated = cv.dilate(imgEroded,structuringElement,iterations=10)
imgDialatedThenEroded = cv.erode(imgDialated,structuringElement,iterations=10)

cv.imwrite("imgOpened.png",cv.bitwise_not(imgErodedThenDialated))
cv.imwrite("imgClosed.png",cv.bitwise_not(imgDialatedThenEroded))