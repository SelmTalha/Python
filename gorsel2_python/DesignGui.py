from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

dosya='ekran.ui'
class BenimEkranim(QMainWindow):
    def __init__(self):
        super(BenimEkranim,self).__init__()
        uic.loadUi(dosya,self)
        
app=QApplication(sys.argv)
be=BenimEkranim()
be.show()
sys.exit(app.exec_())
