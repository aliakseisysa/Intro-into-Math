#3. Сколько решений имеет линейная система

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 5, 1]])
C = np.concatenate((A,B.T), axis=1)

print (C)

print(np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001))

# make change

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 5, 8]])
C = np.concatenate((A,B.T), axis=1)

print (C)

print(np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001))

# as rank is not equal to variables number the system has more then one solution