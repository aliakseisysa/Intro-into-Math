#Вычислите LU-разложение матрицы

import numpy as np
import scipy.linalg

A = np.array([ [1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(A)

print(P)
print("")
print(L)
print("")
print(U)
print("")
PL = np.dot(P, L)
PLU = np.dot(PL, U)
print(PLU)