# This code is made by MRayan Asim
# Packages needed:
# pip install pygame
# pip install matplotlib.pyplot
# pip install sympy
import ast
import math
import matplotlib.pyplot as plt
import time
from sympy import symbols
import sympy

print("Hello! This calculator is made by MRayan Asim. Hope you will like this! 😊")
time.sleep(3)

print("Let's begin...")

while True:
    try:
        x = int(input("Enter the first number: "))
        break
    except ValueError:
        print("You entered wrong value for the first number")
        x = int(input("Enter the first number again: "))

while True:
    try:
        y = int(input("Enter second number: "))
        break
    except ValueError:
        print("You entered wrong value for the second number")
        y = int(input("Enter a number again: "))

while True:
    try:
        z = int(input("Enter third  number: "))
        break
    except ValueError:
        print("You entered wrong value for the third number")
        z = int(input("Enter a number again: "))

start_time = time.time()


def calculator(number_1, number_2, number_3):
    return number_1 + number_2 + number_3


def calculator_1(number_1, number_2, number_3):
    return number_1 - number_2 - number_3


def calculator_2(number_1, number_2, number_3):
    return number_1 * number_2 * number_3


while True:
    try:

        def calculator_3(number_1, number_2, number_3):
            return number_1 / number_2 / number_3

        result = round(calculator_3(x, y, z), 3)
        break
    except ZeroDivisionError:
        print("Error: Cannot divide any number by zero")
        choice = input("Do you want to change the numbers? (yes/no): ")
        if choice.lower() == "yes":
            x = int(input("Enter a new value for the first number: "))
            y = int(input("Enter a new value for the second number: "))
            z = int(input("Enter a new value for the third number: "))

        else:
            break


def calculator_4(number_2):
    return number_2 * number_2


while True:
    try:

        def calculator_5(number_1, number_2, number_3):
            return number_1 % number_2 % number_3

        break
    except ZeroDivisionError:
        print("We cannot take the remainder of a negative number")


def calculator_6(number_1):
    return number_1 * number_1


def calculator_7(number_3):
    return number_3 * number_3


def calculator_8(number_1):
    return number_1 * number_1 * number_1


def calculator_9(number_2):
    return number_2 * number_2 * number_2


def calculator_10(number_3):
    return number_3 * number_3 * number_3


def calculator_11(number_1, number_2, number_3):
    return number_1 // number_2 // number_3


def round_to_3_decimal_places(value):
    return round(value, 3)


u = input("Are you satisfied with your values or you want to change them:")

if u == "yes" or u == "Yes" or "y" in u:
    print("ok")

else:
    x = int(input("Enter your first number again:"))
    y = int(input("Enter your second number again:"))
    z = int(input("Enter the third number again:"))

print(calculator(x, y, z), ", the answer of addition")
print(calculator_1(x, y, z), ", the answer of subtraction")
print(calculator_2(x, y, z), ", the answer of multiplication")
print(result, ", the answer of division")
print(calculator_5(x, y, z), ", the remainder when divided")
print(calculator_11(x, y, x), "the whole number left after there division")
print(calculator_4(y), ", the square of the second number")
print(calculator_7(z), ", the square of the third number")
print(calculator_6(x), ", the square of the first number")
print(calculator_8(x), ". the cube of the first number")
print(calculator_9(y), ". the cube of the second number")
print(calculator_10(z), ". the cube of the third number")


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Invalid input! Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a positive integer.")


try:
    if x < 0:
        print(
            "The first number which you enter is a negative number so the computer does not calculated the factorial"
        )
    elif x > 25:
        print(
            "The first entered number is too large so the computer does not calculated the factorial"
        )
    else:
        print(factorial(x), "is the factorial of the first number")
    if y < 0:
        print(
            "The second number which you enter is a negative number so the computer does not calculated the factorial"
        )
    elif y > 25:
        print(
            "The second entered number is too large so the computer does not calculated the factorial"
        )
    else:
        print(factorial(y), "is the factorial of the second number")
    if z < 0:
        print(
            "The third number which you enter is a negative number so the computer does not calculated the factorial"
        )
    elif z > 25:
        print(
            "The third entered number is too large so the computer does not calculated the factorial"
        )
    else:
        print(factorial(z), "is the factorial of the third number")
except ValueError:
    print("Invalid input!")

while True:
    try:
        print(
            round_to_3_decimal_places(math.sqrt(x)),
            ", the square root of the first number",
        )
        break
    except ValueError:
        print("We cannot take square root of a negative number")
        x = int(input("Enter a positive number for the first number: "))

while True:
    try:
        print(
            round_to_3_decimal_places(math.sqrt(y)),
            ", the square root of the second number",
        )
        break
    except ValueError:
        print("We cannot take square root of a negative number")
        y = int(input("Enter a positive number for the second number: "))

while True:
    try:
        print(
            round_to_3_decimal_places(math.sqrt(z)),
            ", the square root of the third number",
        )
        break
    except ValueError:
        print("We cannot take square root of a negative number")
        z = int(input("Enter a positive number for the third number: "))

