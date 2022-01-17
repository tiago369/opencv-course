from configparser import Interpolation
from turtle import width
import cv2

path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

def rescaleFrame(frame, scale=0.75):
    #Photos, Images, Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

img = cv2.imread(path +"/Photos/cat_large.jpg")
img_resized = rescaleFrame(img, scale=0.1)
cv2.imshow('dog', img)
cv2.imshow('doggo', img_resized)

def changeRes(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv2.VideoCapture(path + "/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv2.imshow('ori', frame)
    cv2.imshow('resi', frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)
