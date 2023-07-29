# This program is made by MRayan Asim
# Packages needed:
# pip install tkcalendar
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date


def get_selected_date():
    selected_date = cal.get_date()
    selected_date_label.config(text=f"Selected Date: {selected_date}")


def set_today():
    today = date.today()
    cal.selection_set(today)


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()


def apply_theme():
    if dark_mode:
        root.config(bg="#333333")
        frame.config(style="DarkFrame.TFrame")
        cal.configure(
            background="#333333",
            foreground="#ffffff",
            selectbackground="#ffff00",
            selectforeground="#000000",
            headersbackground="#333333",
            headersforeground="#ffffff",
        )
        select_date_button.config(style="DarkButton.TButton")
        today_button.config(style="DarkButton.TButton")
        clear_button.config(style="DarkButton.TButton")
        selected_date_label.config(foreground="red")
    else:
        root.config(bg="#f2f2f2")
        frame.config(style="LightFrame.TFrame")
        cal.configure(
            background="#ffffff",
            foreground="#333333",
            selectbackground="#ffff00",
            selectforeground="#000000",
            headersbackground="#f2f2f2",
            headersforeground="#333333",
        )
        select_date_button.config(style="TButton")
        today_button.config(style="TButton")
        clear_button.config(style="TButton")
        selected_date_label.config(foreground="#0080ff")


# Create the main window
root = tk.Tk()
root.title("Calendar")
root.geometry("500x400")

# Create a frame for the calendar and buttons
frame = ttk.Frame(root, padding=20)
frame.pack()

# Set the initial theme to dark
dark_mode = True

# Create a Calendar widget
cal = Calendar(
    frame,
    selectmode="day",
    date_pattern="yyyy-mm-dd",
    background="#333333",
    foreground="#ffffff",
    selectbackground="#ffff00",
    selectforeground="#000000",
    headersbackground="#333333",
    headersforeground="#ffffff",
    font=("Arial", 12),
    cursor="hand2",
)
cal.grid(row=0, column=0, columnspan=2, pady=10)

# Create a button to get the selected date
select_date_button = ttk.Button(
    frame, text="Get Selected Date", command=get_selected_date, cursor="hand2"
)
select_date_button.grid(row=1, column=0, pady=10)

# Create a label to display the selected date
selected_date_label = ttk.Label(
    frame, text="Selected Date: ", font=("Arial", 12, "bold"), foreground="white"
)
selected_date_label.grid(row=1, column=1, pady=10)

# Create a button to set today's date
today_button = ttk.Button(frame, text="Set Today", command=set_today, cursor="hand2")
today_button.grid(row=2, column=0, pady=10)

# Create a button to clear the selected date
clear_button = ttk.Button(
    frame,
    text="Clear Date",
    command=lambda: selected_date_label.config(text="Selected Date:"),
    cursor="hand2",
)
clear_button.grid(row=2, column=1, pady=10)

# Create a button to toggle between dark and light themes
toggle_theme_button = ttk.Button(
    frame, text="Toggle Theme", command=toggle_theme, cursor="hand2"
)
toggle_theme_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create styles for dark and light frames
style = ttk.Style()
style.configure("DarkFrame.TFrame", background="#333333")
style.configure("LightFrame.TFrame", background="#f2f2f2")

# Create styles for dark-themed buttons
style.configure("DarkButton.TButton", foreground="#333333", background="#ffffff")

# Apply the initial dark theme
apply_theme()

# Start the main loop
root.mainloop()
