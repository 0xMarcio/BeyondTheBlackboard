import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

def two_body_orbit(t, y, G, m1, m2):
    # Unpack the input vector
    x1, y1, vx1, vy1, x2, y2, vx2, vy2 = y
    
    # Compute distance between bodies
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Newton's law of universal gravitation
    F = G * m1 * m2 / r**2
    theta = np.arctan2(y2 - y1, x2 - x1)
    Fx = F * np.cos(theta)
    Fy = F * np.sin(theta)

    # Equations of motion
    dvx1_dt = Fx / m1
    dvy1_dt = Fy / m1
    dvx2_dt = -Fx / m2
    dvy2_dt = -Fy / m2

    # Derivatives
    return [vx1, vy1, dvx1_dt, dvy1_dt, vx2, vy2, dvx2_dt, dvy2_dt]

# Constants
G = 6.67430e-11  # Gravitational constant
m1 = 1.989e30    # Mass of the star (e.g., Sun)
m2 = 5.972e24    # Mass of the planet (e.g., Earth)

# Initial conditions (Star at origin, Planet at 1 AU with orbital velocity)
initial_conditions = [0, 0, 0, 0, 1.496e11, 0, 0, 29780]

# Time span (one year)
t_span = (0, 365 * 24 * 3600)
t_eval = np.linspace(0, 365 * 24 * 3600, 1000)

# Solve the ODE
solution = solve_ivp(two_body_orbit, t_span, initial_conditions, args=(G, m1, m2), t_eval=t_eval)

# Plot the orbits
plt.figure(figsize=(8, 8))
plt.plot(solution.y[0], solution.y[1], label='Star')
plt.plot(solution.y[4], solution.y[5], label='Planet')
plt.legend()
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Orbital Mechanics Simulation')
plt.show()
