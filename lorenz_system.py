import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Initial conditions
x0, y0, z0 = 0.1, 0.0, 0.0  # Initial values of x, y, and z
t0, t_max, dt = 0, 50, 0.01  # Time parameters

# Function to compute the derivatives of x, y, and z
def lorenz_derivs(x, y, z):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Simulation parameters
num_steps = int((t_max - t0) / dt)
t_points = np.linspace(t0, t_max, num_steps)
x_points, y_points, z_points = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
x, y, z = x0, y0, z0

# Perform numerical integration (Euler's method)
for i in range(num_steps):
    x_points[i], y_points[i], z_points[i] = x, y, z
    dx, dy, dz = lorenz_derivs(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

# Visualization of the Lorenz attractor
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_points, y_points, z_points, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor")
plt.show()
