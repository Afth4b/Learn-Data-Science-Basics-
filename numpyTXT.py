# numpy program to save a given array to a text file and load it

# np.savetxt - used to store array as textfile
# np.loadtxt - load array from text file 

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

np.savetxt('file.txt',arr,delimiter=',')

arrayy = np.loadtxt('file.txt',delimiter=',')
print(arrayy)