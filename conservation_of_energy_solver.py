# Conservation of Energy Problem Solver

def calculate_mechanical_energy(mass, height, velocity, gravity=9.81):
    """
    Calculate the total mechanical energy (potential and kinetic) of an object.

    Parameters:
    mass (float): Mass of the object (in kg).
    height (float): Height of the object above the ground (in meters).
    velocity (float): Velocity of the object (in m/s).
    gravity (float): Acceleration due to gravity (in m/s^2), default is 9.81 m/s^2.

    Returns:
    float: Total mechanical energy of the object (in Joules).
    """

    # Calculate potential energy: PE = m * g * h
    potential_energy = mass * gravity * height

    # Calculate kinetic energy: KE = 0.5 * m * v^2
    kinetic_energy = 0.5 * mass * velocity**2

    # Total mechanical energy is the sum of potential and kinetic energy
    total_energy = potential_energy + kinetic_energy

    return total_energy

# Main function to run the problem solver
def main():
    print("Conservation of Energy Problem Solver\n")

    # Input for mass, height, and velocity
    mass = float(input("Enter the mass of the object (in kg): "))
    height = float(input("Enter the height of the object above the ground (in meters): "))
    velocity = float(input("Enter the velocity of the object (in m/s): "))

    # Calculate the total mechanical energy
    total_energy = calculate_mechanical_energy(mass, height, velocity)

    # Displaying the results
    print(f"\nThe total mechanical energy of the object is {total_energy:.2f} Joules.")

# Run the main function
if __name__ == "__main__":
    main()
