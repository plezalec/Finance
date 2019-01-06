import sqlite3
class SQLFunkcije():
    def __init__(self, baza):
        self.baza=baza
        self.conn=sqlite3.connect(self.baza)


    def cursor(self):
        return self.conn.cursor()
    def preberi_tabelo(self,tabela):
        stolpci=self.nastej_stolpce(tabela)
        vrstice = self.preberi_stolpec(tabela,stolpci[0])
        a=[]
        cursor=self.cursor()
        for i in range(len(vrstice)):

            cursor.execute('SELECT * FROM ' + tabela + ' WHERE rowid = ' + str(i+1))
            b=cursor.fetchone()
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


class DataBase():
    def __init__(self,database):
        '''
        Ime baze
        Imena tabel
        Seznam Tabela()

        :param database:
        '''
        self.database_name=database
        self.database=SQLFunkcije(self.database_name)

        self.imena_tabel=self.imena_tabel_init()
        self.tabele=self.tabele_init()

    def imena_tabel_init(self):
        '''
        Uporablja se samo na začetku ko bereš bazo iz SQL
        :return:
        '''
        imena_tabel=self.database.nastej_tabele()
        return imena_tabel



    def tabele_init(self):
        '''
        Uporablja se samo na začetku ko bereš bazo iz SQL
        :return:
        '''
        tabele=[]
        for i in range(len(self.imena_tabel_init())):
            tabele.append(Tabela(self.imena_tabel_init()[i],self.database_name))
        return tabele

class Tabela():
    def __init__(self,tabela,database):
        '''
        Ime baze
        Ime tabele
        Imena stolpcev
        Vsa polja
        '''
        self.database_name=database
        self.database=SQLFunkcije(self.database_name)
        self.tabela=tabela
        self.imena_stolpcev=self.imena_stolpcev_init()
        self.vrstice=self.vrstice_init()
        self.stolpci= self.stolpci_init()
        

    def imena_stolpcev_init(self):
        imena_stolpcev=self.database.nastej_stolpce(self.tabela)
        return imena_stolpcev
    def polja(self):
        polja=self.database.preberi_tabelo(self.tabela)
        return polja
    def vrstice_init(self):
        p=[]
        for i in range(len(self.polja())):
            p.append(Vrstica(i,self.tabela,self.database_name))
        return p
    def stolpci_init(self):
        p = []
        stolpci=self.imena_stolpcev
        for i in range(len(stolpci)):
            p.append(Stolpec('PoselID',self.tabela,self.database_name))
        return p

    def dodaj_vrstico(self):
        self.vrstice.append(Vrstica(self.vrstice[-1].ID+1,self.tabela,self.database))

    def dodaj_stolpec(self,stolpec):
        self.stolpci.append(Stolpec(stolpec,self.tabela,self.database))
        self.imena_stolpcev.append(stolpec)

class Vrstica():
    def __init__(self,ID,tabela,database):
        self.ID=ID
        self.tabela=tabela
        self.database=database
        self.data=SQLFunkcije(self.database)
        print(self.ID)
    def vrednosti_vrstice(self):
        vrednosti_vrstice=self.data.preberi_vrstico(self.tabela,self.ID)
        return vrednosti_vrstice
class Stolpec():
    def __init__(self,stolpec,tabela,database):
        self.stolpec=stolpec
        self.tabela=tabela
        self.database=database
        self.data=SQLFunkcije(self.database)
    def vrednosti_stolpca(self):
        vrednosti_stolpca = self.data.preberi_stolpec(self.tabela,self.stolpec)
        return vrednosti_stolpca
if __name__ == "__main__":
    a=SQLFunkcije('FinanceDataBase.db')
    d=DataBase('FinanceDataBase.db')
    t=Tabela('Posel','FinanceDataBase.db')
    v=Vrstica(2,'Posel','FinanceDataBase.db')
    s=Stolpec('PoselID','Posel','FinanceDataBase.db')

    print(d.imena_tabel)
    print(d.tabele[-1].imena_stolpcev)
