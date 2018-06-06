class Zawartosc:
    def __init__(self, idZawartosc = -1, idSkladnika = -1, idPizza = -1):
        self.idZawartosc = idZawartosc
        self.idSkladnika = idSkladnika
        self.idPizza = idPizza

    def __str__(self):
        return " Zawartosc idZawartosc: " + str(self.idZawartosc) + " idSkladnika: " + str(self.idSkladnika) + \
               " idPizza: " + str(self.idPizza)