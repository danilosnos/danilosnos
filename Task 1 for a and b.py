import numpy as np
a=int(input("Введите число:"))
b=int(input("Введите число:"))
A = np.array([[a**2, a*b], [a*b, b**2]])
det_A = np.linalg.det(A)
print("Определитель матрицы:",det_A)
