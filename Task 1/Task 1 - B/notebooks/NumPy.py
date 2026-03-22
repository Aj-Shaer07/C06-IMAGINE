# Create arrays
import numpy as np
a=np.array([1,2,3,4])
print (a)

# Element-wise operations
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)

# Matrix multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.dot(A,B)
print(C)

# Array shapes
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

# Vectorized computation
a=np.array([1,2,3,4])
b=a*2

