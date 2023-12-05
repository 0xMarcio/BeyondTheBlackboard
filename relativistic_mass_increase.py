import math

# Constants
rest_mass = 2  # Rest mass in kg
speed = 0.9 * 3e8  # Speed in m/s (90% of the speed of light)
c = 3e8  # Speed of light in m/s

# Calculate the relativistic mass using the relativistic mass formula
relativistic_mass = rest_mass / math.sqrt(1 - (speed / c)**2)

print(f"Relativistic mass of the particle: {relativistic_mass:.2f} kg")
