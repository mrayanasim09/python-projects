# This code is made by MRayan Asim
# Packages needed:
# pip install bcrypt
import hashlib
import warnings

import bcrypt

print("************** PASSWORD CRACKER ******************")

pass_found = False
input_hash = input("Enter the hashed password: ")

pass_doc = input("Enter path to wordlist file (e.g., rockyou.txt): ")  # nosec B105

# Determine hash type and use appropriate algorithm
if len(input_hash) == 32:  # MD5 length
    warnings.warn(
        "MD5 is cryptographically broken and insecure. "
        "This tool can only attempt to crack MD5 hashes for educational purposes.",
        UserWarning,
    )
    try:
        with open(pass_doc, errors="ignore") as pass_file:
            for word in pass_file:
                word = word.strip()
                # Using MD5 only for cracking existing MD5 hashes (educational)
                hash_word = hashlib.md5(word.encode()).hexdigest()  # nosec B324

                if hash_word == input_hash:
                    print("Password found. The password is:", word)
                    pass_found = True
                    break

    except FileNotFoundError:
        print("Error: " + pass_doc + " is not found. Please provide the correct file path.")
        quit()

    if not pass_found:
        print("Password is not found in the", pass_doc, "file")

elif input_hash.startswith("$2b$") or input_hash.startswith("$2a$"):  # bcrypt
    try:
        with open(pass_doc, errors="ignore") as pass_file:
            for word in pass_file:
                word = word.strip()
                if bcrypt.checkpw(word.encode(), input_hash.encode()):
                    print("Password found. The password is:", word)
                    pass_found = True
                    break
    except FileNotFoundError:
        print("Error: " + pass_doc + " is not found. Please provide the correct file path.")
        quit()
    except Exception as e:
        print(f"Error checking password: {e}")
        quit()

    if not pass_found:
        print("Password is not found in the", pass_doc, "file")
else:
    print("Unsupported hash format. This tool supports MD5 (educational) and bcrypt.")
    quit()

print("\n***************** Thank you **********************")
