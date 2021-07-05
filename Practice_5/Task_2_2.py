#Сгенерируйте десять выборок случайных чисел х0, …, х9.
#и постройте гистограмму распределения случайной суммы  +х1+ …+ х9.

import random
import matplotlib.pyplot as plt

nums = [random.randint(1, 10) for _ in range(10)]
print(nums)
plt.hist(nums)
plt.show()