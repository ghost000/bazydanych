class Pizza:
    def __init__(self, nazwa="", opis="", cena=-1, srednica=-1, idPizza=-1):
        self.nazwa = nazwa
        self.opis = opis
        self.cena = cena
        self.srednica = srednica
        self.idPizza = idPizza

    def __str__(self):
        return " Pizza nazwa: " + self.nazwa + " opis: " + self.opis + " cena: " + str(self.cena) + \
               " srednica: " + str(self.srednica) + " idPizza: " + str(self.idPizza)
