# Improved Newton's Second Law Problem Solver with Units

def calculate_newtons_law(quantity, mass=None, acceleration=None, force=None):
    """
    Calculate the force, mass, or acceleration using Newton's Second Law.

    Parameters:
    quantity (str): The quantity to calculate ('force', 'mass', or 'acceleration').
    mass (float): Mass of the object (in kg), required if calculating force or acceleration.
    acceleration (float): Acceleration of the object (in m/s^2), required if calculating force or mass.
    force (float): Force applied to the object (in Newtons), required if calculating mass or acceleration.

    Returns:
    tuple: A tuple containing the calculated value and its unit.
    """

    if quantity == "force":
        # Calculate force: F = m * a, unit: Newtons (N)
        return (mass * acceleration, "Newtons")
    elif quantity == "mass":
        # Calculate mass: m = F / a, unit: kilograms (kg)
        return (force / acceleration, "kilograms")
    elif quantity == "acceleration":
        # Calculate acceleration: a = F / m, unit: meters per second squared (m/s^2)
        return (force / mass, "meters per second squared")

# Main function to run the problem solver
def main():
    print("Newton's Second Law Problem Solver\n")

    # User chooses which quantity to calculate
    quantity = input("What would you like to calculate (force, mass, acceleration)? ").lower()

    # Input and calculation based on user's choice
    if quantity == "force":
        mass = float(input("Enter the mass of the object (in kg): "))
        acceleration = float(input("Enter the acceleration of the object (in m/s^2): "))
        result, unit = calculate_newtons_law(quantity, mass=mass, acceleration=acceleration)
    elif quantity == "mass":
        force = float(input("Enter the force applied to the object (in Newtons): "))
        acceleration = float(input("Enter the acceleration of the object (in m/s^2): "))
        result, unit = calculate_newtons_law(quantity, force=force, acceleration=acceleration)
    elif quantity == "acceleration":
        force = float(input("Enter the force applied to the object (in Newtons): "))
        mass = float(input("Enter the mass of the object (in kg): "))
        result, unit = calculate_newtons_law(quantity, force=force, mass=mass)

    # Displaying the results with units
    print(f"\nThe calculated {quantity} is {result:.2f} {unit}.")

# Run the main function
if __name__ == "__main__":
    main()
