#Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).

import numpy as np

num = int(np.random.uniform(0, 37))
print(num)
if num == 0:
    print("zero")
elif num in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
    print("red")
else:
    print("black")