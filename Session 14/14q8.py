import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

print("Element Wise-Multiplication: ",A*B)
print("Matrix multiplication: ",np.dot(A,B))

# Element wise multiplication performed on corresponding elements
# multiply row of first matrix by column of second matrix