import cv2 as cv
import numpy as np

img = cv.imread("ThumbImpression.png", cv.IMREAD_GRAYSCALE)

_, thresh = cv.threshold(img, 190, 255, cv.THRESH_BINARY)

structuringElement = np.ones((3, 3), np.uint8)

skeleton = cv.dilate(thresh, structuringElement, iterations=4)

cv.imwrite("skeleton.png", skeleton)
