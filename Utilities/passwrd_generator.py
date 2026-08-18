# This code is made by MRayan Asim
# Packages needed: none (uses stdlib only)
import secrets

CHARSET = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = int(input("Enter the length of password: "))
password = "".join(secrets.choice(CHARSET) for _ in range(passlen))
print(password)
