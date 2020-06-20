import cv2
import numpy as np

apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")

apple_copy = apple.copy()
orange_copy = orange.copy()

apple_gpyramid =[apple]
orange_gpyramid = [orange]
#Gaussian pyramids
for i in range(6):   
    apple_copy= cv2.pyrDown(apple_copy)
    apple_gpyramid.append(apple_copy)
    orange_copy= cv2.pyrDown(orange_copy)
    orange_gpyramid.append(orange_copy)

#Laplacian Pyramids
apple_lp = [apple_gpyramid[5]]
orange_lp = [orange_gpyramid[5]]
for i in range(5,0,-1):
    apple_gaussian_extended = cv2.pyrUp(apple_gpyramid[i])
    lapalcian_apple = cv2.subtract(apple_gpyramid[i-1],apple_gaussian_extended)
    apple_lp.append(lapalcian_apple)
    orange_gaussian_extended = cv2.pyrUp(orange_gpyramid[i])
    lapalcian_orange = cv2.subtract(orange_gpyramid[i-1],orange_gaussian_extended)
    orange_lp.append(lapalcian_orange)

app_orange_pyramid = []
n= 0
for apple_lap,orange_lap in zip(apple_lp,orange_lp):
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):]))
    app_orange_pyramid.append(laplacian)

apple_orange_reconstructed =app_orange_pyramid[0]

for i in range(1,6):
    apple_orange_reconstructed =cv2.pyrUp(apple_orange_reconstructed)
    apple_orange_reconstructed =cv2.add(app_orange_pyramid[i],apple_orange_reconstructed)


cv2.imshow("Result",apple_orange_reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()