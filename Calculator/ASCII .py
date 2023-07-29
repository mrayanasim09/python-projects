# This code is made by MRayan Asim
print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)
