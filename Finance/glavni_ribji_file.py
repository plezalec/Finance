import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import SQLFunkcije

class Window(QtWidgets.QWidget,QtFunkcije,SQLFunkcije):#extend QWidgets

    def __init__(self):
        super().__init__()#call constructor of parent class

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Vodenje evidenc')
        self.setWindowIcon(QtGui.QIcon('slika.png'))
        self.setGeometry(100,100,300,300)

        #osnovni objekti
        self.s=QtWidgets.QLabel('Veš kaj?')
        self.s1=QtWidgets.QLabel('ur mom gay!')
        self.b=QtWidgets.QPushButton('klik')
        self.b1=QtWidgets.QPushButton('no u')
        self.b2 =QtWidgets.QPushButton('Resetiraj')

        #combo box
        self.cb=QtWidgets.QComboBox()
        self.bombo_box_add_items(self.cb,self.dodaj('Prikaži tabelo...'))
        self.cb.setEnabled(True)
        self.cb.setMinimumSize(QtCore.QSize(130, 0))
        self.cb.activated[str].connect(self.onActivated)


        #Naredi tabelo
        #self.tableWidget =self.tabela('FinanceDataBase.db','Posel')
        [self.stack,self.tabele]=self.stacked('FinanceDataBase.db')


        #grajenje layoutou
        self.hbox=QtWidgets.QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.s)
        self.hbox.addStretch()
        self.hbox.addWidget(self.b)
        self.hbox.addStretch()

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.addStretch()
        self.hbox1.addWidget(self.s1)
        self.hbox1.addStretch()
        self.hbox1.addWidget(self.b1)
        self.hbox1.addStretch()

        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.addStretch()
        self.hbox2.addWidget(self.b2)
        self.hbox2.addStretch()

        self.hbox3 = QtWidgets.QHBoxLayout()
        #self.hbox3.addWidget(self.tableWidget)
        self.hbox3.addWidget(self.stack)
        self.hbox3.addStretch()

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.cb)
        self.vbox.addLayout(self.hbox3)


        #connect
        self.b.clicked.connect(self.btn_click)
        self.b1.clicked.connect(self.btn_click1)
        self.b2.clicked.connect(self.btn_click1)



        self.setLayout(self.vbox)
        self.show()
        #self.w.showMaximized()



    def btn_click(self):
        self.s.setText('Mačka ma rep nazaj')

    def btn_click1(self):
        sender= self.sender()
        if sender.text()=='Resetiraj':
            self.reset()
        else:
            self.s1.setText('Fafi rt!')
    def reset(self):
        self.s.setText('Veš kaj?')
        self.s1.setText('ur mom gay!')



    def bombo_box_add_items(self,combo,items):
        for i in range(len(items)):
            combo.addItem(items[i])




    def onActivated(self,text):
        if text in self.tabele:
            self.stack.setCurrentIndex(self.tabele.index(text))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    a_window=Window()
    sys.exit(app.exec_())