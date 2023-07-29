# This code is made by MRayan Asim
tallies = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    # add more numerals if necessary
}


def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum


# Get user input
roman_numeral = input("Enter a Roman numeral: ")

# Convert to decimal
decimal_numeral = RomanNumeralToDecimal(roman_numeral)

# Print the result
print("Decimal equivalent:", decimal_numeral)
