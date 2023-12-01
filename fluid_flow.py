import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the simulation
plate_length = 100  # Length of the flat plate
fluid_velocity = 2  # Velocity of the fluid (m/s)
kinematic_viscosity = 1e-6  # Kinematic viscosity of the fluid (m^2/s)

# Discretization
x = np.linspace(0, plate_length, 100)  # Points along the plate
y = np.linspace(0, 1, 100)  # Points in the boundary layer
X, Y = np.meshgrid(x, y)

# Boundary layer thickness function (simplified model)
def boundary_layer_thickness(x):
    return np.sqrt((kinematic_viscosity * x) / fluid_velocity)

# Velocity profile function (simplified model)
def velocity_profile(y, delta):
    return fluid_velocity * (1 - np.exp(-y / delta))

# Animation function
def animate(i):
    plt.clf()
    delta = boundary_layer_thickness(x[i])
    U = velocity_profile(Y[:, i], delta)
    plt.plot(U, y, label=f"x = {x[i]:.2f} m")
    plt.ylim(0, 1)
    plt.xlim(0, fluid_velocity)
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Distance from plate (m)")
    plt.title("Boundary Layer Development over a Flat Plate")
    plt.legend()

# Creating the animation
ani = FuncAnimation(plt.gcf(), animate, frames=len(x), interval=100, repeat=False)

plt.show()
