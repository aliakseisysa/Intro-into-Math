#Напишите код, который будет переводить полярные координаты в декартовы

import numpy as np

def polar_func(ro, phi):
    x = ro * np.cos(phi)
    y = ro * np.sin(phi)
    return [x, y]

print(polar_func(3, np.pi/3))