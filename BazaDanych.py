# !/usr/bin/python
from Modele import Klient
import sqlite3 as lite



con = None

try:
    con = lite.connect('Database/RadoslawMadrzakBazaDanych.sqlite3')

    cur = con.cursor()
    cur.execute('SELECT * FROM "PIZZA"')

    data = cur.fetchall()#.__str__()

    print "SQLite version: %s" % data.__str__()
    for i in data:
        for j in i:
            print "item1: ", j

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()