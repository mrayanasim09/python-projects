# This calculator is made by MRayan Asim
import tkinter as tk


def collatz(n):
    steps = 0
    while n != 1:
        output_text.insert(tk.END, str(n) + "\n")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    output_text.insert(tk.END, "1\n")
    return steps


def calculate_collatz():
    number = int(input_entry.get())
    output_text.delete(1.0, tk.END)
    step_count = collatz(number)
    output_text.insert(tk.END, f"Reached 1 in {step_count} steps.")


# Create the GUI window
window = tk.Tk()
window.title("Collatz Conjecture by MRayan Asim")
window.configure(background="black")

# Create and position the GUI elements
input_label = tk.Label(window, text="Enter a positive integer:", fg="white", bg="black")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

calculate_button = tk.Button(
    window, text="Calculate", command=calculate_collatz, fg="white", bg="dark green"
)
calculate_button.pack()

output_label = tk.Label(window, text="Sequence:", fg="white", bg="black")
output_label.pack()

output_frame = tk.Frame(window, bg="black")
output_frame.pack()

output_text = tk.Text(output_frame, width=30, height=10, fg="white", bg="black")
output_text.pack(side=tk.LEFT, fill=tk.Y)

scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.configure(yscrollcommand=scrollbar.set)

# Start the GUI event loop
window.mainloop()
