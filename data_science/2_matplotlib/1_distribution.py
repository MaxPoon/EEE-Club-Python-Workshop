import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,1,4,5,6,7,1,2,3,4,9,8,3,3,3,6,6,2,10,9])
plt.hist(x, np.linspace(0,10,11))
plt.show()