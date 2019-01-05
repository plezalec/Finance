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
        #gumbi
        self.b2 = QtWidgets.QPushButton('Shrani')
        self.b3 = QtWidgets.QPushButton('Spremeni tabelo')
        self.b3.setDisabled(True)
        self.b3.clicked.connect(self.b3Akcija)
        self.b5 = QtWidgets.QPushButton('Vnesi')
        self.b5.setDisabled(True)
        self.b5.clicked.connect(self.b5Akcija)
        self.b4 = QtWidgets.QPushButton('Prekliči')
        #combobox
        self.cb = QtWidgets.QComboBox()
        self.combo_box_add_items(self.cb,self.dodaj('Izberi tabelo elementa...'))
        self.cb.setEnabled(True)
        self.cb.setMinimumSize(QtCore.QSize(130, 0))
        self.cb.activated[str].connect(self.cbAkcija)
        #layout
        self.hlo1 = QtWidgets.QHBoxLayout()
        self.hlo1.addWidget(self.cb)
        self.hlo1.addWidget(self.b3)
        self.hlo1.addWidget(self.b5)
        self.hlo1.addStretch()
        #layout
        self.hlo2=QtWidgets.QHBoxLayout()
        self.hlo2.addStretch()
        self.hlo2.addWidget(self.b2)
        self.hlo2.addWidget(self.b4)
        #layout
        self.hlo3 = QtWidgets.QVBoxLayout()
        # layout
        self.vlo4 = QtWidgets.QVBoxLayout()
        #layout
        self.lo= QtWidgets.QVBoxLayout()
        self.lo.addLayout(self.hlo1)
        self.lo.addLayout(self.hlo3)
        self.lo.addLayout(self.vlo4)
        self.lo.addStretch()
        self.lo.addLayout(self.hlo2)

        #lastnosti okna
        self.setWindowTitle('Dodaj element')
        self.setWindowIcon(QtGui.QIcon('slika.png'))
        self.setLayout(self.lo)

    def cbAkcija(self,text):
        if text!='Izberi tabelo elementa...':
            self.cb.setDisabled(True)
            self.b3.setDisabled(False)
            self.b5.setDisabled(False)
            [self.lo1,self.text1,self.lab]=self.dodaj_vrstico_za_vnos(text)
            self.hlo3.addLayout(self.lo1)

            [self.stack, self.tabele] = self.stacked('FinanceDataBase.db')
            self.vlo4.addWidget(self.stack)
            self.stack.setCurrentIndex(self.tabele.index(text))
    def b5Akcija(self):
        self.b3.setDisabled(True)

    def b3Akcija(self):
        self.cb.setDisabled(False)
        self.b3.setDisabled(True)
        self.b5.setDisabled(True)
        self.odstrani_vrstico_za_vnos(self.text1,self.lab)
        self.stack.deleteLater()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a_window = DodajElementTabele()
    a_window.show()
    sys.exit(app.exec_())