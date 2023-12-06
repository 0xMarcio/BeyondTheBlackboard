# Conservation of Momentum Problem Solver

def calculate_final_velocities(m1, v1_initial, m2, v2_initial, perfectly_inelastic=False):
    """
    Calculate the final velocities of two objects after collision using the conservation of momentum.

    Parameters:
    m1 (float): Mass of the first object (in kg).
    v1_initial (float): Initial velocity of the first object (in m/s).
    m2 (float): Mass of the second object (in kg).
    v2_initial (float): Initial velocity of the second object (in m/s).
    perfectly_inelastic (bool): If the collision is perfectly inelastic (objects stick together), set to True.

    Returns:
    tuple: A tuple containing the final velocities of the first and second object (in m/s).
    """

    # The conservation of momentum formula: m1*v1_initial + m2*v2_initial = m1*v1_final + m2*v2_final
    # For a perfectly inelastic collision, the final velocities are the same: v1_final = v2_final

    if perfectly_inelastic:
        # Calculate the final velocity for a perfectly inelastic collision
        v_final = (m1 * v1_initial + m2 * v2_initial) / (m1 + m2)
        return v_final, v_final
    else:
        # For an elastic collision, we need to solve two equations:
        # Conservation of momentum: m1*v1_initial + m2*v2_initial = m1*v1_final + m2*v2_final
        # Conservation of kinetic energy: 0.5*m1*v1_initial**2 + 0.5*m2*v2_initial**2 = 0.5*m1*v1_final**2 + 0.5*m2*v2_final**2

        # Simplify the equations and solve for v1_final and v2_final
        # This can be done using various methods, here we assume a simple elastic collision for the example
        v1_final = (m1 - m2) / (m1 + m2) * v1_initial + (2 * m2) / (m1 + m2) * v2_initial
        v2_final = (2 * m1) / (m1 + m2) * v1_initial + (m2 - m1) / (m1 + m2) * v2_initial
        return v1_final, v2_final

# Main function to run the problem solver
def main():
    print("Conservation of Momentum Problem Solver\n")

    # Input for the masses and initial velocities
    m1 = float(input("Enter the mass of the first object (in kg): "))
    v1_initial = float(input("Enter the initial velocity of the first object (in m/s): "))
    m2 = float(input("Enter the mass of the second object (in kg): "))
    v2_initial = float(input("Enter the initial velocity of the second object (in m/s): "))

    # Asking the user if the collision is perfectly inelastic
    collision_type = input("Is the collision perfectly inelastic (yes/no)? ").lower()
    perfectly_inelastic = True if collision_type == "yes" else False

    # Calculate the final velocities
    v1_final, v2_final = calculate_final_velocities(m1, v1_initial, m2, v2_initial, perfectly_inelastic)

    # Displaying the results
    print("\nResults:")
    if perfectly_inelastic:
        print(f"After the collision, both objects move together with a velocity of {v1_final:.2f} m/s.")
    else:
        print(f"After the collision, the final velocity of the first object is {v1_final:.2f} m/s.")
        print(f"After the collision, the final velocity of the second object is {v2_final:.2f} m/s.")

# Run the main function
if __name__ == "__main__":
    main()
