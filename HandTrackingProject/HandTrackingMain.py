import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1) #video objectimizi oluşturduk

mpHands = mp.solutions.hands
hands = mpHands.Hands() #hand objectimizi oluşturduk
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #hands class'ı sadece rgb kullandığı için RGBye dönüşüm yaptık
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks) #kanera görüntüsinde el olup olmadığını söyler

    if results.multi_hand_landmarks:# kaç el olduğunu belirlemek için
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 4: #Tip of the thumb'ı işaretler
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img) #kamera görüntüsü image adlı pencerede gosterilir
    cv2.waitKey(1)