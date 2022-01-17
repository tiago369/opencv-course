import cv2

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"
img = cv2.imread(path +"/Photos/park.jpg")
cv2.imshow('', img)

# BGR to Grayscale



cv2.waitKey(0)