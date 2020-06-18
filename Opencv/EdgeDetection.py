import cv2
from matplotlib import pyplot as plt 
import numpy as np
img = cv2.imread("/home/darkie/Python/Python/Opencv/sudoku.jpeg",0)
lap = cv2.Laplacian(img,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
print(lap)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)
sobely = np.uint8(np.absolute(sobely))
sobelxy = cv2.bitwise_or(sobelx,sobely)
canny = cv2.Canny(img,100,200)

images = [img,lap,sobelx,sobely,sobelxy,canny]
titles = ["Original","Laplacian","SobelX","SobelY","SobelXY","Canny"]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.xticks([]),plt.yticks([])
    

plt.show()