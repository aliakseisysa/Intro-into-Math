#Напишите код на Python, реализующий построение графиков:
# гиперболы.

import numpy as np
import matplotlib.pyplot as plt
a, b = 1, 10
x=np.arange(-10, 10, 0.01)
plt.plot(x, np.sqrt((x**2/a**2 - 1)*b**2))
plt.plot(x, -np.sqrt((x**2/a**2 - 1)*b**2))
plt.show()