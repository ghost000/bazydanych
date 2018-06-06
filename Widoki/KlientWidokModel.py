from Modele import Klient
import sqlite3 as lite
import sys


class KlientWidokModel:
    def __init__(self, klienci= None, klient = None, con = None, cur = None,
                 path ='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if klienci is None:
            klienci = []

        self.__klienci = klienci
        self.__klient = klient
        self.__con = con
        self.__cur = cur
        self.__path = path

    def getKlienci(self):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM KLIENT''')
            __data = self.__cur.fetchall()
            for element in __data:
                self.__klienci.append(Klient(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__klienci

    def getKlient(self, klient):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM KLIENT WHERE ID_KLIENTA = ?''', (klient.__idKlienta,))
            __data = self.__cur.fetchone()
            self.__klient = Klient(*__data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__klient

    def createKlient(self, klient):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''INSERT INTO KLIENT(ULICA,NAZWA,MIEJSCOWOSC,TELEFON,ID_KLIENTA) 
                                  VALUES (?,?,?,?,?)''',
                        (klient.__nazwa, klient.__ulica, klient.__miejscowosc, klient.__telefon, klient.__idKlienta))
            self.__con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def updateKlient(self, klient):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''UPDATE KLIENT SET (ULICA,NAZWA,MIEJSCOWOSC,TELEFON) 
                                  VALUES (?,?,?,?) WHERE ID_KLIENTA = ?''',
                        (klient.__nazwa, klient.__ulica, klient.__miejscowosc, klient.__telefon, klient.__idKlienta))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def deleteKlient(self, klient):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''DELETE FROM KLIENT WHERE ID_KLIENTA = ?''', (klient.____idKlienta,))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
