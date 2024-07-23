from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')

eq1 = Eq(x + y + z, 2)
eq2 = Eq(x**2 + y**2 + z**2, 6)
eq3 = Eq(x**3 + y**3 + z**3, 8)

solution = solve((eq1, eq2, eq3), (x, y, z))
print(solution)