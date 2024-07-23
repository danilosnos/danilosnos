import numpy as np
from scipy.linalg import expm, sinm, cosm

# Определение матрицы A
A = np.array([[5, 7, 4],
              [1, 2, 1],
              [3, 1, 4]])

# Вычисление sin(A), cos(A), exp(A) и A^(-1)
sinA = sinm(A)
cosA = cosm(A)
expA = expm(A)


# Вывод результатов
print("sin(A):\n", sinA)
print("\ncos(A):\n", cosA)
print("\nexp(A):\n", expA)