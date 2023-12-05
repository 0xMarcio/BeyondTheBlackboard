import sympy as sp

# Define variables and constants
x, t, c = sp.symbols('x t c', real=True, positive=True)
E = sp.Function('E')(x, t)
B = sp.Function('B')(x, t)

# Define Maxwell's equations for the electric and magnetic fields
maxwell_eq1 = sp.Eq(sp.diff(E, x), -sp.diff(B, t))
maxwell_eq2 = sp.Eq(sp.diff(B, x), c**2 * sp.diff(E, t))

# Solve the Maxwell's equations for E(x, t) and B(x, t)
E_solution = sp.pdsolve(maxwell_eq1, E)
B_solution = sp.pdsolve(maxwell_eq2, B)

# Display the solutions for E(x, t) and B(x, t)
print("Electric Field (E) Solution:")
sp.pretty_print(E_solution)
print("\nMagnetic Field (B) Solution:")
sp.pretty_print(B_solution)
