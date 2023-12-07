import matplotlib.pyplot as plt
import numpy as np

def calculate_magnetic_force(charge, velocity, magnetic_field):
    """
    Calculate the magnetic force on a moving charge in a magnetic field.

    Parameters:
    charge (float): Charge of the particle (in Coulombs).
    velocity (np.array): Velocity of the particle (in m/s) as a 3D vector.
    magnetic_field (np.array): Magnetic field (in Tesla) as a 3D vector.

    Returns:
    np.array: Magnetic force on the particle as a 3D vector (in Newtons).
    """
    # Magnetic force: F = q * (v x B)
    force = charge * np.cross(velocity, magnetic_field)
    return force

def plot_vectors(velocity, magnetic_field, force):
    """
    Plot the velocity, magnetic field, and force vectors.

    Parameters:
    velocity (np.array): Velocity vector.
    magnetic_field (np.array): Magnetic field vector.
    force (np.array): Force vector.
    """
    # Creating the figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotting the vectors
    ax.quiver(0, 0, 0, velocity[0], velocity[1], velocity[2], color='blue', label='Velocity (v)')
    ax.quiver(0, 0, 0, magnetic_field[0], magnetic_field[1], magnetic_field[2], color='red', label='Magnetic Field (B)')
    ax.quiver(0, 0, 0, force[0], force[1], force[2], color='green', label='Force (F)')

    # Setting the plot limits
    max_range = np.max(np.abs(np.array([velocity, magnetic_field, force])))
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    # Labels and legend
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.title("Magnetic Force on a Moving Charge")
    ax.legend()

    # Show the plot
    plt.show()

# Example values for the magnetic force problem
charge = 1e-6  # Charge in Coulombs
velocity = np.array([0, 2, 0])  # Velocity in m/s along the y-axis
magnetic_field = np.array([0, 0, 1])  # Magnetic field in Tesla along the z-axis

# Calculate the magnetic force
magnetic_force = calculate_magnetic_force(charge, velocity, magnetic_field)

# Plotting the vectors
plot_vectors(velocity, magnetic_field, magnetic_force)
