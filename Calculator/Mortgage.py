# This code is made by MRayan Asim
def calculate_monthly_mortgage(initial_amount, annual_interest_rate, number_of_months):
    monthly_interest_rate = annual_interest_rate / (
        12 * 100
    )  # Convert annual rate to monthly rate
    monthly_payments = (
        initial_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months)
        / ((1 + monthly_interest_rate) ** number_of_months - 1)
    )
    return monthly_payments


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    print("Welcome to the Mortgage Calculator!")
    print("-----------------------------------")

    initial_amount = get_float_input("Enter the loan amount ($): ")
    annual_interest_rate = get_float_input("Enter the annual interest rate (%): ")
    number_of_months = get_int_input("Enter the loan term in months: ")

    monthly_payment = calculate_monthly_mortgage(
        initial_amount, annual_interest_rate, number_of_months
    )

    print("\nResult:")
    print(f"The monthly mortgage payment is: ${monthly_payment:.2f}")


if __name__ == "__main__":
    main()
