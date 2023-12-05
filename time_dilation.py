import math

# Constants
c = 299792458  # Speed of light (m/s)

# Input the velocity of the object (relative to the observer) and proper time (t0)
v = float(input("Enter the velocity of the object (m/s): "))
t0 = float(input("Enter the proper time experienced by the object (s): "))

# Calculate time dilation
dilated_time = t0 / math.sqrt(1 - (v**2 / c**2))

print(f"Dilated time experienced by the observer: {dilated_time} seconds")
