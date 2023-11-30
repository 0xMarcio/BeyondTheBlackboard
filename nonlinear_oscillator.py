import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation
def equation(y, t):
    y0, y1 = y
    dydt = [y1, -y0 - y0**3]
    return dydt

# Initial conditions
y0 = [0.0, 1.0]

# Time points
t = np.linspace(0, 10, 200)

# Solving the differential equation
sol = odeint(equation, y0, t)

# Plotting the solution
plt.plot(t, sol[:, 0])
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Nonlinear Oscillator')
plt.show()
