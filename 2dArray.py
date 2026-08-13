# write a program to create a 2d array(matrix) using numpy and print it

import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Matrix A = \n",a)
print("Matrix B = \n",b)

c = a + b

print("Matrix addition : \n",c)

c = a - b

print("Matrix subtraction : \n",c)

c = a * b

print("Matrix multiplication: \n",c)

c = np.dot(a,b)

print("Matrix multiplication: \n",c)

c = a.transpose()

print("Transpose of Matrix A: \n",c)

c = b.transpose()

print("Transpose of Matrix B: \n",c)