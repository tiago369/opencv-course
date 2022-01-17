import cv2

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

img = cv2.imread(path +"/Photos/cat_large.jpg")

cv2.imshow('', img)

cv2.waitKey(0)