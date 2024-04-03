import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.category_label = tk.Label(root, text="Select Category:")
        self.category_label.pack()

        self.category_combo = ttk.Combobox(root, values=["Finance", "Analytics", "Management", "Analytic_Thinking", "Apps_Development"])
        self.category_combo.pack()

        self.start_button = tk.Button(root, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        category = self.category_combo.get()
        if not category:
            messagebox.showerror("Error", "Please select a category!")
            return

        self.root.destroy()
        self.quiz_window = tk.Tk()
        self.quiz_window.title("Quiz")

        self.display_question_answers(category)

    def display_question_answers(self, category):
        conn = sqlite3.connect('quiz_database.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {category}")
        self.questions = cursor.fetchall()
        conn.close()

        self.current_question_index = 0
        self.total_questions = len(self.questions)

        self.question_label = tk.Label(self.quiz_window, text=self.questions[self.current_question_index][0])
        self.question_label.pack()

        self.answer_var = tk.StringVar()

        for choice in self.questions[self.current_question_index][1].split(", "):
            radio_button = tk.Radiobutton(self.quiz_window, text=choice, variable=self.answer_var, value=choice)
            radio_button.pack()

        self.submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(side=tk.BOTTOM)

    def check_answer(self):
        selected_answer = self.answer_var.get()
        correct_answer = self.get_correct_answer()

        if selected_answer == correct_answer:
            messagebox.showinfo("Result", "Correct!", icon="info")
        else:
            messagebox.showerror("Result", "Incorrect", icon="warning")

        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.update_question_answers()
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")

    def update_question_answers(self):
        self.question_label.config(text="")

        self.question_label.config(text=self.questions[self.current_question_index][0])

        self.answer_var.set("")
        for widget in self.quiz_window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        for choice in self.questions[self.current_question_index][1].split(", "):
            radio_button = tk.Radiobutton(self.quiz_window, text=choice, variable=self.answer_var, value=choice)
            radio_button.pack()

    def get_correct_answer(self):
        return self.questions[self.current_question_index][2]

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
