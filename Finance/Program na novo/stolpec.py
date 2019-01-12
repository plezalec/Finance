
from termcolor import colored

class Stolpec():
    def __init__(self,stolpec_ime=None,tabela=None):
        '''

        :param stolpec_ime: str
        :param tabela: Tabela
        :param baza: Baza
        '''
        #TODO: izpis za parent
        #TODO: še pri tabelah dodaj parent, child,...
        # TODO vse lastnosti clasa definireane na začetku, tudi če se kasneje generirajo kot self.neki=None
        #TODO self.tabela je lahko tudi več različnih tabelah in imma potem več različnih setov vrednosti za različne sete vrstic ki so lahko samo v posameznih tabelah, isto tudi pri tabelah, vrstica ima lahko samo eno tabelo
        super().__init__()
        self.tabela=tabela
        self.stolpec_ime=stolpec_ime
        if tabela is not None:
            if tabela.stolpci==None:
                tabela.stolpci=[]
            tabela.stolpci.append(self)
            if tabela.vrstice is not None:
                for i in tabela.vrstice:
                    if i.vrstica_vrednosti is None:
                        i.vrstica_vrednosti=[]
                    i.vrstica_vrednosti.append(None)
            if tabela.stolpci_imena is None:
                tabela.stolpci_imena=[]
            tabela.stolpci_imena.append(self.stolpec_ime)
            if tabela.baza is not None:
                self.baza=tabela.baza
            else:
                self.baza=None
        else:
            self.baza=None
        self.stolpec=self


        self.attribute=None
        self.parent=None#Tabela
        self.parent_ime=None#str
        self.parent_stolpec=None#Stolpec
        self.parent_stolpec_ime=None#str
        self.parent_stolpec_vrednosti=None#list
        self.stolpec_vrednosti = None
        self.stolpec_vrednosti_fun()

        #self.vrednosti = self.vrednosti()

    def stolpec_pozicija_v_tabeli(self):
        if self.tabela is not None:
            stolpec_pozicija_v_tabeli=self.tabela.stolpci.index(self.stolpec)
        else:
            stolpec_pozicija_v_tabeli=None
        return stolpec_pozicija_v_tabeli

    def stolpec_vrednosti_fun(self):
        if self.tabela is not None and self.tabela.vrstice!=None:
            self.stolpec_vrednosti=[]
            for i in range(len(self.tabela.vrstice)):
                vr=self.tabela.vrstice[i].vrstica_vrednosti[self.stolpec_pozicija_v_tabeli()]
                self.stolpec_vrednosti.append(vr)
        else:
            self.stolpec_vrednosti=None

    def beri_iz_SQL(self):
        pass

    def izpis(self):
        z = '*********'
        zz = z * 25
        space = '        '
        puscica = ' ->    '
        print(z + colored('  Stolpec   ','cyan') + zz)
        print('Ime:     ' + colored(str(self.stolpec_ime),'cyan') + puscica + str(self.stolpec))
        if self.tabela is not None:
            b = colored(str(self.tabela.tabela_ime),'magenta') + puscica + str(self.tabela)
        else:
            b = str(None)
        print('Tabela:  ' + b)
        if self.baza is not None:
            b = colored(str(self.baza.baza_ime),'blue') + puscica + str(self.baza)
        else:
            b = str(None)
        print('Baza:    ' + b)
        c=[]
        d=[]
        if self.tabela!=None:
            if self.tabela.vrstice_imena!=None:
                for i in range(len(self.tabela.vrstice_imena)):
                    a=str(self.tabela.vrstice_imena[i])
                    b=str(self.stolpec_vrednosti[i])
                    while len(a)!=len(b):
                        if len(a)>len(b):
                            b+=' '
                        if len(b)>len(a):
                            a+=' '
                    c.append(a)
                    d.append(b)
                print('Vrstica: ' + colored(str(c),'yellow'))
                print('Vrednost:'+str(d))
            else:
                print('Vrstica: ' + str(self.tabela.vrstice_imena))
                print('Vrednost:'+str(self.stolpec_vrednosti))
        else:
            print('Vrstica: ' + str(None))
            print('Vrednost:' + str(self.stolpec_vrednosti))
        print()

if __name__ == "__main__":
    Stolpec().izpis()