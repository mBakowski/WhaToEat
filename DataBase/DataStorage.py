import sqlite3

class DataStorage():


    def __init__(self):
        self.connection = sqlite3.connect('WhaToEat.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS przepisy(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tresc TEXT NOT NULL)""")

    def simpleInsert(self):
        self.cursor.execute("INSERT INTO przepisy(id, tresc) VALUES(1, 'Jakaś tresc')")
        self.connection.commit()

    def simpleSelect(self):
        self.cursor.execute('SELECT * FROM przepisy')
        zmienna = self.cursor.fetchall()[0]
        for wszystkie in zmienna:
            print(wszystkie)
