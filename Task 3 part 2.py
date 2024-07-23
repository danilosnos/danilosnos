from scipy.optimize import fsolve
import numpy as np

def equations(vars):
    x, y = vars
    eq1 = x**4 - y**4 - 15
    eq2 = x**3 * y - x * y**3 - 6
    return [eq1, eq2]

# Задаем начальное приближение
initial_guess = [1, 1]

# Решаем систему уравнений
result = fsolve(equations, initial_guess)

print("Решение системы уравнений:")
print("x =", result[0])
print("y =", result[1])