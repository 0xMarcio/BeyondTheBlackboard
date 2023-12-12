import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)

def calculate_trajectory(v0, theta_deg):
    """
    Calculate the trajectory of a projectile.

    Parameters:
    v0 (float): Initial velocity (m/s)
    theta_deg (float): Launch angle in degrees

    Returns:
    tuple: (time_of_flight, max_height, range, x_vals, y_vals)
    """
    theta = np.radians(theta_deg)  # Convert angle to radians

    # Calculating time of flight, maximum height, and range
    time_of_flight = 2 * v0 * np.sin(theta) / g
    max_height = (v0**2) * (np.sin(theta)**2) / (2 * g)
    range = (v0**2) * np.sin(2 * theta) / g

    # Time intervals for plotting
    t_vals = np.linspace(0, time_of_flight, num=500)

    # Calculating x and y values
    x_vals = v0 * np.cos(theta) * t_vals
    y_vals = v0 * np.sin(theta) * t_vals - 0.5 * g * t_vals**2

    return time_of_flight, max_height, range, x_vals, y_vals

def plot_trajectory(x_vals, y_vals, v0, theta):
    """
    Plot the trajectory of the projectile.

    Parameters:
    x_vals (array): X-coordinates
    y_vals (array): Y-coordinates
    v0 (float): Initial velocity
    theta (float): Launch angle
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals)
    plt.title(f"Projectile Motion: v0={v0} m/s, θ={theta}°")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.show()

# Example Usage
v0 = 30  # initial velocity in m/s
theta = 45  # launch angle in degrees

# Calculate trajectory
tof, max_h, rng, x, y = calculate_trajectory(v0, theta)

# Output results
print(f"Time of Flight: {tof:.2f} s")
print(f"Maximum Height: {max_h:.2f} m")
print(f"Range: {rng:.2f} m")

# Plot trajectory
plot_trajectory(x, y, v0, theta)
