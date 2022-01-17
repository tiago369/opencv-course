from ctypes import resize
from turtle import width
import cv2 as cv
import numpy as np

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

img = cv.imread(path + "/Photos/park.jpg")
cv.imshow('bgr', img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 150)
cv.imshow('trans', translated)

# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 120)
cv.imshow('rotate', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resized)

# Flipping
flip = cv.flip(img, 0)
cv.imshow('flip 0', flip)

flip = cv.flip(img, 1)
cv.imshow('flip 1', flip)

flip = cv.flip(img, -1)
cv.imshow('flip -1', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)