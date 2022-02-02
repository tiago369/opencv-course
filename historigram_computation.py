from turtle import circle
import cv2
import matplotlib.pyplot as plt
import numpy as np

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"
img = cv2.imread(path +"/Photos/cats.jpg")
cv2.imshow('', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)

circle = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv2.bitwise_and(img, img, mask=circle)

# Grayscale histogram
# gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram
plt.figure()
plt.title('Rgb Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv2.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv2.waitKey(0)
