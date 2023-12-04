import math

v0 = float(input("Enter the initial velocity (m/s): "))
angle_degrees = float(input("Enter the launch angle (degrees): "))

# Convert angle from degrees to radians
angle_radians = math.radians(angle_degrees)

# Constants
g = 9.81  # Acceleration due to gravity

# Calculate maximum height
h_max = (v0**2 * math.sin(angle_radians)**2) / (2 * g)

# Calculate total flight time
T = (2 * v0 * math.sin(angle_radians)) / g

print(f"Maximum height reached: {h_max} meters")
print(f"Total flight time: {T} seconds")
