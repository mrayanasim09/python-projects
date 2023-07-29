# This code is make by MRayan Asim
import ast
from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def calculate():
    try:
        global expression
        total = str(ast.literal_eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def calculate_percentage():
    try:
        global expression
        total = str(ast.literal_eval(expression) / 100)
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("500x500")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 20, "bold"))
    expression_field.grid(columnspan=4, ipadx=70, pady=20)

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "+", "%"],
    ]

    for i in range(4):
        for j in range(4):
            if buttons[i][j] == "%":
                button = Button(
                    gui,
                    text=buttons[i][j],
                    fg="black",
                    bg="red",
                    font=("Arial", 20, "bold"),
                    command=calculate_percentage,
                    height=1,
                    width=7,
                )
                button.grid(row=i + 2, column=j)
            else:
                button = Button(
                    gui,
                    text=buttons[i][j],
                    fg="black",
                    bg="red",
                    font=("Arial", 20, "bold"),
                    command=lambda x=buttons[i][j]: press(x),
                    height=1,
                    width=7,
                )
                button.grid(row=i + 2, column=j)

    clear_button = Button(
        gui,
        text="Clear",
        fg="black",
        bg="red",
        font=("Arial", 20, "bold"),
        command=clear,
        height=1,
        width=7,
    )
    clear_button.grid(row=6, column=0, columnspan=2)

    equal_button = Button(
        gui,
        text="=",
        fg="black",
        bg="red",
        font=("Arial", 20, "bold"),
        command=calculate,
        height=1,
        width=7,
    )
    equal_button.grid(row=6, column=2, columnspan=2)

    gui.mainloop()
