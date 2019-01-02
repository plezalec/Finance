# Finance
Program z GUI za vodenje osebnih financ. 

## SQL baza

Sql baza:<br>
-Osnova se zgradi z SQLiteStudio

## User interface

User interface:<br>
PyQt5<br>
Inštaliraj si knjižnice v spodnjem videu<br>
-osnova video: https://www.youtube.com/watch?v=ksW59gYEl6Q<br>

Osnovna zasnova UI se naredi v Qt Designerju<br>
To se shrani v datoteko z končnico .ui<br>
Potem se v isti mapi odpre cmd (shift+desni klik -> izberi Okno lupine PowerShell odpri tukaj) in izvede spodnjo kodo in se pretvori .ui v .py file<br>
<br>
Npr. za QtOkno.ui:<br><br>
pyuic5 -x "C:\Users\Pavel\Documents\Business\Finance\Finance\QtOkno.ui" -o "C:\Users\Pavel\Documents\Business\Finance\Finance\QtOkno.py"
<br><br>
Potem se naredi še eno mapo npr. QtOknoSpremembe.py kjer se bo z pythonom delalo spremembe na osnovnem Qt oknu. To se naredi zato ker če z Qt designerjem kaj spreminjaš updataš cel file in se tvoje delo napisano v pythonu izbriše.<br><br>
Za uvoz npr. QtOkno.py v QtOknoSpremembe.py in zagon napišemo v QtOknoSpremembe sledeče:<br>
<br><br><br>
import sys<br>
import os<br>
import site<br>
from QtOkno import Ui_MainWindow<br>
from PyQt5 import QtCore, QtGui, QtWidgets<br>
<br>
<br>
app = QtWidgets.QApplication(sys.argv)<br>
MainWindow = QtWidgets.QMainWindow()<br>
ui = Ui_MainWindow()<br>
ui.setupUi(MainWindow)<br>
funkcija(ui)<br>
MainWindow.show()<br>
sys.exit(app.exec_())<br>
