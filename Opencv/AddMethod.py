import cv2
import numpy as np 
img1 = cv2.imread("dog.jpeg")
img2 = cv2.imread("football.jpg")
img1 = cv2.resize(img1,(img2.shape[1],img2.shape[0]))
print(img1.size,img2.size)
img = cv2.addWeighted(img1,0.5,img2,0.1,0)
cv2.imshow("added",img)
cv2.waitKey(0)
cv2.destroyAllWindows()