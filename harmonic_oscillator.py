import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters for the damped harmonic oscillator
m = 1.0  # Mass (kg)
k = 50.0  # Spring constant (N/m)
c = 0.5  # Damping coefficient (kg/s)

# Damped harmonic oscillator differential equations
def damped_oscillator(y, t, m, k, c):
    x, v = y
    dxdt = v
    dvdt = -(k/m) * x - (c/m) * v
    return dxdt, dvdt

# Initial conditions: x0 (initial displacement), v0 (initial velocity)
x0 = 2.0
v0 = 0.0
initial_conditions = [x0, v0]

# Time points (in seconds)
t = np.linspace(0, 10, 1000)

# Solve the differential equations
solution = odeint(damped_oscillator, initial_conditions, t, args=(m, k, c))
x, v = solution.T

# Plotting displacement and velocity over time
plt.figure(figsize=(12, 6))

# Displacement plot
plt.subplot(2, 1, 1)
plt.plot(t, x, 'b', label='Displacement')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Damped Harmonic Oscillator')
plt.legend()
plt.grid(True)

# Velocity plot
plt.subplot(2, 1, 2)
plt.plot(t, v, 'r', label='Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
