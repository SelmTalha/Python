from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

def fonksiyon():
    print("test")

app=QApplication(sys.argv)
timer=QTimer()
timer.timeout.connect(fonksiyon)
timer.start(1000)
sys.exit(app.exec_())