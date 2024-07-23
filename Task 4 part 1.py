from sympy import symbols, Function, Eq, dsolve, Derivative
from sympy.abc import x

Y = Function('Y')(x)

eq = Eq(Derivative(Y, x) + x*(Y**2) - 5*x*Y, 0)

solution = dsolve(eq, Y, ics={Y.subs(x, 0): 1})

print(solution)