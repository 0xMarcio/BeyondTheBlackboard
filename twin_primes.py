import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def plot_twin_primes(limit):
    """Plot twin primes up to a specified limit."""
    primes = [n for n in range(2, limit) if is_prime(n)]
    twin_primes = [(p, p+2) for p in primes if is_prime(p+2)]

    # Prepare data for plotting
    x_coords = []
    y_coords = []

    for tp in twin_primes:
        # Use the average of the twin prime pair for the x-coordinate
        avg_x = (tp[0] + tp[1]) / 2
        x_coords.append(avg_x)
        y_coords.append(np.log(avg_x))  # Use logarithmic scale for y-axis

    # Plotting
    plt.figure(figsize=(15, 8))
    plt.scatter(x_coords, y_coords, color='red', alpha=0.5, s=10)  # Reduced point size and added transparency

    plt.title("Twin Primes up to " + str(limit))
    plt.xlabel("Average of Twin Prime Pair")
    plt.ylabel("Logarithmic Distribution Pattern")
    plt.grid(True)
    plt.show()

# Visualize twin primes up to 10000
plot_twin_primes(10000)

