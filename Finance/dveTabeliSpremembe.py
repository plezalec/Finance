import sys
from dveTabeli import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets


def tabela(self,tableWidget, st_vrstic, st_stolpcev, vrstice_imena, stolpci_imena, vrednosti):
    ##Odvisnost od self.frame, in postavitve v frame
    tableWidget.setColumnCount(st_stolpcev)
    tableWidget.setRowCount(st_vrstic)


    for i in range(st_vrstic):
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(i, item)
    for i in range(st_stolpcev):
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(i, item)

    for i in range(st_vrstic):
        for j in range(st_stolpcev):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, j, item)

    self.tableWidget.verticalHeader().setDefaultSectionSize(25)
    self.tableWidget.verticalHeader().setMinimumSectionSize(25)

    #self.gridLayout = QtWidgets.QGridLayout(self.frame)
    #self.gridLayout.setObjectName("gridLayout")
    #self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)




    _translate = QtCore.QCoreApplication.translate

    self.tableWidget.setSortingEnabled(True)

    for i in range(st_vrstic):
        item = self.tableWidget.verticalHeaderItem(i)
        item.setText(_translate("Form", vrstice_imena[i]))
    for i in range(st_stolpcev):
        item = self.tableWidget.horizontalHeaderItem(i)
        item.setText(_translate("Form", stolpci_imena[i]))

    __sortingEnabled = self.tableWidget.isSortingEnabled()
    self.tableWidget.setSortingEnabled(False)

    for i in range(st_vrstic):
        for j in range(st_stolpcev):
            item = self.tableWidget.item(i, j)
            item.setText(_translate("Form", vrednosti[i][j]))







app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)



tabela(ui,ui.tableWidget,2, 2, ['2', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])
tabela(ui,ui.tableWidget_2,2, 2, ['1', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])

Form.show()
sys.exit(app.exec_())