import numpy as np

array = np.full((3,2,2),44)
print("First Element:",array[0,0,0])
array[1,1,1] = 20
print("Replaced Element",array[1,1,1])
array[1:3,:,1] = 5
print("Except first grid 2nd colum second row",array[1:3,:,1:])
print("Array:",array)