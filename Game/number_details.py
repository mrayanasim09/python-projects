# This code is made by MRayan Asim
import time

print(
    "Hello this number checker program is made by MRayan Asim hope you will like it 😊"
)
time.sleep(5)


def gcd(a, b):
    # Compute the greatest common divisor (GCD) of two numbers
    while b != 0:
        a, b = b, a % b
    return a


def find_coprimes(num):
    coprimes = []
    for i in range(2, num):
        if gcd(num, i) == 1:
            coprimes.append(i)
    return coprimes


while True:
    try:
        num = int(input("Enter the number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Check if the number is odd or even
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

# Define a flag variable
flag = False

if num < 2:
    print(num, "is not a prime number")
else:
    # Check for factors
    factors = []
    for i in range(2, num):
        if num % i == 0:
            # If factor is found, set flag to True
            flag = True
            factors.append(i)

    # Check if flag is True
    if flag:
        print(num, "is not a prime number")
        print("Factors:", factors)
        coprimes = find_coprimes(num)
        if coprimes:
            print("Co-prime numbers:", coprimes)
        else:
            print("There are no co-prime numbers.")
    else:
        print(num, "is a prime number")
