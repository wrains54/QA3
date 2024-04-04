import tkinter as tk
from tkinter import ttk

class CategorySelectionWindow:
    def __init__(self, master):
        self.master = master
        master.title("Category Selection")

        self.label = ttk.Label(master, text="Please select a category:")
        self.label.pack()

        self.categories = ["Category 1", "Category 2", "Category 3"]
        self.selected_category = tk.StringVar()
        self.category_selector = ttk.Combobox(master, values=self.categories, textvariable=self.selected_category)
        self.category_selector.pack()

        self.start_button = ttk.Button(master, text="Start Quiz Now", command=self.open_quiz_window)
        self.start_button.pack()

    def open_quiz_window(self):
        self.master.destroy()
        quiz_window = tk.Tk()
        QuizWindow(quiz_window, self.selected_category.get())
        quiz_window.mainloop()

class QuizWindow:
    def __init__(self, master, category):
        self.master = master
        master.title("Quiz Window")

        # Placeholder for actual question fetching and handling logic
        self.questions = self.fetch_questions(category)
        self.current_question_index = 0

        self.display_question()

    def fetch_questions(self, category):
        # Placeholder for fetching questions based on the selected category
        # This should interact with your database or question storage
        return [{"question": "What is 2+2?", "choices": ["2", "3", "4", "5"], "correct": "4"}]

    def display_question(self):
        question = self.questions[self.current_question_index]

        self.question_label = ttk.Label(self.master, text=question["question"])
        self.question_label.pack()

        self.selected_answer = tk.StringVar()
        for choice in question["choices"]:
            r = ttk.Radiobutton(self.master, text=choice, variable=self.selected_answer, value=choice)
            r.pack()

        self.submit_button = ttk.Button(self.master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        correct_answer = self.questions[self.current_question_index]["correct"]
        if self.selected_answer.get() == correct_answer:
            print("Correct!")
        else:
            print("Incorrect!")

root = tk.Tk()
app = CategorySelectionWindow(root)
root.mainloop()

