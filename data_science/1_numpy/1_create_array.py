import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)

print("m.shape:")
print(m.shape)

n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
print("n = arange(0,30,2):")
print(n)

n = n.reshape(3, 5) # reshape array to be 3x5
print("n after reshaped")
print(n)

o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
print("linspace:")
print(o)

ones = np.ones((3, 2))
print("ones:")
print(ones)

zeros = np.zeros((2, 3))
print("zeros:")
print(zeros)

eye = np.eye(3)
print("eye:")
print(eye)

print("diagonal:")
print(np.diag([4,5,6]))
