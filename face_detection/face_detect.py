import cv2
from matplotlib import scale

path ="/home/senai/tiago-projects/opencv-course/Resources"
img = cv2.imread(path +"/Photos/group 1.jpg")
cv2.imshow('', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('/home/senai/tiago-projects/opencv-course/face_detection/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)
