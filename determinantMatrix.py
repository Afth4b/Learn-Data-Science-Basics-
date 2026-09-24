# find the determinant of matrix A

import numpy as np

a = np.array([
    [1,2,3],
    [0,1,4],
    [5,6,0]
])

determinant = np.linalg.det(a)
print(determinant)

inverse = np.linalg.inv(a)
print(inverse)