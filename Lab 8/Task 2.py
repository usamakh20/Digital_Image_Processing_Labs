import cv2, numpy as np

img = cv2.imread('smoothing.tif', cv2.IMREAD_GRAYSCALE)
img_height, img_width = img.shape
output_img = np.zeros((img_height, img_width), np.uint8)
curr_filter = np.array(
    [[1, 1, 2, 2, 2, 1, 1], [1, 2, 2, 4, 2, 2, 1], [2, 2, 4, 8, 4, 2, 2], [2, 4, 8, 16, 8, 4, 2], [2, 2, 4, 8, 4, 2, 2],
     [1, 2, 2, 4, 2, 2, 1], [1, 1, 2, 2, 2, 1, 1]])
filter_size = curr_filter.shape[0]
a = b = filter_size / 2
img = np.pad(img, a, 'constant')

sum_of_weighted_products = 0
sum_of_weights = 0

for y in range(a, img_height + a):
    for x in range(b, img_width + b):
        for t in range(-a, a + 1):
            for s in range(-b, b + 1):
                sum_of_weighted_products += img.item(y + t, x + s) * curr_filter.item(t + a, s + b)
                sum_of_weights += curr_filter.item(t, s)

        output_img[y - a, x - b] = int(sum_of_weighted_products / sum_of_weights)
        sum_of_weighted_products = 0
        sum_of_weights = 0

cv2.imwrite('Averaged by Gaussian.png', output_img)
