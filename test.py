import sympy as sp

# Define variables and constants
x, t, c, L = sp.symbols('x t c L', real=True, positive=True)
u = sp.Function('u')(x, t)

# Define the wave equation
wave_eq = sp.Eq(sp.diff(u, t, t), c**2 * sp.diff(u, x, x))

# Define initial conditions and boundary conditions
initial_conditions = [sp.Eq(u.subs(t, 0), 0), sp.Eq(u.diff(t).subs(t, 0), 0)]
boundary_conditions = [sp.Eq(u.subs(x, 0), 0), sp.Eq(u.subs(x, L), 0)]

# Solve the wave equation with conditions
solution = sp.pde.solvers.pdsolve(wave_eq, u, ics={initial_conditions[0], initial_conditions[1],
                                                    boundary_conditions[0], boundary_conditions[1]})

# Display the solution
print("Solution to the Wave Equation:")
sp.pretty_print(solution)
