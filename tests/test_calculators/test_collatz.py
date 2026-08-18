"""
Tests for Calculator/conject.py — pure collatz_steps() function.
"""

from __future__ import annotations

import pytest

from Calculator.conject import collatz_steps


class TestCollatzSteps:
    def test_n_equals_1_is_zero_steps(self):
        """n=1 is already at 1 — 0 steps."""
        assert collatz_steps(1) == 0

    def test_n_equals_2(self):
        """2 → 1 (one step)."""
        assert collatz_steps(2) == 1

    def test_n_equals_6(self):
        """
        6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 = 8 steps.
        """
        assert collatz_steps(6) == 8

    def test_n_equals_27(self):
        """Well-known benchmark: n=27 takes 111 steps."""
        assert collatz_steps(27) == 111

    def test_large_even_input(self):
        """Powers of 2 collapse in exactly log2(n) steps."""
        assert collatz_steps(64) == 6  # 64→32→16→8→4→2→1

    def test_raises_on_zero(self):
        with pytest.raises(ValueError, match="positive"):
            collatz_steps(0)

    def test_raises_on_negative(self):
        with pytest.raises(ValueError, match="positive"):
            collatz_steps(-5)

    def test_return_type_is_int(self):
        assert isinstance(collatz_steps(10), int)
