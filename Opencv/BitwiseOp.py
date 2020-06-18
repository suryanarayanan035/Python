import cv2 
import numpy as np 

img1 = np.zeros((360,360,3))
img2 = np.ones((360,360,3))
img1[0:60,140:220] =np.ones((60,80,3),np.uint8)
img2[0:360,180:360] = np.zeros((360,180,3),np.uint8)
img3 = cv2.bitwise_not(img1)
cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("Bitwise Op",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()