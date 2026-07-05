import numpy as np
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print("First Row: ",arr[0])
print("last Column: ",arr[:,-1])
print("Center 2x2 submatrix: ",arr[1:3,1:3])
print("All Even numbers from the array: ",arr[arr % 2 == 0])