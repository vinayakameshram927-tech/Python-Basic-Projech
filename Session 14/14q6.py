import numpy as np
arr = np.random.randint(1,100,(5,5))
print(arr)
print("Diagonal Elements: ",np.diagonal(arr))
print("Elements greater than 50: ",arr[arr > 50])
arr[arr < 30] = 0
print("Elements less than 30 are replaced by 0: \n",arr)