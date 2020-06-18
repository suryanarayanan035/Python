#!usr/bin/python3
import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread("color balls.jpeg",0)
_,mask = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
kernal = np.ones((2,2),np.uint8)

dilation = cv2.dilate(mask,kernal)
erosion = cv2.erode(mask,kernal)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
hitmiss = cv2.morphologyEx(mask,cv2.MORPH_HITMISS,kernal)
gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
ellipse = cv2.morphologyEx(mask,cv2.MORPH_ELLIPSE,kernal)
images = [img,dilation,erosion,opening,closing,tophat,hitmiss,gradient,ellipse]
titles = ["Original","Dilated","Eroded","Open","Close","Tophat","Hitmiss","Gradient","Ellipse","Images"]
for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
