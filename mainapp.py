import tkinter as tk
from tkinter import *
from tkinter import ttk

rwSelectQuiz = tk.Tk()
root = rwSelectQuiz

class SelectQuiz:

    def __init__(self, root):
        self.labSelectQuiz = tk.Label(root, text = "Select a quiz topic to be tested on.")
        self.labSelectQuiz.grid()

        self.cbobxSelectQuiz = ttk.Combobox(root)
        self.cbobxSelectQuiz.grid()

        self.btnStartQuiz = tk.Button(root, text = 'Start Quiz')
        self.btnStartQuiz.grid()

    def comdCbobxEntry(self):
        self.cbobxSelectQuiz.get()

SelectQuiz(root)

rwSelectQuiz.mainloop()