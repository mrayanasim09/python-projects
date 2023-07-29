# This code is made by MRayan Asim
# Packages needed:
# pip install pygame
import random
import time

print("This master mind game is made by MRayan Asim hope you will like this! 😊")
time.sleep(3)


def play_game():
    # Generate a random 4-digit number
    num = random.randrange(1000, 10000)

    # Initialize variables
    high_score = get_high_score()
    tries = 0

    while True:
        try:
            # Get the user's guess
            n = int(input("Guess the 4-digit number: "))
            if not (1000 <= n <= 9999):
                raise ValueError
        except ValueError:
            print("Please enter a valid 4-digit number!")
            continue

        # Check if the guess is correct
        if n == num:
            tries += 1
            print("Great! You guessed the number in", tries, "tries!")
            if tries < high_score:
                print("Congratulations! You set a new high score!")
                save_high_score(tries)
            break

        # Count the correct digits
        count = 0
        n_str = str(n)
        num_str = str(num)
        correct = []

        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct.append(n_str[i])

        # Provide feedback to the user
        if count != 0:
            print("Not quite the number. But you did get", count, "digit(s) correct!")
            print("Also, these numbers in your input were correct:")
            print(*correct, sep=" ")
        else:
            print("None of the numbers in your input match.")

        # Increase the try count
        tries += 1

    print("Thank you for playing!")


def get_high_score():
    try:
        with open("highscore.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist, set the high score to a large value
        high_score = float("inf")
    except ValueError:
        # If the file contains invalid data, set the high score to a large value
        high_score = float("inf")

    return high_score


def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))


# Start the game
play_game()
