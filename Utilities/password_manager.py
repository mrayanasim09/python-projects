# This code is made by MRayan Asim
# Packages needed:
# pip install cryptography
# Tou use to follow the 3 steps:
# 1-When you run this code it will ask for the master key you can find the key in the master_password.txt which will create when you run the code
# 2-copy and enter the key and add password with the website name then username or email and at last enter the password
# 3- the password would save in passwrods.json they will be coded so to decode go to get passwords option on the code for this you need to remember the name of the website you want to get the password
print(
    """
1-When you run this code it will ask for the master key you can find the key in the master_password.txt which will create when you run the code
2-copy and enter the key and add password with the website name then username or email and at last enter the password 
3- the password would save in passwrods.json they will be coded so to decode go to get passwords option on the code for this you need to remember the name of the website you want to get the password 
"""
)
import json
import os
import getpass
from cryptography.fernet import Fernet

PASSWORD_FILE = "passwords.json"
MASTER_PASSWORD_FILE = "master_password.txt"


def generate_key():
    return Fernet.generate_key()


def load_key():
    try:
        with open(MASTER_PASSWORD_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None


def save_key(key):
    with open(MASTER_PASSWORD_FILE, "wb") as f:
        f.write(key)


def encrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())


def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()


def load_passwords(key):
    try:
        with open(PASSWORD_FILE, "rb") as f:
            encrypted_data = f.read()
            decrypted_data = decrypt_data(encrypted_data, key)
            return json.loads(decrypted_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_passwords(passwords, key):
    with open(PASSWORD_FILE, "wb") as f:
        data = json.dumps(passwords, indent=4)
        encrypted_data = encrypt_data(data, key)
        f.write(encrypted_data)


def create_passwords_file():
    initial_passwords = {}
    with open(PASSWORD_FILE, "w") as f:
        json.dump(initial_passwords, f, indent=4)
    print(f"Created '{PASSWORD_FILE}' with initial content.")


def create_master_password_file(master_password):
    with open(MASTER_PASSWORD_FILE, "w") as f:
        f.write(master_password)
    print(f"Created '{MASTER_PASSWORD_FILE}' with the master password.")


def add_password(passwords, key):
    website = input("Enter website name: ")
    username = input("Enter username/email: ")
    password = getpass.getpass("Enter password: ")

    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords, key)
    print("Password added successfully!")


def get_password(passwords):
    website = input("Enter website name: ")

    if website in passwords:
        print(f"Website: {website}")
        print(f"Username/Email: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("Password not found for the given website.")


def delete_password(passwords, key):
    website = input("Enter website name: ")

    if website in passwords:
        del passwords[website]
        save_passwords(passwords, key)
        print("Password deleted successfully!")
    else:
        print("Password not found for the given website.")


def get_master_password():
    master_password = getpass.getpass("Enter master password: ")
    return master_password.encode()


def main():
    key = load_key()
    if key is None:
        key = generate_key()
        save_key(key)

    master_password = get_master_password()
    if master_password != key:
        print("Master password is incorrect. Exiting...")
        return

    passwords = load_passwords(key)
    if not os.path.exists(PASSWORD_FILE):
        create_passwords_file()

    if not os.path.exists(MASTER_PASSWORD_FILE):
        create_master_password_file(master_password.decode())

    while True:
        print("\nMenu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_password(passwords, key)
        elif choice == "2":
            get_password(passwords)
        elif choice == "3":
            delete_password(passwords, key)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
