import numpy as np
import cv2

def callback(event,x,y,flag,params):
    if event == cv2.EVENT_RBUTTONUP:
        font = cv2.FONT_HERSHEY_SIMPLEX
        red = img[y,x,0]
        blue = img[y,x,1]
        green = img[y,x,2]
        info = str(red)+','+str(blue)+','+str(green)
        cv2.putText(img,info,(x,y),font,2,(0,255,255),3)
        cv2.imshow("image",img)


img = np.ones((512,512,3),np.uint8)
cv2.imshow("image",img)
cv2.setMouseCallback("image",callback)

cv2.waitKey(0)
cv2.destroyAllWindows()