from sympy import symbols, Function, Eq, dsolve, Derivative, cos
from sympy.abc import x

# Define the function Y(x)
Y = Function('Y')(x)

# Define the given differential equation
eq = Eq(Derivative(Y, x) + 3*cos(x**2) - Y, 0)

# Solve the differential equation
solution = dsolve(eq, Y, ics={Y.subs(x, 0): 0})

print(solution)
