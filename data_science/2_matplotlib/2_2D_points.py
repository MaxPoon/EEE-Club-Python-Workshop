import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,21)
y = x**3
plt.plot(x,y,'r.')
plt.show()

z = x**2
plt.plot(x,z,'r-')
plt.show()

plt.plot(x,z,'r--')
plt.show()

plt.plot(x,z,'r+')
plt.show()

plt.plot(x,z,'bs')
plt.show()

plt.plot(x,z,'g:')
plt.show()

plt.plot(x,z,'go')
plt.show()

plt.plot(x,y,'ro', x,z,'bx')
plt.show()