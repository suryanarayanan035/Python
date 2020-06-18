import cv2
import numpy as np 
def callback(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x,y))
        if points.__len__ ()== 2:
            print(points)
            cv2.rectangle(img,points[0],points[1],(0,255,0),3)
            ball = img[283:447,273:440]
            img[0:164,0:167] = ball
            cv2.imshow("image",img)


img = cv2.imread("football.jpg",-1)
cv2.imshow("image",img)
cv2.setMouseCallback("image",callback)

points  = []
cv2.waitKey(0)
cv2.destroyAllWindows()