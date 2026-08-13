# numpy program to create a matrix and to compute sum of all elements, sum of each column and sum of each row

import numpy as np

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print("Total sum : ",np.sum(arr))

# print("Column wise sem : ",np.sum(arr,axis = 0))

# print("Row wise sem : ",np.sum(arr,axis = 1))


arr = np.arange(1,100+1)

arr = arr.reshape(10,10)

print("Total sum : ",np.sum(arr))

print("Column wise sem : ",np.sum(arr,axis = 0))

print("Row wise sem : ",np.sum(arr,axis = 1))

# print(arr)