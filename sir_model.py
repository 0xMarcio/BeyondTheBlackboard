import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# SIR model differential equations
def sir_model(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Total population, N
N = 1000

# Initial number of infected and recovered individuals
I0 = 1
R0 = 0

# Everyone else is susceptible to infection initially
S0 = N - I0 - R0

# Contact rate, beta, and mean recovery rate, gamma (in 1/days)
beta = 0.2
gamma = 1./10 

# Time grid (in days)
t = np.linspace(0, 160, 160)

# Initial conditions vector
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid
ret = odeint(sir_model, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', label='Susceptible')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered')
plt.xlabel('Time /days')
plt.ylabel('Number')
plt.title('SIR Model')
plt.legend()
plt.show()
