import numpy as np
t=int(input("Введите число:"))
c=(1-(t**2)/(1+t**2))
a=2*t/(1+t**2)
b=-2*t/(1+t**2)
A = np.array([[c, a], [b, c]])
det_A = np.linalg.det(A)
print("Определитель матрицы:",det_A)
