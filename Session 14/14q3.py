import numpy as np
arr = np.random.randint(20,80,(4,5))
print(arr)
print("Minimun Value: ",arr.min(),"\tMaximum Value: ",arr.max())
print("Sum of all Elements: ",np.sum(arr))
print("Mean: ",np.mean(arr))
print("Standerd Deviation: ",np.std(arr))
print("Sum of Each row: ",np.sum(arr,axis=1))
print("Sum of Each Column: ",np.sum(arr,axis=0))