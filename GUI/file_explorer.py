# This code is made by MRayan Asim
from tkinter import *
from tkinter import filedialog


# Function for opening the file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


# Create the root window
window = Tk()

# Set window title
window.title("File Explorer")

# Set window size
window.geometry("600x400")

# Set window background color
window.config(background="#f2f2f2")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width / 2) - (600 / 2)
y = (screen_height / 2) - (400 / 2)

# Set the window position to the center of the screen
window.geometry("%dx%d+%d+%d" % (600, 400, x, y))

# Create a File Explorer label
label_file_explorer = Label(
    window,
    text="File Explorer using Tkinter",
    width=40,
    height=2,
    fg="#333",
    font=("Arial", 20),
)

# Create the Browse Files button
button_explore = Button(
    window,
    text="Browse Files",
    command=browseFiles,
    font=("Arial", 16),
    bg="#4CAF50",
    fg="white",
    padx=16,
    pady=8,
    border=0,
    cursor="hand2",
)

# Create the Exit button
button_exit = Button(
    window,
    text="Exit",
    command=exit,
    font=("Arial", 16),
    bg="#F44336",
    fg="white",
    padx=16,
    pady=8,
    border=0,
    cursor="hand2",
)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1, pady=16)
button_explore.grid(column=1, row=2, pady=16)
button_exit.grid(column=1, row=3, pady=16)

# Let the window wait for any events
window.mainloop()
