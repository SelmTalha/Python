from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic 
import sys 
class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pencere.ui',self) ##pencereyi sayfaya bağladık
        self.model=self.modelOlusturVeGeriDondur()
        self.tv.setModel(self.model) #ærtık tableview da içinin dolu olduğunu biliyor.
        self.btnekle.clicked.connect(self.ekleye_tikladiginda)
        self.btnTopla.clicked.connect(self.toplaya_tikladiginda)

    def toplaya_tikladiginda(self):
        toplamlar=[]
        ## daha önce eklendiyse sutun onu sil
        if self.model.columnCount()==3:
            self.model.removeColumn(2)
        ## 1 ve 2. sutunu toplayıp yeni sutun ekle
        for i in range(self.model.rowCount()):
            sayi1=self.model.item(i,0).text()
            sayi2=self.model.item(i,1).text()
            toplam=int(sayi1)+int(sayi2)
            item=QStandardItem(str(toplam))
            toplamlar.append(item)

        self.model.appendColumn(toplamlar)
    
    def ekleye_tikladiginda(self):
        sayi1=self.txt1.text()
        sayi2=self.txt2.text()
        item1=QStandardItem(sayi1)
        item2=QStandardItem(sayi2)
        self.model.appendRow([item1,item2])
    
    def modelOlusturVeGeriDondur(self): ##class ın içinde bir model olduğu için self yazdık. 
        temp=QStandardItemModel() #modeli oluşturuyor.
        for x in range(10):
            item=QStandardItem(str(x))
            item2=QStandardItem(str(x))

            temp.appendRow([item,item2])


        return temp   
    
    
    
    
app=QApplication(sys.argv)
p=Pencere()
p.show() ## sayfayı görüntelemek için
sys.exit(app.exec_())