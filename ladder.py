from sympy import symbols, Function, diff, sqrt, solve

# Define the variables
t = symbols('t')
x = Function('x')(t)  # distance of the bottom of the ladder from the wall
y = Function('y')(t)  # distance of the top of the ladder from the ground

# Given values
ladder_length = 15  # length of the ladder
dx_dt = 1  # rate at which the bottom is moving away from the wall

# Pythagoras' Theorem: x^2 + y^2 = ladder_length^2
equation = x**2 + y**2 - ladder_length**2

# Differentiating w.r.t t
differentiated_eq = diff(equation, t)

# Solve for dy/dt
solved_dy_dt = solve(differentiated_eq, diff(y, t))

# Substitute dx/dt = 1 and x = 9, and solve for dy/dt
dy_dt = solved_dy_dt[0].subs({diff(x, t): dx_dt, x: 9})
print(dy_dt)
