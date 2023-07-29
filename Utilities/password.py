# This code is made by MRayan Asim
# Packages needed:
# pip install hashlib
import hashlib

print("************** PASSWORD CRACKER ******************")

pass_found = False
input_hash = input("Enter the hashed password: ")

pass_doc = r""  # path of rockyou.txt file

try:
    with open(pass_doc, "r", errors="ignore") as pass_file:
        for word in pass_file:
            word = word.strip()
            hash_word = hashlib.md5(word.encode()).hexdigest()

            if hash_word == input_hash:
                print("Password found. The password is:", word)
                pass_found = True
                break

except FileNotFoundError:
    print("Error: " + pass_doc + " is not found. Please provide the correct file path.")
    quit()

if not pass_found:
    print("Password is not found in the", pass_doc, "file")

print("\n***************** Thank you **********************")
