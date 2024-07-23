import numpy as np

A = np.array([[8, 9, 2], [8, 2, 5], [1, 9, 6]])
B = np.array([[9, 5, 2], [4, 7, 6], [4, 7, 2]])
C = np.array([[5, 3, 7], [8, 9, 9], [3, 1, 7]])
# Решаем уравнение AX + B = C для X
X = np.linalg.solve(A, C - B)

print("Матрица X:")
print(X)