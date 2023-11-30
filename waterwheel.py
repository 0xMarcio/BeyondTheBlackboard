import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters for the waterwheel
alpha = 1
beta = 1
gamma = 1
delta = 0.5
omega = 1

# Differential equations for the waterwheel
def waterwheel_eq(y, t, alpha, beta, gamma, delta, omega):
    theta, z, w = y
    dydt = [z, gamma * w - delta * z - alpha * np.sin(theta), -beta * z - omega]
    return dydt

# Initial conditions
y0 = [1, 0, 0]

# Time points
t = np.linspace(0, 50, 1000)

# Solve ODE
solution = odeint(waterwheel_eq, y0, t, args=(alpha, beta, gamma, delta, omega))
theta, z, w = solution.T

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
ax1.plot(t, theta, label='theta')
ax1.plot(t, z, label='z')
ax1.set_ylabel('Angles and Angular Velocity')
ax1.set_title('Chaotic Waterwheel Simulation')
ax1.legend()

ax2.plot(theta, z)
ax2.set_xlabel('theta')
ax2.set_ylabel('z')
ax2.set_title('Phase Space Plot')

plt.tight_layout()
plt.show()
