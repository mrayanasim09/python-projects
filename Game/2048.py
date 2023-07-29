# This code is made by MRayan Asim
import random


def start_game():
    mat = [[0] * 4 for _ in range(4)]
    print("Commands are as follows:")
    print("'W' or 'w': Move Up")
    print("'S' or 's': Move Down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")
    add_new_2(mat)
    return mat


def add_new_2(mat):
    empty_cells = []
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells:
        i, j = random.choice(empty_cells)
        mat[i][j] = 2


def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return "GAME NOT OVER"
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return "GAME NOT OVER"
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return "GAME NOT OVER"
    return "LOST"


def compress(mat):
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed


def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append(mat[i][::-1])
    return new_mat


def transpose(mat):
    new_mat = [[mat[j][i] for j in range(4)] for i in range(4)]
    return new_mat


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid, changed


def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed


def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


if __name__ == "__main__":
    mat = start_game()

    while True:
        x = input("Press the command: ")

        if x.lower() in ["w", "s", "a", "d"]:
            if x.lower() == "w":
                mat, flag = move_up(mat)
            elif x.lower() == "s":
                mat, flag = move_down(mat)
            elif x.lower() == "a":
                mat, flag = move_left(mat)
            elif x.lower() == "d":
                mat, flag = move_right(mat)

            status = get_current_state(mat)
            print(status)

            if status != "GAME NOT OVER":
                break

            if flag:
                add_new_2(mat)
        else:
            print("Invalid Key Pressed")

        for row in mat:
            print(*row)
