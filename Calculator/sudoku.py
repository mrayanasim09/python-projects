# This code is made by MRayan Asim
# Sudoku Solver — backtracking algorithm with an importable SudokuSolver class.
#
# Usage (CLI):
#   python sudoku.py                          # solves the built-in demo board
#   python sudoku.py --board "3,0,6,..."      # comma-separated 81 values, row-major

from __future__ import annotations

import argparse
import time

GRID_SIZE = 9
BOX_SIZE = 3


class SudokuSolver:
    """Backtracking Sudoku solver with board validation."""

    def __init__(self, board: list[list[int]]) -> None:
        """
        Initialise the solver with a 9×9 board.

        Args:
            board: A 9×9 list-of-lists with integers 0–9.
                   0 represents an empty cell.

        Raises:
            ValueError: If the board dimensions are wrong, values are out of range,
                        or the initial clues already contain duplicates.
        """
        self._validate(board)
        self._board: list[list[int]] = [row[:] for row in board]  # deep copy

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def solve(self) -> bool:
        """
        Solve the puzzle in-place using backtracking.

        Returns:
            True  if a solution was found (board is now fully filled).
            False if no solution exists (board is unchanged).
        """
        return self._backtrack(0, 0)

    def is_valid_placement(self, row: int, col: int, num: int) -> bool:
        """Return True if placing *num* at (row, col) respects Sudoku rules."""
        return self._is_safe(self._board, row, col, num)

    def get_board(self) -> list[list[int]]:
        """Return a deep copy of the current board state."""
        return [row[:] for row in self._board]

    def print_board(self) -> None:
        """Pretty-print the board to stdout."""
        for i, row in enumerate(self._board):
            if i > 0 and i % BOX_SIZE == 0:
                print("-" * (GRID_SIZE * 2 + 2))
            row_str = ""
            for j, val in enumerate(row):
                if j > 0 and j % BOX_SIZE == 0:
                    row_str += "| "
                row_str += f"{val} "
            print(row_str)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _backtrack(self, row: int, col: int) -> bool:
        """Recursive backtracking solver."""
        if row == GRID_SIZE - 1 and col == GRID_SIZE:
            return True
        if col == GRID_SIZE:
            row += 1
            col = 0
        if self._board[row][col] > 0:
            return self._backtrack(row, col + 1)
        for num in range(1, GRID_SIZE + 1):
            if self._is_safe(self._board, row, col, num):
                self._board[row][col] = num
                if self._backtrack(row, col + 1):
                    return True
                self._board[row][col] = 0
        return False

    @staticmethod
    def _is_safe(grid: list[list[int]], row: int, col: int, num: int) -> bool:
        """Check row, column, and 3×3 box constraints."""
        if any(grid[row][x] == num for x in range(GRID_SIZE)):
            return False
        if any(grid[x][col] == num for x in range(GRID_SIZE)):
            return False
        start_row = row - row % BOX_SIZE
        start_col = col - col % BOX_SIZE
        for i in range(BOX_SIZE):
            for j in range(BOX_SIZE):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    @staticmethod
    def _validate(board: list[list[int]]) -> None:
        """Raise ValueError if the board is structurally invalid."""
        if len(board) != GRID_SIZE or any(len(row) != GRID_SIZE for row in board):
            raise ValueError(f"Board must be {GRID_SIZE}×{GRID_SIZE}, got {len(board)} rows.")
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if not isinstance(val, int) or not (0 <= val <= 9):
                    raise ValueError(
                        f"Board values must be integers 0–9; got {val!r} at ({r},{c})."
                    )

        # Check for duplicate clues in rows, columns, and boxes
        for i in range(GRID_SIZE):
            row_vals = [v for v in board[i] if v != 0]
            if len(row_vals) != len(set(row_vals)):
                raise ValueError(f"Duplicate values in row {i}.")
            col_vals = [board[r][i] for r in range(GRID_SIZE) if board[r][i] != 0]
            if len(col_vals) != len(set(col_vals)):
                raise ValueError(f"Duplicate values in column {i}.")

        for box_row in range(BOX_SIZE):
            for box_col in range(BOX_SIZE):
                box_vals = [
                    board[box_row * BOX_SIZE + r][box_col * BOX_SIZE + c]
                    for r in range(BOX_SIZE)
                    for c in range(BOX_SIZE)
                    if board[box_row * BOX_SIZE + r][box_col * BOX_SIZE + c] != 0
                ]
                if len(box_vals) != len(set(box_vals)):
                    raise ValueError(f"Duplicate values in 3×3 box at ({box_row},{box_col}).")


# ---------------------------------------------------------------------------
# Demo board & CLI entry point
# ---------------------------------------------------------------------------

_DEMO_BOARD: list[list[int]] = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sudoku Solver by MRayan Asim")
    parser.add_argument(
        "--board",
        type=str,
        default=None,
        help=(
            "81 comma-separated integers (0 = empty), row-major order. "
            "If omitted, the built-in demo puzzle is used."
        ),
    )
    return parser.parse_args()


def _board_from_string(raw: str) -> list[list[int]]:
    vals = [int(v.strip()) for v in raw.split(",")]
    if len(vals) != GRID_SIZE * GRID_SIZE:
        raise ValueError(f"Expected 81 values, got {len(vals)}.")
    return [vals[i * GRID_SIZE : (i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]


def main() -> None:
    print("Sudoku Solver by MRayan Asim 😊")
    time.sleep(1)

    args = _parse_args()
    board = _board_from_string(args.board) if args.board else _DEMO_BOARD

    try:
        solver = SudokuSolver(board)
    except ValueError as exc:
        print(f"Invalid board: {exc}")
        return

    print("\nInitial board:")
    solver.print_board()

    if solver.solve():
        print("\nSolved board:")
        solver.print_board()
    else:
        print("\nNo solution exists for this puzzle.")


if __name__ == "__main__":
    main()
