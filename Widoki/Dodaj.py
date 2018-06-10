import Tkinter as tk

from ModelWidoku.KlientModelWidoku import KlientWidokModel
from ModelWidoku.PizzaModelWidoku import PizzaWidokModel
from ModelWidoku.SkladnikiModelWidoku import SkladnikiWidokModel
from ModelWidoku.ZamowieniaModelWidoku import ZamowieniaWidokModel

from Modele.Klient import Klient
from Modele.Pizza import Pizza
from Modele.Skladniki import Skladniki
from Modele.Zamowienia import Zamowienia

from datetime import date
import time

class Dodaj(tk.Tk):
    def __init__(self, master, danaTabela):
        self.master = master
        self.tab = {}
        self.danaTabela = danaTabela
        self.wielkiIfiacz()

    def close_windows(self):
        self.master.destroy()

    def wielkiIfiacz(self):
        bottomframe1 = tk.Frame(self.master)
        bottomframe2 = tk.Frame(self.master)
        bottomframe3 = tk.Frame(self.master)
        bottomframe4 = tk.Frame(self.master)
        bottomframe5 = tk.Frame(self.master)
        bottomframe6 = tk.Frame(self.master)

        bottomframe1.pack()
        bottomframe2.pack()
        bottomframe3.pack()
        bottomframe4.pack()
        bottomframe5.pack()
        bottomframe6.pack()

        if self.danaTabela == "Klienci":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            self.tab[0] = tk.Entry(bottomframe1, bd=5)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="ulica: ").pack(side=tk.LEFT)
            self.tab[1] = tk.Entry(bottomframe2, bd=5)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="miejscowosc: ").pack(side=tk.LEFT)
            self.tab[2] = tk.Entry(bottomframe3, bd=5)
            self.tab[2].pack(side=tk.RIGHT)
            tk.Label(bottomframe4, text="telefon: ").pack(side=tk.LEFT)
            self.tab[3] = tk.Entry(bottomframe4, bd=5)
            self.tab[3].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe5, text="DODAJ", fg="Brown", command=self.createKlient)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Pizza":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            self.tab[0] = tk.Entry(bottomframe1, bd=5)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="opis: ").pack(side=tk.LEFT)
            self.tab[1] = tk.Entry(bottomframe2, bd=5)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="cena: ").pack(side=tk.LEFT)
            self.tab[2] = tk.Entry(bottomframe3, bd=5)
            self.tab[2].pack(side=tk.RIGHT)
            tk.Label(bottomframe4, text="srednica: ").pack(side=tk.LEFT)
            self.tab[3] = tk.Entry(bottomframe4, bd=5)
            self.tab[3].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe5, text="DODAJ", fg="brown", command=self.createPizza)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Skladniki":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            self.tab[0] = tk.Entry(bottomframe1, bd=5)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="masa: ").pack(side=tk.LEFT)
            self.tab[1] = tk.Entry(bottomframe2, bd=5)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="koszt: ").pack(side=tk.LEFT)
            self.tab[2] = tk.Entry(bottomframe3, bd=5)
            self.tab[2].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe4, text="DODAJ", fg="brown", command=self.createSkladnik)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Zamowienia":
            tk.Label(bottomframe1, text="sztuk: ").pack(side=tk.LEFT)
            self.tab[0] = tk.Entry(bottomframe1, bd=5)
            self.tab[0].pack(side=tk.RIGHT)
            today = time.asctime(time.localtime(time.time()))
            num1 = tk.StringVar()
            num1.set(today)
            tk.Label(bottomframe2, text="dataZam: ").pack(side=tk.LEFT)
            self.tab[1] = tk.Entry(bottomframe2, bd=5, textvariable = num1)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="dataDost: ").pack(side=tk.LEFT)
            self.tab[2] = tk.Entry(bottomframe3, bd=5, textvariable = num1)
            self.tab[2].pack(side=tk.RIGHT)
            tk.Label(bottomframe4, text="idKlienta: ").pack(side=tk.LEFT)
            self.tab[3] = tk.Entry(bottomframe4, bd=5)
            self.tab[3].pack(side=tk.RIGHT)
            tk.Label(bottomframe5, text="idPizza: ").pack(side=tk.LEFT)
            self.tab[4] = tk.Entry(bottomframe5, bd=5)
            self.tab[4].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe6, text="DODAJ", fg="brown", command=self.createZamowienia)
            greenbutton.pack(side=tk.LEFT)

        elif self.danaTabela == "Zawartosc":
            tk.Label(bottomframe1, text="Po co?").pack(side=tk.LEFT)

    def createKlient(self):
        objekt = Klient()
        objekt.nazwa = self.tab[0].get()
        objekt.ulica = self.tab[1].get()
        objekt.miejscowosc = self.tab[2].get()
        objekt.telefon = self.tab[3].get()
        k = KlientWidokModel()
        k.create(objekt)

    def createPizza(self):
        objekt = Pizza()
        objekt.nazwa = self.tab[0].get()
        objekt.opis = self.tab[1].get()
        objekt.cena = self.tab[2].get()
        objekt.srednica = self.tab[3].get()
        p = PizzaWidokModel()
        p.create(objekt)

    def createSkladnik(self):
        objekt = Skladniki()
        objekt.nazwa = self.tab[0].get()
        objekt.masa = self.tab[1].get()
        objekt.koszt = self.tab[2].get()
        s = SkladnikiWidokModel()
        s.create(objekt)

    def createZamowienia(self):
        objekt = Zamowienia()
        objekt.sztuk = self.tab[0].get()
        objekt.dataZam = self.tab[1].get()
        objekt.dataDost = self.tab[2].get()
        objekt.idKlienta = self.tab[3].get()
        objekt.idPizza = self.tab[4].get()
        z = ZamowieniaWidokModel()
        z.create(objekt)
