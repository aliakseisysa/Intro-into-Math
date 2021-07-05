#Напишите код, проверяющий любую из теорем сложения или умножения вероятности
# на примере рулетки или подбрасывания монетки.

import random

orel = 0
reshka = 0

for i in range(1, 1001):
    coin = random.randint(1, 2)

    if coin == 1:
        orel += 1

    elif coin == 2:
        reshka += 1

print("Орел выпал", orel/1000)
print("Решка выпал", reshka/1000)


sum = orel/1000 + reshka/1000
print(sum)
