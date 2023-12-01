import numpy as np
from scipy.linalg import solve
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Given functions and constants
def g(x):
    return np.exp(x)

def kernel(x, t):
    return np.sin(x + t)

lambda_const = 0.5
a, b = 0, np.pi

# Discretization
N = 50  # Number of points (increased for accuracy)
x_vals = np.linspace(a, b, N)
h = (b - a) / (N - 1)

# Construct the matrix representing the integral equation
matrix = np.eye(N)
for i in range(N):
    for j in range(N):
        if i != j:
            matrix[i, j] = -lambda_const * quad(lambda t: kernel(x_vals[i], t), a, b)[0]
        else:
            matrix[i, j] -= lambda_const * quad(lambda t: kernel(x_vals[i], t), a, b)[0] * h

# Construct the right-hand side of the equation
rhs = np.array([g(x) for x in x_vals])

# Solve the system of linear equations
f_vals = solve(matrix, rhs)

# Plotting the solution
plt.plot(x_vals, f_vals, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Solution of Fredholm Integral Equation of the Second Kind')
plt.legend()
plt.show()

