# This code is made by MRayan Asim
# Packages needed:
# pip install bcrypt hashlib
# Python 3 code to demonstrate password hashing
# NOTE: MD5 is insecure for passwords. This script now uses bcrypt by default.

import hashlib
import warnings

import bcrypt

print("************** PASSWORD HASHING TOOL ******************")
print("Note: MD5 is INSECURE for passwords. Using bcrypt (recommended).")
print("For educational MD5 demonstration, use --md5 flag (not recommended)")
print("-------------------------------------------------------")

str2hash = input("Enter password to hash: ")

# Check if user wants MD5 (for educational purposes only)
use_md5 = input("Use MD5 (insecure)? (y/n): ").lower() == "y"

if use_md5:
    warnings.warn(
        "MD5 is cryptographically broken and should NOT be used for password hashing. "
        "Use bcrypt instead. This is for educational purposes only.",
        UserWarning,
    )
    # Using MD5 only for educational demonstration
    result = hashlib.md5(str2hash.encode())  # nosec B324
    print("The hexadecimal equivalent of MD5 hash is: ", end="")
    print(result.hexdigest())
    print("\nWARNING: This MD5 hash is INSECURE and can be cracked easily!")
else:
    # Use bcrypt (secure)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(str2hash.encode(), salt)
    print("The bcrypt hash is: ", end="")
    print(hashed.decode())
    print("\nThis is a secure hash. Store this in your database.")

    # Demonstrate verification
    print("\nTo verify a password against this hash, use:")
    print("bcrypt.checkpw(password.encode(), hashed_password.encode())")

print("\n***************** Thank you **********************")
