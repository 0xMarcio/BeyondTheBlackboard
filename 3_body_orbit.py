import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Gravitational constant
G = 6.67430e-11

# Function to update positions and velocities based on gravitational forces
def update_positions(dt, pos, vel, masses):
    n = len(pos)
    force = np.zeros((n, 2))

    for i in range(n):
        for j in range(n):
            if i != j:
                # Calculate gravitational force
                r_vec = pos[j] - pos[i]
                r_mag = np.linalg.norm(r_vec)
                r_hat = r_vec / r_mag
                force[i] += G * masses[i] * masses[j] * r_hat / r_mag**2

    # Update velocities and positions
    vel += dt * force / masses[:, None]
    pos += dt * vel
    return pos, vel

# Initialize the bodies (mass, position, and velocity)
masses = np.array([5.972e24, 8.348e22, 1.989e30])  # Earth, Moon, Sun
pos = np.array([[-1e11, 0], [-1.02e11, 0], [1e10, 0]])  # Initial positions
vel = np.array([[0, -29.78], [0, -29.78 - 1.022], [0, 0]])  # Initial velocities, in km/s

# Convert velocities to m/s
vel *= 1000

# Time step
dt = 60 * 60 * 24  # One day

# Create the plot
fig, ax = plt.subplots()
lines = [ax.plot([], [], 'o', markersize=mass**(1/3) / 1e8)[0] for mass in masses]

# Set plot limits and labels
ax.set_xlim(-1.5e11, 1.5e11)
ax.set_ylim(-1.5e11, 1.5e11)
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")
ax.set_title("3-Body Orbit Simulation")

# Initialize animation
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Update function for animation
def animate(i):
    global pos, vel
    pos, vel = update_positions(dt, pos, vel, masses)
    for line, p in zip(lines, pos):
        line.set_data(p[0], p[1])
    return lines

# Create the animation
ani = FuncAnimation(fig, animate, frames=500, interval=20, init_func=init, blit=True)

plt.show()
