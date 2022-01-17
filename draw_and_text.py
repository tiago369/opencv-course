import cv2
import numpy as np

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

blank = np.zeros((500,500,3), dtype='uint8')
#cv2.imshow('blank', blank)

blank[:] = 0,255,0
#cv2.imshow('green', blank)

blank[:] = 0,0,255
#cv2.imshow('red', blank)

blank[:] = 0,0,0
blank[200:300, 300:400] = 255,0,0
#cv2.imshow('blue', blank)

#Rectangle

blank[:] = 0,0,0
cv2.rectangle(blank, (0,0), (250,250), (100,150,200), thickness=2)
#cv2.imshow('rectangle', blank)

blank[:] = 0,0,0
cv2.rectangle(blank, (0,0), (250,500), (100,150,200), thickness=cv2.FILLED)
#cv2.imshow('FILL', blank)

blank[:] = 0,0,0
cv2.rectangle(blank, (0,0), (250,500), (100,150,200), thickness=-1)
#cv2.imshow('FILL1', blank)

blank[:] = 0,0,0
cv2.rectangle(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,255,0), thickness=-1)
#cv2.imshow('FILL2', blank)

# Circle
cv2.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0,0,255), thickness=-1)
cv2.imshow('circle', blank)

# Line
cv2.line(blank, (0,0), (500,500), (255,0,0), thickness=5)
cv2.imshow('line', blank)

# Text
cv2.putText(blank, 'Helloo XD', (255,255), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv2.imshow('TXT', blank)

cv2.waitKey(0)