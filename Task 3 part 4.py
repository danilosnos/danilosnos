from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')

eq1 = Eq(x/y + y/z + z/x, 3)
eq2 = Eq(y/x + z/y + x/z, 3)
eq3 = Eq(x + y + z, 3)

solution = solve((eq1, eq2, eq3), (x, y, z))
print(solution)