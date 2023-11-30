import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the Van der Pol equation
def van_der_pol(y, t, mu):
    y0, y1 = y
    dydt = [y1, mu * (1 - y0**2) * y1 - y0]
    return dydt

# Parameter
mu = 5.0

# Initial conditions
y0 = [2.0, 0.0]

# Time points
t = np.linspace(0, 20, 500)

# Solving the differential equation
sol = odeint(van_der_pol, y0, t, args=(mu,))

# Plotting the solution
plt.plot(t, sol[:, 0])
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Van der Pol Oscillator')
plt.show()
