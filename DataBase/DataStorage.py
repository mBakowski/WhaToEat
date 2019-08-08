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


    # TESTING METHOD
    def simpleInsert(self):
        self.cursor.execute("INSERT INTO skladniki(nazwa) VALUES('marchewka')")
        self.connection.commit()

    # TESTING METHOD
    def simpleIngredientSelect(self):
        self.cursor.execute('SELECT * FROM skladniki')
        values = self.cursor.fetchall()
        for x in values:
            print(x['id'], x['nazwa'])

    # TESTING METHOD
    def simpleRecepieSelect(self):
        self.cursor.execute('SELECT * FROM przepisy')
        values = self.cursor.fetchall()
        for x in values:
            print(x['id'], x['tresc'])

    # TESTING METHOD
    def simpleHelpTableSelect(self):
        self.cursor.execute('SELECT * FROM pomocnicza')
        values = self.cursor.fetchall()
        for x in values:
            print(x['id_skladnik'], x['id_przepis'])

    # METHOD THAT ALLOW US TO FIND RECEPIE WHEN WE KNOW THE INGREDIENT
    def complexSelect(self, ingredientName):
        self.cursor.execute("""SELECT p.tresc FROM przepisy p
                                  INNER JOIN pomocnicza pom ON pom.id_przepis = p.id 
                                  INNER JOIN skladniki s ON s.id = pom.id_skladnik 
                                  WHERE s.nazwa=?
                                  """, ingredientName)
        values = self.cursor.fetchall()
        for x in values:
            print(x['tresc'])

    def closingDBConnection(self):
        self.connection.close()




