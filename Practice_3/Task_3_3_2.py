#Напишите код на Python, реализующий построение графиков:
# эллипса.

import numpy as np
import matplotlib.pyplot as plt
a, b = 10, 1
x=np.arange(-10, 11, 0.01)
plt.plot(x, np.sqrt(b**2*((a**2 - x**2)/a**2)))
plt.plot(x, -np.sqrt(b**2*((a**2 - x**2)/a**2)))
plt.show()