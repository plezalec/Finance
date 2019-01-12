from baza import Baza
from finance import Finance
from PyQt5 import QtWidgets
import sys

class Main():
    def __init__(self):
        super().__init__()
        self.setup()
        app = QtWidgets.QApplication(sys.argv)
        self.window=Finance()
        self.window.show()
        sys.exit(app.exec_())

    def setup(self):
        self.baza_ime='FinanceDataBase'
        self.SQL_baza='FinanceDataBase.db'
        self.baza = Baza(self.baza_ime)
        self.baza.beri_iz_SQL(self.SQL_baza)






if __name__ == "__main__":
    Main()

