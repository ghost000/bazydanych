import sqlite3 as lite
import sys

from Modele.Zawartosc import Zawartosc


class ZawartoscWidokModel:
    def __init__(self, zawartosci=None, zawartosc=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if zawartosci is None:
            zawartosci = []

        self.zawartosci = zawartosci
        self.zawartosc = zawartosc
        self.con = con
        self.cur = cur
        self.path = path

    def getZawartosci(self):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM ZAWARTOSC''')
            data = self.cur.fetchall()
            for element in data:
                self.zawartosci.append(Zawartosc(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.zawartosci

    def getZawartosc(self, zawartosc):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM ZAWARTOSC WHERE ID_ZAWARTOSC = ?''', (zawartosc.idZawartosc,))
            data = self.cur.fetchone()
            self.zawartosc = Zawartosc(*data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.zawartosc

    def createZawartosc(self, zawartosc):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''INSERT INTO ZAWARTOSC(ID_SKLADNIKA,ID_PIZZA) 
                                  VALUES (?,?)''',
                               (zawartosc.idSkladnika, zawartosc.idPizza))
            self.con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def updateZawartosc(self, zawartosc):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''UPDATE ZAWARTOSC SET ID_SKLADNIKA = ? ,ID_PIZZA = ? 
                                WHERE ID_ZAWARTOSC = ?''',
                               (zawartosc.idSkladnika, zawartosc.idPizza, zawartosc.idZawartosc))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def deleteZawartosc(self, zawartosc):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''DELETE FROM ZAWARTOSC WHERE ID_ZAWARTOSC = ?''', (zawartosc.idZawartosc,))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
