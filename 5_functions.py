import cv2 as cv

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

img = cv.imread(path + "/Photos/park.jpg")
cv.imshow('bgr', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#Blur image
blur =cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
#cv.imshow('canny', canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny_blur', canny)

# Dilate the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilate', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("erode", eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('crop', cropped)

cv.waitKey(0)