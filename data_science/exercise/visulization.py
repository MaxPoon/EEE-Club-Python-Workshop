import matplotlib.pyplot as plt
import numpy as np

data = np.load('dataset.npy')

plt.hist(data[:,0], np.linspace(0,30,100))
plt.show()

plt.hist(data[:,1], np.linspace(0,30,100))
plt.show()

plt.plot(data[:,0],data[:,1], 'r+')
plt.show()