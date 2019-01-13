from PyQt5 import QtWidgets,QtCore
import sys
from tabela import Tabela
from stolpec import Stolpec

#TODO Fukcija ki doda tabelo elementa Tabela
#TODO Funkcija ki izpolne class Vrstico v classu Tabela
#TODO Funkcija za izbiro atributov za stolpce Tabele za vnos podatkov v Vrstice
#tODO Naredi objekt tabela
#TODO Uporabniški vmesnik za dodajanje tabel in stolpcev
class QtFunkcije(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


    def izpis(self):
        pass

    def combo_box(self,meniji,layout=None,funkcija=None):
        '''
        Hitro kreiranje QComboBox
        :param meniji:
        :param layout:
        :param funkcija:
        :return:
        '''
        combo_box=QtWidgets.QComboBox()
        combo_box.setFixedHeight(20)
        w=[]
        for i in meniji:
            combo_box.addItem(i)
            w.append(len(i))
        combo_box.setFixedWidth(max(w)*12)
        if layout is not None:
            layout.addWidget(combo_box)
        if funkcija is not None:
            combo_box.activated[str].connect(funkcija)
        return combo_box

    def h_layout(self,widgets_and_layouts,layout=None):
        '''
        Hitro dodajanje elementov v QHBoxLayout
        :param widgets_and_layouts:
        :param layout:
        :return:
        '''
        h_layout=QtWidgets.QHBoxLayout()

        for i in widgets_and_layouts:
            if isinstance(i,(QtWidgets.QHBoxLayout,QtWidgets.QVBoxLayout,QtWidgets.QGridLayout)):
                h_layout.addLayout(i)
            else:
                h_layout.addWidget(i)

        if layout is not None:
            layout.addLayout(h_layout)
        return h_layout

    def v_layout(self,widgets_and_layouts,layout=None):
        '''
        Hitro dodajanje elementov v QVBoxLayout
        :param widgets_and_layouts:
        :param layout:
        :return:
        '''
        v_layout=QtWidgets.QVBoxLayout()

        for i in widgets_and_layouts:
            if isinstance(i,(QtWidgets.QHBoxLayout,QtWidgets.QVBoxLayout,QtWidgets.QGridLayout)):
                v_layout.addLayout(i)
            else:
                v_layout.addWidget(i)

        if layout is not None:
            layout.addLayout(v_layout)
        return v_layout

    def quit_button(self):
        btn=QtWidgets.QPushButton('Izhod',self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return btn

class Qt_tabela(QtWidgets.QWidget):
    def __init__(self,tabela,layout):
        super().__init__()
        self.layout=layout
        self.tabela=tabela
        self.tab = []
        self.stevec = 0
        self.polja = []
        self.dodaj_lastnost = []

        self.dodajanje_vrstic()
        self.layout.addWidget(self.tabela_fun())

    def izpis(self):
        pass

    def polje_za_vnos_lastnosti(self,lastnost,attr=None):
        dodaj_lastnost=Dodaj_lastnost(self.stevec,self,attr)
        self.dodaj_lastnost.append(dodaj_lastnost)
        polje_za_vnos_lastnosti=QtWidgets.QVBoxLayout()
        self.lastnost_label=QtWidgets.QLabel(lastnost)
        polje_za_vnos_lastnosti.addWidget(self.lastnost_label)
        polje_za_vnos_lastnosti.addWidget(dodaj_lastnost.lastnost_vnos)
        self.stevec+=1
        self.lastnost_label.setFixedHeight(20)
        return polje_za_vnos_lastnosti

    def dodajanje_vrstic(self):
        vlayout = QtWidgets.QHBoxLayout()
        hlayout=QtWidgets.QHBoxLayout()
        for i in self.tabela.stolpci:
            self.tab.append(None)
            hlayout.addLayout(self.polje_za_vnos_lastnosti(i.stolpec_ime,i.attribute))
        button = QtWidgets.QPushButton('Zapiši')
        button.clicked.connect(self.zapisi_vrstico)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(button)
        self.layout.addLayout(vlayout)

    def tabela_fun(self):
        self.tabela_widget=QtWidgets.QTableWidget()
        if self.tabela.vrstice!=None:
            self.row_count=len(self.tabela.vrstice)
            self.tabela_widget.setRowCount(len(self.tabela.vrstice))
            k=[]
            for i in self.tabela.vrstice_imena:
                k.append(str(i))

                self.tabela_widget.setVerticalHeaderLabels(k)
        if self.tabela.stolpci!=None:
            self.tabela_widget.setColumnCount(len(self.tabela.stolpci))
            self.tabela_widget.setHorizontalHeaderLabels(self.tabela.stolpci_imena)
            self.polja = []

            for i in range(len(self.tabela.vrstice)):
                self.polja.append([])

                for j in range(len(self.tabela.stolpci)):
                    if self.tabela.vrstice[i].vrstica_vrednosti[j]!=None:
                        self.polja[-1].append(QtWidgets.QTableWidgetItem(str(self.tabela.vrstice[i].vrstica_vrednosti[j])))
                        self.tabela_widget.setItem(i, j, self.polja[-1][-1])
            for i in self.tabela.vrstice:
                pass
        #TODO poglej si QTableWidgetItem QTableView QTableWidgetSelectionRange QtableWidget
        return self.tabela_widget

    def zapisi_vrstico(self):
        self.tabela_widget.insertRow(self.row_count)
        self.polja.append([])
        self.tabela.dodaj_vrstico()
        for j in range(len(self.tab)):
            self.tabela.vrstice[-1].vrstica_vrednosti[j]=self.tab[j]
            self.polja[-1].append(QtWidgets.QTableWidgetItem(str(self.tabela.vrstice[-1].vrstica_vrednosti[j])))
            self.tabela_widget.setItem(self.row_count, j, self.polja[-1][-1])
        self.row_count+=1

class Dodaj_lastnost(QtWidgets.QWidget):
    def __init__(self,stolpec_stevilo,qt_tabela,attr):
        super().__init__()
        self.stolpec_stevilo=stolpec_stevilo
        self.qt_tabela=qt_tabela
        self.lastnost_vnos=None
        self.attr=attr
        self.setup()

    def setup(self):
        if self.attr == 'le':
            self.lastnost_vnos=QtWidgets.QLineEdit()
            self.lastnost_vnos.textChanged.connect(self.le_vnos)

        elif self.attr == 'cb':
            self.lastnost_vnos=QtWidgets.QComboBox()
            self.lastnost_vnos.activated[str].connect(self.cb_vnos)

        elif self.attr == 'ch':
            self.lastnost_vnos=QtWidgets.QCheckBox()
            self.lastnost_vnos.stateChanged.connect(self.ch_vnos)

        else:
            self.lastnost_vnos=QtWidgets.QLineEdit()
            self.lastnost_vnos.textChanged[str].connect(self.le_vnos)

            self.lastnost_vnos.setFixedHeight(20)


    def izpis(self):
        print('Izpis')
    def le_vnos(self, text):

        self.qt_tabela.tab[self.stolpec_stevilo] = text

    def cb_vnos(self, text):
        self.qt_tabela.tab[self.stolpec_stevilo] = text

    def ch_vnos(self, text):
        if text!=0:
            zapis='Da'
        else:
            zapis='Ne'
        self.qt_tabela.tab[self.stolpec_stevilo] = zapis

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a=QtWidgets.QWidget()
    a.setMinimumSize(300,300)
    b=QtWidgets.QVBoxLayout()
    c=QtFunkcije()



    t=Tabela('Stoški')
    i=Stolpec('ime',t)
    i.attribute='le'
    m=Stolpec('mesečni',t)
    m.attribute='ch'
    v=Stolpec('vrednost',t)

    k=Stolpec('kategorija',t)
    k.attribute='cb'


    t.tabela_ime='tabela'
    t.dodaj_vrstico()
    v=t.dodaj_vrstico()
    v.vrstica_vrednosti=[1,2,3,4]
    t.dodaj_vrstico()


    #c.dodajanje_vrstic(t, b)
    #b.addWidget(c.tabla(t))
    T=Qt_tabela(t,b)

    b.addWidget(c.quit_button())

    a.setLayout(b)
    a.show()
    sys.exit(app.exec_())
