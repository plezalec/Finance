# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pavel\Documents\Business\Finance\Finance\QtOkno.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from QtFunkcije import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 790)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setMinimumSize(QtCore.QSize(130, 0))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setToolTip("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)


        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(False)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 26))
        self.menubar.setObjectName("menubar")
        self.menuDodaj = QtWidgets.QMenu(self.menubar)
        self.menuDodaj.setObjectName("menuDodaj")
        self.menuAnalize = QtWidgets.QMenu(self.menubar)
        self.menuAnalize.setObjectName("menuAnalize")
        self.menuPregled_podatkov = QtWidgets.QMenu(self.menubar)
        self.menuPregled_podatkov.setObjectName("menuPregled_podatkov")
        self.menuPredloge = QtWidgets.QMenu(self.menubar)
        self.menuPredloge.setObjectName("menuPredloge")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNakupi_v_trgovini = QtWidgets.QAction(MainWindow)
        self.actionNakupi_v_trgovini.setObjectName("actionNakupi_v_trgovini")
        self.actionBele_enje_polo_nic = QtWidgets.QAction(MainWindow)
        self.actionBele_enje_polo_nic.setObjectName("actionBele_enje_polo_nic")
        self.menuPredloge.addAction(self.actionNakupi_v_trgovini)
        self.menuPredloge.addAction(self.actionBele_enje_polo_nic)
        self.menubar.addAction(self.menuDodaj.menuAction())
        self.menubar.addAction(self.menuAnalize.menuAction())
        self.menubar.addAction(self.menuPregled_podatkov.menuAction())
        self.menubar.addAction(self.menuPredloge.menuAction())

        self.retranslateUi(MainWindow)

        self.comboBox.activated['QString'].connect(self.fun())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pregled financ"))
        self.toolButton_2.setText(_translate("MainWindow", "Dodaj predlogo"))
        self.toolButton.setText(_translate("MainWindow", "Dodaj element tabele"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "prva lastnost"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "druga lastnost"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "tretna lastnost"))
        self.comboBox.setItemText(1, _translate("MainWindow", "prvi element"))
        self.comboBox.setItemText(2, _translate("MainWindow", "drugi element"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "prvavrstica"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "drugavrstica"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "tretjavrstica"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "prviStolpec"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "drugiStolpec"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "tretji stolpec"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "adsfdafsdfsa", "nekaj"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "sdfasfdasdf"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "sdfadsfasf"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "asfdasdfaddsfg"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "asdfasdf"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "sfdasdfa"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "sdfasdf"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "asdfsdfaf"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "asdf"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuDodaj.setTitle(_translate("MainWindow", "Prikaži tabelo"))
        self.menuAnalize.setTitle(_translate("MainWindow", "Analize"))
        self.menuPregled_podatkov.setTitle(_translate("MainWindow", "Pregled podatkov"))
        self.menuPredloge.setTitle(_translate("MainWindow", "Predloge"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNakupi_v_trgovini.setText(_translate("MainWindow", "Nakupi v trgovini"))
        self.actionBele_enje_polo_nic.setText(_translate("MainWindow", "Beleženje položnic"))
    def fun(self):
        sys.exit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    a=QtFunkcije()
    #a.tabela(ui.tableWidget, 2, 2, ['2', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])
    #a.akcija(ui.comboBox,ui.tableWidget)
    #ui.comboBox.activated['QString'].connect(ui.fun())
    MainWindow.show()
    sys.exit(app.exec_())

