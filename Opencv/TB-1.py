import cv2

def callbackRGB(x):
    print("X:",x)

def callbackBW(x):
    pass


cv2.namedWindow("image")
cv2.createTrackbar("RGB","image",0,255,callbackRGB)
cv2.createTrackbar("RGB/BW","image",0,1,callbackBW)
while 1:
    img = cv2.imread("dog.jpeg")
    pos = cv2.getTrackbarPos("RGB","image")
    switch = cv2.getTrackbarPos("RGB/BW","image")
    cv2.putText(img,str(pos),(50,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,0,255),1)
    if switch == 1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        pass
    cv2.imshow("image",img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()