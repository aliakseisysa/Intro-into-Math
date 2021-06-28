#1. Задание
# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами.
import numpy as np

def length_vec():

    var_1 = int(input("Enter the X coord: "))
    var_2 = int(input("Enter the Y coord: "))
    var_3 = int(input("Enter the Z coord: "))

    vec_len = np.sqrt(var_1**2 + var_2**2 + var_3**2)

    return vec_len

print(length_vec())