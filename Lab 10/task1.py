import cv2 as cv
import numpy as np

img = cv.imread("fruits.png",cv.IMREAD_GRAYSCALE)

# find otsu's threshold value with OpenCV function
ret, otsu = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
structuringElement = np.ones((3,3),np.uint8)
structuringElement2 = np.ones((5,5),np.uint8)
structuringElement3 = np.ones((9,9),np.uint8)
imgDilated = cv.dilate(otsu,structuringElement,iterations=11)
imgClosed = cv.erode(imgDilated,structuringElement,iterations=12)
# imgDilatedAfterClosing = cv.dilate(imgClosed,structuringElement2,iterations=4)
imgErodedAfterOpening = cv.erode(imgClosed,structuringElement2,iterations=2)

cv.imwrite("result.png",otsu)
cv.imwrite("result1.png",imgDilated)
cv.imwrite("result2.png",imgClosed)
# cv.imwrite("result3.png",imgDilatedAfterClosing)
cv.imwrite("result4.png",imgErodedAfterOpening)