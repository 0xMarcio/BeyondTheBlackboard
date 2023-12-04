import numpy as np
import plotly.graph_objects as go
from scipy.integrate import simps

# Constants
L = 1  # Length of the potential well
N = 500  # Number of points in the space grid
x = np.linspace(0, L, N)  # Spatial grid
dx = x[1] - x[0]  # Space step

# Time variables
dt = 0.001  # Time step (increased for faster simulation)
total_time = 2  # Total time of simulation
time_steps = int(total_time / dt)

# Define the initial wavefunction (e.g., a Gaussian centered at L/2)
def initial_wavefunction(x):
    return np.exp(-(x - L/2)**2 / 0.1**2)

# Normalize the wavefunction
psi = initial_wavefunction(x)
psi = psi / np.sqrt(simps(np.abs(psi)**2, x))

# Evolution of the wavefunction in an infinite potential well
def evolve_wavefunction(psi, dx, dt):
    # Discrete second derivative (Laplacian)
    d2psi = np.roll(psi, -1) - 2*psi + np.roll(psi, 1)
    d2psi[0] = d2psi[-1] = 0  # Zero at boundaries

    # Schrödinger equation
    psi_new = psi - 1j * dt / dx**2 * d2psi
    return psi_new / np.sqrt(simps(np.abs(psi_new)**2, x))  # Normalize

# Simulation over time
psi_time = []
for t in range(time_steps):
    psi = evolve_wavefunction(psi, dx, dt)
    if t % 10 == 0:  # Store every 10th step to reduce data size
        psi_time.append(psi)

# Convert list to array for easier handling in Plotly
psi_time = np.array(psi_time)

# Visualization of the probability density
frames = [go.Frame(data=[go.Scatter(x=x, y=np.abs(psi)**2)],
                   name=str(10 * dt * i)) for i, psi in enumerate(psi_time)]

fig = go.Figure(frames=frames)

# Add play and pause buttons
fig.update_layout(updatemenus=[dict(type="buttons",
                                    buttons=[dict(label="Play",
                                                  method="animate",
                                                  args=[None, dict(frame=dict(duration=100, redraw=True))]),
                                             dict(label="Pause",
                                                  method="animate",
                                                  args=[[None], dict(frame=dict(duration=0, redraw=True))])])])

# Initial plot
fig.add_trace(go.Scatter(x=x, y=np.abs(psi_time[0])**2, mode='lines'))
fig.update_layout(title='Probability Density of a Particle in an Infinite Potential Well',
                  xaxis_title='Position',
                  yaxis_title='Probability Density',
                  showlegend=False)
fig.show()

