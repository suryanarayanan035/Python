import cv2

img = cv2.imread("index.jpeg",-1)
img = cv2.line(img,(0,50),(10,0),(0,255,0),5)
img=cv2.circle(img,(150,100),20,(255,0,255),-1)
cv2.imshow("image",img)
cv2.waitKey(0)