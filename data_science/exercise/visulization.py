import matplotlib.pyplot as plt
import numpy as np

data = np.load('dataset.npy')
plt.plot(data[:,0],data[:,1], 'r+')
plt.show()