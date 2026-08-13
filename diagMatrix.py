# write a numpy program to create 5*5 0 matrix on the main diagonal equal to 1 2 3 4 5 

import numpy as np

arr = np.diag(np.arange(1,5+1))

print(arr)