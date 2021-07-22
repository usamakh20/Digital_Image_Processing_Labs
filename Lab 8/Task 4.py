import cv2,numpy as np

img = cv2.imread('saltandpaper.tif', cv2.IMREAD_GRAYSCALE)
img_height, img_width = img.shape

filter_size = int(input("Enter filter size: "))
a=filter_size/2
img = np.pad(img, a, 'constant')
filtered_image = np.zeros((img_height, img_width), np.uint8)
for y in range(a,img_height+a):
    for x in range(a,img_width+a):
        filtered_image[y-a,x-a] = np.median(img[y:y+filter_size,x:x+filter_size])


cv2.imwrite("salt_paper_filtered.png",filtered_image)