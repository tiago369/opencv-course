import cv2


path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"
img = cv2.imread(path +"/Photos/cats.jpg")
cv2.imshow('', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple Threshold
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('simple thresh', thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('simple thresh', thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow('Adaptive threshold', adaptive_thresh)

cv2.waitKey(0)
