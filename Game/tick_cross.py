# This code is made by MRayan Asim
import random
import time


def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells


def make_human_move(board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if row in range(3) and col in range(3) and board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("Invalid move. Try again.")


def make_computer_move(board, difficulty):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        if difficulty == "easy":
            row, col = random.choice(empty_cells)
        elif difficulty == "medium":
            # Check for winning moves
            for cell in empty_cells:
                temp_board = [
                    row[:] for row in board
                ]  # Create a temporary board for simulation
                temp_board[cell[0]][cell[1]] = "O"
                if check_winner(temp_board) == "O":
                    row, col = cell
                    break
            else:
                # Check for blocking moves
                for cell in empty_cells:
                    temp_board = [
                        row[:] for row in board
                    ]  # Create a temporary board for simulation
                    temp_board[cell[0]][cell[1]] = "X"
                    if check_winner(temp_board) == "X":
                        row, col = cell
                        break
                else:
                    row, col = random.choice(empty_cells)
        else:
            # Choose the best move using a more advanced algorithm (e.g., Minimax)
            # Implementation of Minimax is beyond the scope of this example
            row, col = random.choice(empty_cells)

        time.sleep(1)  # Add a delay of 1 second before computer's move
        board[row][col] = "✓"  # Use tick symbol instead of "O"


def play_again():
    response = input("Do you want to play again? (yes/no): ")
    return response.lower() == "yes"


def select_difficulty():
    while True:
        difficulty = input("Select difficulty level (easy/medium/hard): ")
        if difficulty.lower() in ["easy", "medium", "hard"]:
            return difficulty.lower()
        else:
            print("Invalid difficulty level. Try again.")


def play_game():
    while True:
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        current_player = "X"
        winner = None

        difficulty = select_difficulty()

        while not winner and get_empty_cells(board):
            print_board(board)
            if current_player == "X":
                make_human_move(board)
            else:
                make_computer_move(board, difficulty)

            winner = check_winner(board)
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        print_board(board)
        if winner:
            if winner == "X":
                print("You win!")
            else:
                print("Computer wins!")
        else:
            print("It's a tie!")

        if not play_again():
            break


play_game()
