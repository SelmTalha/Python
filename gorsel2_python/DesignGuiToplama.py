from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

dosya='toplama.ui'
class BenimEkranim(QMainWindow):
    def __init__(self):
        super(BenimEkranim,self).__init__()
        uic.loadUi(dosya,self)
        self.btnTopla.clicked.connect(self.toplamaFonksiyonu)
    
    def toplamaFonksiyonu(self):
        toplam=int(self.txtsayi1.text())+int(self.txtsayi2.text())
        self.lblToplam.setText(str(toplam))
        
app=QApplication(sys.argv)
be=BenimEkranim()
be.show()
sys.exit(app.exec_())