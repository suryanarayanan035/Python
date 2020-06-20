import cv2

img = cv2.imread("opencv-logo.png")
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresholded_image = cv2.threshold(grayimg,200,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresholded_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,1,(100,80,255),3)
cv2.imshow("image",img)
cv2.imshow("Thresholded Image",thresholded_image)
print(len(contours))
cv2.waitKey(0)
cv2.destroyAllWindows()