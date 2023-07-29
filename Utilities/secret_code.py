# This code is made by MRayan Asim
# Packages needed:
# pip install pygame
import random
import time


# Function to encode a word
def encode_word(word):
    encoded_word = "".join(random.sample(word, len(word)))
    return encoded_word


# Function to save a secret code and word pair
def save_secret_code(secret_word, secret_code):
    with open("secret_code.txt", "a") as file:
        file.write(secret_code + ":" + secret_word + "\n")


# Function to load secret codes and words from file
def load_secret_codes():
    secret_codes = {}
    with open("secret_code.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(":")
                if len(parts) == 2:
                    code, word = parts
                    secret_codes[code] = word
    return secret_codes


# Main program
print(
    "Hello! This secret code generator is made by MRayan Asim. Hope you will like it! 😊"
)
time.sleep(3)

# Ask the user for input
print("Choose an option:")
print("1. Encode a secret word")
print("2. Decode a secret code")

option = input("Enter the option number: ")

if option == "1":
    secret_word = input("Enter the secret word: ")
    secret_code = encode_word(secret_word)
    save_secret_code(secret_word, secret_code)
    print("The secret code is:", secret_code)
elif option == "2":
    secret_code = input("Enter the secret code to decode: ")
    secret_codes = load_secret_codes()
    decoded_word = secret_codes.get(secret_code, "Code not found")
    print("The decoded word is:", decoded_word)
else:
    print("Invalid option. Please enter a valid option number.")
