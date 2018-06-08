import Tkinter as tk

from ModelWidoku.KlientModelWidoku import KlientWidokModel
from ModelWidoku.PizzaModelWidoku import PizzaWidokModel
from ModelWidoku.SkladnikiModelWidoku import SkladnikiWidokModel
from ModelWidoku.ZamowieniaModelWidoku import ZamowieniaWidokModel
from Modele.Klient import Klient
from Modele.Pizza import Pizza
from Modele.Skladniki import Skladniki
from Modele.Zamowienia import Zamowienia


class Update(tk.Tk):
    def __init__(self, master, danaTabela, obj):
        self.master = master
        self.tab = []
        self.danaTabela = danaTabela
        self.wielkiIfiacz()
        self.obj = obj

    def close_windows(self):
        self.master.destroy()

    def wielkiIfiacz(self):
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
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe1, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe2, text="ulica: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe2, bd=5, textvariable = self.obj).pack(side=tk.RIGHT))
            tk.Label(bottomframe3, text="miejscowosc: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe3, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe4, text="telefon: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe4, bd=5).pack(side=tk.RIGHT))
            greenbutton = tk.Button(bottomframe5, text="UPDATE", fg="Brown", command=self.createKlient)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Pizza":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe1, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe2, text="opis: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe2, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe3, text="cena: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe3, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe4, text="srednica: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe4, bd=5).pack(side=tk.RIGHT))
            greenbutton = tk.Button(bottomframe5, text="UPDATE", fg="brown", command=self.createPizza)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Skladniki":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe1, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe2, text="masa: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe2, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe3, text="koszt: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe3, bd=5).pack(side=tk.RIGHT))
            greenbutton = tk.Button(bottomframe4, text="UPDATE", fg="brown", command=self.createSkladnik())
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Zamowienia":
            tk.Label(bottomframe1, text="sztuk: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe1, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe2, text="dataZam: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe2, bd=5).pack(side=tk.RIGHT))
            tk.Label(bottomframe3, text="dataDost: ").pack(side=tk.LEFT)
            self.tab.append(tk.Entry(bottomframe3, bd=5).pack(side=tk.RIGHT))
            greenbutton = tk.Button(bottomframe4, text="UPDATE", fg="brown", command=self.createZamowienia)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Zawartosc":
            tk.Label(bottomframe1, text="Po co?").pack(side=tk.LEFT)

    def createKlient(self):
        objekt = Klient()
        objekt.nazwa = self.tab[0]
        objekt.ulica = self.tab[1]
        objekt.miejscowosc = self.tab[2]
        objekt.telefon = self.tab[3]
        k = KlientWidokModel()
        self.create(k, objekt)

    def createPizza(self):
        objekt = Pizza()
        objekt.nazwa = self.tab[0]
        objekt.opis = self.tab[1]
        objekt.cena = self.tab[2]
        objekt.srednica = self.tab[3]
        p = PizzaWidokModel()
        self.create(p, objekt)

    def createSkladnik(self):
        objekt = Skladniki()
        objekt.nazwa = self.tab[0]
        objekt.masa = self.tab[1]
        objekt.koszt = self.tab[2]
        s = SkladnikiWidokModel()
        self.create(s, objekt)

    def createZamowienia(self):
        objekt = Zamowienia()
        objekt.sztuk = self.tab[0]
        objekt.dataZam = self.tab[1]
        objekt.dataDost = self.tab[2]
        z = ZamowieniaWidokModel()
        self.create(z, objekt)
