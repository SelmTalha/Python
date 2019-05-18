from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5 import uic
import sys
class Pencere(QMainWindow):
    def __init__(self):
        super(Pencere,self).__init__()
        uic.loadUi('pencere.ui',self)
        self.model =QStandardItemModel()
        self.liste =[]
        self.listeyi_dosyadan_doldur()
        self.modeli_listeden_doldur()
        self.btnDoldur.clicked.connect(self.listedoldurma_fonk)
        self.txtyazi.textChanged.connect(self.yaziyor)
        self.btnDoldur.clicked.connect(self.yaziyortemizle)
        
        
        # self kullanımı = class içinde tanımlıysa self. yazıyoruz.Class dışındaysa yazmıyoruz.
    def listedoldurma_fonk(self):
        yazi = self.txtyazi.text()
        item = QStandardItem(yazi)
        self.model.appendRow(item)
        self.listView.setModel(self.model)
        self.liste.append(yazi)
        # self.dosyaya_yaz(yazi)
        self.son_elemani_kaydet(yazi)
    def modeli_listeden_doldur(self):
        for satir in self.liste:
            self.model.appendRow(QStandardItem(satir))
        self.listView.setModel(self.model)
    def listeyi_dosyadan_doldur(self):
        with open('dosya.txt','r') as dosya:
            for satir in dosya.readlines():
                self.liste.append(satir[:-1])
        print(self.liste)
    def son_elemani_kaydet(self,yazi):
        print(yazi,file=open('dosya.txt','a'))
    def dosyaya_yaz(self,yazi):
        for satir in self.liste:
            print(satir,file=open('dosya.txt','a'))
    def yaziyor(self):
        self.lblyazi.setText('Yaziyor...')
    def yaziyortemizle(self):
        self.lblyazi.setText('')
    
app=QApplication(sys.argv)
pen=Pencere()
pen.show()

sys.exit(app.exec_())