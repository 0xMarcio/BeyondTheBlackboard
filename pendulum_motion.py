import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants and initial conditions
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 2  # Length of the pendulum (meters)
theta0 = np.pi / 4  # Initial angle (45 degrees)
omega0 = 0  # Initial angular velocity

# Time span
t_max = 10  # Total time of simulation (seconds)
time = np.linspace(0, t_max, 300)  # Time points for the simulation

# Differential equation for the pendulum's motion
def pendulum_equation(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Solving the differential equation
solution = solve_ivp(pendulum_equation, [0, t_max], [theta0, omega0], t_eval=time)

# Extracting the solution
theta = solution.y[0]

# Converting polar coordinates to Cartesian coordinates for animation
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Animation function
def animate(i):
    plt.clf()
    plt.plot([0, x[i]], [0, y[i]], color='b')  # Pendulum rod
    plt.scatter([x[i]], [y[i]], color='r')  # Pendulum bob
    plt.xlim(-L, L)
    plt.ylim(-L, L)
    plt.title("Simple Pendulum Motion")
    plt.gca().set_aspect('equal', adjustable='box')

# Creating the animation
ani = FuncAnimation(plt.gcf(), animate, frames=len(time), interval=100, repeat=False)

plt.show()
