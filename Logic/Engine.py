from Logic.Client import Client
from DataBase.DataStorage import DataStorage

class Engine:
    def __init__(self):
        self.user = Client()
        self.db = DataStorage()

    def choice(self):
        print()
        Client.userMenuDisplay()
        userChoice = int(input())
        return userChoice

    def logic(self):

        while True:
            choice = self.choice()
            if choice == 1:
                ingredient = self.user.userIngredientAsk()
                print("Możesz z tym ugotować:")
                self.db.complexSelect((ingredient, ))
            elif choice == 0:
                self.db.closingDBConnection()
                print("Do zobaczenia :)")
                break
