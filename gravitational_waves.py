import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
wave_speed = 3  # Arbitrary units for visualization
num_waves = 20
distance_between_sources = 2  # Binary system separation

# Wave simulation function
def wavefront(x, y, t, source):
    return np.sin(np.sqrt((x - source[0])**2 + (y - source[1])**2) - wave_speed * t)

# Grid setup
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Source positions (binary system)
source1 = (-distance_between_sources / 2, 0)
source2 = (distance_between_sources / 2, 0)

# Animation function
def animate(t):
    Z = wavefront(X, Y, t, source1) + wavefront(X, Y, t, source2)
    cont.set_array(Z)
    return cont,

# Plot setup
fig, ax = plt.subplots()
Z = wavefront(X, Y, 0, source1) + wavefront(X, Y, 0, source2)
cont = plt.contourf(X, Y, Z, cmap='plasma', levels=num_waves)
ax.set_aspect('equal')
plt.colorbar(cont)


# Animation function
def animate(t):
    ax.clear()
    Z = wavefront(X, Y, t, source1) + wavefront(X, Y, t, source2)
    cont = ax.contourf(X, Y, Z, cmap='plasma', levels=num_waves)
    ax.set_title(f"Time: {t}")
    return cont.collections

# Create and run the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
