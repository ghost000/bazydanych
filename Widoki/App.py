import Tkinter as tk

from ModelWidoku.KlientModelWidoku import KlientWidokModel
from ModelWidoku.PizzaModelWidoku import PizzaWidokModel
from ModelWidoku.SkladnikiModelWidoku import SkladnikiWidokModel
from ModelWidoku.ZamowieniaModelWidoku import ZamowieniaWidokModel
from ModelWidoku.ZawartoscModelWidoku import ZawartoscWidokModel

from Widoki.Dodaj import Dodaj


class App( object):
    def __init__(self, master, title="Super Pizza"):
        self.master = master
        self.tabKlienci = []
        self.tabPizza = []
        self.tabSkladniki = []
        self.tabZamowienia = []
        self.tabZawartosci = []
        self.danaTabela = ""
        self.zaczytajDane()
        self.master.title(title)
        self.setGeometry()
        self.dzialamyNaFrame()

    def close_windows(self):
        self.master.destroy()

    def run(self):
        self.master.mainloop()

    def setGeometry(self):
        self.master.update()
        szerokosc = self.master.winfo_width() + 1200
        wysokosc = self.master.winfo_height() + 400
        polozenieX = self.master.winfo_screenwidth()
        polozenieY = self.master.winfo_screenheight()
        x = (polozenieX - szerokosc) // 2
        y = (polozenieY - wysokosc) // 2
        self.master.geometry(str(szerokosc) + "x" + str(wysokosc) + "+" + str(x) + "+" + str(y))

    def dzialamyNaFrame(self):
        frame = tk.Frame(self.master)
        frame.pack()

        bottomframe = tk.Frame(self.master)
        bottomframe.pack(side=tk.BOTTOM)

        self.scrollBar = tk.Scrollbar(self.master)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

        self.mylist = tk.Listbox(self.master, width=self.master.winfo_width() + 1200, yscrollcommand=self.scrollBar.set)
        self.mylist.pack(side=tk.LEFT, fill=tk.BOTH)

        self.klienci()

        self.scrollBar.config(command=self.mylist.yview)

        klientButton = tk.Button(frame, width=self.master.winfo_width() // 6, text="Klient", fg="red", command=self.klienci)
        klientButton.pack(side=tk.LEFT)

        PizzaButton = tk.Button(frame, width=self.master.winfo_width() // 6, text="Pizza", fg="brown", command=self.Pizza)
        PizzaButton.pack(side=tk.LEFT)

        SkladnikiButton = tk.Button(frame, width=self.master.winfo_width() // 6, text="Skladiki", fg="blue",
                                    command=self.Skladniki)
        SkladnikiButton.pack(side=tk.LEFT)

        ZamowieniaButton = tk.Button(frame, width=self.master.winfo_width() // 6, text="Zamowienia", fg="black",
                                     command=self.Zamowienia)
        ZamowieniaButton.pack(side=tk.LEFT)

        ZawartoscButton = tk.Button(frame, width=self.master.winfo_width() // 6, text="Zawartosc", fg="green",
                                    command=self.Zawartosc)
        ZawartoscButton.pack(side=tk.LEFT)

        DodajButton = tk.Button(bottomframe, width=self.master.winfo_width() // 4, text="Dodaj", fg="black", command=self.Dodaj)
        DodajButton.pack(side=tk.LEFT)

        EdytujButton = tk.Button(bottomframe, width=self.master.winfo_width() // 4, text="Edytuj", fg="black", command=self.Edytuj)
        EdytujButton.pack(side=tk.LEFT)

        UsunButton = tk.Button(bottomframe, width=self.master.winfo_width() // 4, text="Usun", fg="magenta", command=self.Usun)
        UsunButton.pack(side=tk.LEFT)

    def klienci(self):
        self.danaTabela = "Klienci"
        self.mylist.delete(0, 'end')
        for element in self.tabKlienci:
            self.mylist.insert(tk.END, " Klient nazwa: " + element.nazwa + " ulica: " + element.ulica +
                               " miejscowosc: " + element.miejscowosc +
                               " telefon: " + str(element.telefon) + " idKlienta: " + str(element.idKlienta))

    def Pizza(self):
        self.danaTabela = "Pizza"
        self.mylist.delete(0, 'end')
        for element in self.tabPizza:
            self.mylist.insert(tk.END, " Pizza nazwa: " + element.nazwa + " opis: " + element.opis + " cena: " +
                               str(element.cena) + " srednica: " + str(element.srednica) + " idPizza: " +
                               str(element.idPizza))

    def Skladniki(self):
        self.danaTabela = "Skladniki"
        self.mylist.delete(0, 'end')
        for element in self.tabSkladniki:
            self.mylist.insert(tk.END, " Skladniki nazwa: " + element.nazwa + " masa: " + str(element.masa) +
                               " koszt: " + str(element.koszt) + " idSkladnika: " + str(element.idSkladnika))

    def Zamowienia(self):
        self.danaTabela = "Zamowienia"
        self.mylist.delete(0, 'end')
        for element in self.tabZamowienia:
            self.mylist.insert(tk.END, " Zamowienia sztuk: " + str(element.sztuk) + " idZam: " + str(element.idZam)
                               + " dataZam: " + str(element.dataZam) + " dataDost: " + str(element.dataDost) +
                               " idPizza: " + str(element.idPizza) + " idKlienta: " + str(element.idKlienta))

    def Zawartosc(self):
        self.danaTabela = "Zawartosc"
        self.mylist.delete(0, 'end')
        for element in self.tabZawartosci:
            self.mylist.insert(tk.END, " Zawartosc idZawartosc: " + str(element.idZawartosc) + " idSkladnika: "
                               + str(element.idSkladnika) + " idPizza: " + str(element.idPizza))

    def Dodaj(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Dodaj(self.newWindow, self.danaTabela)
        self.app.run()

    def Edytuj(self):
        pass

    def Usun(self):
        pass

    def zaczytajDane(self):
        obj1 = KlientWidokModel()
        obj2 = PizzaWidokModel()
        obj3 = SkladnikiWidokModel()
        obj4 = ZamowieniaWidokModel()
        obj5 = ZawartoscWidokModel()

        for element in obj1.getKlienci():
            self.tabKlienci.append(element)
            #print(element)
        for element in obj2.getPizze():
            self.tabPizza.append(element)
            #print(element)
        for element in obj3.getSkladniki():
            self.tabSkladniki.append(element)
            #print(element)
        for element in obj4.getZamowienia():
            self.tabZamowienia.append(element)
            #print(element)
        for element in obj5.getZawartosci():
            self.tabZawartosci.append(element)
            #print(element)
