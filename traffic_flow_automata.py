import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
length = 100  # Length of the road
density = 0.2  # Density of cars
max_speed = 5  # Maximum speed of cars
slow_prob = 0.3  # Probability of random slowdown
steps = 50  # Number of steps to simulate

# Initialize the road
np.random.seed(42)
road = -np.ones(length, dtype=int)  # -1 represents an empty cell
car_indices = np.random.choice(length, size=int(density * length), replace=False)
road[car_indices] = np.random.randint(0, max_speed + 1, size=len(car_indices))

# Function to update the road
def update(road):
    new_road = -np.ones(length, dtype=int)
    for i in range(length):
        if road[i] >= 0:
            distance = 1
            while road[(i + distance) % length] == -1:
                distance += 1
            speed = min(road[i] + 1, max_speed, distance - 1)
            if speed > 0 and np.random.rand() < slow_prob:
                speed -= 1
            new_road[(i + speed) % length] = speed
    return new_road

# Simulate
fig, ax = plt.subplots()
ax.set_xlim(0, length)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], 'ks')

def animate(i):
    global road
    road = update(road)
    line.set_data(np.where(road >= 0)[0], np.zeros(np.count_nonzero(road >= 0)))
    return line,

ani = animation.FuncAnimation(fig, animate, frames=steps, interval=100, blit=True)
plt.show()
