import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def double_pendulum_deriv(t, y, L1, L2, m1, m2, g=9.81):
    θ1, z1, θ2, z2 = y
    c, s = np.cos(θ1 - θ2), np.sin(θ1 - θ2)

    θ1_dot = z1
    θ2_dot = z2

    z1_dot = (m2*g*np.sin(θ2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
              (m1+m2)*g*np.sin(θ1)) / L1 / (m1 + m2*s**2)

    z2_dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(θ2) + g*np.sin(θ1)*c) +
              m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)

    return θ1_dot, z1_dot, θ2_dot, z2_dot

# Parameters
L1, L2 = 1.0, 1.0  # lengths of the pendulums
m1, m2 = 1.0, 1.0  # masses of the pendulums
y0 = [np.pi/2, 0, np.pi/2, 0]  # initial conditions

# Time span
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Solve the ODE
solution = solve_ivp(double_pendulum_deriv, t_span, y0, args=(L1, L2, m1, m2), t_eval=t_eval)

# Extracting the solution
θ1, θ2 = solution.y[0], solution.y[2]
x1 = L1 * np.sin(θ1)
y1 = -L1 * np.cos(θ1)
x2 = x1 + L2 * np.sin(θ2)
y2 = y1 - L2 * np.cos(θ2)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x1, y1, label='Mass 1')
plt.plot(x2, y2, label='Mass 2')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Double Pendulum Simulation')
plt.show()
