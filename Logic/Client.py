class Client:

    def userIngredientAsk(self):

        ingredient = input("Wprowadź posiadany składnik: ")
        while True:
            if ingredient.isdigit():
                ingredient = input("Proszę o podanie nazwy składnika: ")
            else:
                return ingredient

    @classmethod
    def userMenuDisplay(cls):
        print("Co dzisiaj będziemy robić?")
        print("1) Wyszukiwanie na podstawie składnika")
        print("2) Wyświetl wszystkie przepisy")
        print("3) Wyświetl wszystkie składniki")
        print("4) Dodawanie nowego przepisu")
        print("5) Dodawanie nowego składnika")
        print("0) Wyjście z programu")

    def userPrepMessage(self):
        print("Ups, funkcjonalność w przygotowaniu")

    def userErrorMessage(self):
        print("UPS, COŚ POSZŁO NIE TAK")