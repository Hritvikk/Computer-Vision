import cv2
import time
import os
import HandTrackingModule as htm
 
wCam, hCam = 640, 480

# Real Time Video Input 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
 
pTime = 0
 
detector = htm.handDetector(detectionCon=0.75)
 
tipIds = [4, 8, 12, 16, 20]
 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
 
    if len(lmList) != 0:
        fingers = []
 
        # Thumb
        if lmList[4][1] > lmList[3][1]:
            fingers.append("T")
        
        # Index Finger
        if lmList[8][2] < lmList[6][2]:
            fingers.append("I")    

        # Middle Finger
        if lmList[12][2] < lmList[10][2]:
            fingers.append("M")

        # Ring Finger
        if lmList[16][2] < lmList[14][2]:
            fingers.append("R")
        
        # Baby Finger
        if lmList[20][2] < lmList[18][2]:
            fingers.append("B")
        
        # Displaying Output
        cv2.putText(img, ",".join(fingers), (400, 110), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)
 
    # FPS Calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    # Displaying FPS
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Finger Detector", img)
    cv2.waitKey(1)
