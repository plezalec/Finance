import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import *

class Finance(QtWidgets.QWidget):#extend QWidgets
    def __init__(self):
        super().__init__()  # call constructor of parent class
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('Finance')
        self.setWindowIcon(QtGui.QIcon('slika.png'))
        self.setMinimumWidth(500)

        self.layout=QtWidgets.QVBoxLayout()
        self.button=QtWidgets.QPushButton('Hello world!')
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a_window = Finance()
    a_window.show()
    sys.exit(app.exec_())