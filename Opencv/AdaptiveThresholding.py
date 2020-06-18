import cv2

img = cv2.imread("dog.jpeg",0)
th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,11)
cv2.imshow("TH1",th)
cv2.waitKey(0)
cv2.destroyAllWindows()