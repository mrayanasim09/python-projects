def decimal_to_binary(decimal):
    return bin(decimal)[2:]


def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]


def decimal_to_octal(decimal):
    return oct(decimal)[2:]


def binary_to_decimal(binary):
    return int(binary, 2)


def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)


def octal_to_decimal(octal):
    return int(octal, 8)


def calculator():
    print("Welcome to the number conversion calculator!")
    print("Choose the number type:")
    print("1. Binary")
    print("2. Decimal")
    print("3. Hexadecimal")
    print("4. Octal")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        print("Decimal:", decimal)
        print("Hexadecimal:", decimal_to_hexadecimal(decimal))
        print("Octal:", decimal_to_octal(decimal))
    elif choice == 2:
        decimal = int(input("Enter a decimal number: "))
        print("Binary:", decimal_to_binary(decimal))
        print("Hexadecimal:", decimal_to_hexadecimal(decimal))
        print("Octal:", decimal_to_octal(decimal))
    elif choice == 3:
        hexadecimal = input("Enter a hexadecimal number: ")
        decimal = hexadecimal_to_decimal(hexadecimal)
        print("Binary:", decimal_to_binary(decimal))
        print("Decimal:", decimal)
        print("Octal:", decimal_to_octal(decimal))
    elif choice == 4:
        octal = input("Enter an octal number: ")
        decimal = octal_to_decimal(octal)
        print("Binary:", decimal_to_binary(decimal))
        print("Decimal:", decimal)
        print("Hexadecimal:", decimal_to_hexadecimal(decimal))
    else:
        print("Invalid choice. Please select a number type from 1 to 4.")


calculator()
