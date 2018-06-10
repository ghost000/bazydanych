import sqlite3 as lite
import sys

from Modele.Skladniki import Skladniki


class SkladnikiWidokModel:
    def __init__(self, skladniki=None, skladnik=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if skladniki is None:
            skladniki = []

        self.skladniki = skladniki
        self.skladnik = skladnik
        self.con = con
        self.cur = cur
        self.path = path

    def getSkladniki(self):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM SKLADNIKI''')
            data = self.cur.fetchall()
            for element in data:
                self.skladniki.append(Skladniki(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.skladniki

    def getSkladnik(self, skladnik):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM SKLADNIKI WHERE ID_SKLADNIKA = ?''', (skladnik.idSkladnika,))
            data = self.cur.fetchone()
            self.skladnik = Skladniki(*data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.skladnik

    def create(self, skladnik):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''INSERT INTO SKLADNIKI(NAZWA,MASA,KOSZT) 
                                  VALUES (?,?,?)''',
                               (skladnik.nazwa, skladnik.masa, skladnik.koszt))
            self.con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def updateSkladnik(self, skladnik):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute("UPDATE SKLADNIKI SET NAZWA=?,MASA=?,KOSZT=? WHERE _rowid_=? ;",
                               (skladnik.nazwa, skladnik.masa, skladnik.koszt, skladnik.idSkladnika))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def deleteSkladnik(self, skladnik):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''DELETE FROM SKLADNIKI WHERE ID_SKLADNIKA = ?''', (skladnik.idSkladnika,))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
