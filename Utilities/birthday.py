# This code is made by MRayan Asim
# Packages needed:
# pip install hijri_converter
import datetime
import time
from hijri_converter import convert


def get_day_of_week(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        day_of_week = date.strftime("%A")
        return day_of_week
    except ValueError:
        return "Invalid date format. Please enter the date in dd-mm-yyyy format."


def get_days_until_birthday(date_str):
    try:
        today = datetime.datetime.now().date()
        birth_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
        next_birthday = datetime.date(today.year, birth_date.month, birth_date.day)
        if today > next_birthday:
            next_birthday = datetime.date(
                today.year + 1, birth_date.month, birth_date.day
            )
        days_left = (next_birthday - today).days
        return days_left
    except ValueError:
        return "Invalid date format. Please enter the date in dd-mm-yyyy format."


def get_islamic_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        hijri_date = convert.Gregorian(date.year, date.month, date.day).to_hijri()
        return hijri_date
    except ValueError:
        return "Invalid date format. Please enter the date in dd-mm-yyyy format."


def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"


def calculate_life_path_number(date_str):
    date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
    day = date.day
    month = date.month
    year = date.year
    # Calculate the sum of day, month, and year digits
    total = day + month + year
    # Reduce the total to a single digit
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total


def get_birthstone(month):
    birthstones = {
        1: "Garnet",
        2: "Amethyst",
        3: "Aquamarine",
        4: "Diamond",
        5: "Emerald",
        6: "Pearl",
        7: "Ruby",
        8: "Peridot",
        9: "Sapphire",
        10: "Opal",
        11: "Topaz",
        12: "Turquoise",
    }
    return birthstones.get(month, "Unknown")


def get_birth_flower(month):
    birth_flowers = {
        1: "Carnation",
        2: "Violet",
        3: "Daffodil",
        4: "Daisy",
        5: "Lily of the Valley",
        6: "Rose",
        7: "Larkspur",
        8: "Gladiolus",
        9: "Aster",
        10: "Marigold",
        11: "Chrysanthemum",
        12: "Poinsettia",
    }
    return birth_flowers.get(month, "Unknown")


print(
    "\nHello, this birthday finder is made by MRayan Asim. Hope you will like this! 😊"
)
time.sleep(3)

# Get user input
date_of_birth = input("Enter your date of birth (dd-mm-yyyy): ")

# Call the functions to get the day of the week, days until the next birthday, Islamic date, and zodiac sign
day = get_day_of_week(date_of_birth)
days_left = get_days_until_birthday(date_of_birth)
islamic_date = get_islamic_date(date_of_birth)

# Extract the day, month, and year from the date of birth
birth_date = datetime.datetime.strptime(date_of_birth, "%d-%m-%Y")
birth_month = birth_date.month
birth_day = birth_date.day

# Calculate the zodiac sign
zodiac_sign = get_zodiac_sign(birth_day, birth_month)

# Calculate the age
current_year = datetime.datetime.now().year
age = current_year - birth_date.year

# Calculate the life path number
life_path_number = calculate_life_path_number(date_of_birth)

# Get the birthstone and birth flower
birthstone = get_birthstone(birth_month)
birth_flower = get_birth_flower(birth_month)

# Display the results
print("You were born on a", day + ".")
print("There are", days_left, "days left until your next birthday.")
print("According to the Islamic calendar, your birth date is:", islamic_date)
print("Your zodiac sign is:", zodiac_sign)
print("Your life path number is:", life_path_number)
print("Your birthstone is:", birthstone)
print("Your birth flower is:", birth_flower)
print("You are currently", age, "years old.")
