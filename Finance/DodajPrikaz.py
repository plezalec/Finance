# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pavel\Documents\Business\Finance\Finance\DodajPrikaz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from SQLFunkcije import Tabela,DataBase,Stolpec

class DodajPrikaz(QtWidgets.QWidget,QtFunkcije):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Dodaj prikaz")
        MainWindow.setWindowIcon(QtGui.QIcon('slika.png'))
        MainWindow.setGeometry(800, 300, 800, 500)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.hbox2 = QtWidgets.QVBoxLayout(self.frame)
        self.hbox2.addLayout(self.gridLayout)

        self.hbox=QtWidgets.QVBoxLayout()
        self.hbox2.addLayout(self.hbox)

        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setDisabled(True)
        self.gridLayout.addWidget(self.comboBox_3, 0, 5, 1, 1)
        self.comboBox_3.activated[str].connect(self.action3)

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 10, 1, 1)
        self.pushButton_4.setDisabled(True)
        self.pushButton_4.clicked.connect(self.action2)

        self.pushButton_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_1.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 9, 1, 1)
        self.pushButton_1.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 11, 1, 1)
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.clicked.connect(self.action4)
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout.addWidget(self.comboBox_8, 0, 1, 1, 1)
        self.comboBox_8.activated[str].connect(self.action1)

        self.combo_box_add_items(self.comboBox_8,self.dodaj('Izberi tabelo...'))

        self.label_4.raise_()
        self.comboBox_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_1.raise_()
        self.comboBox_8.raise_()
        self.verticalLayout.addWidget(self.frame)



        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.hbox2.addWidget(self.tableWidget)

        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Sam definiral spremenljivke
        self.dodajanje_filtrov=[]#sem se shranjujejo filtri
        self.stevec_dodaj_filter1=1

        self.pozicije_dodaj_stolpec=[[1]]


        self.dodajanje_stolpcev=[]
        self.st_filtrov=0
        self.prazna_tabela=False
        self.tabela=str()
        self.Tabela=Tabela
        self.stolpci=[]


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Vsi elementi"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Prazna tabela"))
        self.label_4.setText(_translate("MainWindow", "Filter:"))
        self.pushButton_4.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.pushButton_1.setText(_translate("MainWindow", "Zamenjaj tabelo"))
        self.pushButton_2.setText(_translate("MainWindow", "Dodaj stolpec"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stolpec 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Stolpec2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stolpec3"))
        self.pushButton.setText(_translate("MainWindow", "Shrani pogled"))
        self.pushButton_6.setText(_translate("MainWindow", "Prekliči"))


    def action1(self,text):
        if text=="Izberi tabelo...":
            self.comboBox_3.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_1.setDisabled(True)
            self.tabela=str()
        else:
            self.comboBox_3.setDisabled(False)
            self.pushButton_2.setDisabled(False)
            self.pushButton_4.setDisabled(False)
            self.pushButton_1.setDisabled(True)
            self.tabela=text
            self.Tabela=Tabela(self.tabela,'FinanceDataBase.db')
            self.Tabela.beri_podatke()
            print('sedaj bi morala tabela biti dodana')

    def action2(self):
        self.comboBox_8.setDisabled(True)
        self.dodaj_filter(self.stevec_dodaj_filter1)
        self.stevec_dodaj_filter1+=1

    def action3(self,text):
        if text=="Prazna tabela":
            self.pushButton_4.setDisabled(True)
            self.prazna_tabela=True
        else:
            self.pushButton_4.setDisabled(False)

            self.prazna_tabela=False

    def action4(self):

        self.dodaj_meni_stolpec()
        self.comboBox_3.setDisabled(True)
        self.comboBox_8.setDisabled(True)
        self.pushButton_1.setDisabled(False)


    def dodaj_meni_stolpec(self):
        grid=QtWidgets.QVBoxLayout()
        self.hbox.addLayout(grid)
        s=Dodaj_stolpec(grid,0,self.prazna_tabela,self.Tabela)
        print(s.vrni)
        self.dodajanje_stolpcev.append(s)
        self.st_filtrov+=1


    def  dodaj_filter(self,vrstica,stolpec=0):
        #print(self.Tabela)
        s=Dodaj_filter(self.gridLayout,vrstica,self.Tabela,self.Tabela.imena_stolpcev[0])
        self.dodajanje_filtrov.append(s)

class Dodaj_filter(QtWidgets.QWidget,QtFunkcije):

    def __init__(self,gridLayout,vrstica,tabela,stolpec,filtri=[]):
        super().__init__()
        self.tabela=tabela
        self.tabela.beri_podatke()
        self.stolpec=stolpec
        self.vrstica=vrstica
        self.gridLayout=gridLayout
        self.dodaj1()
        self.retranslateUi()
        print('----------------------')
        print(self.stolpec)

    def dodaj1(self):

        self.pushButton_5 = QtWidgets.QPushButton()#self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, self.vrstica, 11, 1, 1)

        self.pushButton_5.clicked.connect(self.clear)

        self.comboBox_5 = QtWidgets.QComboBox()#self.frame)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, self.vrstica, 5, 1, 1)
        print('to')
        i=self.tabela.imena_stolpcev
        st=Stolpec(self.stolpec, self.tabela.tabela, 'FinanceDataBase.db')
        print(st.tabela)
        print(st.stolpec)
        print(st.vrednosti_stolpca)
        vr=['Izberi filter...']+list(set(st.vrednosti_stolpca))
        print('********************************')
        print(vr)
        self.combo_box_add_items(self.comboBox_5,vr)



        self.label_5 = QtWidgets.QLabel()#self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, self.vrstica, 4, 1, 1)


        self.comboBox_5.raise_()
        self.label_5.raise_()
        #self.pushButton_3.raise_()
        self.pushButton_5.raise_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", "Filter:"))
        #self.pushButton_3.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.pushButton_5.setText(_translate("MainWindow", "Izbriši filter"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Izberi filter..."))

    def clear(self):
        self.pushButton_5.deleteLater()
        self.label_5.deleteLater()
        self.comboBox_5.deleteLater()



class Dodaj_stolpec(QtWidgets.QWidget,QtFunkcije):

    def __init__(self,gridLayout1,vrstica,prazna_tabela,tabela,filtri=[]):
        super().__init__()
        self.tabela=tabela
        self.prazna_tabela=prazna_tabela
        self.ime_tabele=self.tabela.tabela
        self.vrstica = vrstica
        self.gridLayout1=gridLayout1
        self.dodajanje_filtrov=[]
        self.st_filtrov=int(0)
        self.Tabela=self.tabela#Tabela(tabela,'FinanceDataBase.db')
        self.prazna_tabela=prazna_tabela

        self.dodaj1()
        self.retranslateUi()

    def vrni(self):
        return 'neki'

    def dodaj1(self):
        self.gridLayout = QtWidgets.QGridLayout()

        self.pushButton_7 = QtWidgets.QPushButton()
        self.pushButton_7.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, self.vrstica, 8, 1, 1)
        self.pushButton_7.setDisabled(self.prazna_tabela)
        self.pushButton_7.clicked.connect(self.dodaj_filter)
        self.pushButton_7.setDisabled(True)

        self.pushButton_11 = QtWidgets.QPushButton()
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_11.clicked.connect(self.clear)
        self.gridLayout.addWidget(self.pushButton_11, self.vrstica, 11, 1, 1)


        #self.pushButton_8 = QtWidgets.QPushButton()
        #self.pushButton_8.setObjectName("pushButton_8")
        #self.gridLayout.addWidget(self.pushButton_8, self.vrstica, 9, 1, 1)
        #self.pushButton_8.setDisabled(True)

        self.label_3 = QtWidgets.QLabel()
        self.label_3.setMaximumSize(QtCore.QSize(73, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, self.vrstica, 6, 1, 1)

        #self.comboBox_4 = QtWidgets.QComboBox()
        #self.comboBox_4.setObjectName("comboBox_4")
        #self.gridLayout.addWidget(self.comboBox_4, self.vrstica, 5, 1, 1)
        #self.comboBox_4.setDisabled(self.prazna_tabela)
        #self.combo_box_add_items(self.comboBox_4, self.dodaj_stolpce_vrednosti_stolpcev(self.tabela, 'Izberi stolpec...'))
        #self.comboBox_4.setDisabled(True)

        self.comboBox_9 = QtWidgets.QComboBox()
        self.comboBox_9.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout.addWidget(self.comboBox_9, self.vrstica, 1, 1, 1)
        #print(self.tabela)
        self.combo_box_add_items(self.comboBox_9,self.dodaj_stolpce(self.ime_tabele,'Izberi stolpec...'))

        self.comboBox_9.activated[str].connect(self.action)

        #self.comboBox_6 = QtWidgets.QComboBox()
        self.comboBox_6=QtWidgets.QCheckBox()
        self.comboBox_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox_6.setObjectName("comboBox_6")
        #self.comboBox_6.addItem("")
        #self.comboBox_6.addItem("")
        self.gridLayout.addWidget(self.comboBox_6, self.vrstica, 7, 1, 1)
        self.comboBox_6.setDisabled(self.prazna_tabela)
        self.comboBox_6.setChecked(True)

        #self.label_6 = QtWidgets.QLabel()
        #self.label_6.setObjectName("label_6")

        #self.label_6.setMaximumSize(QtCore.QSize(40, 16777215))
        #self.gridLayout.addWidget(self.label_6, self.vrstica, 4, 1, 1)


        #self.label_6.raise_()
        #self.comboBox_4.raise_()
        self.label_3.raise_()
        self.comboBox_6.raise_()
        self.pushButton_7.raise_()
        #self.pushButton_8.raise_()
        self.pushButton_11.raise_()
        self.comboBox_9.raise_()

        self.gridLayout1.addLayout(self.gridLayout)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.pushButton_8.setText(_translate("MainWindow", "Dodaj stolpec"))
        self.label_3.setText(_translate("MainWindow", "Prikaži:"))
        #self.comboBox_6.setItemText(0, _translate("MainWindow", "Da"))
        #self.comboBox_6.setItemText(1, _translate("MainWindow", "Ne"))
        #self.label_6.setText(_translate("MainWindow", "Filter:"))
        self.pushButton_7.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.pushButton_11.setText(_translate("MainWindow", "Izbriši stolpec"))
        #self.comboBox_4.setItemText(0, _translate("MainWindow", "Vse"))

    def action(self,text):
        if text!='Izberi stolpec...':
            self.stolpec=text
            self.pushButton_7.setDisabled(False)
            #self.comboBox_4.setDisabled(False)
            #i=self.tabela.imena_stolpcev
            #print(i)
            #vr=['Izberi filter...']+Stolpec(i[0],self.tabela.tabela,'FinanceDataBase.db').vrednosti_stolpca
            #print(vr)
            #self.combo_box_add_items(self.comboBox_4,vr)
            #print(self.stolpec)
            self.comboBox_9.setDisabled(True)
            self.dodaj_filter()
    def clear(self):
        self.comboBox_9.deleteLater()
        self.label_6.deleteLater()
        self.comboBox_4.deleteLater()
        self.label_3.deleteLater()
        self.comboBox_6.deleteLater()
        self.pushButton_7.deleteLater()
        self.pushButton_11.deleteLater()


    def  dodaj_filter(self):
        self.pushButton_11.setDisabled(True)
        s=Dodaj_filter(self.gridLayout,self.st_filtrov+1,self.tabela,self.stolpec)
        print(self.stolpec)
        self.dodajanje_filtrov.append(s)
        self.st_filtrov+=1
        #print(self.dodajanje_filtrov)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DodajPrikaz()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

