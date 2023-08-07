# This code is made by MRayan Asim
import tkinter as tk
from tkinter import messagebox


class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")

        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("What is 2 + 2?", "4"),
            ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
            ("What is the largest planet in our solar system?", "Jupiter"),
            ("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare"),
            ("What is the chemical symbol for water?", "H2O"),
            ("What is the tallest mammal on Earth?", "Giraffe"),
            ("In which city is the Taj Mahal located?", "Agra"),
        ]

        self.current_question = 0

        self.question_label = tk.Label(self, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_text, _ = self.questions[self.current_question]
            self.question_label.config(text=question_text)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Over", "You have completed the quiz!")
            self.destroy()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        _, correct_answer = self.questions[self.current_question]

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror(
                "Incorrect", f"Sorry, the correct answer is {correct_answer}."
            )

        self.current_question += 1
        self.load_question()


if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
