import math

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
c = 299792458  # Speed of light (m/s)

# Input mass of the object (in kilograms)
mass = float(input("Enter the mass of the object (kg): "))

# Calculate Schwarzschild radius
schwarzschild_radius = 2 * G * mass / (c**2)

# Calculate escape velocity at Schwarzschild radius
escape_velocity = math.sqrt(2 * G * mass / schwarzschild_radius)

print(f"Schwarzschild radius: {schwarzschild_radius} meters")
print(f"Escape velocity at Schwarzschild radius: {escape_velocity} m/s")
