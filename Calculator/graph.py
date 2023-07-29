# This is made by MRayan Asim
# packages needed:
# pip install numpy
# pip install  matplotlib.pyplot
import ast
import matplotlib.pyplot as plt
import numpy as np

print("Hello! This program of graph is made by MRayan Asim. Hope you will like this! 😊")

equation = input("Enter an equation using 'x' variable: ")
print("Your Equation:", equation)


t = input("Are you satisfied with this equation? (yes/no) ")
while t.lower() == "no":
    print("OK, enter it again:")
    equation = input("Enter the equation again: ")
    print("Equation:", equation)
    t = input("Are you satisfied with this equation? (yes/no) ")

x_start = float(input("Enter the starting value of x of which you make the graph of: "))
x_end = float(input("Enter the ending value of x of which you make the graph of: "))

x_values = np.linspace(x_start, x_end, num=100)
y_values = [ast.literal_eval(equation) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of " + equation)
plt.scatter(x_values, y_values, color="red")
plt.show()
