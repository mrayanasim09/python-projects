# This code is made by MRayan Asim
from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    Listbox,
    Scrollbar,
    END,
    Toplevel,
    messagebox,
)
import json


class Task:
    def __init__(self, title, category, details, due_date, priority):
        self.title = title
        self.category = category
        self.details = details
        self.due_date = due_date
        self.priority = priority


class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Set window size and position
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Task input fields
        self.title_label = Label(root, text="Title:", fg="blue")
        self.title_entry = Entry(root)
        self.category_label = Label(root, text="Category:", fg="blue")
        self.category_entry = Entry(root)
        self.details_label = Label(root, text="Details:", fg="blue")
        self.details_entry = Entry(root)
        self.due_date_label = Label(root, text="Due Date:", fg="blue")
        self.due_date_entry = Entry(root)
        self.priority_label = Label(root, text="Priority:", fg="blue")
        self.priority_entry = Entry(root)

        # Task listbox and scrollbar
        self.task_listbox = Listbox(root, height=10)
        self.scrollbar = Scrollbar(root)

        # Buttons
        self.add_button = Button(
            root, text="Add Task", command=self.add_task, bg="green", fg="white"
        )
        self.edit_button = Button(
            root, text="Edit Task", command=self.edit_task, bg="orange", fg="white"
        )
        self.delete_button = Button(
            root, text="Delete Task", command=self.delete_task, bg="red", fg="white"
        )
        self.view_button = Button(
            root, text="View Tasks", command=self.view_tasks, bg="blue", fg="white"
        )
        self.save_button = Button(
            root, text="Save", command=self.save_tasks, bg="purple", fg="white"
        )

        # Grid layout
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.details_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.details_entry.grid(row=2, column=1, padx=5, pady=5)
        self.due_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.due_date_entry.grid(row=3, column=1, padx=5, pady=5)
        self.priority_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry.grid(row=4, column=1, padx=5, pady=5)

        self.task_listbox.grid(
            row=0, column=2, rowspan=5, padx=5, pady=5, sticky="nsew"
        )
        self.scrollbar.grid(row=0, column=3, rowspan=5, sticky="ns")

        self.add_button.grid(row=5, column=0, padx=5, pady=5)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)
        self.delete_button.grid(row=5, column=2, padx=5, pady=5)
        self.view_button.grid(row=6, column=0, padx=5, pady=5)
        self.save_button.grid(row=6, column=1, padx=5, pady=5)

        # Configure scrollbar to work with the task listbox
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Create a list to store tasks
        self.tasks = []

        # Load tasks from file
        self.load_tasks()

        # Handle application exit event
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)

    def add_task(self):
        title = self.title_entry.get()
        category = self.category_entry.get()
        details = self.details_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if title and category and details and due_date and priority:
            task = Task(title, category, details, due_date, priority)
            self.tasks.append(task)
            self.clear_entry_fields()
            self.display_tasks()
        else:
            messagebox.showwarning(
                "Incomplete Fields", "Please fill in all the task details."
            )

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            edit_window = Toplevel(self.root)
            edit_window.title("Edit Task")
            edit_window.geometry(
                "+%d+%d" % (self.root.winfo_x() + 50, self.root.winfo_y() + 50)
            )

            title_label = Label(edit_window, text="Title:", fg="blue")
            title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            title_entry = Entry(edit_window)
            title_entry.insert(END, task.title)
            title_entry.grid(row=0, column=1, padx=5, pady=5)

            category_label = Label(edit_window, text="Category:", fg="blue")
            category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
            category_entry = Entry(edit_window)
            category_entry.insert(END, task.category)
            category_entry.grid(row=1, column=1, padx=5, pady=5)

            details_label = Label(edit_window, text="Details:", fg="blue")
            details_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
            details_entry = Entry(edit_window)
            details_entry.insert(END, task.details)
            details_entry.grid(row=2, column=1, padx=5, pady=5)

            due_date_label = Label(edit_window, text="Due Date:", fg="blue")
            due_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
            due_date_entry = Entry(edit_window)
            due_date_entry.insert(END, task.due_date)
            due_date_entry.grid(row=3, column=1, padx=5, pady=5)

            priority_label = Label(edit_window, text="Priority:", fg="blue")
            priority_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
            priority_entry = Entry(edit_window)
            priority_entry.insert(END, task.priority)
            priority_entry.grid(row=4, column=1, padx=5, pady=5)

            update_button = Button(
                edit_window,
                text="Update",
                command=lambda: self.update_task(
                    task,
                    title_entry.get(),
                    category_entry.get(),
                    details_entry.get(),
                    due_date_entry.get(),
                    priority_entry.get(),
                    edit_window,
                ),
                bg="green",
                fg="white",
            )
            update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        else:
            messagebox.showwarning("No Task Selected", "Please select a task to edit.")

    def update_task(
        self, task, title, category, details, due_date, priority, edit_window
    ):
        if title and category and details and due_date and priority:
            task.title = title
            task.category = category
            task.details = details
            task.due_date = due_date
            task.priority = priority
            edit_window.destroy()
            self.display_tasks()
        else:
            messagebox.showwarning(
                "Incomplete Fields", "Please fill in all the task details."
            )

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            confirmation = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete the task:\n\nTitle: {task.title}\nCategory: {task.category}\nDetails: {task.details}\nDue Date: {task.due_date}\nPriority: {task.priority}",
            )
            if confirmation:
                self.tasks.pop(selected_task_index[0])
                self.display_tasks()
        else:
            messagebox.showwarning(
                "No Task Selected", "Please select a task to delete."
            )

    def view_tasks(self):
        self.display_tasks()

    def display_tasks(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(
                END,
                f"Title: {task.title} | Category: {task.category} | Details: {task.details} | Due Date: {task.due_date} | Priority: {task.priority}",
            )

    def clear_entry_fields(self):
        self.title_entry.delete(0, END)
        self.category_entry.delete(0, END)
        self.details_entry.delete(0, END)
        self.due_date_entry.delete(0, END)
        self.priority_entry.delete(0, END)

    def save_tasks(self):
        try:
            with open("tasks.json", "w") as file:
                task_list = [
                    {
                        "title": task.title,
                        "category": task.category,
                        "details": task.details,
                        "due_date": task.due_date,
                        "priority": task.priority,
                    }
                    for task in self.tasks
                ]
                json.dump(task_list, file)
            messagebox.showinfo("Save Successful", "Tasks saved successfully.")
        except IOError:
            messagebox.showerror(
                "Error", "An error occurred while saving tasks to file."
            )

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                task_list = json.load(file)
                for task_data in task_list:
                    title = task_data.get("title", "")
                    category = task_data.get("category", "")
                    details = task_data.get(
                        "details", ""
                    )  # Set default value if 'details' key is missing
                    due_date = task_data.get("due_date", "")
                    priority = task_data.get("priority", "")
                    task = Task(title, category, details, due_date, priority)
                    self.tasks.append(task)
                self.display_tasks()
        except IOError:
            messagebox.showwarning(
                "File Not Found",
                "Tasks file not found. New file will be created when saving tasks.",
            )

    def exit_application(self):
        self.save_tasks()
        self.root.destroy()


root = Tk()
task_manager = TaskManagerGUI(root)
root.mainloop()
