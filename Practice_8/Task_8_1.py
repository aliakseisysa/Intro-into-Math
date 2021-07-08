#1. Решите линейную систему

import numpy as np

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([2, 5, 1])

print(A)
print(B)
print(np.linalg.solve(A, B))