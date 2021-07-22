import cv2

tiling_factor = 2  # tiling factor defines no of tiles that can fit vertically or horizontally
img = cv2.imread('lab07.jpg', 0)

img_height, img_width = img.shape
tile_width = img_width / tiling_factor
tile_height = img_height / tiling_factor

for tile_vertical in range(tiling_factor):
    for tile_horizontal in range(tiling_factor):
        start = (tile_vertical*tile_height,tile_horizontal*tile_width)
        end = (start[0] + tile_height, start[1] + tile_width)
        img[start[0]:end[0],start[1]:end[1]]=cv2.equalizeHist(img[start[0]:end[0],start[1]:end[1]])


cv2.imwrite('TileEqualized.png', img)
