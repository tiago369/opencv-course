import cv2

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"
img = cv2.imread(path +"/Photos/park.jpg")
cv2.imshow('', img)

# Averaging
average = cv2.blur(img, (7,7))
cv2.imshow('Average blur', average)

# Gaussian Blur
gauss = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gauss", gauss)

# Median Blur
median = cv2.medianBlur(img, 7)
cv2.imshow('Median', median)

# Bilateral
bilateral = cv2.bilateralFilter(img, 10, 35, 25)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
