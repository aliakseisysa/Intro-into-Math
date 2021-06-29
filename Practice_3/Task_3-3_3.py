#Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах

import numpy as np
import matplotlib.pyplot as plt


phi = np.arange(4, 6, 1)
ro = np.arange(4, 6, 1)

plt.polar(phi, ro)
plt.show()