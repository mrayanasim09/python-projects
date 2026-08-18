"""
Tests for Calculator/Mortgage.py — calculate_mortgage() and MortgageResult.
"""

from __future__ import annotations

import pytest

from Calculator.Mortgage import MortgageResult, calculate_mortgage


class TestCalculateMortgageValid:
    def test_standard_30_year_mortgage(self):
        """
        Classic 30-year, $200,000 loan at 6% annual rate.
        Known monthly payment ≈ $1,199.10.
        """
        result = calculate_mortgage(200_000, 6.0, 360)
        assert isinstance(result, MortgageResult)
        assert abs(result.monthly_payment - 1199.10) < 0.10

    def test_total_paid_equals_monthly_times_months(self):
        result = calculate_mortgage(100_000, 5.0, 120)
        assert abs(result.total_paid - result.monthly_payment * 120) < 0.01

    def test_total_interest_equals_total_minus_principal(self):
        result = calculate_mortgage(100_000, 5.0, 120)
        assert abs(result.total_interest - (result.total_paid - 100_000)) < 0.01

    def test_zero_interest_rate(self):
        """At 0% interest, monthly payment should equal principal / months."""
        result = calculate_mortgage(12_000, 0.0, 12)
        assert abs(result.monthly_payment - 1_000.0) < 0.01
        assert abs(result.total_interest) < 0.01

    def test_result_stores_inputs(self):
        result = calculate_mortgage(50_000, 3.5, 60)
        assert result.principal == 50_000
        assert result.annual_rate_pct == 3.5
        assert result.months == 60

    def test_result_is_immutable(self):
        result = calculate_mortgage(50_000, 3.5, 60)
        with pytest.raises((AttributeError, TypeError)):
            result.monthly_payment = 0  # type: ignore[misc]


class TestCalculateMortgageValidation:
    def test_raises_on_zero_principal(self):
        with pytest.raises(ValueError, match="principal"):
            calculate_mortgage(0, 5.0, 120)

    def test_raises_on_negative_principal(self):
        with pytest.raises(ValueError, match="principal"):
            calculate_mortgage(-10_000, 5.0, 120)

    def test_raises_on_negative_rate(self):
        with pytest.raises(ValueError, match="annual_rate_pct"):
            calculate_mortgage(100_000, -1.0, 120)

    def test_raises_on_zero_months(self):
        with pytest.raises(ValueError, match="months"):
            calculate_mortgage(100_000, 5.0, 0)

    def test_raises_on_negative_months(self):
        with pytest.raises(ValueError, match="months"):
            calculate_mortgage(100_000, 5.0, -12)
