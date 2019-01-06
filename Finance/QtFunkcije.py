from PyQt5 import QtCore, QtGui, QtWidgets
from SQLFunkcije import Tabela,DataBase
from SQLFunkcije import *


class QtFunkcije:
    def __init__(self):
        pass

    def tabela(self, database,tabela):

        '''
        primer: self.tableWidget =self.tabela( 2, 2, ['2', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])

        :param st_vrstic:
        :param st_stolpcev:
        :param vrstice_imena:
        :param stolpci_imena:
        :param vrednosti:
        :return:
        '''
        a = SQLFunkcije(database)
        b=a.nastej_stolpce(tabela)[0]
        st_vrstic=len(a.preberi_stolpec(tabela,b))


        stolpci_imena=a.nastej_stolpce(tabela)
        st_stolpcev=len(stolpci_imena)

        vrednosti=a.preberi_tabelo(tabela)
        vrstice_imena=a.preberi_stolpec(tabela,b)

        tableWidget = QtWidgets.QTableWidget()
        tableWidget.setColumnCount(st_stolpcev)
        tableWidget.setRowCount(st_vrstic)
        #kreira se vrstice, stolpce in polja
        for i in range(st_stolpcev):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setHorizontalHeaderItem(i, item)
        for i in range(st_vrstic):
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
        return tableWidget

    def tabela_Tabela(self,tabela):

        '''

        :param tabela: SQLFunkcije.py class Tabela
        :return:


        :param st_vrstic:
        :param st_stolpcev:
        :param vrstice_imena:
        :param stolpci_imena:
        :param vrednosti:
        '''

        stolpci_imena=tabela.imena_stolpcev
        st_stolpcev=len(stolpci_imena)
        st_vrstic=tabela.st_vr
        #tabela.stolpci[1].vrednosti_st()


        vrstice_imena=tabela.imena_vrstic
        vrednosti=tabela.polja()



        tableWidget = QtWidgets.QTableWidget()
        tableWidget.setColumnCount(st_stolpcev)
        tableWidget.setRowCount(st_vrstic)
        #kreira se vrstice, stolpce in polja
        for i in range(st_stolpcev):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setHorizontalHeaderItem(i, item)
        for i in range(st_vrstic):
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
        return tableWidget

    def akcija(self,comboBox,tableWidget):
        comboBox.activated['QString'].connect(tableWidget.clear)
        #self.tabela(tableWidget, 2, 2, ['2', 'b'], ['c', 'd'], [['ac', 'ad'], ['bc', 'bd']])

    def combo_box_add_items(self,combo,items):
        for i in range(len(items)):
            combo.addItem(items[i])

    def dodaj(self,str):
        a = SQLFunkcije('FinanceDataBase.db')
        pr = a.nastej_tabele()
        return [str]+pr

    def stacked(self,database):
        Stack=QtWidgets.QStackedWidget()
        a=SQLFunkcije(database)
        tabele=a.nastej_tabele()
        w=[]
        for i in range(len(tabele)):
            w.append(self.tabela(database,tabele[i]))
            Stack.addWidget(w[i])
        return  Stack,a.nastej_tabele()

    def stacked_DataBase(self,database):
        Stack = QtWidgets.QStackedWidget()
        database=DataBase('FinanceDataBase.db')
        database.beri_podatke()
        tabele=database.tabele
        w=[]

        for i in range(len(tabele)):
            w.append(self.tabela_Tabela(tabele[i]))
            Stack.addWidget(w[i])
        return Stack, database.imena_tabel

    def dodaj_vrstico_za_vnos(self,tabela):
        vrstica=QtWidgets.QVBoxLayout()
        zgoraj=QtWidgets.QHBoxLayout()
        spodaj=QtWidgets.QHBoxLayout()
        vrstica.addLayout(zgoraj)
        vrstica.addLayout(spodaj)
        b=[]
        l=[]
        a=SQLFunkcije('FinanceDataBase.db')
        stolpci=a.nastej_stolpce(tabela)
        for i in range(len(stolpci)):
            b.append(QtWidgets.QLineEdit())
            l.append(QtWidgets.QLabel(stolpci[i]))
            spodaj.addWidget(b[-1])
            zgoraj.addWidget(l[-1])
        return vrstica,b,l

    def odstrani_vrstico_za_vnos(self,a,c):
        for i in range(len(a)):
            b=a[i]
            b.deleteLater()
            b = c[i]
            b.deleteLater()

    #def dodaj_stack(self):

    #def odstrani_stack(self):

    def tabela_vnos(self,tabela_input):
        d=DataBase('FinanceDataBase.db')
        d.beri_podatke()
        for i in range(len(d.imena_tabel)):
            if tabela_input == d.imena_tabel[i]:
                tabela=d.tabele[i]

        return self.tabela_Tabela(tabela)

    def razvrsti_okno(self,st):
        self.setGeometry(0,35+st*338, 800, 300)

if __name__ == "__main__":
    pass