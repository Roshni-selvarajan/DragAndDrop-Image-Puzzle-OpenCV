import cv2
import HandTrackingModule as htm 

detector=htm.handDetector()


cap=cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)
colorR=(255,0,255)

cx,cy,w,h=100,100,200,200 

while True:
    success, img=cap.read()

    img=cv2.flip(img,1)
    #find hands
    img=detector.findHands(img)
    #find landmarks
    
    lmList,_=detector.findPosition(img)
    if lmList:
        cursor = lmList[8]
        if isinstance(cursor, list) and len(cursor) >= 2:
            if cx - w//2 < cursor[0] < cx + w//2 and cy - h//2 < cursor[1] < cy + h//2:
                colorR = (0, 255, 0)
                cx, cy = cursor[0], cursor[1]
            else:
                colorR = (255, 0, 255)
        else:
        # Handle case where cursor doesn't contain expected coordinates
            colorR = (255, 0, 255)
            cv2.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),colorR,cv2.FILLED)
            if len(lmList) != 0:
                print(lmList[4])
                cv2.imshow("image",img)
                if cv2.waitKey(1) & 0xFF==27:break

cv2.release()
cv2.destroyAllWindows()

