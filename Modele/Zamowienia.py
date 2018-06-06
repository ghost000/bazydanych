from datetime import date

class Zamowienia:
    def __init__(self, sztuk=-1, idZam=-1, dataZam=date.max, dataDost=date.max, idPizza=-1, idKlienta=-1):
        self.__sztuk = sztuk
        self.__idZam = idZam
        self.__dataZam = dataZam
        self.__dataDost = dataDost
        self.__idPizza = idPizza
        self.__idKlienta = idKlienta
