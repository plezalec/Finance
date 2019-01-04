import sqlite3
class SQLFunkcije():
    def __init__(self, baza):
        self.baza=baza
        self.conn=sqlite3.connect(self.baza)


    def cursor(self):
        return self.conn.cursor()
    def preberi_tabelo(self,tabela):
        vrstice=self.preberi_indeks(tabela)
        stolpci=self.nastej_stolpce(tabela)
        a=[]
        cursor=self.cursor()
        for i in range(len(vrstice)):

            cursor.execute('SELECT * FROM ' + tabela + ' WHERE rowid = ' + str(i+1))
            b=cursor.fetchone()
            #print(b)
            a.append(str(b[0]))
            a[i]=[a[i]]
            for j in range(len(stolpci)-1):
                pass
                a[i].append(str(b[j+1]))
        return a

        #return cursor.fetchall()
    def preberi_vrstico(self,tabela,vrstica):
        cursor=self.cursor()
        cursor.execute('SELECT * FROM '+tabela+' WHERE rowid = '+str(vrstica))
        a=cursor.fetchone()
        return a

    def preberi_stolpec(self,tabela, stolpec):
        cursor=self.cursor()
        cursor.execute('SELECT ' + stolpec + ' FROM ' + tabela)
        b = []
        i = 0
        a = cursor.fetchone()
        while a != None:
            b.append(str(a)[1:-2])
            a = cursor.fetchone()
        return b
    def preberi_indeks(self,tabela):
        c=self.preberi_stolpec(tabela,self.nastej_stolpce(tabela)[0])
        b=[]
        for i in range(len(c)):
            b.append(str(c[i]))
        return b
    def nastej_stolpce(self,tabela):
        cursor=self.cursor()
        cursor.execute('PRAGMA table_info(' + tabela + ')')
        b = []
        i = 0
        a = cursor.fetchone()
        while a != None:
            b.append(a[1])
            a = cursor.fetchone()
        return b

    def nastej_tabele(self):
        cursor=self.cursor()
        cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
        b=[]
        a=cursor.fetchone()
        i=0
        a = cursor.fetchone()
        while a!=None:

            c=str(a)[2:-3]
            b.append(c)
            a = cursor.fetchone()
        return b
    def pripravi_tabelo_za_zapis(self,tabela):
        stolpci=self.nastej_stolpce(tabela)
        ID=self.preberi_stolpec(tabela,stolpci[0])
        a=len(stolpci)
        b=len(ID)
        c=self.preberi_tabelo(tabela)
        return [a]

if __name__ == "__main__":
    a=SQLFunkcije('FinanceDataBase.db')

    pr=a.preberi_tabelo('Posel')
    print(pr)