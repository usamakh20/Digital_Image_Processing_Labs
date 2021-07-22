import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('hist2.tif', cv.IMREAD_GRAYSCALE)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
# plt.show()
plt.savefig("hist.png")
plt.hist()
