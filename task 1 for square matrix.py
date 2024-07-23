import numpy as np

matrix = np.array([[5, 2, 0], [7, 3, 0], [0, 0, 1]])
# Вычисляем определитель матрицы
determinant = np.linalg.det(matrix)

# Выводим результат
print(f"Определитель матрицы: {determinant}")