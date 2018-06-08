class Klient:
    def __init__(self, nazwa="", ulica="", miejscowosc="", telefon=-1, idKlienta=-1):
        self.nazwa = nazwa
        self.ulica = ulica
        self.miejscowosc = miejscowosc
        self.telefon = telefon
        self.idKlienta = idKlienta

    def __str__(self):
        return " Klient nazwa: " + self.nazwa + " ulica: " + self.ulica + " miejscowosc: " + self.miejscowosc + \
               " telefon: " + str(self.telefon) + " idKlienta: " + str(self.idKlienta)
