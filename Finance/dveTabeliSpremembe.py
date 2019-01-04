import sys
from dveTabeli import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets


def tabela(tableWidget, st_vrstic, st_stolpcev, vrstice_imena, stolpci_imena, vrednosti):
    #nastavi se število vrstic instolpcev
    tableWidget.setColumnCount(st_stolpcev)
    tableWidget.setRowCount(st_vrstic)
    #kreira se vrstice, stolpce in polja
    for i in range(st_vrstic):
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(i, item)
    for i in range(st_stolpcev):
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setVerticalHeaderItem(i, item)
    for i in range(st_vrstic):
        for j in range(st_stolpcev):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setItem(i, j, item)
    #Default višina stolpcev
    tableWidget.verticalHeader().setDefaultSectionSize(25)
    tableWidget.verticalHeader().setMinimumSectionSize(25)
    #translate
    _translate = QtCore.QCoreApplication.translate

    for i in range(st_vrstic):
        item = tableWidget.verticalHeaderItem(i)
        item.setText(_translate("Form", vrstice_imena[i]))
    for i in range(st_stolpcev):
        item = tableWidget.horizontalHeaderItem(i)
        item.setText(_translate("Form", stolpci_imena[i]))

    __sortingEnabled = tableWidget.isSortingEnabled()
    tableWidget.setSortingEnabled(True)

    for i in range(st_vrstic):
        for j in range(st_stolpcev):
            item = tableWidget.item(i, j)
            item.setText(_translate("Form", vrednosti[i][j]))







app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)



tabela(ui.tableWidget,2, 2, ['2', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])
tabela(ui.tableWidget_2,2, 2, ['1', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])

Form.show()
sys.exit(app.exec_())