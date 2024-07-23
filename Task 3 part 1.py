import numpy as np
from scipy.optimize import fsolve

def equations(p):
    x, y = p
    eq1 = np.sqrt(x - 4*y) - 2*np.sqrt(x + 3*y) - 1
    eq2 = 7*np.sqrt(x + 3*y) - 5*x + 22*y - 13
    return (eq1, eq2)

# Начальное приближение решения (можно выбрать произвольно)
initial_guess = [1, 1]

# Решение системы уравнений
solution = fsolve(equations, initial_guess)

print(f"Решение: x = {solution[0]}, y = {solution[1]}")
