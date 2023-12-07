import matplotlib.pyplot as plt
import numpy as np

def calculate_radiation_pattern(wavelength, antenna_length):
    """
    Calculate the radiation pattern of a simple dipole antenna.

    Parameters:
    wavelength (float): Wavelength of the electromagnetic radiation (in meters).
    antenna_length (float): Length of the antenna (in meters).

    Returns:
    np.array, np.array: Arrays representing angles (in radians) and corresponding radiation intensities.
    """
    # Angles from 0 to 360 degrees (in radians)
    angles = np.linspace(0, 2*np.pi, 360)

    # Radiation pattern calculation for a dipole antenna
    # Intensity is proportional to (cos(pi*antenna_length*sin(theta)/wavelength))^2
    # Normalized to have values between 0 and 1
    intensity = (np.cos(np.pi * antenna_length * np.sin(angles) / wavelength))**2

    return angles, intensity

def plot_radiation_pattern(angles, intensity):
    """
    Plot the radiation pattern of an antenna.

    Parameters:
    angles (np.array): Array of angles (in radians).
    intensity (np.array): Array of corresponding radiation intensities.
    """
    # Converting to Cartesian coordinates for plotting
    x = intensity * np.cos(angles)
    y = intensity * np.sin(angles)

    # Plotting the radiation pattern
    plt.figure(figsize=(8, 8))
    plt.polar(angles, intensity)
    plt.fill(angles, intensity, color='blue', alpha=0.3)

    plt.title("Radiation Pattern of a Dipole Antenna")
    plt.grid(True)
    plt.show()

# Example values for antenna radiation pattern
wavelength = 1  # Wavelength in meters
antenna_length = 0.5  # Antenna length in meters

# Calculate the radiation pattern
angles, intensity = calculate_radiation_pattern(wavelength, antenna_length)

# Plotting the radiation pattern
plot_radiation_pattern(angles, intensity)
