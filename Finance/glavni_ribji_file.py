import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import SQLFunkcije
from PyQt5.QtWidgets import QDesktopWidget

from DodajElementTabele import DodajElementTabele
from DodajPredlogo import DodajPredlogo
from DodajPrikaz import DodajPrikaz

class Window(QtWidgets.QWidget,QtFunkcije):#extend QWidgets

    def __init__(self):
        super().__init__()#call constructor of parent class

        self.init_ui()

    def init_ui(self):
        #gumb
        self.b=QtWidgets.QPushButton('Dodaj element tabele')
        self.b.setToolTip('Dodaj element tabele')
        self.b.clicked.connect(self.onActivated1)

        self.b1 = QtWidgets.QPushButton('Dodaj predlogo')
        self.b1.clicked.connect(self.dodaj_predlogo)
        self.b2 = QtWidgets.QPushButton('Dodaj prikaz')
        self.b2.clicked.connect(self.dodaj_prikaz)

        #combo box
        self.cb=QtWidgets.QComboBox()
        self.combo_box_add_items(self.cb,self.dodaj('Prikaži tabelo...'))
        self.cb.setEnabled(True)
        self.cb.setMinimumSize(QtCore.QSize(130, 0))
        self.cb.activated[str].connect(self.onActivated)
        #stack tabel
        [self.stack,self.tabele]=self.stacked('FinanceDataBase.db')
        #hbox3
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox3.addWidget(self.stack)
        #hbox4
        self.hbox4 = QtWidgets.QHBoxLayout()
        self.hbox4.addWidget(self.b)
        self.hbox4.addWidget(self.b1)
        self.hbox4.addWidget(self.b2)
        self.hbox4.addStretch()
        self.hbox4.addWidget(self.cb)
        #vbox
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox3)

        #ostale nastavitve okna
        self.setWindowTitle('Vodenje evidenc')
        self.setWindowIcon(QtGui.QIcon('slika.png'))
        self.setGeometry(800,300,800,500)
        self.setLayout(self.vbox)
        self.dialogs=list()
        self.st_dialogs=0
        self.dodaj_pr = DodajPredlogo()

        self.dodaj_prikaz = QtWidgets.QMainWindow()
        ui = DodajPrikaz()
        ui.setupUi(self.dodaj_prikaz)


    def onActivated1(self):
        dialog=DodajElementTabele()
        dialog.razvrsti_okno(self.st_dialogs)
        self.dialogs.append(dialog)
        dialog.show()
        self.st_dialogs+=1
        if self.st_dialogs>=3:
            self.st_dialogs-=3

    def onActivated(self,text):
        if text in self.tabele:
            self.stack.setCurrentIndex(self.tabele.index(text))

    def dodaj_predlogo(self):
        self.dodaj_pr.show()
    def dodaj_prikaz(self):
        self.dodaj_prikaz.show()
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('slika.png'))
    a_window=Window()
    a_window.show()
    sys.exit(app.exec_())