import numpy as np

x = np.ones([2, 3])
y = np.array([[1,2,3],[4,5,6]])

vstack = np.vstack([x,y])
print("vstack:")
print(vstack)

hstack = np.hstack([x,y])
print("hstack:")
print(hstack)