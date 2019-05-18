from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import csv

class AdresDefteri(QMainWindow):
    def __init__(self):
        super(AdresDefteri,self).__init__()
        uic.loadUi('pencere.ui',self)
        self.liste=[]
        # self.dosyadan_oku()
        self.csv_ile_dosyadan_oku()
        self.model=self.get_model()
        self.tv.setModel(self.model)
        self.model.setHorizontalHeaderLabels(['Ad','Soyad','Telefon'])
        self.tablo_doldur()
        #print(self.liste)
    def get_model(self):
        model=QStandardItemModel()
        for kisi in self.liste:
            ad=kisi['ad']
            soyad=kisi['soyad']
            telefon=kisi['telefon']
            model.appendRow([QStandardItem(ad),QStandardItem(soyad),QStandardItem(telefon)])
        return model
    def csv_ile_dosyadan_oku(self):
        reader = csv.DictReader(open('dosya.csv','r'))
        for kayit in reader:
            self.liste.append(kayit)
    # def dosyadan_oku(self):
    #     with open('dosya.csv','r') as f:
    #         for satir in f:
    #             self.liste.append(satir[-1])
    def tablo_doldur(self):
        for kisi in self.liste:
            print(kisi['ad'])

app=QApplication(sys.argv)
pencere=AdresDefteri()
pencere.show()
sys.exit(app.exec_())