import sqlite3 as sql

class QuizBowlDatabase:
    def __init__(self, databaseName = 'problems.db'):
        self.databaseName = databaseName
        self.conn = sql.connect(self.databaseName)
        self.cur = self.conn.cursor()

    def createTables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS problems(
                         q_id INT PRIMARY KEY,
                         course TEXT,
                         question TEXT,
                         p_type TEXT,
                         p_options TEXT,
                         p_answer TEXT,
                         fb_correct TETX,
                         fb_incorrect TEXT);''')
        self.conn.commit()

    def populateTables(self, problemData):
        formatData = []
        for problem in problemData:
            formatOptions = problem[3].replace(',', '\n')
            formatProblem = (*problem[:3], formatOptions, *problem[4:])
            formatData.append(formatProblem)

        self.cur.executemany('''INSERT INTO problems (
                             course,
                             question,
                             p_type,
                             p_options,
                             p_answer,
                             fb_correct,
                             fb_incorrect)
                             VALUES (
                             ?,
                             ?,
                             ?,
                             ?,
                             ?,
                             ?,
                             ?)''', formatData)
        
        self.conn.commit()

    def endConnection(self):
        self.conn.close()

problemData = [
    #DS3850
    ('DS3850', 'question 1', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 2', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 3', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 4', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 5', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 6', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 7', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 8', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 9', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3850', 'question 10', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),

    #DS3865
    ('DS3865', 'question 1', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 2', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 3', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 4', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 5', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 6', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 7', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 8', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 9', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3865', 'question 10', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),

    #FIN3210
    ('FIN3210', 'question 1', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 2', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 3', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 4', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 5', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 6', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 7', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 8', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 9', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('FIN3210', 'question 10', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),

    #DS3841
    ('DS3841', 'question 1', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 2', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 3', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 4', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 5', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 6', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 7', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 8', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 9', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('DS3841', 'question 10', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),

    #ECON3320
    ('ECON3320', 'question 1', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 2', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 3', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 4', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 5', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 6', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 7', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 8', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 9', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer'),
    ('ECON3320', 'question 10', 'ABCD', 'A, B, C, D', 'A', 'A is the correct answer', 'That is incorrect, A is the correct answer')
]

quizbowlDatabase = QuizBowlDatabase()

quizbowlDatabase.createTables()

quizbowlDatabase.populateTables(problemData)

quizbowlDatabase.endConnection()