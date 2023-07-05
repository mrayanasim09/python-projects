#This code is made by MRayan Asim
#Packages needed:
#pip install pygame
#pip install os
#pip install matplotlib.pyplot
import matplotlib.pyplot as plt
import time
import pygame
import os

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
                print(f"Value should be greater than or equal to {min_val}. Please try again.")
            elif max_val is not None and val > max_val:
                print(f"Value should be less than or equal to {max_val}. Please try again.")
            else:
                return val
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_feedback_from_user():
    name = input("Enter your name: ")
    feedback = input("Please provide your feedback: ")
    return f"{name}: {feedback} :grade_calculator"

def save_feedback_to_file(feedback_text, filename):
    with open(filename, "a") as file:
        file.write(  feedback_text + "\n")

def display_feedback_from_file(filename):
    if not os.path.isfile(filename):
        print("No previous feedback found.")
        return

    print("Previous Feedbacks:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

def get_suggestion_from_user():
    suggestion_input = input("Would you like to provide any suggestions? (yes/no): ")
    if suggestion_input.lower() == "yes":
        suggestion_text = input("Enter your suggestions: ")
        return suggestion_text
    else:
        return None

def save_suggestion_to_file(suggestion_text, filename):
    with open(filename, "a") as suggestion_file:
        suggestion_file.write(suggestion_text + ' :grade_calculator \n')

def play_sound_file(sound_filename):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_filename)
        pygame.mixer.music.play()
        input("Press Enter to quit...")
        pygame.mixer.music.stop()
    except pygame.error as e:
        print(f"Error playing sound: {e}")
    finally:
        pygame.mixer.quit()

print("Hello! This program of grade calculator is made by MRayan Asim. Hope you will like this! 😊")
time.sleep(3)

num_subjects = get_valid_integer_input("Enter the number of subjects: ", min_val=1)

subjects = []
marks = []
total_marks = []

for i in range(1, num_subjects + 1):
    subject_name = input(f"Enter the name of subject {i}: ")
    subjects.append(subject_name)
    
    total_mark = get_valid_integer_input(f"Enter the total marks for subject {subject_name}: ", min_val=1)
    total_marks.append(total_mark)
    
    obtained_marks = get_valid_integer_input(f"Enter marks obtained for subject {subject_name}: ", min_val=0, max_val=total_mark)
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

feedback_text = get_feedback_from_user()
save_feedback_to_file(feedback_text, "feedback.txt")

display_feedback_from_file("feedback.txt")

suggestion_text = get_suggestion_from_user()
if suggestion_text is not None:
    save_suggestion_to_file(suggestion_text, "suggestion.txt")

print("Ok, hope you liked our grade calculator. Goodbye! MRayanasim")
text = "MRayanasim made this grade calculator thanks for using"
formatted_text = "** " + text.upper() + " **"
print("*" * len(formatted_text))
print(formatted_text)
print("*" * len(formatted_text))

sound_filename = r"C:\Users\Muhammad Asim Hanif\Downloads\dad-says-bye-bye-113119.wav"
play_sound_file(sound_filename)

