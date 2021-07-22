import cv2 as cv
from PIL import Image
import PIL.ImageOps
import numpy as np

image = Image.open('lena_color.gif')
rgb_image = image.convert('RGB')
gray_image_pil = image.convert('L')
gray_image_opencv = np.array(gray_image_pil)
ret, bin_image_inv = cv.threshold(gray_image_opencv, 120, 255, cv.THRESH_BINARY_INV)

inverted_image = PIL.ImageOps.invert(rgb_image)
inverted_grey_image = PIL.ImageOps.invert(gray_image_pil)
inverted_image.save('inverted.png')
inverted_grey_image.save('greyscale.png')
cv.imwrite('binary.png', bin_image_inv)

rows, cols = rgb_image.size
grey_pix = gray_image_pil.load()
gray_image_copy = gray_image_pil.copy()  # <-- Instead of copy.copy(image)
gray_copy_pix = gray_image_copy.load()

# Horizontal gradient
for y in range(rows):
    for x in range(cols - 1):
        grey_pix[x, y] = grey_pix[x + 1, y] - grey_pix[x, y]


#Vertical gradient
for x in range(cols):
    for y in range(rows-1):
        gray_copy_pix[x, y] = gray_copy_pix[x, y+1] - gray_copy_pix[x, y]

for y in range(rows):
    for x in range(cols - 1):
        grey_pix[x, y] = gray_copy_pix[x, y] + grey_pix[x, y]


gray_image_pil.save('gradient.png')