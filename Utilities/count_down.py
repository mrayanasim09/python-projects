#This code is made by MRayan Asim
#Packages needed:
#pip install pygame
import threading
import time
import pygame
from datetime import datetime

print("hello this count down  is made by MRayan Asim hope you will like this!😊")
time.sleep(3)
 #to allow time for the user to read the message before proceeding 
def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def countdown_timer(seconds):
    # Start time
    start_time = time.time()

    # Wait until the specified time has passed
    while time.time() - start_time < seconds:
        remaining_seconds = int(seconds - (time.time() - start_time))
        print(f"{remaining_seconds} seconds left | Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(1)
    

    # Print "Start" and start playing the sound
    print("Start")
    sound_file = input("Enter the path of the sound file") #enter sound file path
    sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
    sound_thread.start()

    # Wait for user input to stop the sound
    input("Press Enter to stop the sound...")
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    save_feedback_with_name()
    display_previous_feedbacks()

    suggestion_input = input("Would you like to provide any suggestions? (yes/no): ")
    if suggestion_input.lower() == "yes":
        suggestion_text = input("Enter your suggestions: ")
        with open(new_filename, "a") as suggestion_file:
            suggestion_file.write(suggestion_text + ' :count_down \n')

    print("Ok, hope you liked our count down timer. Goodbye! MRayanasim")
    text = "MRayanasim made this count down timer thanks for using"
    formatted_text = "** " + text.upper() + " **"
    print("*" * len(formatted_text))
    print(formatted_text)
    print("*" * len(formatted_text))
    quit()

def save_feedback_with_name():
    name = input("Enter your name: ")
    feedback = input("Please provide your feedback: ")
    with open("feedback.txt", "a") as file:
        file.write(name + ": " + feedback +' :countdown_timer'+ "\n")

def display_previous_feedbacks():
    print("Previous Feedbacks:")
    with open("feedback.txt", "r") as file:
        for line in file:
            print(line.strip())

filename = "feedback.txt"
new_filename = "suggestion.txt"

# Wait for user to enter "start"
start_input = input("Enter 'start' to begin the countdown: ")
if start_input.lower() != "start":
    print("Invalid input. Exiting...")
    quit()

# Get the user input for the countdown duration
seconds = int(input("Enter the countdown duration in seconds: "))

# Start the countdown timer
countdown_thread = threading.Thread(target=countdown_timer, args=(seconds,))
countdown_thread.start()

