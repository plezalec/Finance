import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import SQLFunkcije

class DodajElementTabele(QtWidgets.QWidget,QtFunkcije):#extend QWidgets
    def __init__(self):
        super().__init__()  # call constructor of parent class
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('Dodaj element')
        self.setWindowIcon(QtGui.QIcon('slika.png'))

        self.b1=QtWidgets.QPushButton('Dodaj')
        self.b2 = QtWidgets.QPushButton('Shrani')
        self.b3 = QtWidgets.QPushButton('Spremeni')

        self.b4 = QtWidgets.QPushButton('Prekliči')
        self.b3.setDisabled(True)

        self.cb = QtWidgets.QComboBox()


        self.combo_box_add_items(self.cb,self.dodaj('Izberi tabelo elementa...'))
        self.cb.setEnabled(True)
        self.cb.setMinimumSize(QtCore.QSize(130, 0))



        self.hlo1 = QtWidgets.QHBoxLayout()
        self.hlo1.addWidget(self.cb)
        self.hlo1.addWidget(self.b3)
        self.hlo1.addStretch()

        self.hlo2=QtWidgets.QHBoxLayout()
        self.hlo2.addStretch()
        self.hlo2.addWidget(self.b1)
        self.hlo2.addWidget(self.b2)
        self.hlo2.addWidget(self.b4)

        self.hlo3 = QtWidgets.QVBoxLayout()




        self.lo= QtWidgets.QVBoxLayout()
        self.lo.addLayout(self.hlo1)
        self.lo.addLayout(self.hlo3)
        self.lo.addStretch()
        self.lo.addLayout(self.hlo2)
        self.setLayout(self.lo)


        self.cb.activated[str].connect(self.onActivated)

        self.b3.clicked.connect(self.onActivated1)

    def dodaj_st(self,st):
        self.setGeometry(0,35+st*338, 800, 300)


    def onActivated(self,text):
        if text!='Izberi tabelo elementa...':
            self.cb.setDisabled(True)
            self.b3.setDisabled(False)
            [self.lo1,self.text1,self.lab]=self.dodajvrsticozavnos(text)
            self.hlo3.addLayout(self.lo1)

    def dodajvrsticozavnos(self,tabela):
        vrstica=QtWidgets.QVBoxLayout()
        zgoraj=QtWidgets.QHBoxLayout()
        spodaj=QtWidgets.QHBoxLayout()
        vrstica.addLayout(zgoraj)
        vrstica.addLayout(spodaj)
        b=[]
        l=[]
        a=SQLFunkcije('FinanceDataBase.db')
        stolpci=a.nastej_stolpce(tabela)
        for i in range(len(stolpci)):
            b.append(QtWidgets.QLineEdit())
            l.append(QtWidgets.QLabel(stolpci[i]))
            spodaj.addWidget(b[-1])
            zgoraj.addWidget(l[-1])
        return vrstica,b,l
    def onActivated1(self):
        self.cb.setDisabled(False)
        self.b3.setDisabled(True)
        self.delete(self.text1)
        self.delete(self.lab)
    def delete(self,a):
        for i in range(len(a)):
            b=a[i]
            b.deleteLater()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a_window = DodajElementTabele()
    a_window.show()
    sys.exit(app.exec_())