import cv2
import numpy as np

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"
img = cv2.imread(path +"/Photos/cats.jpg")
cv2.imshow('', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv2.circle(blank, (img.shape[1]//2+45  , img.shape[0]//2), 100, 255, -1)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('masked', masked)




cv2.waitKey(0)
