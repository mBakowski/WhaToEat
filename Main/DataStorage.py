import sqlite3

class DataStorage:
    def __init__(self):
        pass

    connection = sqlite3.connect('WhaToEat.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    
