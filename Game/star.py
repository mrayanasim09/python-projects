# This code is made by MRayan Asim
import time

print(
    "Hello! This program of star pattern generating  is made by MRayan Asim. Hope you will like this! 😊"
)
time.sleep(3)


# Right Triangle
def print_right_triangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end="")
        print()


# Inverted Right Triangle
def print_inverted_right_triangle(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


# Pyramid
def print_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print("*" * (2 * i + 1))


# Diamond
def print_diamond(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print("*" * (2 * i + 1))

    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1), end="")
        print("*" * (2 * i + 1))


# Butterfly
def print_butterfly(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end="")
        for j in range(2 * (rows - i - 1)):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()

    for i in range(rows - 1, -1, -1):
        for j in range(i + 1):
            print("*", end="")
        for j in range(2 * (rows - i - 1)):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()


# Hollow Square
def print_hollow_square(rows):
    for i in range(rows):
        if i in (0, rows - 1):
            print("*" * rows)
        else:
            print("*" + " " * (rows - 2) + "*")


# Hourglass
def print_hourglass(rows):
    for i in range(rows):
        print(" " * i, end="")
        print("*" * (2 * (rows - i) - 1))
    for i in range(rows - 2, -1, -1):
        print(" " * i, end="")
        print("*" * (2 * (rows - i) - 1))


# Get user input for number of rows
num_rows = int(input("Enter the number of rows: "))

print("Right Triangle:")
print_right_triangle(num_rows)
print()

print("Inverted Right Triangle:")
print_inverted_right_triangle(num_rows)
print()

print("Pyramid:")
print_pyramid(num_rows)
print()

print("Diamond:")
print_diamond(num_rows)
print()

print("Butterfly:")
print_butterfly(num_rows)
print()

print("Hollow Square:")
print_hollow_square(num_rows)
print()

print("Hourglass:")
print_hourglass(num_rows)
print()
