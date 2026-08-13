import numpy as np

# sample = np.array([1,2,3,4,5,6])

# print(sample.shape)

# sample = sample.reshape(2,3)

# print(sample)
# print(sample.shape)

# sample2 = np.array([10,20,30,40])

# print(sample2)

# print(sample2.shape)

# sample2 = sample2.reshape(4,1)
# print(sample2)

# sample2 = sample2.reshape(1,-1) #parameter 1 = row num, parameter 2 = automatically calculate the column num
# print(sample2)

a1 = np.array([10,20,30,40,50,60])

print(a1.shape)

a2 = a1.reshape(1,-1)

print(a1,"\n",a2)

print("shape a2 : ",a2.shape)