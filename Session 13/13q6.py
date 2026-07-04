import numpy as np
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])
add = v1 + v2
sub = v1 - v2
mul = v1 * v2
dot = np.dot(v1,v2)
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",mul)
print("Dot Product: ",dot)