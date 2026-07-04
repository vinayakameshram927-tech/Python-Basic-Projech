import numpy as np
arr1 = np.random.rand(10)   # 1D array of 10 random number between 0 and 1
arr2 = np.random.randn(3,3) # 3x3 matrix of random numbers
arr3 = np.random.randint(10,50,(4,5))
print("1D array of 10 random numbers from 0 to 1: ")
print(arr1)
print("\n3x3 matrix of random numbers using np.random.randn(): ")
print(arr2)
print("\n2D array(4x5) of random integer between 10 and 50: ")
print(arr3)

