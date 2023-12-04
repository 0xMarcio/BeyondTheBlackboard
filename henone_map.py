import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 1.4
b = 0.3
num_iterations = 10000

# Initial conditions
x = [0.1]
y = [0]

# Generate the Hénon Map
for _ in range(num_iterations):
    x_n = 1 - a * x[-1] ** 2 + y[-1]
    y_n = b * x[-1]
    x.append(x_n)
    y.append(y_n)

# Plot the Hénon Map
plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=1, c='blue', marker='.')
plt.title('Hénon Map')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
