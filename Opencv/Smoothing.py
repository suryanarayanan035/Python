import cv2
from matplotlib import pyplot as plt 
import numpy as np 

img = cv2.imread("//home//darkie//Python//Python//Opencv//saltandpepper.png")
print(img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
filter2d = cv2.filter2D(img,-1,kernel)
gaussianblur = cv2.GaussianBlur(img,(3,3),5,5)
medianblur = cv2.medianBlur(img,3)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)

outputs = [img,filter2d,gaussianblur,medianblur,bilateralFilter]
titles = ["Original","Filtered2D","Gaussian Blur","MedianBlur","BilateralFilter"]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(outputs[i],"gray")
    plt.xticks([]),plt.yticks([])
    plt.title(titles[i])

plt.show()

