import csv
import sqlite3

conn = sqlite3.connect('FinanceDataBase.db')
c = conn.cursor()
d = conn.cursor()
def preberi_tabelo(cursor,tabela):
    cursor.execute('SELECT * FROM '+tabela)
def preberi_stolpec(cursor,tabela,stolpec):
    cursor.execute('SELECT '+stolpec+' FROM ' + tabela)

preberi_tabelo(c,'Posel')
preberi_stolpec(d,'Posel','PoselID,PoselIme')
print(d.fetchone())
print(c.fetchall())
print(d.fetchone())
print(d.fetchone())