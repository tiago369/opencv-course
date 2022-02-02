import cv2


path ="/home/senai/tiago-projects/opencv-tutorials/opencv-course/Resources"

capture = cv2.VideoCapture(path + "/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv2.imshow('', frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)