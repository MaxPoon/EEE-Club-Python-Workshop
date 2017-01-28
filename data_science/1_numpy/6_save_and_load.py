import numpy as np

x1 = np.arange(0,100,2)
print(x1)
np.save('x.npy',x1)

x2 = np.load('x.npy')
print(x2)