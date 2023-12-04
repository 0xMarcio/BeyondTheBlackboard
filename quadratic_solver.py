import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The solutions are real and distinct: x1 = {root1}, x2 = {root2}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print(f"The solution is real and equal: x = {root1}")
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminant) / (2*a)
    print(f"The solutions are complex: x1 = {realPart} + {imaginaryPart}i, x2 = {realPart} - {imaginaryPart}i")
