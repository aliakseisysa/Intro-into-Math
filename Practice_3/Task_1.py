#Нарисуйте график функции:
#для некоторых (2-3 различных) значений параметров k, a, b.


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = x
y2 = 5 * x + 5
y3 = -5 * x - 5
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.show()