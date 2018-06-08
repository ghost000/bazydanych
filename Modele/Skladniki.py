class Skladniki:
    def __init__(self, nazwa="", masa=-1, koszt=-1, idSkladnika=-1):
        self.nazwa = nazwa
        self.masa = masa
        self.koszt = koszt
        self.idSkladnika = idSkladnika

    def __str__(self):
        return " Skladniki nazwa: " + self.nazwa + " masa: " + str(self.masa) + " koszt: " + str(self.koszt) + \
               " idSkladnika: " + str(self.idSkladnika)
