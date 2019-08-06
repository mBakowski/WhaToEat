import sqlite3

class DataStorage():


    def __init__(self):
        self.connection = sqlite3.connect('WhaToEat.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS przepisy(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tresc TEXT NOT NULL)""")
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS skladniki(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nazwa TEXT NOT NULL)""")
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS pomocnicza(
                    id_skladnik INTEGER,
                    id_przepis INTEGER,
                    FOREIGN KEY (id_skladnik) REFERENCES przepisy(id),
                    FOREIGN KEY (id_przepis) REFERENCES skladniki(id))""")

    def simpleInsert(self):
        self.cursor.execute("INSERT INTO przepisy(tresc) VALUES('Jakaś tresc, nowa tresc')")
        self.connection.commit()

    def simpleSelect(self):
        self.cursor.execute('SELECT * FROM przepisy')
        colnames = self.cursor.fetchall()
        for x in colnames:
            print(x['id'], x['tresc'])
       


