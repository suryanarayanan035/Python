import datetime
import cv2

cap = cv2.VideoCapture(-1)

while True:
    ret,frame = cap.read()
    if ret == True:
        dateandtime = str(datetime.datetime.now())
        info = str(cap.get(3))+"X"+str(cap.get(4))
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(frame,dateandtime,(10,50),font,2,(0,0,0),4,cv2.LINE_AA,)
        cv2.putText(frame,info,(30,100),font,2,(0,0,0),4,cv2.LINE_AA)
        cv2.imshow("Live",frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()