import sqlite3 as lite
import sys

from Modele.Pizza import Pizza


class PizzaWidokModel:
    def __init__(self, pizze=None, pizza=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if pizze is None:
            pizze = []

        self.__pizze = pizze
        self.__pizza = pizza
        self.__con = con
        self.__cur = cur
        self.__path = path

    def getPizze(self):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM PIZZA''')
            __data = self.__cur.fetchall()
            for element in __data:
                self.__pizze.append(Pizza(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__pizze

    def getPizza(self, pizza):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''SELECT * FROM PIZZA WHERE ID_PIZZA = ?''', (pizza.__idPizza,))
            __data = self.__cur.fetchone()
            self.__pizza = Pizza(*__data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
            return self.__pizza

    def create(self, pizza):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''INSERT INTO PIZZA(NAZWA,OPIS,CENA,SREDNICA,ID_PIZZA) 
                                  VALUES (?,?,?,?,?)''',
                               (pizza.__nazwa, pizza.__opis, pizza.__cena, pizza.__srednica, pizza.__idPizza))
            self.__con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def updatePizza(self, pizza):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''UPDATE PIZZA SET (NAZWA,OPIS,CENA,SREDNICA) 
                                  VALUES (?,?,?,?) WHERE ID_PIZZA = ?''',
                               (pizza.__nazwa, pizza.__opis, pizza.__cena, pizza.__srednica, pizza.__idPizza))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()

    def deletePizza(self, pizza):
        try:
            self.__con = lite.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''DELETE FROM PIZZA WHERE ID_PIZZA = ?''', (pizza.__idPizza,))
            self.__con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.__con:
                self.__con.close()
