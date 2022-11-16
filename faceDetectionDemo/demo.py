import cv2
import mediapipe as mp

cap = cv2.VideoCapture(2) #video objectimizi oluşturduk

while True:
    success, img = cap.read()

    haar_cascade = cv2.CascadeClassifier("haar_face.xml")
    faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)

    print(f"Number of faces found = {len(faces_rect)}")

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)


    cv2.imshow("Image", img)  # kamera görüntüsü image adlı pencerede gosterilir
    cv2.waitKey(1)