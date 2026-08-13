import numpy as np

array = np.array([1,2,3,4,5,6])
print(array)
print(array.shape)
a1 = array.reshape(2,3)
print(a1)
print(a1.shape)
a2 = np.array([10,20,30,40])
print(a2)
print(a2.shape)
print(a2.reshape(4,1))
print(a2.reshape(1,-1))#the parameter 1 make the array have 1 row and -1 numpy automatically calculate the number of columns
