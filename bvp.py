import numpy as np
import matplotlib.pyplot as plt

# Constants and Parameters
alpha = 0.01
L = 10
T = 2
Nx = 100  # Number of spatial points
Nt = 500  # Number of time points
dx = L / (Nx - 1)
dt = T / (Nt - 1)

# Function for T_0(t)
def T_0(t):
    return 100 * np.sin(np.pi * t / T)

# Initial condition f(x)
def f(x):
    return 20  # Constant initial temperature

# Create grid
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)
u = np.zeros((Nx, Nt))

# Set initial condition
u[:, 0] = f(x)

# Finite difference method
for n in range(0, Nt - 1):
    for i in range(1, Nx - 1):
        u[i, n + 1] = u[i, n] + alpha * dt / dx**2 * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])
    
    # Boundary conditions
    u[0, n + 1] = T_0(t[n + 1])
    u[-1, n + 1] = 50  # T_L

# Plotting the results
plt.imshow(u, extent=[0, T, 0, L], origin='lower', aspect='auto')
plt.colorbar(label='Temperature')
plt.xlabel('Time')
plt.ylabel('Position along rod')
plt.title('Heat Equation with Non-Uniform Boundary Conditions')
plt.show()
