import numpy as np

array = np.full((5,5),22,np.uint8)
array[1:-1,1:-1] = 5

print(array.min())
print(array.min())
print(array.mean())
print(np.cos(array))
print(np.median(array))
print(np.linalg.det(array))
array[0,4] = 4
array[0,3] = 56
print(np.min(array,axis=0))
print(np.max(array,axis=1))
