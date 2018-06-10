import sqlite3 as lite
import sys

from Modele.Pizza import Pizza


class PizzaWidokModel:
    def __init__(self, pizze=None, pizza=None, con=None, cur=None,
                 path='Database/RadoslawMadrzakBazaDanych.sqlite3'):
        if pizze is None:
            pizze = []

        self.pizze = pizze
        self.pizza = pizza
        self.con = con
        self.cur = cur
        self.path = path

    def getPizze(self):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM PIZZA''')
            data = self.cur.fetchall()
            for element in data:
                self.pizze.append(Pizza(*element))

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.pizze

    def getPizza(self, pizza):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''SELECT * FROM PIZZA WHERE ID_PIZZA = ?''', (pizza.idPizza,))
            data = self.cur.fetchone()
            self.pizza = Pizza(*data)

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
            return self.pizza

    def create(self, pizza):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''INSERT INTO PIZZA(NAZWA,OPIS,CENA,SREDNICA) 
                                  VALUES (?,?,?,?)''',
                               (pizza.nazwa, pizza.opis, pizza.cena, pizza.srednica))
            self.con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def updatePizza(self, pizza):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''UPDATE PIZZA SET NAZWA = ?,OPIS = ?,CENA = ?,SREDNICA = ? 
                                  WHERE ID_PIZZA = ?''',
                               (pizza.nazwa, pizza.opis, pizza.cena, pizza.srednica, pizza.idPizza))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()

    def deletePizza(self, pizza):
        try:
            self.con = lite.connect(self.path)
            self.cur = self.con.cursor()
            self.cur.execute('''DELETE FROM PIZZA WHERE ID_PIZZA = ?''', (pizza.idPizza,))
            self.con.commit()

        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()
