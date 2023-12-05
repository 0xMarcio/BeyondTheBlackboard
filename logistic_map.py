import matplotlib.pyplot as plt

# Initial population and growth rate
P0 = 0.5
r_values = [2.4, 3.5, 3.9]  # Try different values of r

# Number of iterations
iterations = 100

# Function to generate the logistic map data
def logistic_map(P0, r, iterations):
    data = []
    P = P0
    for _ in range(iterations):
        P = r * P * (1 - P)
        data.append(P)
    return data

# Plot the logistic map for different values of r
for r in r_values:
    population_data = logistic_map(P0, r, iterations)
    plt.plot(range(iterations), population_data, label=f'r = {r}')

plt.xlabel('Iterations')
plt.ylabel('Population')
plt.legend()
plt.title('Logistic Map')
plt.show()
