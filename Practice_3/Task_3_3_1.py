#Напишите код на Python, реализующий построение графиков:
# окружности.

import numpy as np
import matplotlib.pyplot as plt
x0, y0 = 5, 10
Radius = 10
x=np.arange(x0-Radius,x0+Radius+0.01,0.01)
plt.plot(x, np.sqrt(Radius**2 - (x-x0)**2)+y0)
plt.plot(x, -np.sqrt(Radius**2 - (x-x0)**2)+y0)
plt.show()

