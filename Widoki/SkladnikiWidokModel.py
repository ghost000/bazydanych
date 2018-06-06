from Modele import Skladniki
import sqlite3 as lite
import sys


class SkladnikiWidokModel:
    def __init__(self, skladniki= None, skladnik = None, con = None, cur = None,
                 path ='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if skladniki is None:
            skladniki = []

        self.__skladniki = skladniki
        self.__skladnik = skladnik
        self.__con = con
        self.__cur = cur
        self.__path = path

    def getSkladniki(self):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM SKLADNIKI''')
            __data = self.__cur.fetchall()
            for element in __data:
                self.__skladniki.append(Skladniki(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__skladniki

    def getSkladnik(self, skladnik):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM SKLADNIKI WHERE ID_SKLADNIKA = ?''', (skladnik.__idSkladnika,))
            __data = self.__cur.fetchone()
            self.__skladnik = Skladniki(*__data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__skladnik

    def createSkladnik(self, skladnik):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''INSERT INTO SKLADNIKI(NAZWA,MASA,KOSZT,ID_SKLADNIKA) 
                                  VALUES (?,?,?,?)''',
                               (skladnik.__nazwa, skladnik.__masa, skladnik.__koszt, skladnik.__idSkladnika))
            self.__con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def updateSkladnik(self, skladnik):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''UPDATE SKLADNIKI SET (NAZWA,MASA,KOSZT) 
                                  VALUES (?,?,?) WHERE ID_SKLADNIKA = ?''',
                               (skladnik.__nazwa, skladnik.__masa, skladnik.__koszt, skladnik.__idSkladnika))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def deleteSkladnik(self, skladnik):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''DELETE FROM SKLADNIKI WHERE ID_SKLADNIKA = ?''', (skladnik.__idSkladnika,))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
