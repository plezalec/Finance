import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import SQLFunkcije
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

from DodajElementTabele import DodajElementTabele

class Window(QtWidgets.QWidget,QtFunkcije,SQLFunkcije):#extend QWidgets

    def __init__(self):
        super().__init__()#call constructor of parent class

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Vodenje evidenc')
        self.setWindowIcon(QtGui.QIcon('slika.png'))
        self.setGeometry(0,0,800,500)
        #postavi na sredo
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.move(800,300)



        #osnovni objekti
        self.b=QtWidgets.QPushButton('Dodaj element tabele')

        self.b.clicked.connect(self.onActivated1)

        #combo box
        self.cb=QtWidgets.QComboBox()
        self.bombo_box_add_items(self.cb,self.dodaj('Prikaži tabelo...'))
        self.cb.setEnabled(True)
        self.cb.setMinimumSize(QtCore.QSize(130, 0))
        self.cb.activated[str].connect(self.onActivated)


        #Naredi tabelo
        #self.tableWidget =self.tabela('FinanceDataBase.db','Posel')
        [self.stack,self.tabele]=self.stacked('FinanceDataBase.db')



        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox3.addWidget(self.stack)

        self.hbox4 = QtWidgets.QHBoxLayout()
        self.hbox4.addWidget(self.b)
        self.hbox4.addStretch()
        self.hbox4.addWidget(self.cb)


        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox3)



        self.setLayout(self.vbox)
        #self.dod=DodajElementTabele()


        self.dialogs=list()
        self.st_dialogs=0

        #self.w.showMaximized()



    def onActivated1(self):
        #self.dod.show()
        dialog=DodajElementTabele()
        dialog.dodaj_st(self.st_dialogs)
        self.dialogs.append(dialog)
        dialog.show()
        self.st_dialogs+=1


    def bombo_box_add_items(self,combo,items):
        for i in range(len(items)):
            combo.addItem(items[i])




    def onActivated(self,text):
        if text in self.tabele:
            self.stack.setCurrentIndex(self.tabele.index(text))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    a_window=Window()
    a_window.show()
    sys.exit(app.exec_())