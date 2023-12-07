import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def plot_twin_primes_plotly(limit):
    """Plot twin primes up to a specified limit using Plotly."""
    primes = [n for n in range(2, limit) if is_prime(n)]
    twin_primes = [(p, p+2) for p in primes if is_prime(p+2)]

    # Prepare data for plotting
    x_coords = []
    y_coords = []
    twin_prime_pairs = []

    for tp in twin_primes:
        avg_x = (tp[0] + tp[1]) / 2
        x_coords.append(avg_x)
        y_coords.append(np.log(avg_x))  # Use logarithmic scale for y-axis
        twin_prime_pairs.append(f"{tp[0]}, {tp[1]}")

    # Create Plotly figure
    fig = go.Figure(data=go.Scatter(x=x_coords, y=y_coords, mode='markers',
                                    marker=dict(color='red', size=10, opacity=0.5),
                                    text=twin_prime_pairs, hoverinfo='text'))

    # Update layout
    fig.update_layout(title=f"Twin Primes up to {limit}",
                      xaxis_title="Average of Twin Prime Pair",
                      yaxis_title="Logarithmic Distribution Pattern",
                      yaxis=dict(type='log'))  # Setting y-axis to logarithmic

    fig.show()

# Visualize twin primes up to 5000 using Plotly
plot_twin_primes_plotly(5000)
