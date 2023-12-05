import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
M = 5.972e24  # Mass of the Earth in kg
R = 6.371e6  # Radius of the Earth in meters

# Function defining the satellite's motion equations
def satellite_motion(state, t):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    return [vx, vy, ax, ay]

# Initial conditions
initial_state = [R, 0, 0, 7.66e3]  # Initial position and velocity

# Time points for integration
t = np.linspace(0, 3600, 1000)  # Time from 0 to 3600 seconds (1 hour)

# Numerically integrate the satellite's motion equations
result = odeint(satellite_motion, initial_state, t)

# Extract the x and y positions
x_positions, y_positions, _, _ = result.T

# Plot the satellite's trajectory
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions)
plt.title("Satellite's Trajectory")
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.grid()
plt.show()
