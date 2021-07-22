import cv2 as cv

img = cv.imread("Signature.png", cv.IMREAD_GRAYSCALE)
ret, thresh = cv.threshold(img, 20, 255, cv.THRESH_BINARY)

height, width = img.shape

# Task 1

left, top = width, height
right = bottom = 0

for y in range(height):
    for x in range(width):
        pixel = img.item(y, x)
        if pixel == 0:
            if x > right:
                right = x
            if x < left:
                left = x
            if y > bottom:
                bottom = y
            if y < top:
                top = y

boundaryImg = thresh[top:bottom, left:right]

cv.imwrite("Task1_output.png", boundaryImg)

# Task 2
cx = 0
cy = 0
n = 0

for y in range(height):
    for x in range(width):
        if thresh.item(y, x) is 0:
            cx += x
            cy += y
            n = n+1

cx = cx/n
cy = cy/n


#Task 3

for y in range(height):
    thresh[y,cx] = 0

for x in range(width):
    thresh[cy,x] = 0

cv.imwrite("Task3_output.png", boundaryImg)

#Task 4

prev = thresh.item(0,0)
NoOfBlackToWhiteTransitions=0

for y in range(1,height):
    for x in range(1,width):
        curr = thresh.item(y,x)
        if curr is 255 and prev is 0:
            NoOfBlackToWhiteTransitions += 1

        prev = curr


print ("No of Black to white transitions are: "+str(NoOfBlackToWhiteTransitions))