import Tkinter as tk

from ModelWidoku.KlientModelWidoku import KlientWidokModel
from ModelWidoku.PizzaModelWidoku import PizzaWidokModel
from ModelWidoku.SkladnikiModelWidoku import SkladnikiWidokModel
from ModelWidoku.ZamowieniaModelWidoku import ZamowieniaWidokModel
from ModelWidoku.ZawartoscModelWidoku import ZawartoscWidokModel

from Modele.Klient import Klient
from Modele.Pizza import Pizza
from Modele.Skladniki import Skladniki
from Modele.Zamowienia import Zamowienia
from Modele.Zawartosc import Zawartosc

from datetime import date
import time

class Update(tk.Tk):
    def __init__(self, master, danaTabela, obj, obj2, obj3):
        self.master = master
        self.tab = {}
        self.wyn = {}
        self.danaTabela = danaTabela
        self.wielkiIfiacz(obj,obj2, obj3)
        self.obj = obj

    def close_windows(self):
        self.master.destroy()

    def wielkiIfiacz(self,obj, obj2, obj3):
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
            t1 = tk.StringVar()
            t1.set(obj.nazwa)
            self.tab[0] = tk.Entry(bottomframe1, bd=5, textvariable = t1)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="ulica: ").pack(side=tk.LEFT)
            t2 = tk.StringVar()
            t2.set(obj.ulica)
            self.tab[1] = tk.Entry(bottomframe2, bd=5, textvariable = t2)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="miejscowosc: ").pack(side=tk.LEFT)
            t3 = tk.StringVar()
            t3.set(obj.miejscowosc)
            self.tab[2] = tk.Entry(bottomframe3, bd=5, textvariable = t3)
            self.tab[2].pack(side=tk.RIGHT)
            tk.Label(bottomframe4, text="telefon: ").pack(side=tk.LEFT)
            t4 = tk.StringVar()
            t4.set(obj.telefon)
            self.tab[3] = tk.Entry(bottomframe4, bd=5, textvariable = t4)
            self.tab[3].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe5, text="UPDATE", fg="Brown", command=self.updateKlient)
            greenbutton.pack(side=tk.LEFT)
            print(obj.idKlienta)
            self.id = obj.idKlienta

        elif self.danaTabela == "Pizza":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            t1 = tk.StringVar()
            t1.set(obj.nazwa)
            self.tab[0] = tk.Entry(bottomframe1, bd=5, textvariable = t1)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="opis: ").pack(side=tk.LEFT)
            t2 = tk.StringVar()
            t2.set(obj.opis)
            self.tab[1] = tk.Entry(bottomframe2, bd=5, textvariable = t2)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="cena: ").pack(side=tk.LEFT)
            t3 = tk.StringVar()
            t3.set(obj.cena)
            self.tab[2] = tk.Entry(bottomframe3, bd=5, textvariable = t3)
            self.tab[2].pack(side=tk.RIGHT)
            tk.Label(bottomframe4, text="srednica: ").pack(side=tk.LEFT)
            t4 = tk.StringVar()
            t4.set(obj.srednica)
            self.tab[3] = tk.Entry(bottomframe4, bd=5, textvariable = t4)
            self.tab[3].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe5, text="UPDATE", fg="brown", command=self.updatePizza)
            greenbutton.pack(side=tk.LEFT)
            self.id = obj.idPizza

        elif self.danaTabela == "Skladniki":
            tk.Label(bottomframe1, text="Nazwa: ").pack(side=tk.LEFT)
            t1 = tk.StringVar()
            t1.set(obj.nazwa)
            self.tab[0] = tk.Entry(bottomframe1, bd=5, textvariable = t1)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="masa: ").pack(side=tk.LEFT)
            t2 = tk.StringVar()
            t2.set(obj.masa)
            self.tab[1] = tk.Entry(bottomframe2, bd=5, textvariable = t2)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="koszt: ").pack(side=tk.LEFT)
            t3 = tk.StringVar()
            t3.set(obj.koszt)
            self.tab[2] = tk.Entry(bottomframe3, bd=5, textvariable = t3)
            self.tab[2].pack(side=tk.RIGHT)
            greenbutton = tk.Button(bottomframe4, text="UPDATE", fg="brown", command=self.updateSkladnik)
            greenbutton.pack(side=tk.LEFT)
            self.id = obj.idSkladnika

        elif self.danaTabela == "Zamowienia":
            tk.Label(bottomframe1, text="sztuk: ").pack(side=tk.LEFT)
            t1 = tk.StringVar()
            t1.set(obj.sztuk)
            self.tab[0] = tk.Entry(bottomframe1, bd=5, textvariable = t1)
            self.tab[0].pack(side=tk.RIGHT)
            tk.Label(bottomframe2, text="dataZam: ").pack(side=tk.LEFT)
            t2 = tk.StringVar()
            t2.set(obj.dataZam)
            self.tab[1] = tk.Entry(bottomframe2, bd=5, textvariable = t2)
            self.tab[1].pack(side=tk.RIGHT)
            tk.Label(bottomframe3, text="dataDost: ").pack(side=tk.LEFT)
            t3 = tk.StringVar()
            t3.set(obj.dataDost)
            self.tab[2] = tk.Entry(bottomframe3, bd=5, textvariable = t3)
            self.tab[2].pack(side=tk.RIGHT)

            tab = obj2[-1].klienci
            tab2 = obj2[-1].pizze

            t4 = tk.StringVar()
            t4.set(obj.idKlienta)
            self.wyn[0] = obj.idKlienta
            self.wyn[1] = obj.idPizza
            t5 = tk.StringVar()
            t5.set(obj.idPizza)
            print()
            mb = tk.Menubutton(bottomframe4, text=tab[obj.idKlienta][0], relief=tk.RAISED)

            rr = []
            rr2 = []

            def opt1():
                j = 0
                for i in rr:
                    if (i.get()):
                        self.wyn[0] = tab[j][1]
                        mb.configure(text=tab[j][0])
                    j += 1
                return

            mb.menu = tk.Menu(mb, tearoff=0)
            for key, value in tab.iteritems():
                rr.append(tk.BooleanVar())
                mb.menu.add_checkbutton(label=value[0], variable=rr[-1], command=opt1)
            mb["menu"] = mb.menu
            mb.pack()

            mb2 = tk.Menubutton(bottomframe5, text=tab2[obj.idPizza][0], relief=tk.RAISED)

            z = 0

            def opt2():
                z = 0
                for i in rr2:
                    if (i.get()):
                        self.wyn[1] = tab2[z][1]
                        mb2.configure(text=tab2[z][0])
                    z += 1
                return

            mb2.menu = tk.Menu(mb2, tearoff=0)
            for key, value in tab2.iteritems():
                rr2.append(tk.BooleanVar())
                mb2.menu.add_checkbutton(label=value[0],
                                         variable=rr2[-1], command=opt2)
            mb2["menu"] = mb2.menu
            mb2.pack()

            greenbutton = tk.Button(bottomframe6, text="UPDATE", fg="brown", command= self.updateZamowienia)#lambda: self.updateZamowienia(obj.idZam))
            greenbutton.pack(side=tk.LEFT)
            self.id = obj.idZam

        elif self.danaTabela == "Zawartosc":
            tab = obj3[-1].skladniki
            tab2 = obj2[-1].pizze
            mb = tk.Menubutton(bottomframe4, text=tab[obj.idSkladnika][0], relief=tk.RAISED)

            rr = []
            rr2 = []

            self.id = obj.idZawartosc
            self.wyn[0] = obj.idSkladnika
            self.wyn[1] = obj.idPizza
            def opt1():
                j = 0
                for i in rr:
                    if (i.get()):
                        self.wyn[0] = tab[j][1]
                        mb.configure(text=tab[j][0])
                    j += 1
                return

            mb.menu = tk.Menu(mb, tearoff=0)
            for key, value in tab.iteritems():
                rr.append(tk.BooleanVar())
                mb.menu.add_checkbutton(label=value[0], variable=rr[-1], command=opt1)
            mb["menu"] = mb.menu
            mb.pack()

            mb2 = tk.Menubutton(bottomframe5, text=tab2[obj.idPizza][0], relief=tk.RAISED)

            z = 0

            def opt2():
                z = 0
                for i in rr2:
                    if (i.get()):
                        self.wyn[1] = tab2[z][1]
                        mb2.configure(text=tab2[z][0])
                    z += 1
                return

            mb2.menu = tk.Menu(mb2, tearoff=0)
            for key, value in tab2.iteritems():
                rr2.append(tk.BooleanVar())
                mb2.menu.add_checkbutton(label=value[0],
                                         variable=rr2[-1], command=opt2)
            mb2["menu"] = mb2.menu
            mb2.pack()

            greenbutton = tk.Button(bottomframe6, text="UPDATE", fg="brown", command=self.createZawartosc)
            greenbutton.pack(side=tk.LEFT)

    def updateKlient(self):
        objekt = Klient()
        objekt.nazwa = self.tab[0].get()
        objekt.ulica = self.tab[1].get()
        objekt.miejscowosc = self.tab[2].get()
        objekt.telefon = self.tab[3].get()
        objekt.idKlienta = self.id
        k = KlientWidokModel()
        k.updateKlient(objekt)

    def updatePizza(self):
        objekt = Pizza()
        objekt.nazwa = self.tab[0].get()
        objekt.opis = self.tab[1].get()
        objekt.cena = self.tab[2].get()
        objekt.srednica = self.tab[3].get()
        objekt.idPizza = self.id
        p = PizzaWidokModel()
        p.updatePizza(objekt)

    def updateSkladnik(self):
        objekt = Skladniki()
        objekt.nazwa = self.tab[0].get()
        objekt.masa = self.tab[1].get()
        objekt.koszt = self.tab[2].get()
        objekt.idSkladnika = self.id
        s = SkladnikiWidokModel()
        s.updateSkladnik(objekt)

    def updateZamowienia(self):
        objekt = Zamowienia()
        objekt.sztuk = self.tab[0].get()
        objekt.dataZam = self.tab[1].get()
        objekt.dataDost = self.tab[2].get()
        objekt.idKlienta = self.wyn[0]
        objekt.idPizza = self.wyn[1]
        objekt.idZam = self.id
        z = ZamowieniaWidokModel()
        z.updateZamowienie(objekt)

    def createZawartosc(self):
        objekt = Zawartosc()
        objekt.idSkladnika = self.wyn[0]
        objekt.idPizza = self.wyn[1]
        print(self.id)
        objekt.idZawartosc = self.id
        z = ZawartoscWidokModel()
        z.updateZawartosc(objekt)