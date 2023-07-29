# This code is made by MRayan Asim
import time


def calculate_grade(marks, total_mark):
    percentage = (marks / total_mark) * 100

    if percentage >= 90:
        grade = "A*"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade


def get_valid_integer_input(prompt, min_val=0, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if val < min_val:
                print(
                    f"Value should be greater than or equal to {min_val}. Please try again."
                )
            elif max_val is not None and val > max_val:
                print(
                    f"Value should be less than or equal to {max_val}. Please try again."
                )
            else:
                return val
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


print(
    "Hello! This program of grade calculator is made by MRayan Asim. Hope you will like this! 😊"
)
time.sleep(3)

num_subjects = get_valid_integer_input("Enter the number of subjects: ", min_val=1)

subjects = []
marks = []
total_marks = []

for i in range(1, num_subjects + 1):
    subject_name = input(f"Enter the name of subject {i}: ")
    subjects.append(subject_name)

    total_mark = get_valid_integer_input(
        f"Enter the total marks for subject {subject_name}: ", min_val=1
    )
    total_marks.append(total_mark)

    obtained_marks = get_valid_integer_input(
        f"Enter marks obtained for subject {subject_name}: ",
        min_val=0,
        max_val=total_mark,
    )
    marks.append(obtained_marks)

grades = [calculate_grade(marks[i], total_marks[i]) for i in range(num_subjects)]

print("\nSubject-wise Grades:")
for i in range(num_subjects):
    print(f"{subjects[i]}: {grades[i]}")

total_obtained_marks = sum(marks)
overall_percentage = (total_obtained_marks / sum(total_marks)) * 100
overall_grade = calculate_grade(total_obtained_marks, sum(total_marks))

print("\nOverall Grade:")
print(f"Grade: {overall_grade}")
print(f"Percentage: {overall_percentage:.2f}%")
