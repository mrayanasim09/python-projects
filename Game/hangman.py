# This code is made by MRaynasim
import random
import time


def hangman():
    words = [
        "apple",
        "banana",
        "cherry",
        "orange",
        "strawberry",
        "watermelon",
        "pineapple",
        "kiwi",
        "mango",
        "pear",
        "grapefruit",
        "blueberry",
    ]
    word = random.choice(words)
    guessed_letters = []
    attempts = 5

    while attempts > 0:
        print("\nAttempts left:", attempts)
        hidden_word = ""

        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter + " "
            else:
                hidden_word += "_ "

        print(hidden_word)

        if hidden_word == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)


# Run the Hangman game
print("Hello! This Hangman game is made by MRayan Asim. Hope you will enjoy it! 😊")
time.sleep(3)
print("Let's play Hangman!")
hangman()
