import numpy as np 

array1 = np.zeros((5,5))
array2 = np.ones(5,np.int)
array3 = np.arange(100,200,5,np.int32)
array3 = np.reshape(array3,(5,4))
array4 = np.linspace(1,3,3)
array5 = np.random.rand(8,2)
array5.reshape(4,4)
print("array 1:",array1)
print("array 2:",array2)
print("array 3:",array3)
print("array 4:",array4)
print("array 5:",array5.reshape(2,8))

