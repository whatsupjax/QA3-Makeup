import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

class QuizBowlApp:
    def __init__(self):
        
        self.databaseName = 'problems.db'
        self.conn = sql.connect(self.databaseName)
        self.cur = self.conn.cursor()
        self.courses = self.getCourses()
        self.score = 0
    
    def getCourses(self):
        self.cur.execute('SELECT DISTINCT Course FROM problems')
        return [row[0] for row in self.cur.fetchall()]
    
    def start(self):
        self.mainWindow()

    def mainWindow(self):
        self.root = tk.Tk()
        self.root.title('Course Selection')

        tk.Label(self.root, text = 'Select a course to be quized on:').grid()
        self.courseVal = tk.StringVar(self.root)
        self.courseVal.set(self.courses[0])
        tk.OptionMenu(self.root, self.courseVal, *self.courses).grid()

        tk.Button(self.root, text = 'Start Quiz', command = self.startQuiz).grid()

        self.root.mainloop()

    def startQuiz(self):
        selectedCourse = self.courseVal.get()
        problems = self.getProblems(selectedCourse)
        if not problems:
            messagebox.showerror('ERROR')
            return
        self.quizbowlWindow(problems)

    def getProblems(self, course):
        self.cur.execute('SELECT * FROM problems WHERE course = ?', (course,))
        return self.cur.fetchall()
    
    def quizbowlWindow(self, problems):
        self.root.destroy()

        self.qbRoot = tk.Tk()
        self.qbRoot.title('Quiz')

        self.currentProblem = 0
        self.problems = problems

        self.displayProblem()

        self.qbRoot.mainloop()

    def displayProblem(self):
        self.qbRoot.destroy()
        self.qbRoot = tk.Tk()
        self.qbRoot.title('Question {}'.format(self.currentProblem + 1))

        problem = self.problems[self.currentProblem]
        tk.Label(self.qbRoot, text = problem[2]).grid()

        if problem[3] == 'ABCD':
            options = problem[4].split('\n')
            tk.Label(self.qbRoot, text = 'Answer Choices: ' + ', '.join(options)).grid()
            self.abcdAnswer = tk.StringVar()
            respFrame = tk.Frame(self.qbRoot)
            respFrame.grid()
            tk.Label(respFrame, text = 'Your Answer:').grid()
            tk.Entry(respFrame, textvariable = self.abcdAnswer).grid()

        submitButton = tk.Button(self.qbRoot, text = 'Submit Answer', command = self.submitAnswer)
        submitButton.grid()

    def submitAnswer(self):
        problem = self.problems[self.currentProblem]
        correctAnswer = problem[5]

        if problem[3] == 'ABCD':
            selectedAnswer = self.abcdAnswer.get().upper()
            if selectedAnswer == correctAnswer:
                self.score += 1
                feedback = 'That is correct'
                color = 'green'
            
            else:
                feedback = 'That is incorrect'
                color = 'red'
        
        fbLabel = tk.Label(self.qbRoot, text = feedback, fg = color)
        fbLabel.grid()

        self.currentProblem =+ 1

        if self.currentProblem < len(self.problems):
            btnNext = tk.Button(self.qbRoot, text = 'Next Question', command = self.displayProblem)
            btnNext.grid()
        
        else:
            labScore = tk.Label(self.qbRoot, text = 'Score: {}/{}'.format(self.score, len(self.problems)))
            labScore.grid()

            btnComplete = tk.Button(self.qbRoot, text = 'Complete Quiz', command = self.completeQuiz)
            btnComplete.grid()

    def completeQuiz():
        self.qbRoot.destroy()
        messagebox.showinfo('Quiz Complete', 'This quiz is now done')

if __name__ == '__main__':
    app = QuizBowlApp()
    app.start()