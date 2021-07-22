import cv2, numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lab07.jpg', 0)
equ = cv2.equalizeHist(img)

plt.hist(img.ravel(), 256, [0, 256], color="green" ,label="original")
plt.hist(equ.ravel(), 256, [0, 256], color="blue",label="equalized")
plt.ylabel('Intensities')
plt.xlabel('Pixel Values')
plt.savefig("hist.png")
plt.legend()
plt.savefig("hist.png")
res = np.hstack((img, equ))  # stacking images side-by-side

cv2.imwrite('OriginalAndEqualized.png', res)
