import cv2 as cv
import numpy as np

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

img = cv.imread(path +"/Photos/cats.jpg")
cv.imshow('', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('b', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'lenght of list = {len(contours)}')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('cont', blank)

cv.waitKey(0)