import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#ececec')
        self.style.configure('TButton', background='#0078d7', foreground='#000000', font=('Arial', 10, 'bold'))
        self.style.configure('TLabel', background='#ececec', foreground='#333333', font=('Arial', 10))

        self.category_label = ttk.Label(root, text="Select Category:")
        self.category_label.pack()

        self.category_combo = ttk.Combobox(root, values=["Finance", "Analytics", "Management", "Analytic_Thinking", "Apps_Development"])
        self.category_combo.pack()

        self.start_button = ttk.Button(root, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        category = self.category_combo.get()
        if not category:
            messagebox.showerror("Error", "Please select a category!")
            return

        self.root.withdraw()
        self.quiz_window = tk.Toplevel()
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
        self.selected_answers = [''] * self.total_questions

        self.question_label = ttk.Label(self.quiz_window, text=self.questions[self.current_question_index][0])
        self.question_label.pack(pady=10)

        self.answer_var = tk.StringVar()

        for choice in self.questions[self.current_question_index][1].split(", "):
            radio_button = ttk.Radiobutton(self.quiz_window, text=choice, variable=self.answer_var, value=choice)
            radio_button.pack()

        self.feedback_label = ttk.Label(self.quiz_window, text="")
        self.feedback_label.pack(pady=10)

        self.submit_button = ttk.Button(self.quiz_window, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.next_button = ttk.Button(self.quiz_window, text="Next Question", command=self.next_question)
        self.next_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        selected_answer = self.answer_var.get()
        correct_answer = self.questions[self.current_question_index][2]

        if selected_answer == correct_answer:
            feedback_text = "Correct!"
            color = "green"
        else:
            feedback_text = f"Incorrect. Correct answer: {correct_answer}"
            color = "red"

        self.feedback_label.config(text=feedback_text, foreground=color)

        self.selected_answers[self.current_question_index] = selected_answer

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.update_question_answers()
        else:
            self.show_score()

    def update_question_answers(self):
        self.question_label.config(text="")

        self.question_label.config(text=self.questions[self.current_question_index][0])

        self.answer_var.set(self.selected_answers[self.current_question_index])
        for widget in self.quiz_window.winfo_children():
            if isinstance(widget, ttk.Radiobutton):
                widget.destroy()

        for choice in self.questions[self.current_question_index][1].split(", "):
            radio_button = ttk.Radiobutton(self.quiz_window, text=choice, variable=self.answer_var, value=choice)
            radio_button.pack()

        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def show_score(self):
        total_correct = sum(1 for selected, correct in zip(self.selected_answers, [q[2] for q in self.questions]) if selected == correct)
        percentage = (total_correct / self.total_questions) * 100
        score_window = tk.Toplevel(self.root)
        score_window.title("Quiz Score")

        score_label = ttk.Label(score_window, text=f"Your score: {percentage:.0f}%")
        score_label.pack(pady=10)

        retry_button = ttk.Button(score_window, text="Take Another Quiz", command=self.retry_quiz(score_window))
        retry_button.pack()

    def retry_quiz(self, window):
        def close_window():
            window.destroy()
            self.quiz_window.destroy()
            self.root.deiconify()

        return close_window

root = tk.Tk()
app = QuizApp(root)
root.mainloop()

