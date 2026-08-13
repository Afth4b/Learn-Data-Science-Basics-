# numpy program to create a vector with values fro m 0-20 and 
# change this sign of the numbers in the range from 9-15

import numpy as np

arr = np.arange(0,20+1)

print(arr)

var = (arr > 8) & (arr < 15)

arr[var] *= -1

print(arr)