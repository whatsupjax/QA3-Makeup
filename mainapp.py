import tkinter as tk
from tkinter import *
from tkinter import ttk

rwSelectQuiz = tk.Tk()
root = rwSelectQuiz

class SelectQuiz:

    def __init__(self, root):
        self.labSelectQuiz = tk.Label(root, text = "Select a quiz topic to be tested on.")
        self.labSelectQuiz.grid()

        self.cmbobxSelectQuiz = ttk.Combobox(root)
        self.cmbobxSelectQuiz.grid()

        self.cmbobxSelectQuiz['values'] = ('DS3850', 'DS3865', 'FIN3220', 'DS3841')

        self.btnStartQuiz = tk.Button(root, text = 'Start Quiz', command = self.comdStartQuiz)
        self.btnStartQuiz.grid()

    def comdCmbobxEntry(self):
        user = self.cmbobxSelectQuiz.get()

    def comdStartQuiz(self):
        root.destroy()

SelectQuiz(root)

rwSelectQuiz.mainloop()

rwQuizApp = tk.Tk()

label = tk.Label(text = SelectQuiz.comdCmbobxEntry)
label.grid()

rwQuizApp.mainloop()