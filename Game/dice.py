# This code is made by MRayan Asim
import random
import time

print("hello this dice rolling game is made by MRayan Asim hope you will like this!😊")
time.sleep(3)


def roll_dice():
    dice_faces = [
        # Dice face 1
        """
        ----------
        |        |
        |   O    |
        |        |
        ----------
        """,
        # Dice face 2
        """
        ----------
        | O      |
        |        |
        |      O |
        ----------
        """,
        # Dice face 3
        """
        ----------
        | O      |
        |   O    |
        |      O |
        ----------
        """,
        # Dice face 4
        """
        ----------
        | O   O |
        |        |
        | O   O |
        ----------
        """,
        # Dice face 5
        """
        ----------
        | O   O |
        |   O    |
        | O   O |
        ----------
        """,
        # Dice face 6
        """
        ----------
        | O O O |
        |        |
        | O O O |
        ----------
        """,
    ]

    min_value = 1
    max_value = 6
    score = 0
    roll_again = True

    while roll_again:
        user_guess = int(input("Guess the number for dice (1-6): "))

        print("Rolling the dice...")
        time.sleep(1)  # Pause for 1 second to create rolling effect
        dice_value = random.randint(min_value, max_value)
        print(dice_faces[dice_value - 1])  # Display the corresponding dice face

        if user_guess == dice_value:
            print("Congratulations! You guessed it right.")
            score += 1
        else:
            print("Sorry, wrong guess.")

        print("Score:", score)

        roll_again_input = input("Roll the dice again? (y/n): ")
        roll_again = roll_again_input.lower() == "y"

    print("Final score:", score)
    print("Thank you for playing!")


roll_dice()
