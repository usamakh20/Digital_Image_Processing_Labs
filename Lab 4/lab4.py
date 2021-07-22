import cv2 as cv
import random
import numpy as np

similar_labels = {}


def getcolor():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


def getneighbourlabel(x, y):
    color = getcolor()
    neighbour_north = identified_objects[y - 1, x]
    neighbour_west = identified_objects[y, x - 1]
    labeled = False
    if all(neighbour_north != [0, 0, 0]):
        color = neighbour_north
        labeled = True
    elif all(neighbour_west != [0, 0, 0]):
        color = neighbour_west
        labeled = True

    if (labeled == True) and all(neighbour_north != neighbour_west):
        if all(neighbour_west != [0, 0, 0]):
            similar_labels[str(neighbour_north)] = neighbour_west

    return color


# img = cv.imread('Lab4.png', cv.IMREAD_GRAYSCALE)
# ret, thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
# rows, cols = thresh.shape
# identified_objects = np.zeros((rows + 2, cols + 2, 3), np.uint8)
# cv.imwrite("thresh.png", thresh)

array = np.array([[1,1,0,1,1,1,0,1],
                  [1,1,0,1,0,1,0,1],
                  [1,1,1,1,0,0,0,1],
                  [0,0,0,0,0,0,0,1],
                  [1,1,1,1,0,1,0,1],
                  [],
                  [],
                  []])


for y in range(rows):
    for x in range(cols):
        if thresh.item(y, x) == 255:
            identified_objects[y, x] = getneighbourlabel(x, y)

for y in range(rows):
    for x in range(cols):
        if all(identified_objects[y, x] != [0, 0, 0]):
            newcolor = similar_labels.get(str(identified_objects[y, x]), None)
            if newcolor is not None:
                identified_objects[y, x] = newcolor

# imS = cv.resize(identified_objects, (1016, 662))  # Resize image
cv.imwrite("output.png", identified_objects)
