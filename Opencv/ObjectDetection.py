import cv2
import numpy as np

def callback(x):
    pass
cv2.namedWindow("Tracker")
cv2.createTrackbar("LH","Tracker",0,255,callback)
cv2.createTrackbar("LS","Tracker",0,255,callback)
cv2.createTrackbar("LV","Tracker",0,255,callback)
cv2.createTrackbar("UH","Tracker",0,255,callback)
cv2.createTrackbar("US","Tracker",0,255,callback)
cv2.createTrackbar("UV","Tracker",0,255,callback)

while True:
    img = cv2.imread("color balls.jpeg")
    lh = cv2.getTrackbarPos("LH","Tracker")
    ls = cv2.getTrackbarPos("LS","Tracker")
    lv = cv2.getTrackbarPos("LV","Tracker")
    uh = cv2.getTrackbarPos("UH","Tracker")
    us = cv2.getTrackbarPos("US","Tracker")
    uv = cv2.getTrackbarPos("UV","Tracker")

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_bound = np.array([lh,ls,lv])
    upper_bound = np.array([uh,us,uv])
    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    res = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("mask",mask)
    cv2.imshow("HSV",hsv)
    cv2.imshow("Result",res)
    cv2.waitKey(1)

cv2.destroyAllWindows()