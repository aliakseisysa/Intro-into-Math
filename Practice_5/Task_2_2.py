#Сгенерируйте десять выборок случайных чисел х0, …, х9.
#и постройте гистограмму распределения случайной суммы  +х1+ …+ х9.

import numpy as np
import matplotlib.pyplot as plt

x0 = np.random.randn(10)
x1 = np.random.randn(10)
x2 = np.random.randn(10)
x3 = np.random.randn(10)
x4 = np.random.randn(10)
x5 = np.random.randn(10)
x6 = np.random.randn(10)
x7 = np.random.randn(10)
x8 = np.random.randn(10)
x9 = np.random.randn(10)
nums = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8+ x9
print(nums)
plt.hist(nums)
plt.show()