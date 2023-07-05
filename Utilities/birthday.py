#This code is made by MRayan Asim
#Packages needed:
#pip install hijri_converter
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
            next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)
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

print("\nHello, this birthday finder is made by MRayan Asim. Hope you will like this! 😊")
time.sleep(3)

# Get user input
date_of_birth = input("Enter your date of birth (dd-mm-yyyy): ")

# Call the functions to get the day of the week, days until birthday, and Islamic date
day = get_day_of_week(date_of_birth)
days_left = get_days_until_birthday(date_of_birth)
islamic_date = get_islamic_date(date_of_birth)

# Display the results
print("You were born on a", day + ".")
print("There are", days_left, "days left until your birthday.")
print("According to the Islamic calendar, your birth date is:", islamic_date)

