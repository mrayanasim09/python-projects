# This code is made by MRayan Asim
import string

sentence = input("Enter the text: ")


def count_letters_in_sentence(sentence):
    # Remove any punctuation marks and split the sentence into words
    words = sentence.replace(",", "").replace(".", "").split()

    # Initialize the letter count
    count = 0

    # Iterate over each word and count the letters
    for word in words:
        count += len(word)

    # Return the total count of letters
    return count


# Printing original string
print("The original string is: " + sentence)

# Using sum() + strip() + split() function
res = sum([i.strip(string.punctuation).isalpha() for i in sentence.split()])

# Number of words
letter_count = count_letters_in_sentence(sentence)
print("Number of letters:", letter_count)
print("The number of words in the string is:", str(res))
