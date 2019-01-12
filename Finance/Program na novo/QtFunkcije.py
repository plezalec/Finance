from PyQt5 import QtWidgets
import sys
from tabela import Tabela
from stolpec import Stolpec

#TODO Fukcija ki doda tabelo elementa Tabela
#TODO Funkcija ki izpolne class Vrstico v classu Tabela
#TODO Funkcija za izbiro atributov za stolpce Tabele za vnos podatkov v Vrstice
class QtFunkcije(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        pass

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
        print(meniji)
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
        self.polje_za_vnos_lastnosti(text,b,'ch')

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
        polje_za_vnos_lastnosti=QtWidgets.QVBoxLayout()
        lastnost_label=QtWidgets.QLabel(lastnost)
        polje_za_vnos_lastnosti.addWidget(lastnost_label)
        if attr == None:
            lastnost_vnos=QtWidgets.QLineEdit()
        if attr == 'le':
            lastnost_vnos=QtWidgets.QLineEdit()

        if attr == 'cb':
            lastnost_vnos=QtWidgets.QComboBox()

        if attr == 'ch':
            lastnost_vnos=QtWidgets.QCheckBox()
        else:
            lastnost_vnos = QtWidgets.QLineEdit()
        lastnost_label.setMaximumHeight(20)
        lastnost_vnos.setMaximumHeight(20)
        polje_za_vnos_lastnosti.addWidget(lastnost_vnos)

        return polje_za_vnos_lastnosti

    def dodajanje_vrstic(self,tabela,layout):
        a=[]
        for i in tabela.stolpci:
            a.append(self.polje_za_vnos_lastnosti(i.stolpec_ime,i.attribute))

        h_layout=self.h_layout(a,layout)
        return h_layout


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a=QtWidgets.QWidget()
    a.setMinimumSize(300,300)
    b=QtWidgets.QVBoxLayout()
    c=QtFunkcije()
    t=Tabela()
    s=Stolpec('ime',t)
    s1=Stolpec('priimek',t)
    s1.attribute='cb'
    s.attribute='ch'
    g=QtWidgets.QVBoxLayout()
    c0=c.combo_box(['prdec','prdula'],None,c.poop)
    c1=c.combo_box(['prdec','prdula'],None,c.poop)
    c2=c.combo_box(['prdec', 'prdula'], g, c.poop)
    c3=c.combo_box(['prdec', 'prdula'], g, c.poop)
    c.v_layout([c1,c0,g],b)
    c.polje_za_vnos_lastnosti('Smrad',b,'ch')
    c.dodajanje_vrstic(t,g)

    a.setLayout(b)
    a.show()
    sys.exit(app.exec_())
