import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Constants
k_e = 8.9875517873681764e9  # Coulomb's constant (N m^2 C^-2)

# Parameters
R = 1.0  # Radius of the ring (meters)
Q = 1e-9  # Total charge on the ring (Coulombs)
z = 0.5  # Distance from the center of the ring to point P (meters)

# Charge density (charge per unit length) along the ring
lambda_charge = Q / (2 * np.pi * R)

# Function to calculate electric field magnitude at a point P
def electric_field(z, R, lambda_charge, k_e):
    def dE(theta):
        dq = lambda_charge * R  # Charge element
        r = np.sqrt(R**2 + z**2)  # Distance from dq to point P
        cos_theta = R / r  # Cosine of the angle between r and the axis
        return k_e * dq * cos_theta / r**2

    # Integrate over theta from 0 to 2*pi
    E, _ = integrate.quad(dE, 0, 2*np.pi)
    return E

# Range of distances z to plot
z_values = np.linspace(0, 5, 500)  # 0 to 5 meters
E_values = [electric_field(z, R, lambda_charge, k_e) for z in z_values]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(z_values, E_values, label='Electric Field')
plt.xlabel('Distance from Center of Ring (m)')
plt.ylabel('Electric Field (N/C)')
plt.title('Electric Field Along the Axis of a Charged Ring')
plt.legend()
plt.grid(True)
plt.show()

