# write a numpy program to create am element wise comparison of two arrays : >,>=,<,<=, ==

import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,5,3,5,9])



print("Equal : ",np.equal(arr1,arr2))

print("Greater : ",np.greater(arr1,arr2))

print("Greater than or equal : ",np.greater_equal(arr1,arr2))

print("Less : ",np.less(arr1,arr2))

print("Less than or equal  : ",np.less_equal(arr1,arr2))
