import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('hist2.tif', cv.IMREAD_GRAYSCALE)

rows, cols = img.shape
intensities = {}
for y in range(rows):
    for x in range(cols):
        pix_value = img.item(y, x)
        if pix_value in intensities:
            intensities[pix_value] += 1
        else:
            intensities[pix_value] = 1

Transform_dict = {}
prev_val = 0
for key, value in intensities.iteritems():
    Transform_dict[key] = int((value / float(rows * cols)) * 255) + prev_val
    prev_val = Transform_dict[key]

for y in range(rows):
    for x in range(cols):
        pix_value = img.item(y, x)
        img[y, x] = Transform_dict[pix_value]

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
# plt.show()
plt.savefig("equalized_hist.png")
cv.imwrite("equalized.jpg", img)