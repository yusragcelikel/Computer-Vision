import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(2)

while True:
  success, img = cap.read()


  while True:
    success, img = cap.read()
    cv2.imshow("Image", img)  # kamera görüntüsü image adlı pencerede gosterilir

    haar_cascade = cv2.CascadeClassifier("haar_face.xml")
    faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)


    #print(f"Number of faces found = {len(faces_rect)}")
    cv2.putText(img, f"Number of faces found = {len(faces_rect)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)


    for (x, y, w, h) in faces_rect:
      cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)