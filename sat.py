from sympy import symbols, pi

# Defining symbols
r_A, r_B = symbols('r_A r_B')

# Given relation
r_A = (1/3) * r_B

# Circumferences
C_A = 2 * pi * r_A
C_B = 2 * pi * r_B

# Calculating the number of revolutions
#number_of_revolutions = C_B / C_A
#number_of_revolutions.simplify()


# Given that r_A = (1/3) * r_B, we already have the circumferences as:
# C_A = 2 * pi * r_A and C_B = 2 * pi * r_B

# The number of revolutions Circle A makes just by rolling (without considering the circular path) is:
revolutions_rolling = C_B / C_A

# Adding the extra revolution due to the circular path
total_revolutions = revolutions_rolling + 1

total_revolutions.simplify()
