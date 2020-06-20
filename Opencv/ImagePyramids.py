import cv2
 

img = cv2.imread("/home/darkie/Python/Python/Opencv/lena.jpg")
gp =[img]
for i in range(6):
    gp.append(cv2.pyrDown(gp[i])) 
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()