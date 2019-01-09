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
        self.beri_podatke()


    def beri_podatke(self):
        self.imena_tabel = self.imena_tabel_init()
        self.tabele = self.tabele_init()

    def beri_imena_tabel_in_stolpce(self):

        self.imena_tabel = self.imena_tabel_init()
        self.tabele = []
        for i in range(len(self.imena_tabel_init())):
            self.tabele.append(Tabela(self.imena_tabel_init()[i], self.database_name))
            self.tabele[-1].beri_stolpce()

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
            tabele[-1].beri_podatke()
        return tabele

    def dodaj_tabelo(self,tabela):
        self.imena_tabel.append(tabela)
        self.tabele.append(Tabela(tabela,self.database_name))
        self.tabele[-1].imena_stolpcev.append('ID')
        self.tabele[-1].stolpci.append(Stolpec('ID',tabela,self.database_name))

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
        self.imena_stolpcev=[]
        self.imena_vrstic= []
        self.vrstice=[]
        self.st_vr=0
        self.parent = []
        self.parent_stolpec = []
        self.key_stolpec = []
        self.stolpci=[]
        print('klicana tabela')


    def beri_podatke(self):
        self.imena_stolpcev=self.imena_stolpcev_init()
        self.imena_vrstic = self.imena_vrstic_init()
        self.vrstice=self.vrstice_init()
        self.st_vr=len(self.vrstice)
        #self.nastej_kljuce_tabele()
        self.stolpci= self.stolpci_init()
    def beri_stolpce(self):
        self.imena_stolpcev = self.imena_stolpcev_init()

    def imena_stolpcev_init(self):
        imena_stolpcev=self.database.nastej_stolpce(self.tabela)
        return imena_stolpcev
    def imena_vrstic_init(self):
        ime_stolpca = self.database.nastej_stolpce(self.tabela)[0]
        imena_vrstic=self.database.preberi_stolpec(self.tabela,ime_stolpca)
        return imena_vrstic
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

            if stolpci[i] in self.key_stolpec:
                a=self.key_stolpec.index(stolpci[i])

                p.append(Stolpec(stolpci[i], self.tabela, self.database_name,self.parent[a]))
                p[-1].vrednosti_st()
                a+=1
            else:
                p.append(Stolpec(stolpci[i],self.tabela,self.database_name))
        return p

    def dodaj_vrstico(self,vrednosti='None'):
        ID=self.st_vr+1
        self.vrstice.append(Vrstica(ID,self.tabela,self.database_name))
        self.st_vr+=1
        for i in range(len(self.imena_stolpcev)-1):
            if vrednosti!='None':
                self.vrstice[-1].vrednosti_vrstice.append(vrednosti[i])
            else:
                self.vrstice[-1].vrednosti_vrstice.append('None')


    def dodaj_stolpec(self,stolpec):
        self.stolpci.append(Stolpec(stolpec,self.tabela,self.database))
        self.imena_stolpcev.append(stolpec)
        for i in range(self.st_vr):
            self.stolpci[-1].vrednosti_stolpca.append('None')
            self.vrstice[i].vrednosti_vrstice.append('None')
    def poveži_kljuce_tabele(self):
        cursor = self.database.cursor()
        cursor.execute('PRAGMA foreign_key_list('+self.tabela+')')

        a = cursor.fetchall()

        for i in range(len(a)):
            self.parent.append(list(a[i])[2])
            self.key_stolpec.append(list(a[i])[3])
            self.parent_stolpec.append(list(a[i])[4])
class Vrstica():
    def __init__(self,ID,tabela,database):
        self.ID=ID
        self.tabela=tabela
        self.database=database
        self.data=SQLFunkcije(self.database)
        self.vrednosti_vrstice=[ID]
    def preberi_vrstico(self):
        self.vrednosti_vrstice=self.data.preberi_vrstico(self.tabela,self.ID)
class Stolpec():
    def __init__(self,stolpec,tabela,database,parent=[None]):
        self.parent=parent


        self.stolpec=stolpec
        self.tabela=tabela
        self.database=database

        self.vrednosti_stolpca=[]
        self.vrednosti_st()

    def vrednosti(self,stolpec_za_prikaz=None):
        self.data = SQLFunkcije(self.database)
        self.vrednosti_stolpca = self.data.preberi_stolpec(self.tabela,self.stolpec)
        print('tabela')
        print(self.tabela)

        print('stolpec')
        print(self.stolpec)
        print('vrednosti stolpca')
        print(self.vrednosti_stolpca)
        if self.parent!=[None]:
            #print('-------------------------------------------')
            #print(self.parent)
            #print(self.stolpec)
            self.parent_tabela=Tabela(self.parent,self.database)
            self.parent_tabela.beri_podatke()
            self.ime_parent_IDstolpec=self.parent_tabela.imena_stolpcev[0]
            #print(self.ime_parent_IDstolpec)
            self.parent_IDstolpec=Stolpec(self.ime_parent_IDstolpec,self.parent,self.database)
            self.parent_IDstolpec.vrednosti_st()
            self.parent_tabela_vrednosti_ID_stolpca=self.parent_IDstolpec.vrednosti_stolpca
            if stolpec_za_prikaz!=None:
                self.drug_stolpec=Stolpec(stolpec_za_prikaz,self.parent,self.database)
            else:
                self.drug_stolpec=Stolpec(self.parent_tabela.imena_stolpcev[1],self.parent,self.database)
            self.drug_stolpec.vrednosti_st()
            #print(self.vrednosti_stolpca)
            #print(self.parent_tabela_vrednosti_ID_stolpca)
            self.nove=self.drug_stolpec.vrednosti_stolpca
            #print(self.nove)
            #self.parent=[None]# ???? mogoče je to treba !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for i in range(len(self.vrednosti_stolpca)):
                if self.vrednosti_stolpca[i]!='None':
                    mesto=self.parent_tabela_vrednosti_ID_stolpca.index(self.vrednosti_stolpca[i])
                    self.vrednosti_stolpca[i]=str(self.nove[mesto]).replace('\'','')


                    #print(self.vrednosti_stolpca)
            #print(self.vrednosti_stolpca[i])

            #print(self.tabela)
            #print(self.stolpec)
            #print(self.parent_tabela.tabela)
            #print(self.parent_IDstolpec.stolpec)
            #print()

    def  vrednosti_st(self):
        self.vrednosti()

    #def pridobi_parent(self):
    #    cursor = self.database.cursor()
    #    cursor.execute('PRAGMA foreign_key_list('+self.tabela+')')

     #   a = cursor.fetchall()

      #  for i in range(len(a)):
       #     self.parent.append(list(a[i])[2])
        #    self.key_stolpec.append(list(a[i])[3])
         #   self.parent_stolpec.append(list(a[i])[4])


if __name__ == "__main__":
    a=SQLFunkcije('FinanceDataBase.db')
    d=DataBase('FinanceDataBase.db')
    tabele=d.imena_tabel
    for i in range(len((tabele))):
        t=Tabela(tabele[i],'FinanceDataBase.db')
        t.poveži_kljuce_tabele()
        t.beri_podatke()
        for j in range(len(t.imena_stolpcev)):

            print(t.stolpci[j].vrednosti_stolpca)
    v=Vrstica(2,'Posel','FinanceDataBase.db')
    s=Stolpec('PoselID','Posel','FinanceDataBase.db')