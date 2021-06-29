#Напишите код, который будет рисовать график окружности в полярных координатах

import numpy as np
import matplotlib.pyplot as plt

phi=np.arange(0 * np.pi, 2 * np.pi, np.pi/180)
Radius = 45
ro = 2 * Radius * np.sin(phi)

plt.polar(phi, ro)
plt.show()
