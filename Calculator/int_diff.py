# This is made by MRayan Asim
# Packages needed:
# pip install sympy
import sympy


def differentiate_equation(equation, x):
    x = sympy.Symbol("x")
    derivative_equation = sympy.diff(equation, x)
    return derivative_equation


def integrate_equation(equation, var, lower, upper):
    integrated_equation = sympy.integrate(equation, var)
    result = integrated_equation.subs(var, upper) - integrated_equation.subs(var, lower)
    return integrated_equation, result


equation = input("Enter a mathematical expression: ")
var = sympy.Symbol("x")

choice = input("Enter 'd' to differentiate, or 'i' to integrate: ")

if choice == "d":
    x = float(input("Enter the value of x: "))
    derivative_equation = differentiate_equation(equation, var)
    result = derivative_equation.subs(var, x)
    print(f"The derivative of {equation} with respect to x is {derivative_equation}")
    print(f"The derivative of {equation} at x={x} is {result}")

elif choice == "i":
    lower = float(input("Enter the lower limit: "))
    upper = float(input("Enter the upper limit: "))
    integrated_equation, result = integrate_equation(equation, var, lower, upper)
    print(f"The integral of {equation} with respect to x is {integrated_equation}")
    print(f"The integral of {equation} from {lower} to {upper} is {result}")

else:
    print("Invalid choice. Please enter 'd' or 'i'.")
