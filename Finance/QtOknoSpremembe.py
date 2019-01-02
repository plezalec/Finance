#Ker se Qt okno generira z Qt Designerjem, se obupdatu izbriše vse kar narediš in ga je potrebno klicat kot funkcijo če ga želiš spreminjat z kodo
#V Qt designerju narediš grob osnutek, potem ga shraniš kot .ui in ga pretvoriš po navodilih v .py potem narediš ---Spremembe.py file kot  je ta za spremembe

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


