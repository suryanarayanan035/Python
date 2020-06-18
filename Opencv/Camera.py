import cv2

cap = cv2.VideoCapture(-1)
cap.set(3,3000)
cap.set(4,3000)
print("Cam status:",cap.isOpened())
while True:
    ret,frame=cap.read()
    print("Ret:",ret)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()