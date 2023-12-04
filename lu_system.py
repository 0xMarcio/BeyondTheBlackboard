import numpy as np
import plotly.graph_objects as go

# Constants
a = 40.0
b = 3.0
F = 16.0

# Initial conditions
x0, y0, z0 = 0.1, 0.0, 0.0  # Initial values of x, y, and z
t0, t_max, dt = 0, 50, 0.01  # Time parameters

# Function to compute the derivatives of x, y, and z for the Lü System
def lu_system_derivs(x, y, z):
    dx_dt = -a * x + a * y
    dy_dt = -x * z + F * x - y
    dz_dt = x * y - b * z
    return dx_dt, dy_dt, dz_dt

# Simulation parameters
num_steps = int((t_max - t0) / dt)
t_points = np.linspace(t0, t_max, num_steps)
x_points, y_points, z_points = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
x, y, z = x0, y0, z0

# Perform numerical integration
for i in range(num_steps):
    x_points[i], y_points[i], z_points[i] = x, y, z
    dx, dy, dz = lu_system_derivs(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

# Create an animation of the Lü System's trajectories
fig = go.Figure()

# Add a 3D scatter plot for the trajectories
fig.add_trace(go.Scatter3d(x=x_points, y=y_points, z=z_points, mode='lines',
                           line=dict(color='blue', width=2), name='Trajectories'))

# Customize the layout
fig.update_layout(scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
                  title="Lü System")

# Show the 3D scatter plot
fig.show()
