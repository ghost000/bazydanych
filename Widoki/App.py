import Tkinter as tk

from ModelWidoku.KlientModelWidoku import KlientWidokModel
from ModelWidoku.PizzaModelWidoku import PizzaWidokModel
from ModelWidoku.SkladnikiModelWidoku import SkladnikiWidokModel
from ModelWidoku.ZamowieniaModelWidoku import ZamowieniaWidokModel
from ModelWidoku.ZawartoscModelWidoku import ZawartoscWidokModel


class App(tk.Tk, object):
    def __init__(self, title="Super Pizza"):
        super(App, self).__init__()
        self.tabKlienci = []
        self.tabPizza = []
        self.tabSkladniki = []
        self.tabZamowienia = []
        self.tabZawartosci = []
        self.title(title)
        self.setGeometry()
        self.dzialamyNaFrame()
        self.zaczytajDane()

    def run(self):
        self.mainloop()

    def setGeometry(self):
        self.update()
        szerokosc = self.winfo_width()+1200
        wysokosc = self.winfo_height()+400
        polozenieX = self.winfo_screenwidth()
        polozenieY = self.winfo_screenheight()
        x = (polozenieX - szerokosc) // 2
        y = (polozenieY - wysokosc) // 2
        self.geometry(str(szerokosc) + "x" + str(wysokosc) + "+" + str(x) + "+" + str(y))

    def dzialamyNaFrame(self):
        frame = tk.Frame(self.master)
        frame.pack()

        bottomframe = tk.Frame(self.master)
        bottomframe.pack(side=tk.BOTTOM)

        scrollBar = tk.Scrollbar(self.master)
        scrollBar.pack(side=tk.TOP, fill=tk.Y)

        mylist = tk.Listbox(self.master, yscrollcommand=scrollBar.set)
        for line in range(100):
            mylist.insert(tk.END, "This is line number " + str(line))

        mylist.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollBar.config(command=mylist.yview)

        klientButton = tk.Button(frame, width=self.winfo_width()//6, text="Klient", fg="red")
        klientButton.pack(side=tk.LEFT)

        PizzaButton = tk.Button(frame, width=self.winfo_width()//6, text="Pizza", fg="brown")
        PizzaButton.pack(side=tk.LEFT)

        SkladnikiButton = tk.Button(frame, width=self.winfo_width()//6, text="Skladiki", fg="blue")
        SkladnikiButton.pack(side=tk.LEFT)

        ZamowieniaButton = tk.Button(frame, width=self.winfo_width()//6, text="Zamowienia", fg="black")
        ZamowieniaButton.pack(side=tk.LEFT)

        ZawartoscButton = tk.Button(frame, width=self.winfo_width()//6, text="Zawartosc", fg="green")
        ZawartoscButton.pack(side=tk.LEFT)

        DodajButton = tk.Button(bottomframe, width=self.winfo_width()//4, text="Dodaj", fg="black")
        DodajButton.pack(side=tk.LEFT)

        EdytujButton = tk.Button(bottomframe, width=self.winfo_width()//4, text="Edytuj", fg="black")
        EdytujButton.pack(side=tk.LEFT)

        UsunButton = tk.Button(bottomframe, width=self.winfo_width()//4, text="Usun", fg="magenta")
        UsunButton.pack(side=tk.LEFT)

    def klienci(self):
        tab

    def zaczytajDane(self):
        obj1 = KlientWidokModel()
        obj2 = PizzaWidokModel()
        obj3 = SkladnikiWidokModel()
        obj4 = ZamowieniaWidokModel()
        obj5 = ZawartoscWidokModel()

        for element in obj1.getKlienci():
            self.tabKlienci.append(element)
        for element in obj2.getPizze():
            self.tabPizza.append(element)
        for element in obj3.getSkladniki():
            self.tabSkladniki.append(element)
        for element in obj4.getZamowienia():
            self.tabZamowienia.append(element)
        for element in obj5.getZawartosci():
            self.tabZawartosci.append(element)
