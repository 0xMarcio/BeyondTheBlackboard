import sympy as sp
from sympy import sqrt, factorial, assoc_legendre, exp, I

# Define variables and constants
r, theta, phi = sp.symbols('r theta phi', real=True, positive=True)
n, l, m = sp.symbols('n l m', integer=True, positive=True)
R = sp.Function('R')(r)
Y = sp.Function('Y')(theta, phi)

# Define the Schrödinger equation for the hydrogen atom
k, hbar, m = sp.symbols('k hbar m', real=True, positive=True)
V = -k / r
E = sp.Symbol('E', real=True)  # Energy eigenvalue
schrodinger_eq = -hbar**2 / (2 * m) * (1 / r**2 * R.diff(r, r) - 2 / r * R.diff(r) + (l * (l + 1) / r**2) * R) + V * R - E * R

# Solve the Schrödinger equation for R(r)
R_solution = sp.dsolve(schrodinger_eq, R)

# Define the angular part of the wave function Y(theta, phi)
Y_solution = sqrt(((2 * l + 1) / (4 * sp.pi)) * factorial(l - m) / factorial(l + m)) * assoc_legendre(l, m, sp.cos(theta)) * exp(I * m * phi)

# Display the solutions for R and Y
print("Solution for R(r):")
sp.pretty_print(R_solution)
print("\nAngular Part of the Wave Function Y(theta, phi):")
sp.pretty_print(Y_solution)
