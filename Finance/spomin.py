import pickle
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui#za slike
from PyQt5 import QtCore
from QtFunkcije import QtFunkcije
from PyQt5 import QtCore, QtGui, QtWidgets
from SQLFunkcije import Tabela,DataBase
from SQLFunkcije import *
import os
import errno
import numpy as np
import os

# Create directory

class Spomin():
    def __init__(self,ime):
        self.ime=ime
        self.izgradnja_datotek('tempDir')

        favorite_color = [1, 2]
        self.save(favorite_color)
        #a=self.load()
        #print(a)
        #with open()
    #def load(self):
    #    return pickle.load(open(self.file1,'wb'))

    def save(self,s):
        self.izgradnja_txt(self.ime)
        pickle.dump(s, self.file1)
    def izgradnja_txt(self,ime):
        save_path = 'C:/Users/Pavel/Documents/Business/Finance/Finance/tempDir'

        name_of_file = ime

        completeName = os.path.join(save_path, ime + ".txt")
        self.file1= open(os.path.join('/path/to/Documents', completeName), "wb")
    def izgradnja_datotek(self,dirName):
        try:
        # Create target Directory
            os.mkdir(dirName)
            print("Directory ", dirName, " Created ")
        except FileExistsError:
            pass
            #print("Directory ", dirName, " already exists")

if __name__ == "__main__":
    s=Spomin('Nastavitve tabel')

