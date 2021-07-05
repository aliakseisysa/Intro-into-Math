#Дополните код Монте-Карло последовательности независимых испытаний расчетом
# соответствующих вероятностей (через биномиальное распределение)
# и сравните результаты.

import numpy as np
import math

k, n = 0, 100000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
v=math.factorial(10)*(0.5**5)*(0.5**(10-5))/(math.factorial(5)*math.factorial(10-5))
#print(a, b, c, d)
#print(x)
print(k, n, k/n,v)

