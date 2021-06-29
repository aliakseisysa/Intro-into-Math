#Решите систему уравнений и неравенств

import numpy as np
from scipy.optimize import fsolve


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, np.exp(x) + x * (1 - y) - 1)


x1, y1 = fsolve(equations, (-10, 10))

print(x1, y1)