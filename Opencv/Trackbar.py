import cv2
def nothing(x):
    pass

cv2.namedWindow("image")
cv2.createTrackbar("POS","image",0,255,nothing)
cv2.createTrackbar("BW/RGB","image",0,1,nothing)
while(1):
    img = cv2.imread("dog.jpeg")
    pos=cv2.getTrackbarPos("POS","image")
    cv2.putText(img,str(pos),(50,100),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
    s = int(cv2.getTrackbarPos("BW/RGB","image"))
    k = cv2.waitKey(1) 
    if k == 27:
        break
    if s==1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        pass
  
    cv2.imshow("image",img)
    

cv2.destroyAllWindows()