print(
    round_to_3_decimal_places(math.pow(x, 1 / 3)), ", the cube root of the first number"
)
print(
    round_to_3_decimal_places(math.pow(y, 1 / 3)),
    ", the cube root of the second number",
)
print(
    round_to_3_decimal_places(math.pow(z, 1 / 3)), ", the cube root of the third number"
)
print(round(x * (math.pi / 180), 3), ", the answer of the first number in radians")
print(round(y * (math.pi / 180), 3), ", the answer of the second number in radians")
print(round(z * (math.pi / 180), 3), ", the answer of the third number in radians")


def calculate_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


factors_x = calculate_factors(x)
factors_y = calculate_factors(y)
factors_z = calculate_factors(z)

print(f"The factors of {x} ,the first number are: {factors_x}")
print(f"The factors of {y} ,the second number are: {factors_y}")
print(f"The factors of {z} ,for third number are: {factors_z}")

binary = bin(x)
octal = oct(x)
hexadecimal = hex(x)
print(f"{x} in Binary: {binary}")
print(f"{x} in Octal: {octal}")
print(f"{x} in Hexadecimal: {hexadecimal}")

binary = bin(y)
octal = oct(y)
hexadecimal = hex(y)
print(f"{y} in Binary: {binary}")
print(f"{y} in Octal: {octal}")
print(f"{y} in Hexadecimal: {hexadecimal}")

binary = bin(z)
octal = oct(z)
hexadecimal = hex(z)
print(f"{z} in Binary: {binary}")
print(f"{z} in Octal: {octal}")
print(f"{z} in Hexadecimal: {hexadecimal}")


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_composite(number):
    return not is_prime(number)


if is_even(x):
    print(f"{x} the first number is even.")
else:
    print(f"{x} the first number is odd.")

if is_prime(x):
    print(f"{x} the first number is prime.")
else:
    print(f"{x} the first number is composite.")

if is_even(y):
    print(f"{y} the second number is even.")
else:
    print(f"{y}  the second number is odd.")

if is_prime(y):
    print(f"{y}  the second number is prime.")
else:
    print(f"{y}  the second number is composite.")

if is_even(z):
    print(f"{z} the third number is even.")
else:
    print(f"{z}  the third number is odd.")

if is_prime(z):
    print(f"{z} the third number is prime.")
else:
    print(f"{z}  the third number is composite.")


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_coprime_numbers(num):
    coprimes = []
    for i in range(1, num):
        if gcd(num, i) == 1:
            coprimes.append(i)
    return coprimes


def print_coprimes(co_primes, variable):
    if max(co_primes) >= 100:
        print(f"The entered number for {variable} is greater than 100.")
        pass
    else:
        print(f"The coprime numbers for {variable} are:")
        print(co_primes)


coprimes_x = get_coprime_numbers(x)
coprimes_y = get_coprime_numbers(y)
coprimes_z = get_coprime_numbers(z)

print_coprimes(coprimes_x, "the coprime numbers for the first number are")
print_coprimes(coprimes_y, "the coprime numbers for the second number are")
print_coprimes(coprimes_z, "the coprime numbers for the third number are")


def calculate_lcm(num_1, num_2, num_3):
    max_num = max(x, y, z)

    while True:
        if max_num % x == 0 and max_num % y == 0 and max_num % z == 0:
            lcm = max_num
            break
        max_num += 1
    return lcm


def calculate_hcf(x, y, z):
    min_num = min(x, y, z)

    while True:
        if x % min_num == 0 and y % min_num == 0 and z % min_num == 0:
            hcf = min_num
            break
        min_num -= 1
    return hcf


lcm = calculate_lcm(x, y, z)
hcf = calculate_hcf(x, y, z)

print(f"The LCM of {x}, {y}, and {z} is {lcm}")
print(f"The HCF of {x}, {y}, and {z} is {hcf}")

while True:
    try:
        r = int(input("Enter a number you want to use it as your angle: "))
        break
    except ValueError:
        print("Enter a valid number:")
        r = int(input("Enter a number in degrees:"))

e = r * ((math.pi) / 180)
try:
    print(round(math.sin(e), 3), ", the answer of sin")
except ValueError:
    print("The value of sin for this value is  not right ")

try:
    print(round(math.cos(e), 3), ", the answer of cos")
except ValueError:
    print("The value of cos for this value is  not right ")

try:
    print(round(math.tan(e), 3), ", the answer of tan")
except ValueError:
    print("The value of tan for this value is  not right ")

print(round(math.log(r), 3), ", the answer of natural logarithm")
print(round(math.log10(r), 3), ", the answer of logarithm with the base of 10")


