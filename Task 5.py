import sympy as sp
import numpy as np

# Символьные переменные для углов поворота
theta_x, theta_y, theta_z = sp.symbols('theta_x theta_y theta_z')

# Символьные переменные для вектора смещения
dx, dy, dz = sp.symbols('dx dy dz')

# Матрица сдвига
T_translation = sp.Matrix([[1, 0, 0, dx],
                           [0, 1, 0, dy],
                           [0, 0, 1, dz],
                           [0, 0, 0, 1]])

# Матрица поворота вокруг оси X
T_rot_x = sp.Matrix([[1, 0, 0, 0],
                     [0, sp.cos(theta_x), -sp.sin(theta_x), 0],
                     [0, sp.sin(theta_x), sp.cos(theta_x), 0],
                     [0, 0, 0, 1]])

# Матрица поворота вокруг оси Y
T_rot_y = sp.Matrix([[sp.cos(theta_y), 0, sp.sin(theta_y), 0],
                     [0, 1, 0, 0],
                     [-sp.sin(theta_y), 0, sp.cos(theta_y), 0],
                     [0, 0, 0, 1]])

# Матрица поворота вокруг оси Z
T_rot_z = sp.Matrix([[sp.cos(theta_z), -sp.sin(theta_z), 0, 0],
                     [sp.sin(theta_z), sp.cos(theta_z), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

# Задаем значения для углов поворота и вектора смещения
theta_x_val = sp.pi / 6  # 30 градусов
theta_y_val = -sp.pi / 4  # -45 градусов
dx_val = 10
dy_val = 10
dz_val = 1

# Подставляем значения в матрицы трансформаций
T_translation_num = T_translation.subs({dx: dx_val, dy: dy_val, dz: dz_val})
T_rot_x_num = T_rot_x.subs({theta_x: theta_x_val})
T_rot_y_num = T_rot_y.subs({theta_y: theta_y_val})

# Выводим матрицы трансформаций в символьном виде
print("Матрица сдвига:")
sp.pprint(T_translation)
print("\nМатрица поворота вокруг оси X:")
sp.pprint(T_rot_x)
print("\nМатрица поворота вокруг оси Y:")
sp.pprint(T_rot_y)

# Выводим матрицы трансформаций в виде NumPy-матриц
print("\nМатрица сдвига (NumPy):")
print(np.array(T_translation_num).astype(np.float64))
print("\nМатрица поворота вокруг оси X (NumPy):")
print(np.array(T_rot_x_num).astype(np.float64))
print("\nМатрица поворота вокруг оси Y (NumPy):")
print(np.array(T_rot_y_num).astype(np.float64))

# Результирующая матрица трансформаций
T_total = T_translation_num * T_rot_x_num * T_rot_y_num

# Выводим результирующую матрицу трансформаций в символьном виде
print("\nРезультирующая матрица трансформаций:")
sp.pprint(T_total)

# Выводим результирующую матрицу трансформаций в виде NumPy-матрицы
print("\nРезультирующая матрица трансформаций (NumPy):")
print(np.array(T_total).astype(np.float64))