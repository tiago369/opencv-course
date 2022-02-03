import numpy as np
import cv2

haar_cascade = cv2.CascadeClassifier('/home/senai/tiago-projects/opencv-course/face_detection/haar_face.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']


# features = np.load('features.npy')
# labels =np.load('labels.npy')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv2.imread(r'/home/senai/tiago-projects/opencv-course/Resources/Faces/val/ben_afflek/2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('pessoa', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,225,0), thickness=2)

cv2.imshow('detected face', img)

cv2.waitKey(0)