
from termcolor import colored
class Vrstica():
    def __init__(self,tabela=None):
        '''

        :param tabela:
        '''
        # TODO vse lastnosti clasa definireane na začetku, tudi če se kasneje generirajo kot self.neki=None
        # TODO: ne sme se dat dvakrat iste vrstice dodat(verjetno se je že ne da)
        super().__init__()
        if tabela is None:
            print('Vrstica mora nujno imeti tabelo')

        self.baza=tabela.baza
        self.tabela=tabela
        self.vrstica=self
        self.vrstica_ime=None
        self.vrstica_vrednosti=None


        self.vrstica_ime=self.vrstica_ime_fun()
        self.dodaj_ime_vrstice_v_tabelo()
        self.vrstica_vrednosti=self.vrstica_vrednosti_fun()


    def vrstica_ime_fun(self):
        if self.tabela.vrstice_imena is not None:
            k=self.tabela.vrstice_imena[-1]
        else:
            k=0
        vrstica_ime=k+1
        return vrstica_ime

    def dodaj_ime_vrstice_v_tabelo(self):
        if self.tabela.vrstice_imena is None:
            self.tabela.vrstice_imena=[]
            self.tabela.vrstice=[]
        self.tabela.vrstice_imena.append(self.vrstica_ime)
        self.tabela.vrstice.append(self)
        if self.tabela.stolpci_imena is not None:
            for i in self.tabela.stolpci:
                if i.stolpec_vrednosti is None:
                    i.stolpec_vrednosti=[]
                i.stolpec_vrednosti.append(None)

    def vrstica_vrednosti_fun(self):
        vrstica_vrednosti=[]
        if self.tabela.stolpci is not None:
            for i in range(len(self.tabela.stolpci)):
                vrstica_vrednosti.append(None)
        return vrstica_vrednosti

    def beri_iz_SQL(self):
        pass

    def izpis(self):
        z = '*********'
        zz = z * 25
        space = '        '
        puscica = ' ->    '
        print(z + colored('  Vrstica  ','yellow') + zz)
        print('Ime:    ' + colored(str(self.vrstica_ime),'yellow') + puscica + str(self.vrstica))
        if self.tabela is not None:
            b = colored(str(self.tabela.tabela_ime),'magenta') + puscica + str(self.tabela)
        else:
            b = str(None)
        print('Tabela: ' + b)
        if self.baza is not None:
            b = colored(str(self.baza.baza_ime),'blue') + puscica + str(self.baza)
        else:
            b = str(None)
        print('Baza:   ' + b)
        c = []
        d = []
        for i in range(len(self.tabela.stolpci_imena)):
            a = str(self.tabela.stolpci_imena[i])
            b = str(self.vrstica_vrednosti[i])
            while len(a) != len(b):
                if len(a) > len(b):
                    b += ' '
                if len(b) > len(a):
                    a += ' '
            c.append(a)
            d.append(b)
        print('Stolpci:  '+colored(str(c),'cyan'))
        print('Vrednosti:'+str(d))
        print()


if __name__ == "__main__":
    Vrstica()