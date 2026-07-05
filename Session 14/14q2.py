import numpy as np
arr = np.random.randint(1,50,20)
print(arr)
print("Minimum: ",arr.min(),"  Index: ",np.argmin(arr))
print("MAximum: ",arr.max(),"  Index: ",np.argmax(arr))
print("Sum of all Numbers: ",np.sum(arr))
print("Mean: ",np.mean(arr),"  Standerd Deviation: ",np.std(arr))