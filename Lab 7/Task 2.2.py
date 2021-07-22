import cv2, numpy as np

window_size_factor = 2  # window size factor defines what fraction will be the size of window compared to the original image
img = cv2.imread('lab07.jpg', 0)

img_height, img_width = img.shape
window_width = img_width / window_size_factor
window_height = img_height / window_size_factor

window_start = (0, 0)
window_end = (window_height, window_width)

tile_equalized = np.zeros((img_height, img_width), np.uint8)

for y in range(window_height):
    for x in range(window_width):
        tile_equalized[y:window_height+y, x:window_width+x] = cv2.equalizeHist(img[y:window_height+y, x:window_width+x])

cv2.imwrite('SlideEqualized.png', tile_equalized)
