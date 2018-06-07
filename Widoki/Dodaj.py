import Tkinter as tk

from Modele.Klient import Klient
from Modele.Pizza import Pizza
from Modele.Skladniki import Skladniki
from Modele.Zamowienia import Zamowienia

from ModelWidoku.KlientModelWidoku import KlientWidokModel
from ModelWidoku.PizzaModelWidoku import PizzaWidokModel
from ModelWidoku.SkladnikiModelWidoku import SkladnikiWidokModel
from ModelWidoku.ZamowieniaModelWidoku import ZamowieniaWidokModel

class Dodaj(tk.Tk):
    def __init__(self, master, danaTabela):
        self.master = master
        self.tab = []
        self.danaTabela = danaTabela
        self.wielkiIfiacz()

    def close_windows(self):
        self.master.destroy()

    def create(self, modelWidoku, objekt):
        modelWidoku.create(objekt)

    def wielkiIfiacz(self):
        obiekt = None

        bottomframe1 = tk.Frame(self.master)
        bottomframe2 = tk.Frame(self.master)
        bottomframe3 = tk.Frame(self.master)
        bottomframe4 = tk.Frame(self.master)
        bottomframe5 = tk.Frame(self.master)

        bottomframe1.pack()
        bottomframe2.pack()
        bottomframe3.pack()
        bottomframe4.pack()
        bottomframe5.pack()

        if self.danaTabela == "Klienci":
            objekt = Klient()

            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            #objekt.nazwa = tk.Entry(bottomframe1, bd=5).pack(side = tk.RIGHT)
            self.tab.append(tk.Entry(bottomframe1, bd=5).pack(side = tk.RIGHT))
            tk.Label(bottomframe2, text="ulica: ").pack(side=tk.LEFT)
            #objekt.ulica = tk.Entry(bottomframe2, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe3, text="miejscowosc: ").pack(side=tk.LEFT)
            #objekt.miejscowosc = tk.Entry(bottomframe3, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe4, text="telefon: ").pack(side=tk.LEFT)
            #objekt.telefon = tk.Entry(bottomframe4, bd=5).pack(side = tk.RIGHT)
            greenbutton = tk.Button(bottomframe5, text="DODAJ", fg="Brown")
            greenbutton.pack(side=tk.LEFT)
            k = KlientWidokModel()
            self.create(k,obiekt)

        elif self.danaTabela == "Pizza":
            objekt = Pizza()

            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            #objekt.nazwa = tk.Entry(bottomframe1, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe2, text="opis: ").pack(side=tk.LEFT)
            #objekt.opis = tk.Entry(bottomframe2, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe3, text="cena: ").pack(side=tk.LEFT)
            #objekt.cena = tk.Entry(bottomframe3, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe4, text="srednica: ").pack(side=tk.LEFT)
            #objekt.srednica = tk.Entry(bottomframe4, bd=5).pack(side = tk.RIGHT)
            greenbutton = tk.Button(bottomframe5, text="DODAJ", fg="brown")
            greenbutton.pack(side=tk.LEFT)
            p = PizzaWidokModel()
            self.create(p,obiekt)

        elif self.danaTabela == "Skladniki":
            objekt = Skladniki()
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            #objekt.nazwa = tk.Entry(bottomframe1, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe2, text="masa: ").pack(side=tk.LEFT)
            #objekt.masa = tk.Entry(bottomframe2, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe3, text="koszt: ").pack(side=tk.LEFT)
            #objekt.koszt = tk.Entry(bottomframe3, bd=5).pack(side = tk.RIGHT)
            greenbutton = tk.Button(bottomframe4, text="DODAJ", fg="brown")
            greenbutton.pack(side=tk.LEFT)
            s = SkladnikiWidokModel()
            self.create(s,obiekt)

        elif self.danaTabela == "Zamowienia":
            objekt = Zamowienia()

            tk.Label(bottomframe1, text="sztuk: ").pack(side=tk.LEFT)
            #objekt.sztuk = tk.Entry(bottomframe1, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe2, text="dataZam: ").pack(side=tk.LEFT)
            #objekt.dataZam = tk.Entry(bottomframe2, bd=5).pack(side = tk.RIGHT)
            tk.Label(bottomframe3, text="dataDost: ").pack(side=tk.LEFT)
            #objekt.dataDost = tk.Entry(bottomframe3, bd=5).pack(side = tk.RIGHT)
            greenbutton = tk.Button(bottomframe4, text="DODAJ", fg="brown")
            greenbutton.pack(side=tk.LEFT)
            z = ZamowieniaWidokModel()
            self.create(z,obiekt)

        elif self.danaTabela == "Zawartosc":
            tk.Label(bottomframe1, text="Po co?").pack(side=tk.LEFT)

