import cv2

img = cv2.imread('unsharpmasking.tif', cv2.IMREAD_GRAYSCALE)
img_height, img_width = img.shape
blur = cv2.GaussianBlur(img, (7, 7), 0)

for y in range(img_height):
    for x in range(img_width):
        img[y, x] = (img.item(y, x) - blur.item(y, x)) + img.item(y, x)

cv2.imwrite('unsharp.png',img)