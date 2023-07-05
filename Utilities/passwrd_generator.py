#This code is made by MRayan Asim
#Packages needed:
#pip install num2words
import random
import string   
from num2words import num2words


print("Hello this password generator  program is made by MRayan Asim hope you will like it 😊")

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "weak"

    # Check if password contains uppercase, lowercase, digits, and special characters
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in string.punctuation for char in password)

    if has_uppercase and has_lowercase and has_digit and has_special_char:
        return "strong"
    else:
        return "weak"

def generate_strong_password(password):
    # Generate a strong password related to the entered password
    if password.isdigit():
        new_password = num2words(int(password))
    else:
        password_list = list(password)
        random.shuffle(password_list)
        new_password = ''.join(password_list)

    return new_password

def password_checker():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    
    if strength == "weak":
        print(" Generating a stronger password...")
        stronger_password = generate_strong_password(password)
        print("Stronger password:", stronger_password)
    else:
        print("Password is strong.")

password_checker()
