# This code is made by MRayan Asim
import random

print("this rock paper scissors game is made by MRayan Asim hope you will like this!😊")


def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    else:
        return "computer"


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Let's play 5 games.")

    for game in range(1, 6):
        print(f"\nGame {game}:")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player_choice = int(input("Enter your choice (1-3): ")) - 1

        if player_choice < 0 or player_choice > 2:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.randint(0, 2)

        print("Player's move:", choices[player_choice])
        print("Computer's move:", choices[computer_choice])

        result = play_game(choices[player_choice], choices[computer_choice])

        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("Player score:", player_score)
        print("Computer score:", computer_score)

    print("\nGame over!")
    print("Total scores:")
    print("Player score:", player_score)
    print("Computer score:", computer_score)


rock_paper_scissors()
