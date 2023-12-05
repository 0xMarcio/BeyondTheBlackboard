import sympy as sp

# Define variables and constants
x, t, c, L, n = sp.symbols('x t c L n', real=True, positive=True)
u = sp.Function('u')(x, t)

# Define the wave equation
wave_eq = sp.Eq(u.diff(t, t), c**2 * u.diff(x, x))

# Assume separation of variables u(x, t) = X(x)T(t)
X = sp.Function('X')(x)
T = sp.Function('T')(t)

# Substitute the separation of variables into the wave equation
wave_eq_separated = wave_eq.subs(u, X * T)

# Solve the separated ODEs for X(x) and T(t)
X_eq = sp.Eq(X.diff(x, x) + (n * sp.pi / L)**2 * X, 0)  # Spatial part
T_eq = sp.Eq(T.diff(t, t) + (c**2 * (n * sp.pi / L)**2) * T, 0)  # Temporal part

# Solve the ODEs for X and T
X_solution = sp.dsolve(X_eq, X).rhs
T_solution = sp.dsolve(T_eq, T).rhs

# Combine the solutions to get the general solution
u_solution = X_solution * T_solution

# Display the general solution
print("General Solution to the 1D Wave Equation:")
sp.pretty_print(u_solution)
