from __future__ import division
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('XY-cutss.png', cv.IMREAD_GRAYSCALE)
ret, thresh = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
# imS = cv.resize(thresh, (582, 777))               # Resize image
# cv.imshow("output", img)                            # Show image
# cv.waitKey(0)
# hist = cv.calcHist([img],[0],None,[256],[0,256])
# plt.plot(hist)
# plt.show()

rows, cols = thresh.shape
lineStart = 0
imgCount = 0
for y in range(rows):
    whitePixelCount = 1
    blackPixelCount = 1
    for x in range(cols):
        if thresh.item(y, x) == 255:
            whitePixelCount += 1
        else:
            blackPixelCount += 1
    # print (str(y)+". "+str(round((blackPixelCount / whitePixelCount), 2)))
    if round((blackPixelCount / whitePixelCount), 4) > 0.76:
        if (y-lineStart)>85:
            crop_img = thresh[lineStart+28:y+28, :]
            imgCount += 1
            cv.imwrite("line" + str(imgCount) + ".png", crop_img)
        lineStart = y