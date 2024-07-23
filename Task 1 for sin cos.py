import numpy as np
alpha=int(input("Введите размер угла в градусах:"))
beta=int(input("Введите размер угла в градусах:"))
# Определяем матрицу
matrix = np.array([
    [np.cos(alpha), np.sin(alpha)],
    [np.sin(beta), np.cos(beta)]
])

# Вычисляем определитель матрицы
determinant = np.linalg.det(matrix)

# Выводим результат
print(f"Определитель матрицы: {determinant}")