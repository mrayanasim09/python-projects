"""
Tests for Calculator/sudoku.py — SudokuSolver class.
"""

from __future__ import annotations

import pytest

from Calculator.sudoku import SudokuSolver

# ---------------------------------------------------------------------------
# Known valid puzzle and its solution
# ---------------------------------------------------------------------------

_VALID_BOARD = [
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

_SOLVED_BOARD = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9],
]

# A puzzle with no valid solution
_UNSOLVABLE_BOARD = [
    [5, 5, 0, 0, 7, 0, 0, 0, 0],  # two 5s in row 0 — invalid, no solution
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


# ---------------------------------------------------------------------------
# Valid puzzle tests
# ---------------------------------------------------------------------------


class TestSudokuSolverValid:
    def test_solve_returns_true_for_valid_puzzle(self):
        solver = SudokuSolver(_VALID_BOARD)
        assert solver.solve() is True

    def test_solved_board_matches_known_solution(self):
        solver = SudokuSolver(_VALID_BOARD)
        solver.solve()
        assert solver.get_board() == _SOLVED_BOARD

    def test_get_board_returns_deep_copy(self):
        solver = SudokuSolver(_VALID_BOARD)
        solver.solve()
        board = solver.get_board()
        board[0][0] = 99  # mutate returned copy
        # Original board inside solver must be unchanged
        assert solver.get_board()[0][0] != 99

    def test_is_valid_placement_detects_conflict(self):
        solver = SudokuSolver(_VALID_BOARD)
        # Row 0 already has a 3 in col 0
        assert solver.is_valid_placement(0, 1, 3) is False  # 3 already in row 0

    def test_is_valid_placement_allows_valid_number(self):
        solver = SudokuSolver(_VALID_BOARD)
        # Cell (0,1) is 0 — placing 1 should be valid
        assert solver.is_valid_placement(0, 1, 1) is True


# ---------------------------------------------------------------------------
# Unsolvable puzzle
# ---------------------------------------------------------------------------


class TestSudokuSolverUnsolvable:
    def test_solve_returns_false_for_unsolvable(self):
        # The board has duplicate 5s in row 0 → validation should catch it
        with pytest.raises(ValueError, match="Duplicate"):
            SudokuSolver(_UNSOLVABLE_BOARD)


# ---------------------------------------------------------------------------
# Validation tests
# ---------------------------------------------------------------------------


class TestSudokuSolverValidation:
    def test_raises_on_wrong_row_count(self):
        bad_board = [[0] * 9 for _ in range(8)]  # 8 rows instead of 9
        with pytest.raises(ValueError, match="9×9"):
            SudokuSolver(bad_board)

    def test_raises_on_wrong_column_count(self):
        bad_board = [[0] * 8 for _ in range(9)]  # 9 rows, 8 cols
        with pytest.raises(ValueError, match="9×9"):
            SudokuSolver(bad_board)

    def test_raises_on_out_of_range_value(self):
        bad_board = [row[:] for row in _VALID_BOARD]
        bad_board[0][0] = 10  # 10 is out of range
        with pytest.raises(ValueError, match="0–9"):
            SudokuSolver(bad_board)

    def test_raises_on_duplicate_in_column(self):
        bad_board = [row[:] for row in _VALID_BOARD]
        bad_board[1][0] = 3  # col 0 already has 3 at row 0
        with pytest.raises(ValueError, match="Duplicate"):
            SudokuSolver(bad_board)
