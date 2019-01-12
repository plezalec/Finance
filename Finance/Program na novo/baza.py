from tabela import Tabela
from stolpec import Stolpec
from termcolor import colored
import copy


# TODO: vse lastnosti clasa definireane na začetku, tudi če se kasneje generirajo kot self.neki=None
# TODO: dodaj za parents and children
# TODO: izpis za parent, child,...

class Baza():
    def __init__(self, baza_ime=None):
        '''

        :param baza_ime: str
        '''
        super().__init__()
        self.baza_ime = baza_ime
        self.baza = self
        self.prebrano_iz_SQL = False
        self.neshranjene_spremembe = False
        self.povezave = None
        self.tabele_imena = None
        self.tabele = None



    def dodaj_tabelo(self, tabela=None):  # še funkcija dodaj [tabele]
        if tabela == None:
            a = True
            tabela = Tabela(None, self)
        else:
            if tabela in self.tabele:
                print(colored('POZOR!: Ista tabela je dodana večkrat v isto bazo', 'red'))
            a = False
            self.tabele.append(tabela)
            if self.tabele_imena is None:
                self.tabele_imena = []
            self.tabele_imena.append(tabela.tabela_ime)
        if a == True:
            return tabela

    def dodaj_podobno_tabelo(self,podobna_tabela):
        tabela=copy.copy(podobna_tabela)
        tabela.vrstice=None
        tabela.vrstice_imena=None
        tabela.baza=self
        tabela.tabela=tabela
        if self.tabele_imena is None:
            self.tabele_imena=[]
            self.tabele = []
        self.tabele_imena.append(tabela.tabela_ime)
        self.tabele.append(tabela)
        return tabela

    def beri_iz_SQL(self, SQL_baza):
        self.prebrano_iz_SQL = True

    def izpis(self):
        z = '*********'
        zz = z * 25
        space = '        '
        puscica = ' ->    '
        print(z + colored('  Baza  ', 'blue') + zz)
        print('Ime:    ' + colored(str(self.baza_ime), 'blue') + puscica + str(self.baza))
        print('Tabele: ')
        if self.tabele_imena is not None:
            for i in range(len(self.tabele_imena)):
                m = max(len(str(w)) for w in self.tabele_imena)
                k = m - len(str(self.tabele_imena[i]))
                s = ' ' * k
                print(space + colored(str(self.tabele_imena[i]), 'magenta') + s + puscica + str(self.tabele[i]))

        else:
            print(space + str(None))

        print('Prebrano iz SQL:       ' + str(self.prebrano_iz_SQL))
        print('Neshranjene spremembe: ' + str(self.neshranjene_spremembe))
        print()


if __name__ == "__main__":
    b = Baza('Aladeen')
    b.izpis()
    t=Tabela('Neki')
    t.dodaj_vrstico()
    t.dodaj_vrstico()
    t.dodaj_vrstico()
    t.dodaj_vrstico()
    t.dodaj_vrstico()
    t1=Tabela('Neki druzga')
    t1.dodaj_vrstico()
    t1.dodaj_vrstico()
    t1.dodaj_vrstico()
    s1=Stolpec('neki bolšga')
    s1.izpis()
    s2=t.dodaj_podoben_stolpec(s1)
    s3=t1.dodaj_podoben_stolpec(s2)
    s1.izpis()
    s2.izpis()
    s3.izpis()