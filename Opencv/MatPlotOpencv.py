import cv2
from matplotlib import pyplot as plt 

img = cv2.imread("dog.jpeg",0)
ret,th1 = cv2.threshold(img,50,50,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,50,50,cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(img,50,50,cv2.THRESH_TOZERO)
ret,th4 = cv2.threshold(img,50,50,cv2.THRESH_TRUNC)
ret,th5 = cv2.threshold(img,50,50,cv2.THRESH_TOZERO_INV)

titles=['Original',"BINARY","BINARY_INV","ZERO","ZERO_INV","TRUNC"]
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()