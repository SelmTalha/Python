from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

dosya='toplama.ui'
class BenimEkranim(QMainWindow):
    def __init__(self):
        super(BenimEkranim,self).__init__()
        uic.loadUi(dosya,self)
        self.btnTopla.clicked.connect(self.toplamaFonksiyonu)#btnTopla butonuna tıklandığında toplamafonksiyonunu çağır
    
    def toplamaFonksiyonu(self):
        toplam=int(self.txtsayi1.text())+int(self.txtsayi2.text())#toplam değişkenine txtsayi1 ve txtsayi2 değerlerini toplatarak atama                                                                     işlemini yap.txtsayi1 ve txtsayi2'yi self ile class içinde olduğunu belirt!                                                             (lineEdit içerisindeki değerler string olduğundan onları int'a çevir.)
        self.lblToplam.setText(str(toplam)) #setText ile lblToplam içine sonucu ekle!(label olduğundan burada yeniden str ile stringe çevir.)
        
app=QApplication(sys.argv)
be=BenimEkranim()
be.show()
sys.exit(app.exec_())