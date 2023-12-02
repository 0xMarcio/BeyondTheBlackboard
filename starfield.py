import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d
from scipy.signal import deconvolve

# Function to generate a simulated starfield image
def generate_starfield(size, num_stars, max_brightness):
    """
    Generate a simulated starfield image.

    Parameters:
    size (int): Size of the image (size x size pixels)
    num_stars (int): Number of stars to simulate
    max_brightness (int): Maximum brightness of the stars

    Returns:
    image (np.ndarray): Simulated starfield image
    """
    image = np.zeros((size, size))
    for _ in range(num_stars):
        x, y = np.random.randint(0, size, 2)
        brightness = np.random.randint(1, max_brightness)
        image[x, y] = brightness
    return image

# Function to generate a Point Spread Function (PSF)
def generate_psf(size, std_dev):
    """
    Generate a Point Spread Function (PSF) using a Gaussian distribution.

    Parameters:
    size (int): Size of the PSF (size x size pixels)
    std_dev (float): Standard deviation of the Gaussian distribution

    Returns:
    psf (np.ndarray): Generated PSF
    """
    x = np.linspace(-size // 2, size // 2, size)
    y = x[:, np.newaxis]
    psf = np.exp(-(x**2 + y**2) / (2 * std_dev**2))
    psf /= psf.sum()  # Normalize the PSF
    return psf

# Function to perform Richardson-Lucy deconvolution
def richardson_lucy(image, psf, iterations):
    """
    Perform Richardson-Lucy deconvolution.

    Parameters:
    image (np.ndarray): The blurred image
    psf (np.ndarray): The Point Spread Function
    iterations (int): Number of iterations for the deconvolution algorithm

    Returns:
    deconvolved (np.ndarray): Deconvolved image
    """
    u = np.full(image.shape, 0.5)
    for _ in range(iterations):
        conv = convolve2d(u, psf, mode='same')
        ratio = image / conv
        u *= convolve2d(ratio, psf[::-1, ::-1], mode='same')
    return u

# Parameters
image_size = 100
num_stars = 50
max_brightness = 255
psf_size = 21
std_dev = 3
deconv_iterations = 30

# Generate simulated starfield and PSF
starfield = generate_starfield(image_size, num_stars, max_brightness)
psf = generate_psf(psf_size, std_dev)

# Blur the image using the PSF
blurred_starfield = convolve2d(starfield, psf, mode='same')

# Perform deconvolution
deconvolved_starfield = richardson_lucy(blurred_starfield, psf, deconv_iterations)

# Visualization
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Original Starfield
ax[0].imshow(starfield, cmap='gray')
ax[0].set_title('Original Starfield')
ax[0].axis('off')

# Blurred Starfield
ax[1].imshow(blurred_starfield, cmap='gray')
ax[1].set_title('Blurred Starfield')
ax[1].axis('off')

# Deconvolved Starfield
ax[2].imshow(deconvolved_starfield, cmap='gray')
ax[2].set_title('Deconvolved Starfield')
ax[2].axis('off')

plt.show()
