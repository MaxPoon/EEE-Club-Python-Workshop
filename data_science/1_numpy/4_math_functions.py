import numpy as np
a = np.array([[-4, -2, 1, 3, 5], [4, 2, 7, 1, 3]])
print(a)

print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())

# mean value of each column
print("mean value of each column:")
print(a.mean(0))
# std of each column
print("std of each column:")
print(a.std(0))

# mean value of each row
print("mean value of each row:")
print(a.mean(1))