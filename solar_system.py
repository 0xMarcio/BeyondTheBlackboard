import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the orbital parameters of the planets
planets = {
    "Mercury": {"a": 0.39, "T": 0.24},
    "Venus": {"a": 0.72, "T": 0.62},
    "Earth": {"a": 1.00, "T": 1.00},
    "Mars": {"a": 1.52, "T": 1.88},
    "Jupiter": {"a": 5.20, "T": 11.86},
    "Saturn": {"a": 9.58, "T": 29.46},
    "Uranus": {"a": 19.22, "T": 84.01},
    "Neptune": {"a": 30.05, "T": 164.8}
}

def planet_position(a, T, time):
    """Calculate the position of a planet in its orbit."""
    angle = 2 * np.pi * (time % T) / T
    x = a * np.cos(angle)
    y = a * np.sin(angle)
    return x, y

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_aspect('equal', 'box')
ax.set_title("Orbits of Planets in Our Solar System")

# Plotting the Sun
ax.plot(0, 0, 'yo', markersize=10, label='Sun')

# Dictionary to store planet plot elements and their orbit paths
planet_plots = {}
orbit_paths = {}

# Plot initial positions of the planets and initialize their orbit paths
for planet, params in planets.items():
    x, y = planet_position(params['a'], params['T'], 0)
    planet_plots[planet], = ax.plot(x, y, 'o', label=planet)
    orbit_paths[planet], = ax.plot([], [], 'k-', lw=0.5)  # Thin line for orbit path

# Adding legend
ax.legend()

# Animation function
def update(frame):
    """Update the positions of the planets and their orbits for the animation."""
    for planet, params in planets.items():
        x, y = planet_position(params['a'], params['T'], frame)
        planet_plots[planet].set_data([x], [y])
        
        # Update orbit paths
        if len(orbit_paths[planet].get_xdata()) > 0:
            xdata, ydata = orbit_paths[planet].get_xdata(), orbit_paths[planet].get_ydata()
            orbit_paths[planet].set_data(np.append(xdata, x), np.append(ydata, y))
        else:
            orbit_paths[planet].set_data([x], [y])

    return list(planet_plots.values()) + list(orbit_paths.values())

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 100, 1000), interval=50, blit=True)

# Show the plot
plt.show()
