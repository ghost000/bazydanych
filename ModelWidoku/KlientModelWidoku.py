import sqlite3 as lite
import sys

from Modele.Klient import Klient


class KlientWidokModel():
    def __init__(self, klienci=None, klient=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if klienci is None:
            klienci = []

        self.klienci = klienci  # model widoku
        self.klient = klient
        self.con = con
        self.cur = cur
        self.path = path

    def getKlienci(self):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM KLIENT''')
            __data = self.cur.fetchall()
            for element in __data:
                self.klienci.append(Klient(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.klienci

    def getKlient(self, klient):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM KLIENT WHERE ID_KLIENTA = ?''', (klient.idKlienta,))
            __data = self.cur.fetchone()
            self.klient = Klient(*__data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.klient

    def create(self, klient):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''INSERT INTO KLIENT(ULICA,NAZWA,MIEJSCOWOSC,TELEFON,ID_KLIENTA) 
                                  VALUES (?,?,?,?,?)''',
                             (klient.nazwa, klient.ulica, klient.miejscowosc, klient.telefon, klient.idKlienta))
            self.con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def updateKlient(self, klient):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''UPDATE KLIENT SET (ULICA,NAZWA,MIEJSCOWOSC,TELEFON) 
                                  VALUES (?,?,?,?) WHERE ID_KLIENTA = ?''',
                             (klient.nazwa, klient.ulica, klient.miejscowosc, klient.telefon, klient.idKlienta))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def deleteKlient(self, klient):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''DELETE FROM KLIENT WHERE ID_KLIENTA = ?''', (klient.__idKlienta,))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
