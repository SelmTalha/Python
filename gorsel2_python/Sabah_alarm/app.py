from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindow.ui",self)
        self.progressBar.setValue(100)
        # self.spinBox.valueChanged.connect(self.pb_guncelle)
        now = QDateTime.currentDateTime()
        self.timer=QTimer()
        self.dateTimeEdit.setDateTime(now)
        self.btnSetAlarm.clicked.connect(self.alarm_kur)

    def alarm_kur(self):
        
        now = QDateTime.currentDateTime()
        zaman=self.dateTimeEdit.dateTime()
        fark = now.msecsTo(zaman)
        if fark < 1:
            mb = QMessageBox()
            mb.setText("Geçmiş Tarih'e alarm kuramazsınız !")
            mb.exec()
            return

        #butonu disable et !
        self.btnSetAlarm.setEnabled(False)
        self.timer.timeout.connect(self.tick)
        self.timer.start(fark*5/100)

    def tick(self):
        pb_deger = self.progressBar.value()
        self.pb_guncelle(pb_deger - 5)

        if pb_deger < 1:
            self.timer.stop()
            self.btnSetAlarm.setEnabled(True)
            self.progressBar.setValue(100)

    def pb_guncelle(self,sayi):
        self.progressBar.setValue(sayi)


app=QApplication(sys.argv)
mw=MyWindow()
mw.show()
sys.exit(app.exec_())