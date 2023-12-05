# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
c = 299792458  # Speed of light (m/s)
solar_mass_to_kg = 1.989e30  # Mass of the Sun in kilograms

# Input mass of the black hole in solar masses
mass_solar_mass = float(input("Enter the mass of the black hole in solar masses: "))

# Convert solar masses to kilograms
mass_kg = mass_solar_mass * solar_mass_to_kg

# Calculate Schwarzschild radius
schwarzschild_radius = 2 * G * mass_kg / (c**2)

# Calculate event horizon radius
event_horizon_radius = schwarzschild_radius

print(f"Schwarzschild radius: {schwarzschild_radius} meters")
print(f"Event horizon radius: {event_horizon_radius} meters")
