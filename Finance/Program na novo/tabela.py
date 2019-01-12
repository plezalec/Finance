from vrstica import Vrstica
from stolpec import Stolpec
from termcolor import colored
import copy
# TODO vse lastnosti clasa definireane na začetku, tudi če se kasneje generirajo kot self.neki=None
#TODO: izpis za parent, child,...
# TODO: ko kreiraš oz dodaš stolpec oz povezavo naje se tudi povsod vse posodobi
class Tabela():
    def __init__(self, tabela_ime=None, baza=None):
        '''

        :param tabela_ime: str
        :param baza: Baza
        '''
        super().__init__()
        self.baza = baza#Baza
        self.tabela_ime = tabela_ime
        if baza is not None:
            if baza.tabele_imena is None:
                baza.tabele_imena=[]
                baza.tabele=[]

            baza.tabele_imena.append(tabela_ime)
            baza.tabele.append(self)

        self.tabela=self

        self.parents=None
        self.childern=None
        self.parents_imena=None
        self.children_imena=None
        self.parents_stolpci=None
        self.parents_stolpci_imena=None
        self.children_stolpci=None
        self.childern_stolpci_imena=None
        self.vrstice_imena = None
        self.vrstice = None
        self.stolpci_imena = None
        self.stolpci = None




    def parents_imena(self):#se nanaša na Baza(baza)
        pass

    def vrstice(self):
        vrstice=[]
        if self.vrstice_imena is not None:
            for i in self.vrstice_imena:
                vrstice.append(Vrstica(i,self.tabela_ime,self.baza))
        return vrstice

    def stolpci(self):
        stolpci=[]
        if self.stolpci_imena is not None:
            for i in self.stolpci_imena:
                stolpci.append(Stolpec(i,self.tabela_ime,self.baza))
        return stolpci

    def dodaj_vrstico(self):
        vrstica=Vrstica(self)
        return vrstica

    def dodaj_stolpec(self,stolpec=None):

        if self.stolpci == None:
            self.stolpci=[]
        if stolpec is None:
            a=True
            stolpec=Stolpec(None,self)
        else:
            if stolpec in self.stolpci:
                print(colored('POZOR!: Isti stolpec je dodana večkrat v isto tabelo','red'))
            a=False
        if self.stolpci_imena is None:
            self.stolpci_imena = []
        self.stolpci_imena.append(stolpec.stolpec_ime)
        self.stolpci.append(stolpec)
        stolpec.tabela=self
        return stolpec

    def dodaj_podoben_stolpec(self,podoben_stolpec):
        stolpec=self.dodaj_stolpec(copy.copy(podoben_stolpec))
        stolpec.stolpec=stolpec
        stolpec.stolpec_vrednosti=None
        if self.vrstice!=None:
            for i in self.vrstice:
                i.vrstica_vrednosti.append(None)
        stolpec.stolpec_vrednosti_fun()
        return stolpec

    def izpis(self):
        z = '*********'
        zz=z*25
        space = '        '
        puscica = ' ->    '
        print(z + colored('  Tabela  ','magenta') + zz)
        print('Ime:    '+colored(str(self.tabela_ime),'magenta')+puscica+str(self.tabela))
        if self.baza is not None:
            b=colored(str(self.baza.baza_ime),'blue') + puscica + str(self.baza)
        else:
            b=str(None)
        print('Baza:   '+b)
        print('Stolpci:')
        if self.stolpci_imena is not None:
            for i in range(len(self.stolpci_imena)):
                m = max(len(str(w)) for w in self.stolpci_imena)
                k = m - len(str(self.stolpci_imena[i]))
                s = ' ' * k
                print(space+colored(str(self.stolpci_imena[i]),'cyan')+s+puscica+str(self.stolpci[i]))
        else:
            print(space+str(None))
        print('Vrstice:')
        if self.vrstice_imena is not None:
            for i in range(len(self.vrstice_imena)):
                m = max(len(str(w)) for w in self.vrstice_imena)
                k = m - len(str(self.vrstice_imena[i]))
                s = ' ' * k
                print(space + colored(str(self.vrstice_imena[i]),'yellow') + s + puscica + str(self.vrstice[i]))
        else:
            print(space + str(None))
        print()


if __name__ == "__main__":
    Tabela().izpis()
