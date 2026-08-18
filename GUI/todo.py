# This code is made by MRayan Asim
from __future__ import annotations

import json
import os
import tempfile
from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tkinter import Tk


# ---------------------------------------------------------------------------
# Domain model — fully decoupled from Tkinter
# ---------------------------------------------------------------------------


@dataclass
class Task:
    """Represents a single to-do task (UI-independent domain model)."""

    title: str
    category: str
    details: str
    due_date: str
    priority: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> Task:
        return cls(
            title=data.get("title", ""),
            category=data.get("category", ""),
            details=data.get("details", ""),
            due_date=data.get("due_date", ""),
            priority=data.get("priority", ""),
        )


class TaskStore:
    """Manages a list of Tasks with atomic JSON persistence."""

    def __init__(self, filepath: str = "tasks.json") -> None:
        self._filepath = filepath
        self._tasks: list[Task] = []

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def delete(self, index: int) -> None:
        self._tasks.pop(index)

    def update(self, index: int, task: Task) -> None:
        self._tasks[index] = task

    def get_all(self) -> list[Task]:
        return list(self._tasks)

    def __len__(self) -> int:
        return len(self._tasks)

    # ------------------------------------------------------------------
    # Persistence — atomic writes prevent data loss on crash
    # ------------------------------------------------------------------

    def save(self) -> None:
        """Atomically write tasks to the JSON file."""
        data = [t.to_dict() for t in self._tasks]
        dir_name = os.path.dirname(os.path.abspath(self._filepath)) or "."
        with tempfile.NamedTemporaryFile(
            mode="w", dir=dir_name, suffix=".tmp", delete=False, encoding="utf-8"
        ) as tmp:
            json.dump(data, tmp, indent=2)
            tmp_path = tmp.name
        os.replace(tmp_path, self._filepath)

    def load(self) -> None:
        """Load tasks from the JSON file, silently ignoring a missing file."""
        try:
            with open(self._filepath, encoding="utf-8") as f:
                data = json.load(f)
            self._tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self._tasks = []
        except (json.JSONDecodeError, KeyError) as exc:
            # Corrupt file — start fresh but warn
            self._tasks = []
            raise ValueError(f"Could not parse tasks file: {exc}") from exc


# ---------------------------------------------------------------------------
# GUI
# ---------------------------------------------------------------------------


class TaskManagerGUI:
    def __init__(self, root: Tk) -> None:
        from tkinter import (
            Button,
            Entry,
            Label,
            Listbox,
            Scrollbar,
        )

        self.root = root
        self.root.title("Task Manager")
        self.store = TaskStore()

        # Centre the window
        window_width, window_height = 600, 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Input fields
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

        # Listbox + scrollbar
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
            root, text="View Tasks", command=self.display_tasks, bg="blue", fg="white"
        )
        self.save_button = Button(
            root, text="Save", command=self.save_tasks, bg="purple", fg="white"
        )

        # Layout
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry.grid(row=0, column=0 + 1, padx=5, pady=5)
        self.category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.details_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.details_entry.grid(row=2, column=1, padx=5, pady=5)
        self.due_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.due_date_entry.grid(row=3, column=1, padx=5, pady=5)
        self.priority_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry.grid(row=4, column=1, padx=5, pady=5)
        self.task_listbox.grid(row=0, column=2, rowspan=5, padx=5, pady=5, sticky="nsew")
        self.scrollbar.grid(row=0, column=3, rowspan=5, sticky="ns")
        self.add_button.grid(row=5, column=0, padx=5, pady=5)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)
        self.delete_button.grid(row=5, column=2, padx=5, pady=5)
        self.view_button.grid(row=6, column=0, padx=5, pady=5)
        self.save_button.grid(row=6, column=1, padx=5, pady=5)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self._load_tasks()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def add_task(self) -> None:
        from tkinter import messagebox

        fields = self._read_fields()
        if all(fields.values()):
            self.store.add(Task(**fields))
            self._clear_fields()
            self.display_tasks()
        else:
            messagebox.showwarning("Incomplete Fields", "Please fill in all the task details.")

    def edit_task(self) -> None:
        from tkinter import END, Button, Entry, Label, Toplevel, messagebox

        sel = self.task_listbox.curselection()
        if not sel:
            messagebox.showwarning("No Task Selected", "Please select a task to edit.")
            return
        index = sel[0]
        task = self.store.get_all()[index]
        edit_win = Toplevel(self.root)
        edit_win.title("Edit Task")
        edit_win.geometry(f"+{self.root.winfo_x() + 50}+{self.root.winfo_y() + 50}")

        entries: dict[str, Entry] = {}
        for row, (field, value) in enumerate(task.to_dict().items()):
            Label(edit_win, text=f"{field.replace('_', ' ').title()}:", fg="blue").grid(
                row=row, column=0, padx=5, pady=5, sticky="w"
            )
            entry = Entry(edit_win)
            entry.insert(END, value)
            entry.grid(row=row, column=1, padx=5, pady=5)
            entries[field] = entry

        def _save() -> None:
            updated = {k: e.get() for k, e in entries.items()}
            if all(updated.values()):
                self.store.update(index, Task(**updated))
                edit_win.destroy()
                self.display_tasks()
            else:
                messagebox.showwarning("Incomplete Fields", "Please fill in all the task details.")

        Button(edit_win, text="Update", command=_save, bg="green", fg="white").grid(
            row=len(entries), column=0, columnspan=2, padx=5, pady=5
        )

    def delete_task(self) -> None:
        from tkinter import messagebox

        sel = self.task_listbox.curselection()
        if not sel:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")
            return
        index = sel[0]
        task = self.store.get_all()[index]
        if messagebox.askyesno(
            "Confirm Deletion",
            f"Delete task:\n\nTitle: {task.title}\nCategory: {task.category}\n"
            f"Details: {task.details}\nDue Date: {task.due_date}\nPriority: {task.priority}",
        ):
            self.store.delete(index)
            self.display_tasks()

    def display_tasks(self) -> None:
        from tkinter import END

        self.task_listbox.delete(0, END)
        for task in self.store.get_all():
            self.task_listbox.insert(
                END,
                f"Title: {task.title} | Category: {task.category} | "
                f"Details: {task.details} | Due: {task.due_date} | Priority: {task.priority}",
            )

    def save_tasks(self) -> None:
        from tkinter import messagebox

        try:
            self.store.save()
            messagebox.showinfo("Save Successful", "Tasks saved successfully.")
        except OSError as exc:
            messagebox.showerror("Error", f"Could not save tasks: {exc}")

    def exit_application(self) -> None:
        self.save_tasks()
        self.root.destroy()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _read_fields(self) -> dict[str, str]:
        return {
            "title": self.title_entry.get(),
            "category": self.category_entry.get(),
            "details": self.details_entry.get(),
            "due_date": self.due_date_entry.get(),
            "priority": self.priority_entry.get(),
        }

    def _clear_fields(self) -> None:
        from tkinter import END

        for entry in (
            self.title_entry,
            self.category_entry,
            self.details_entry,
            self.due_date_entry,
            self.priority_entry,
        ):
            entry.delete(0, END)

    def _load_tasks(self) -> None:
        from tkinter import messagebox

        try:
            self.store.load()
        except ValueError as exc:
            messagebox.showwarning("Load Warning", str(exc))
        self.display_tasks()


def main() -> None:
    from tkinter import Tk

    root = Tk()
    TaskManagerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
