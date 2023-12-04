initial_velocity = 0  # m/s
final_velocity = 30  # m/s
time = 8  # seconds

# Calculate acceleration using the kinematic equation: a = (v - u) / t
acceleration = (final_velocity - initial_velocity) / time

# Calculate distance traveled using the kinematic equation: s = ut + 0.5 * at^2
distance = initial_velocity * time + 0.5 * acceleration * time**2

print(f"Acceleration of the car: {acceleration} m/s^2")
print(f"Distance traveled by the car: {distance} meters")
