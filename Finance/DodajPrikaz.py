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

class DodajPrikaz(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
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

        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 4, 1, 1)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 0, 5, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 9, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 9, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 8, 1, 1)

        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 10, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 10, 1, 1)

        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 10, 1, 1)

        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.gridLayout.addWidget(self.comboBox_7, 3, 5, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 9, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 6, 1, 1)

        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout.addWidget(self.comboBox_6, 2, 7, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 10, 1, 1)

        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 2, 5, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 8, 1, 1)

        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 1, 5, 1, 1)

        self.comboBox_9 = QtWidgets.QComboBox(self.frame)
        self.comboBox_9.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.gridLayout.addWidget(self.comboBox_9, 2, 1, 1, 1)

        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.gridLayout.addWidget(self.comboBox_8, 0, 1, 1, 1)


        self.label.raise_()
        self.label_4.raise_()
        self.comboBox_3.raise_()
        self.comboBox_5.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.comboBox_4.raise_()
        self.label_3.raise_()
        self.comboBox_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_11.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.label_7.raise_()
        self.comboBox_7.raise_()
        self.comboBox_9.raise_()
        self.comboBox_8.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 250))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
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
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Dodaj stolpec:"))
        self.label_5.setText(_translate("MainWindow", "Filter:"))
        self.label_6.setText(_translate("MainWindow", "Filter:"))
        self.label.setText(_translate("MainWindow", "Izvorna tabela:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Izberi filter...."))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Vsi elementi"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Prazna tabela"))
        self.label_4.setText(_translate("MainWindow", "Filter:"))
        self.pushButton_3.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.pushButton_4.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.pushButton_7.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.pushButton_11.setText(_translate("MainWindow", "Izbriši stolpec"))
        self.pushButton_5.setText(_translate("MainWindow", "Izbriši filter"))
        self.pushButton_10.setText(_translate("MainWindow", "Izbriši filter"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Izberi filter..."))
        self.label_7.setText(_translate("MainWindow", "Filter:"))
        self.pushButton_8.setText(_translate("MainWindow", "Dodaj stolpec"))
        self.label_3.setText(_translate("MainWindow", "Prikaži:"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Da"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Ne"))
        self.pushButton_2.setText(_translate("MainWindow", "Dodaj stolpec"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Vse"))
        self.pushButton_9.setText(_translate("MainWindow", "Dodaj še en filter"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Izberi filter..."))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Izberi stolpec..."))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Izberi tabelo...      "))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DodajPrikaz()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

