import sympy as sp

# Define variables and constants
B0, omega, L, R, t = sp.symbols('B0 omega L R t', real=True, positive=True)
phi = B0 * L**2 * sp.cos(omega * t)  # Magnetic flux through the loop

# Calculate the induced electromotive force (emf) using Faraday's law
emf = -sp.diff(phi, t)

# Calculate the current in the loop using Ohm's law (emf = IR)
current = emf / R

# Display the induced emf and current
print("Induced Electromotive Force (emf):")
sp.pretty_print(emf)
print("\nCurrent in the Loop:")
sp.pretty_print(current)
