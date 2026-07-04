import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

add = A + B
dot = np.dot(A,B)
mul = A * B
print("Matrix Addition: \n",add)
print("\nMatrix Multiplication (np.dot()): \n",dot)
print("\nMatrix Multiplication (Element-wise): \n",mul)