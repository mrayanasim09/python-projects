# This is made by MRayan Asim
# packages needed:
# pip install matplotlib.pyplot
import matplotlib.pyplot as plt


def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        sequence = [0]
    elif n == 2:
        sequence = [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
    return sequence


print(
    "Hello! This program of Fibonacci series is made by MRayan Asim. Hope you will like this! 😊"
)

# Get user input
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fib_sequence = fibonacci_sequence(num_terms)

# Display the formula
print("Formula: F(n) = F(n-1) + F(n-2)")

# Display the result with commas
fib_str = ", ".join(str(num) for num in fib_sequence)
print("Fibonacci sequence:")
print(fib_str)

# Create the graph
plt.plot(range(1, num_terms + 1), fib_sequence, marker="o")
plt.xlabel("Number of Terms")
plt.ylabel("Fibonacci Term Value")
plt.title("Fibonacci Sequence")
plt.grid(True)
time.sleep(3)
plt.show()
