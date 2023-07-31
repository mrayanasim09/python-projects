# This code is made by MRayan Asim
# Packages to installed:
# pip install numpy
# pip install matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
import math

# Get quadratic equation coefficients from user
while True:
    try:
        a = float(input("Enter the coefficient of x^2: "))
        break
    except (ValueError, TypeError):
        print("Please enter a valid value.")

while True:
    try:
        b = float(input("Enter the coefficient of x: "))
        break
    except (ValueError, TypeError):
        print("Please enter a valid value.")

while True:
    try:
        c = float(input("Enter the constant term: "))
        break
    except (ValueError, TypeError):
        print("Please enter a valid value.")

print(a, "x^2", "+", b, "x", "+", c, "= 0")

t = input("Are you satisfied with this equation? (yes/no) ")

if t.lower() == "no":
    print("OK, enter them again:")
    while True:
        try:
            a = float(input("Enter the coefficient of x^2: "))
            break
        except (ValueError, TypeError):
            print("Please enter a valid value.")

    while True:
        try:
            b = float(input("Enter the coefficient of x: "))
            break
        except (ValueError, TypeError):
            print("Please enter a valid value.")

    while True:
        try:
            c = float(input("Enter the constant term: "))
            break
        except (ValueError, TypeError):
            print("Please enter a valid value.")
time.sleep(3)


# Solve quadratic equation
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = np.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


# Factorize quadratic equation into two brackets
def factorize_quadratic(a, b, c):
    factors = []

    # Convert coefficients to integers
    a = int(a)
    b = int(b)
    c = int(c)

    # Factor out common factors from the coefficients
    gcd = math.gcd(a, math.gcd(b, c))
    a //= gcd
    b //= gcd
    c //= gcd

    # Factorize the coefficient of x^2
    if a != 1:
        factors.append(f"{a}(x^2)")
    else:
        factors.append("(x^2)")

    # Factorize the coefficient of x
    if b != 0:
        if b < 0:
            factors.append(f"(x{-b})")
        else:
            factors.append(f"(x+{b})")

    # Factorize the constant term
    if c != 0:
        factors.append(f"({c})")

    return tuple(factors)


# Get the range of x values from the user
x_values = input("Enter the range of x values (start, end): ")
x_start, x_end = map(float, x_values.split(","))

num_points = 100

# Generate x values
x = np.linspace(x_start, x_end, num_points)

# Compute y values
y = a * x ** 2 + b * x + c

# Find the vertex of the quadratic equation
vertex_x = -b / (2 * a)
vertex_y = a * vertex_x ** 2 + b * vertex_x + c

# Create the plot
plt.plot(x, y)

# Set the x and y labels
plt.xlabel("x")
plt.ylabel("y")

# Set the title
plt.title("Quadratic Equation: y = {}x^2 + {}x + {}".format(a, b, c))

# Set y-axis at the center
plt.axhline(0, color="black", linewidth=0.5)

# Mark the vertex on the graph
plt.plot(vertex_x, vertex_y, "ro")
plt.annotate(
    f"({vertex_x:.2f}, {vertex_y:.2f})",
    (vertex_x, vertex_y),
    xytext=(vertex_x + 1, vertex_y - 10),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
)

# Solve quadratic equation
roots = solve_quadratic(a, b, c)

# Print the roots
print("\nRoots:")
for root in roots:
    if isinstance(root, complex):
        print(f"x = {root.real:.2f} + {root.imag:.2f}j")
    else:
        print(f"x = {root:.2f}")

# Factorize quadratic equation into two brackets
factors = factorize_quadratic(a, b, c)

# Print the factorization
print("\nFactorization:")
print("".join(factors))

time.sleep(10)

# Show the plot
plt.show()
