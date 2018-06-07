import Tkinter as tk

from Modele.Klient import Klient
from Modele.Pizza import Pizza
from Modele.Skladniki import Skladniki
from Modele.Zamowienia import Zamowienia


class Dodaj( object):
    def __init__(self, danaTabela, master, title="Super Pizza"):
        self.master = master
        self.tab = []
        self.danaTabela = danaTabela
        self.wielkiIfiacz()

    def run(self):
        pass
        #self.mainloop()

    def wielkiIfiacz(self):
        obiekt = None
        if self.danaTabela == "Klienci":
            objekt = Klient();
            L1 = tk.Label(self.master, tk.TOP, text="Nazwa: ")
            L1.pack(side=tk.LEFT)
            objekt.nazwa = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="ulica: ")
            L1.pack(side=tk.LEFT)
            objekt.ulica = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="miejscowosc: ")
            L1.pack(side=tk.LEFT)
            objekt.miejscowosc = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="telefon: ")
            L1.pack(side=tk.LEFT)
            objekt.telefon = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

        elif self.danaTabela == "Pizza":
            objekt = Pizza();
            L1 = tk.Label(self.master, tk.TOP, text="Nazwa: ")
            L1.pack(side=tk.LEFT)
            objekt.nazwa = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="opis: ")
            L1.pack(side=tk.LEFT)
            objekt.opis = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="cena: ")
            L1.pack(side=tk.LEFT)
            objekt.cena = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="srednica: ")
            L1.pack(side=tk.LEFT)
            objekt.srednica = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

        elif self.danaTabela == "Skladniki":
            objekt = Skladniki();
            L1 = tk.Label(self.master, tk.TOP, text="Nazwa: ")
            L1.pack(side=tk.LEFT)
            objekt.nazwa = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="masa: ")
            L1.pack(side=tk.LEFT)
            objekt.masa = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="koszt: ")
            L1.pack(side=tk.LEFT)
            objekt.koszt = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

        elif self.danaTabela == "Zamowienia":
            objekt = Zamowienia();
            L1 = tk.Label(self.master, tk.TOP, text="sztuk: ")
            L1.pack(side=tk.LEFT)
            objekt.sztuk = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="dataZam: ")
            L1.pack(side=tk.LEFT)
            objekt.dataZam = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

            L1 = tk.Label(self.master, tk.TOP, text="dataDost: ")
            L1.pack(side=tk.LEFT)
            objekt.dataDost = tk.Entry(tk.TOP, bd=5)
            objekt.pack(side=tk.RIGHT)

        elif self.danaTabela == "Zawartosc":
            L1 = tk.Label(self.master, tk.TOP, text="Po co?")
            L1.pack(side=tk.LEFT)
        return obiekt;

    def close_windows(self):
        self.master.destroy()
