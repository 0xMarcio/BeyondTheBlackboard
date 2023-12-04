import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
G = 9.81  # Acceleration due to gravity (m/s^2)
L1 = 1.0  # Length of the first pendulum (m)
L2 = 1.0  # Length of the second pendulum (m)
M1 = 1.0  # Mass of the first pendulum bob (kg)
M2 = 1.0  # Mass of the second pendulum bob (kg)

# Initial conditions (angles and angular velocities)
theta1_initial = np.pi / 2  # Initial angle of the first pendulum (radians)
omega1_initial = 0.0  # Initial angular velocity of the first pendulum (radians/s)
theta2_initial = np.pi / 2  # Initial angle of the second pendulum (radians)
omega2_initial = 0.0  # Initial angular velocity of the second pendulum (radians/s)

# Time variables
t_max = 20.0  # Total simulation time (s)
dt = 0.05  # Time step (s)
num_steps = int(t_max / dt)

# Function to calculate the derivatives of angles and angular velocities
def derivatives(state, t):
    theta1, omega1, theta2, omega2 = state
    
    # Equations of motion for a double pendulum
    delta_theta = theta2 - theta1
    denominator1 = (M1 + M2) * L1 - M2 * L1 * np.cos(delta_theta)**2
    denominator2 = (L2 / L1) * denominator1
    
    theta1_dot = omega1
    omega1_dot = (M2 * L1 * omega1**2 * np.sin(delta_theta) * np.cos(delta_theta)
                 + M2 * G * np.sin(theta2) * np.cos(delta_theta)
                 + M2 * L2 * omega2**2 * np.sin(delta_theta)
                 - (M1 + M2) * G * np.sin(theta1)) / denominator1
    
    theta2_dot = omega2
    omega2_dot = (-L2 / L1 * omega1**2 * np.sin(delta_theta) * np.cos(delta_theta)
                 + (M1 + M2) * G * np.sin(theta1) * np.cos(delta_theta)
                 - (M1 + M2) * L1 * omega1**2 * np.sin(delta_theta)
                 - (M1 + M2) * G * np.sin(theta2)) / denominator2
    
    return [theta1_dot, omega1_dot, theta2_dot, omega2_dot]

# Initialize the state vector
state_initial = [theta1_initial, omega1_initial, theta2_initial, omega2_initial]

# Time points for simulation
t_points = np.arange(0, t_max, dt)

# Perform the numerical integration using the Runge-Kutta method
state_history = np.zeros((len(t_points), 4))
state_history[0] = state_initial

for i in range(1, len(t_points)):
    k1 = derivatives(state_history[i-1], t_points[i-1])
    k2 = derivatives(state_history[i-1] + dt/2 * np.array(k1), t_points[i-1] + dt/2)
    k3 = derivatives(state_history[i-1] + dt/2 * np.array(k2), t_points[i-1] + dt/2)
    k4 = derivatives(state_history[i-1] + dt * np.array(k3), t_points[i-1] + dt)
    
    state_history[i] = state_history[i-1] + (dt / 6) * (np.array(k1) + 2*np.array(k2) + 2*np.array(k3) + np.array(k4))

# Extract angles for plotting
theta1_history = state_history[:, 0]
theta2_history = state_history[:, 2]

# Function to update the animation
def update_animation(num, line1, line2):
    line1.set_data([0, L1 * np.sin(theta1_history[num])], [0, -L1 * np.cos(theta1_history[num])])
    line2.set_data([L1 * np.sin(theta1_history[num]), L1 * np.sin(theta1_history[num]) + L2 * np.sin(theta2_history[num])],
                   [-L1 * np.cos(theta1_history[num]), -L1 * np.cos(theta1_history[num]) - L2 * np.cos(theta2_history[num])])
    return line1, line2

# Create the figure and axes for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5 * (L1 + L2), 1.5 * (L1 + L2))
ax.set_ylim(-1.5 * (L1 + L2), 1.5 * (L1 + L2))

# Create lines for the pendulum
line1, = ax.plot([], [], 'o-', lw=2, markersize=8)
line2, = ax.plot([], [], 'o-', lw=2, markersize=8)

# Create an animation
ani = animation.FuncAnimation(fig, update_animation, len(t_points), fargs=(line1, line2), interval=dt*1000, blit=True)

# Display the animation
plt.title("Double Pendulum Motion")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
