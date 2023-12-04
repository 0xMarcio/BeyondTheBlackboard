import numpy as np
import plotly.graph_objects as go

# Constants
a = 0.2
b = 0.2
c = 5.7

# Initial conditions
x0, y0, z0 = 0.0, 0.0, 0.0  # Initial values of x, y, and z
t0, t_max, dt = 0, 100, 0.01  # Time parameters

# Function to compute the derivatives of x, y, and z for the Rössler attractor
def rossler_derivs(x, y, z):
    dx_dt = -y - z
    dy_dt = x + a * y
    dz_dt = b + z * (x - c)
    return dx_dt, dy_dt, dz_dt

# Simulation parameters
num_steps = int((t_max - t0) / dt)
t_points = np.linspace(t0, t_max, num_steps)
x_points, y_points, z_points = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)
x, y, z = x0, y0, z0

# Perform numerical integration
for i in range(num_steps):
    x_points[i], y_points[i], z_points[i] = x, y, z
    dx, dy, dz = rossler_derivs(x, y, z)
    x += dx * dt
    y += dy * dt
    z += dz * dt

# Create an animation of the Rössler attractor's motion
fig = go.Figure()

# Add a 3D scatter plot for the attractor's trajectories
fig.add_trace(go.Scatter3d(x=x_points, y=y_points, z=z_points, mode='lines',
                           line=dict(color='blue', width=2), name='Trajectories'))

# Customize the layout
fig.update_layout(scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
                  title="Rössler Attractor")

# Show the 3D scatter plot
fig.show()
