import sqlite3 as lite
import sys

from Modele.Zamowienia import Zamowienia


class ZamowieniaWidokModel:
    def __init__(self, zamowienia=None, zamowienie=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if zamowienia is None:
            zamowienia = []

        self.zamowienia = zamowienia
        self.zamowienie = zamowienie
        self.con = con
        self.cur = cur
        self.path = path

    def getZamowienia(self):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM ZAMOWIENIA''')
            data = self.cur.fetchall()
            for element in data:
                self.zamowienia.append(Zamowienia(*element))
            self.cur.execute('''SELECT NAZWA, ID_KLIENTA FROM KLIENT''')
            data = self.cur.fetchall()
            p = {}
            j = 0
            for i in data:
                p[j] = (list(i))
                j+=1
            self.zamowienia[-1].klienci = p

            self.cur.execute('''SELECT NAZWA, ID_PIZZA FROM PIZZA''')
            data = self.cur.fetchall()
            p = {}
            j = 0
            for i in data:
                p[j] = (list(i))
                j+=1
            self.zamowienia[-1].pizze = p

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.zamowienia

    def getZamowienie(self, zamowienie):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM ZAMOWIENIA WHERE ID_ZAM = ?''', (zamowienie.idZam,))
            data = self.cur.fetchone()
            self.zamowienie = Zamowienia(*data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.zamowienie

    def create(self, zamowienie):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''INSERT INTO ZAMOWIENIA(SZTUK,DATA_ZAM,DATA_DOSTARCZENIA,ID_PIZZA,ID_KLIENTA) 
                                  VALUES (?,?,?,?,?)''',
                               (zamowienie.sztuk, zamowienie.dataZam, zamowienie.dataDost, zamowienie.idPizza,
                                zamowienie.idKlienta))
            self.con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def updateZamowienie(self, zamowienie):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            print(zamowienie)
            self.cur.execute('''UPDATE ZAMOWIENIA SET SZTUK = ? WHERE ID_ZAM = ?''',
                               (zamowienie.sztuk, zamowienie.idZam))
            self.cur.execute('''UPDATE ZAMOWIENIA SET DATA_ZAM = ? WHERE ID_ZAM = ?''',
                               (zamowienie.dataZam, zamowienie.idZam))
            self.cur.execute('''UPDATE ZAMOWIENIA SET DATA_DOSTARCZENIA = ? WHERE ID_ZAM = ?''',
                               ('\''+zamowienie.dataDost+'\n', zamowienie.idZam))
            self.cur.execute('''UPDATE ZAMOWIENIA SET ID_PIZZA = ? WHERE ID_ZAM = ?''',
                               (zamowienie.idPizza, zamowienie.idZam))
            self.cur.execute('''UPDATE ZAMOWIENIA SET ID_KLIENTA = ? WHERE ID_ZAM = ?''',
                               (zamowienie.idKlienta, zamowienie.idZam))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def deleteZamowienie(self, zamowienie):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''DELETE FROM ZAMOWIENIA WHERE ID_ZAM = ?''', (zamowienie.idZam,))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
