import sqlite3 as lite
import sys

from Modele.Zamowienia import Zamowienia


class ZamowieniaWidokModel:
    def __init__(self, zamowienia=None, zamowienie=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if zamowienia is None:
            zamowienia = []

        self.__zamowienia = zamowienia
        self.__zamowienie = zamowienie
        self.__con = con
        self.__cur = cur
        self.__path = path

    def getZamowienia(self):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM ZAMOWIENIA''')
            __data = self.__cur.fetchall()
            for element in __data:
                self.__zamowienia.append(Zamowienia(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__zamowienia

    def getZamowienie(self, zamowienie):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM ZAMOWIENIA WHERE ID_ZAM = ?''', (zamowienie.__idZam,))
            __data = self.__cur.fetchone()
            self.__zamowienie = Zamowienia(*__data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__zamowienie

    def create(self, zamowienie):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''INSERT INTO ZAMOWIENIA(SZTUK,DATA_ZAM,DATA_DOSTARCZENIA,ID_PIZZA,ID_KLIENTA,ID_ZAM) 
                                  VALUES (?,?,?,?,?,?)''',
                               (zamowienie.__sztuk, zamowienie.__dataZam, zamowienie.__dataDost, zamowienie.__idPizza,
                                zamowienie.__idKlienta, zamowienie.__idZam))
            self.__con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def updateZamowienie(self, zamowienie):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''UPDATE ZAMOWIENIA SET (SZTUK,DATA_ZAM,DATA_DOSTARCZENIA,ID_PIZZA,ID_KLIENTA) 
                                  VALUES (?,?,?,?,?) WHERE ID_ZAM = ?''',
                               (zamowienie.__sztuk, zamowienie.__dataZam, zamowienie.__dataDost, zamowienie.__idPizza,
                                zamowienie.__idKlienta, zamowienie.__idZam))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def deleteZamowienie(self, zamowienie):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''DELETE FROM ZAMOWIENIA WHERE ID_ZAM = ?''', (zamowienie.__idZam,))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
