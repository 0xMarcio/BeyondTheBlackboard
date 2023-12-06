# Updated Gravitational Force Problem Solver with Mass in Solar Masses and Distance in Astronomical Units (AU)

def calculate_gravitational_force(m1_solar_masses, m2_solar_masses, distance_au, gravitational_constant=6.67430e-11):
    """
    Calculate the gravitational force between two objects with masses in solar masses and distance in astronomical units.

    Parameters:
    m1_solar_masses (float): Mass of the first object in solar masses.
    m2_solar_masses (float): Mass of the second object in solar masses.
    distance_au (float): Distance between the centers of the two masses in astronomical units (AU).
    gravitational_constant (float): Gravitational constant, default is 6.67430 x 10^-11 N(m/kg)^2.

    Returns:
    float: Gravitational force between the two objects (in Newtons).
    """

    # Convert solar masses to kilograms (1 solar mass = 1.989 x 10^30 kg)
    solar_mass_to_kg = 1.989e30
    m1 = m1_solar_masses * solar_mass_to_kg
    m2 = m2_solar_masses * solar_mass_to_kg

    # Convert astronomical units to meters (1 AU = 1.496 x 10^11 meters)
    au_to_meters = 1.496e11
    distance_meters = distance_au * au_to_meters

    # Calculate the gravitational force: F = G * (m1 * m2) / r^2
    force = gravitational_constant * (m1 * m2) / (distance_meters**2)

    return force

# Main function to run the problem solver
def main():
    print("Gravitational Force Problem Solver\n")

    # Input for the masses in solar masses and the distance in AU
    m1_solar_masses = float(input("Enter the mass of the first object (in solar masses): "))
    m2_solar_masses = float(input("Enter the mass of the second object (in solar masses): "))
    distance_au = float(input("Enter the distance between the centers of the two objects (in astronomical units): "))

    # Calculate the gravitational force
    gravitational_force = calculate_gravitational_force(m1_solar_masses, m2_solar_masses, distance_au)

    # Displaying the results with units
    print(f"\nThe gravitational force between the objects is {gravitational_force:.2e} Newtons.")

# Run the main function
if __name__ == "__main__":
    main()
