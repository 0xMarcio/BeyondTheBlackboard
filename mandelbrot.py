import numpy as np
import matplotlib.pyplot as plt

# Mandelbrot-like iteration function
def mandelbrot_like(c, max_iter=100):
    z = 0
    for _ in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:  # Break the loop if z diverges
            return False  # Indicate divergence
    return True  # Indicate non-divergence

# Parameters
real_range = np.linspace(-2, 1, 800)  # Real part of c
imag_range = np.linspace(-1.5, 1.5, 800)  # Imaginary part of c
max_iter = 50

# Plotting the Mandelbrot-like set
plt.figure(figsize=(10, 10))
for real in real_range:
    for imag in imag_range:
        c = complex(real, imag)
        if mandelbrot_like(c, max_iter):
            plt.plot(real, imag, 'k.', markersize=1)

plt.title("Mandelbrot-like Set")
plt.xlabel('Real part of c')
plt.ylabel('Imaginary part of c')
plt.xlim(-2, 1)
plt.ylim(-1.5, 1.5)
plt.show()

