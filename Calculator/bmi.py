# This is made by MRayan Asim
def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) based on weight and height.
    Returns the calculated BMI value.
    """
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    """
    Determines the BMI category based on the BMI value.
    Returns the BMI category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_weight_range(height):
    """
    Provides a suggested weight range based on the height.
    Returns a tuple containing the lower and upper weight limits.
    """
    lower_limit = 18.5 * (height ** 2)
    upper_limit = 24.9 * (height ** 2)
    return lower_limit, upper_limit


def get_height_range(weight):
    """
    Provides a suggested height range based on the weight.
    Returns a tuple containing the lower and upper height limits.
    """
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    return lower_limit, upper_limit


def main():
    print("BMI Calculator")
    print("--------------------")

    weight_unit = input("Enter weight unit (lbs or kgs): ")
    weight = float(input("Enter your weight in {}: ".format(weight_unit)))

    height_unit = input("Enter height unit (feet or meters): ")
    height = float(input("Enter your height in {}: ".format(height_unit)))

    # Convert weight to kg if entered in lbs
    if weight_unit.lower() == "lbs":
        weight = weight * 0.453592

    # Convert height to meters if entered in feet
    if height_unit.lower() == "feet":
        height = height * 0.3048

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\nResults")
    print("--------------------")
    print("BMI: {:.2f}".format(bmi))
    print("Category: {}".format(category))

    weight_range = get_weight_range(height)
    height_range = get_height_range(weight)

    print("\nSuggested Weight Range for Height {:.2f} meters".format(height))
    print("--------------------")
    print("Lower Limit: {:.2f} kg".format(weight_range[0]))
    print("Upper Limit: {:.2f} kg".format(weight_range[1]))

    print("\nSuggested Height Range for Weight {:.2f} kg".format(weight))
    print("--------------------")
    print("Lower Limit: {:.2f} meters".format(height_range[0]))
    print("Upper Limit: {:.2f} meters".format(height_range[1]))


if __name__ == "__main__":
    main()
