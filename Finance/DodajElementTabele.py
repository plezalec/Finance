import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import SQLFunkcije

class Window(QtWidgets.QWidget,QtFunkcije):#extend QWidgets
    def __init__(self):
        super().__init__()  # call constructor of parent class

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dodaj element')
        self.setWindowIcon(QtGui.QIcon('slika.png'))
        self.setGeometry(100, 100, 300, 300)

        self.b1=QtWidgets.QPushButton('Dodaj')
        self.b2 = QtWidgets.QPushButton('Shrani')

        self.cb = QtWidgets.QComboBox()


        self.combo_box_add_items(self.cb,self.dodaj('Izberi tabelo elementa...'))
        self.cb.setEnabled(True)
        self.cb.setMinimumSize(QtCore.QSize(130, 0))


        self.hlo1 = QtWidgets.QHBoxLayout()
        self.hlo1.addWidget(self.cb)
        self.hlo1.addStretch()

        self.hlo2=QtWidgets.QHBoxLayout()
        self.hlo2.addStretch()
        self.hlo2.addWidget(self.b1)
        self.hlo2.addWidget(self.b2)

        self.lo= QtWidgets.QVBoxLayout()
        self.lo.addLayout(self.hlo1)
        self.lo.addStretch()
        self.lo.addLayout(self.hlo2)
        self.setLayout(self.lo)

        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec_())