import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3 as sql

class QuizBowlApp:
    def __init__(self):
        
        self.databaseName = 'problems.db'
        self.conn = sql.connect(self.databaseName)
        self.cur = self.conn.cursor()
        self.courses = self.getCourses()
        self.score = 0
    
    def getCourses():
        self.cur.execute('SELECT DISTINCT Course FROM problems')

        self.labSelectQuiz = tk.Label(root, text = "Select a quiz topic to be tested on.")
        self.labSelectQuiz.grid()

        self.cmbobxSelectQuiz = ttk.Combobox(root)
        self.cmbobxSelectQuiz.grid()
        self.cmbobxSelectQuiz['values'] = ('DS3850', 'DS3865', 'FIN3220', 'DS3841')
        
        self.courseVal = tk.StringVar(root)

        self.btnStartQuiz = tk.Button(root, text = 'Start Quiz', command = self.comdStartQuiz)
        self.btnStartQuiz.grid()

    def comdCmbobxEntry(self):
        user = self.cmbobxSelectQuiz.get()

    def comdStartQuiz(self):
        root.destroy()

SelectQuiz(root)

rwSelectQuiz.mainloop()

rwQuizApp = tk.Tk()

label = tk.Label()
label.grid()

rwQuizApp.mainloop()