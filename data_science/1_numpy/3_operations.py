import numpy as np

x = np.array([[2,3,4],[3,4,5]])
y = np.array([[1,2,3],[4,5,6]])

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(y**2)
print(y.T)
print(x.dot(y.T))