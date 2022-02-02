import cv2
import numpy as np


path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"
img = cv2.imread(path +"/Photos/cats.jpg")
cv2.imshow('', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('laplacian', lap)


cv2.waitKey(0)