w = input(
    "Do you want to continue with the old values you entered: "
    + str(x)
    + ", "
    + str(y)
    + ", "
    + str(z)
    + ", "
    + str(r)
    + ":"
)
if w in ("yes", "Yes"):
    print("Ok")
    try:
        print(round(math.asin(e), 3), ", the answer of arcsin in radians")
        print(round(math.acos(e), 3), ", the answer of arccos in radians")
        print(round(math.atan(e), 3), ", the answer of arctan in radians")
    except ValueError:
        print("The entered value is out of range ")

    print(round(math.sinh(e), 3), ", the answer of sinh")
    print(round(math.cosh(e), 3), ", the answer of cosh")
    print(round(math.tanh(e), 3), ", the answer of tanh")
    print(round(1 / math.sinh(e), 3), ", the answer of sinh")
    print(round(1 / math.cosh(e), 3), ", the answer of cosh")
    print(round(1 / math.tanh(e), 3), ", the answer of tanh")

else:
    try:
        print("Ok, enter them again so we can continue")
        x = int(input("Enter the first number: "))
        y = int(input("Enter your second number: "))
        z = int(input("Enter your third number: "))
        h = int(input("Enter the number in degree:"))
    except (ValueError, TypeError, ZeroDivisionError):
        print("You entered a invalid number")
        x = int(input("Enter the first number: "))
        y = int(input("Enter your second number: "))
        z = int(input("Enter your third number: "))
        h = int(input("Enter the number in degree:"))

    if type(x) is str or type(y) is str or type(z) is str or type(h) is str:
        print("You entered a invalid number please enter them again")
        x = int(input("Enter the first number: "))
        y = int(input("Enter your second number: "))
        z = int(input("Enter your third number: "))
        h = int(input("Enter the number in degree:"))

    else:
        pass

    try:
        print(round(math.asin(h), 3), ", the answer of arcsin in radians")
        print(round(math.acos(h), 3), ", the answer of arccos in radians")
        print(round(math.atan(h), 3), ", the answer of arctan in radians")
    except ValueError:
        print("The entered value is out of range ")

    print(round(math.sinh(h), 3), ", the answer of sinh")
    print(round(math.cosh(h), 3), ", the answer of cosh")
    print(round(math.tanh(h), 3), ", the answer of tanh")
    print(round(1 / math.sinh(h), 3), ", the answer of sinh")
    print(round(1 / math.cosh(h), 3), ", the answer of cosh")
    print(round(1 / math.tanh(h), 3), ", the answer of tanh")


while True:
    try:
        g = input("Do you want to enter a function, graph, or both: ")
        if g.lower() not in ["function", "graph", "both"]:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid option.")

if g.lower() == "graph" or g.lower() == "both":
    equation = input("Enter an equation using 'x' variable for graph: ")
    try:
        x_values = input("Enter x-values (comma-separated): ")
        x_values = [float(x) for x in x_values.split(",")]
        y_values = [
            ast.literal_eval(equation, {"math": math, "x": x}) for x in x_values
        ]
        plt.plot(x_values, y_values, color="red")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Graph of " + equation)
        plt.scatter(x_values, y_values, color="red")
        plt.show()
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        print("Invalid equation or input. Please try again.")

if g.lower() == "function" or g.lower() == "both":
    p = input("Enter a function: ")
    try:
        x_values = input("Enter values of x for the function (comma-separated): ")
        x_values = [float(x) for x in x_values.split(",")]
        x = symbols("x")
        y_values = [
            ast.literal_eval(p, {"math": math, "x": x, "sin": math.sin})
            for x in x_values
        ]
        plt.plot(x_values, y_values, color="blue")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Graph of function " + p)
        plt.scatter(x_values, y_values, color="blue")
        plt.show()

        eval_x = float(input("Enter the value of x to evaluate the function at: "))
        eval_result = ast.literal_eval(p, {"math": math, "x": eval_x, "sin": math.sin})
        print(f"The value of the function at x = {eval_x} is: {eval_result}")
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        print("Invalid function or input. Please try again.")

    print("Now we will do the differentiation and integration")

    def differentiate_equation(equation, x):
        x = sympy.Symbol("x")
        derivative_equation = sympy.diff(equation, x)
        return derivative_equation

    def integrate_equation(equation, var, lower, upper):
        integrated_equation = sympy.integrate(equation, var)
        result = integrated_equation.subs(var, upper) - integrated_equation.subs(
            var, lower
        )
        return integrated_equation, result

    var = sympy.Symbol("x")

    x = float(input("Enter the value of x for differentiation : "))
    derivative_equation = differentiate_equation(p, var)
    result = derivative_equation.subs(var, x)
    print(f"The derivative of {p} with respect to x is {derivative_equation}")
    print(f"The derivative of {p} at x={x} is {result}")

    print("Now integration")

    lower = float(input("Enter the lower limit : "))
    upper = float(input("Enter the upper limit: "))
    integrated_equation, result = integrate_equation(p, var, lower, upper)
    print(f"The integral of {p} with respect to x is {integrated_equation}")
    print(f"The integral of {p} from {lower} to {upper} is {result}")
