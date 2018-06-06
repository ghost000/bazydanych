from datetime import date

class Zamowienia:
    def __init__(self, sztuk=-1, idZam=-1, dataZam=date.max, dataDost=date.max, idPizza=-1, idKlienta=-1):
        self.sztuk = sztuk
        self.idZam = idZam
        self.dataZam = dataZam
        self.dataDost = dataDost
        self.idPizza = idPizza
        self.idKlienta = idKlienta

    def __str__(self):
        return " Zamowienia sztuk: " + str(self.sztuk) + " idZam: " + str(self.idZam) + " dataZam: " + \
               str(self.dataZam) + " dataDost: " + str(self.dataDost) + " idPizza: " + str(self.idPizza) + \
               " idKlienta: " + str(self.idKlienta)