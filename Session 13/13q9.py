import numpy as np
arr = np.random.randint(1,50,20)
arr2 = np.reshape(arr,(4,5))
print("Reshaped in 4x5 Matrix: \n",arr2)
print("Sum of matrix: ",np.sum(arr2))
print("Mean of Matrix: ",np.mean(arr2))
print("Standerd Deviation : ",round(np.std(arr2)))

narr = np.max(arr2,axis=1)
print("Maximum value in each row: ",narr)
