import sys
import os
import site
from QtOkno import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

# MOJE
def funkcija(a):
    for i in range(10):
        dodajMenije(a,i)


def dodajMenije(self, i):
    self.neki = QtWidgets.QAction(MainWindow)
    self.neki.setObjectName("Neki")
    self.menuPredloge.addAction(self.neki)
    _translate = QtCore.QCoreApplication.translate
    a = str(i)
    self.neki.setText(_translate("MainWindow", "NEKI " + a))





app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
funkcija(ui)
MainWindow.show()
sys.exit(app.exec_())