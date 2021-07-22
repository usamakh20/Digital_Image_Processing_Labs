import cv2, numpy as np

img = cv2.imread('two_cats.jpg', cv2.IMREAD_GRAYSCALE)
img_height, img_width = img.shape
output_img = np.zeros((img_height, img_width), np.uint8)

hedge_filter = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
vedge_filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

a = b = 3/2
img = np.pad(img, a, 'constant')

sum_of_weighted_products = 0

for y in range(a, img_height + a):
    for x in range(b, img_width + b):
        for t in range(-a, a + 1):
            for s in range(-b, b + 1):
                sum_of_weighted_products += img.item(y + t, x + s) * hedge_filter.item(t + a, s + b) # Horizontal edges extraction
                sum_of_weighted_products += img.item(y + t, x + s) * vedge_filter.item(t + a, s + b) # Vertical edges extraction

        output_img[y - a, x - b] = int(sum_of_weighted_products)

cv2.imwrite('Edge extraction.png', output_img)