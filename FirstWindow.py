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

root = tk.Tk()
app = CategorySelectionWindow(root)
root.mainloop()

