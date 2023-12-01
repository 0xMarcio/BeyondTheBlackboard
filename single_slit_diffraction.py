import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
wavelength = 500e-9  # Wavelength of light (500 nm)
slit_width = 1e-6    # Width of the slit (1 micron)
screen_distance = 2  # Distance to the screen (meters)

# Diffraction intensity calculation function
def diffraction_intensity(theta, wavelength, slit_width):
    # Angular position of the minima and maxima
    alpha = (np.pi * slit_width * np.sin(theta)) / wavelength

    # Avoid division by zero for alpha
    alpha[alpha == 0] = 1e-10

    # Intensity distribution formula
    intensity = (np.sin(alpha) / alpha) ** 2
    return intensity

# Range of angles for the diffraction pattern
theta = np.linspace(-np.pi/2, np.pi/2, 1000)
intensity = diffraction_intensity(theta, wavelength, slit_width)

# Create the plot for diffraction pattern
plt.figure(figsize=(10, 6))
plt.plot(theta, intensity, color='blue', label='Diffraction Pattern')
plt.xlabel('Angle (radians)')
plt.ylabel('Relative Intensity')
plt.title('Single Slit Diffraction Pattern')
plt.grid(True)
plt.legend()
plt.show()
