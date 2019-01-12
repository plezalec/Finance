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
        self.setup()

    def setup(self):
        self.tab=[]
        self.stevec=0
        self.polja=[]
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

    def poop(self,text):
        '''
        Testna funkcija
        :param text:
        :return:
        '''
        a=self.polje_za_vnos_lastnosti(text,self.layout,'ch')
        self.layout.addLayout(a)

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

    def polje_za_vnos_lastnosti(self,lastnost,attr=None,funkcija=None):
        dodaj_lastnost=Dodaj_lastnost(self.stevec,self)
        self.polja.append(dodaj_lastnost)
        self.stevec+=1

        polje_za_vnos_lastnosti=QtWidgets.QVBoxLayout()
        lastnost_label=QtWidgets.QLabel(lastnost)
        polje_za_vnos_lastnosti.addWidget(lastnost_label)
        if attr == None:
            lastnost_vnos=QtWidgets.QLineEdit()
            lastnost_vnos.textChanged[str].connect(dodaj_lastnost.le_vnos)
        elif attr == 'le':
            lastnost_vnos=QtWidgets.QLineEdit()
            lastnost_vnos.textChanged.connect(dodaj_lastnost.le_vnos)

        elif attr == 'cb':
            lastnost_vnos=QtWidgets.QComboBox()
            lastnost_vnos.activated[str].connect(dodaj_lastnost.cb_vnos)

        elif attr == 'ch':
            lastnost_vnos=QtWidgets.QCheckBox()
            lastnost_vnos.stateChanged.connect(dodaj_lastnost.ch_vnos)
        else:
            pass
        lastnost_label.setFixedHeight(20)
        lastnost_vnos.setFixedHeight(20)
        polje_za_vnos_lastnosti.addWidget(lastnost_vnos)

        return polje_za_vnos_lastnosti

    def dodajanje_vrstic(self,tabela,layout):
        a=[]
        for i in tabela.stolpci:
            self.tab.append(None)
            a.append(self.polje_za_vnos_lastnosti(i.stolpec_ime,i.attribute))

        vlayout=QtWidgets.QVBoxLayout()
        h_layout=self.h_layout(a,vlayout)
        button=QtWidgets.QPushButton('Zapiši')
        button.clicked.connect(self.zapisi_vrstico)
        vlayout.addWidget(button)
        layout.addLayout(vlayout)
        return vlayout

    def tabla(self,tabela,layout=None):
        self.tabela=tabela
        self.tabela_widget=QtWidgets.QTableWidget()
        if layout!=None:
            layout.AddWidget(self.tabela_widget)
        if tabela.vrstice!=None:
            self.row_count=len(tabela.vrstice)
            self.tabela_widget.setRowCount(len(tabela.vrstice))
            k=[]
            for i in tabela.vrstice_imena:
                k.append(str(i))

                self.tabela_widget.setVerticalHeaderLabels(k)
        if tabela.stolpci!=None:
            self.tabela_widget.setColumnCount(len(tabela.stolpci))
            self.tabela_widget.setHorizontalHeaderLabels(tabela.stolpci_imena)
            self.polja = []

            for i in range(len(tabela.vrstice)):
                self.polja.append([])

                for j in range(len(tabela.stolpci)):
                    if tabela.vrstice[i].vrstica_vrednosti[j]!=None:
                        self.polja[-1].append(QtWidgets.QTableWidgetItem(str(tabela.vrstice[i].vrstica_vrednosti[j])))
                        self.tabela_widget.setItem(i, j, self.polja[-1][-1])
            for i in tabela.vrstice:
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
            #self.tabela.vrstice[-1].izpis()
        self.row_count+=1



    def quit_button(self):
        btn=QtWidgets.QPushButton('Izhod',self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return btn

class Qt_tabela(QtWidgets.QWidget):
    def __init__(self,stolpec_stevilo,qt_funkcije):
        super().__init__()
        self.tab = []
        self.stevec = 0
        self.polja = []

    def izpis(self):

        pass

class Dodaj_lastnost(QtWidgets.QWidget):
    def __init__(self,stolpec_stevilo,qt_funkcije):
        super().__init__()
        self.stolpec_stevilo=stolpec_stevilo
        self.qt=qt_funkcije

    def izpis(self):

        pass

    def le_vnos(self, text):
        self.qt.tab[self.stolpec_stevilo] = text

    def cb_vnos(self, text):
        self.qt.tab[self.stolpec_stevilo] = text

    def ch_vnos(self, text):
        self.qt.tab[self.stolpec_stevilo] = text

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


    c.dodajanje_vrstic(t, b)
    b.addWidget(c.tabla(t))


    b.addWidget(c.quit_button())

    a.setLayout(b)
    a.show()
    sys.exit(app.exec_())
