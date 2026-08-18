# This code is made by MRayan Asim
# Mortgage Calculator — amortisation formula with input validation.
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MortgageResult:
    """Immutable result of a mortgage calculation."""

    monthly_payment: float
    total_paid: float
    total_interest: float
    principal: float
    annual_rate_pct: float
    months: int

    def __str__(self) -> str:
        return (
            f"Loan amount:      ${self.principal:,.2f}\n"
            f"Annual rate:      {self.annual_rate_pct:.2f}%\n"
            f"Term:             {self.months} months "
            f"({self.months / 12:.1f} years)\n"
            f"Monthly payment:  ${self.monthly_payment:,.2f}\n"
            f"Total paid:       ${self.total_paid:,.2f}\n"
            f"Total interest:   ${self.total_interest:,.2f}"
        )


def calculate_mortgage(
    principal: float,
    annual_rate_pct: float,
    months: int,
) -> MortgageResult:
    """
    Calculate fixed-rate mortgage payments using the standard amortisation formula.

    Args:
        principal:        Loan amount in dollars (must be > 0).
        annual_rate_pct:  Annual interest rate as a percentage, e.g. 5.0 for 5%
                          (must be >= 0).
        months:           Loan term in months (must be > 0).

    Returns:
        A MortgageResult dataclass with monthly_payment, total_paid, and
        total_interest fields.

    Raises:
        ValueError: If any argument fails validation.
    """
    if principal <= 0:
        raise ValueError(f"principal must be positive, got {principal!r}")
    if annual_rate_pct < 0:
        raise ValueError(f"annual_rate_pct must be non-negative, got {annual_rate_pct!r}")
    if months <= 0:
        raise ValueError(f"months must be a positive integer, got {months!r}")

    monthly_rate = annual_rate_pct / (12 * 100)

    if monthly_rate == 0:
        # Zero-interest loan: principal divided equally over the term
        monthly_payment = principal / months
    else:
        monthly_payment = (
            principal
            * (monthly_rate * (1 + monthly_rate) ** months)
            / ((1 + monthly_rate) ** months - 1)
        )

    total_paid = monthly_payment * months
    total_interest = total_paid - principal

    return MortgageResult(
        monthly_payment=monthly_payment,
        total_paid=total_paid,
        total_interest=total_interest,
        principal=principal,
        annual_rate_pct=annual_rate_pct,
        months=months,
    )


def _get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def _get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main() -> None:
    print("Welcome to the Mortgage Calculator!")
    print("-----------------------------------")
    principal = _get_float("Enter the loan amount ($): ")
    annual_rate_pct = _get_float("Enter the annual interest rate (%): ")
    months = _get_int("Enter the loan term in months: ")

    try:
        result = calculate_mortgage(principal, annual_rate_pct, months)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    main()
