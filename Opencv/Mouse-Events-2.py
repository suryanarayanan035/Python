import cv2
import numpy as np

def callback(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        red = img[x,y,0]
        green = img[x,y,1]
        blue = img[x,y,2]
        img1 = np.zeros((512,512,3),np.uint8)
        img1[:] =[red,green,blue] 
        cv2.imshow("image1",img1)
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x,y))
        if(points.__len__()>1):
            cv2.line(img,points[-1],points[-2],(0,0,255),5)
            cv2.imshow("image",img)
        else:
            cv2.circle(img,(x,y),5,(255,0,0),3)
            cv2.imshow("image",img)

img = cv2.imread("index.jpeg",-1)
cv2.imshow("image",img)
cv2.setMouseCallback("image",callback)
points = []
cv2.waitKey(0)
cv2.destroyAllWindows()

