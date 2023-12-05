import sympy as sp

# Define variables and constants
V1, V2, P_ext, T = sp.symbols('V1 V2 P_ext T', real=True, positive=True)
R = sp.symbols('R', real=True, positive=True)  # Gas constant
n = sp.symbols('n', real=True, positive=True)  # Number of moles

# Calculate the work done during the ideal gas expansion
work_done = n * R * T * sp.ln(V2 / V1)

# Display the work done during the expansion
print("Work Done during Ideal Gas Expansion:")
sp.pretty_print(work_done)
