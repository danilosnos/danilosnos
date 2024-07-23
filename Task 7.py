import sympy as sp

x = sp.symbols('x')

# Разложение sin(x) в ряд Тейлора
sin_expansion = sp.series(sp.sin(x), x, 0, 9)
print("sin(x) =", sin_expansion)

# Разложение cos(x) в ряд Тейлора
cos_expansion = sp.series(sp.cos(x), x, 0, 9)
print("cos(x) =", cos_expansion)

# Разложение exp(x) в ряд Тейлора
exp_expansion = sp.series(sp.exp(x), x, 0, 9)
print("exp(x) =", exp_expansion)