# This code is made by MRayan Asim
# Packages needed:
# pip install hashlib
# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

# initializing string
str2hash = input("")

# e
# then sending to md5()
result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())
