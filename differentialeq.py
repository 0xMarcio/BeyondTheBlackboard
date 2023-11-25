#!/usr/bin/env python3
import numpy as np
import sys

# Physical constants
g = 9.81  # m/s^2
L = 2  # m
mu = 0.1  # friction coefficient

THETA_0 = np.pi / 2  # Initial angle
THETA_DOT_0 = 0  # Initial angular velocity

# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)

# Solution to the differential equation
def theta(t):
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01  # Time step
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
    return theta

# Print the solution
print(theta(float(sys.argv[1])))
