# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pavel\Documents\Business\Finance\Finance\QtOkno.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1170, 991)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1170, 47))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pregled financ"))
        self.toolButton.setText(_translate("MainWindow", "Dodaj element tabele"))
        self.toolButton_2.setText(_translate("MainWindow", "Dodaj predlogo"))
        self.menuDodaj.setTitle(_translate("MainWindow", "Dodaj"))
        self.menuAnalize.setTitle(_translate("MainWindow", "Analize"))
        self.menuPregled_podatkov.setTitle(_translate("MainWindow", "Pregled podatkov"))
        self.menuPredloge.setTitle(_translate("MainWindow", "Predloge"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNakupi_v_trgovini.setText(_translate("MainWindow", "Nakupi v trgovini"))
        self.actionBele_enje_polo_nic.setText(_translate("MainWindow", "Beleženje položnic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

