import sympy as sp
import matplotlib.pyplot as plt

# Defining symbols for symbolic calculation
x, R1, R2 = sp.symbols('x R1 R2')

# Beam parameters
length_of_beam = 10  # meters

# Load definitions
# Assuming a point load of 20 kN at 4 meters from the left support
# and a uniformly distributed load of 5 kN/m over the entire length of the beam
point_load_position = 4  # meters from the left support
point_load_magnitude = 20  # kN
udl_magnitude = 5  # kN/m

# Calculating Reactions at Supports using Equilibrium Equations
# ∑M = 0, taking moment about point 1 (left support)
# ∑Fy = 0, sum of vertical forces
moment_eq = sp.Eq(R2 * length_of_beam - point_load_magnitude * point_load_position - udl_magnitude * length_of_beam * length_of_beam / 2, 0)
vertical_eq = sp.Eq(R1 + R2 - point_load_magnitude - udl_magnitude * length_of_beam, 0)

# Solving the equations
reactions = sp.solve((moment_eq, vertical_eq), (R1, R2))
R1_value, R2_value = reactions[R1], reactions[R2]

# Function to calculate shear force at a given point x
def shear_force(x_val):
    if x_val < point_load_position:
        return R1_value - udl_magnitude * x_val
    else:
        return R1_value - udl_magnitude * x_val - point_load_magnitude

# Function to calculate bending moment at a given point x
def bending_moment(x_val):
    if x_val < point_load_position:
        return R1_value * x_val - (udl_magnitude * x_val**2) / 2
    else:
        return R1_value * x_val - (udl_magnitude * x_val**2) / 2 - point_load_magnitude * (x_val - point_load_position)

# Generating values for plotting
x_values = [i for i in range(0, length_of_beam + 1)]
shear_values = [shear_force(x) for x in x_values]
moment_values = [bending_moment(x) for x in x_values]

# Plotting SFD and BMD
plt.figure(figsize=(15, 6))

# Shear Force Diagram
plt.subplot(1, 2, 1)
plt.plot(x_values, shear_values, color='blue', marker='o')
plt.title('Shear Force Diagram (SFD)')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.grid(True)

# Bending Moment Diagram
plt.subplot(1, 2, 2)
plt.plot(x_values, moment_values, color='red', marker='o')
plt.title('Bending Moment Diagram (BMD)')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (kNm)')
plt.grid(True)

plt.tight_layout()
plt.show()

R1_value, R2_value, reactions

