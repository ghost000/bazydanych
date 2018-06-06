from Modele.Zawartosc import Zawartosc
import sqlite3 as lite
import sys


class ZawartoscWidokModel:
    def __init__(self, zawartosci=None, zawartosc=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if zawartosci is None:
            zawartosci = []

        self.__zawartosci = zawartosci
        self.__zawartosc = zawartosc
        self.__con = con
        self.__cur = cur
        self.__path = path

    def getZawartosci(self):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM ZAWARTOSC''')
            __data = self.__cur.fetchall()
            for element in __data:
                self.__zawartosci.append(Zawartosc(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__zawartosci

    def getZawartosc(self, zawartosc):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM ZAWARTOSC WHERE ID_ZAWARTOSC = ?''', (zawartosc.__idZawartosc,))
            __data = self.__cur.fetchone()
            self.__zawartosc = Zawartosc(*__data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__zawartosc

    def createZawartosc(self, zawartosc):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''INSERT INTO ZAWARTOSC(ID_ZAWARTOSC,ID_SKLADNIKA,ID_PIZZA) 
                                  VALUES (?,?,?)''',
                               (zawartosc.__idZawartosc, zawartosc.__idSkladnika, zawartosc.__idPizza))
            self.__con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def updateZawartosc(self, zawartosc):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''UPDATE ZAWARTOSC SET (ID_SKLADNIKA,ID_PIZZA) 
                                  VALUES (?,?) WHERE ID_ZAWARTOSC = ?''',
                               (zawartosc.__idSkladnika, zawartosc.__idPizza, zawartosc.__idZawartosc))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def deleteZawartosc(self, zawartosc):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''DELETE FROM ZAWARTOSC WHERE ID_ZAWARTOSC = ?''', (zawartosc.__idZawartosc,))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
