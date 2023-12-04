import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def create_cylinder(center, radius, grid_x, grid_y):
    """ Create a mask for a cylinder within the grid """
    X, Y = np.meshgrid(grid_x, grid_y)
    return (X - center[0])**2 + (Y - center[1])**2 < radius**2

def load_velocity_data(grid_x, grid_y):
    """ Generate more realistic synthetic velocity field data """
    U = np.zeros((len(grid_y), len(grid_x)))
    V = np.zeros((len(grid_y), len(grid_x)))

    # Velocity increases around the cylinder to mimic flow separation
    for i, y in enumerate(grid_y):
        for j, x in enumerate(grid_x):
            if (x - 0.5)**2 + (y - 0.5)**2 >= 0.1**2:
                U[i, j] = np.sin(np.pi * y) * (1 - np.exp(-(x - 0.5)**2 / 0.01))
                V[i, j] = np.cos(np.pi * x) * (1 - np.exp(-(y - 0.5)**2 / 0.01))

    return U, V

def load_pressure_data(grid_x, grid_y):
    """ Generate more realistic synthetic pressure data """
    X, Y = np.meshgrid(grid_x, grid_y)
    pressure = np.exp(-((X - 0.5)**2 + (Y - 0.5)**2) / 0.01)

    return pressure

# Grid definition
x_grid = np.linspace(0, 1, 100)
y_grid = np.linspace(0, 1, 100)

# Load the data
u, v = load_velocity_data(x_grid, y_grid)
pressure = load_pressure_data(x_grid, y_grid)

# Plot the velocity field (quiver plot) and pressure field (contour plot)
plt.figure(figsize=(10, 6))

# Quiver plot for velocity field
plt.quiver(x_grid, y_grid, u, v, color='blue')

# Contour plot for pressure field
pressure_levels = np.linspace(pressure.min(), pressure.max(), 40)
plt.contourf(x_grid, y_grid, pressure, levels=pressure_levels, cmap=cm.jet, alpha=0.7)
plt.colorbar(label='Pressure')

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('CFD Airflow Visualization over a Cylinder (Enhanced Synthetic Data)')
plt.axis('equal')
plt.show()
