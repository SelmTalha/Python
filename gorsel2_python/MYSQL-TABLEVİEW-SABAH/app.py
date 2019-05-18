from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from mysql.connector import MySQLConnection
from mysql.connector.errors import DatabaseError, ProgrammingError

class AdresDefteri(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pencere.ui', self)

        
        
        self.database_olustur()
        self.tablo_olustur()
        self.kayit_ekle('turkalp', 'kayrancioglu', '552')
        
        self.model = self.get_model()
        self.tv.setModel(self.model)
        self.tv.clicked.connect(self.secildiginde)
        self.secili = None
        self.btnGuncelle.clicked.connect(self.guncelle)
        self.btnSil.clicked.connect(self.sil)
        
    
    def guncelle(self):
        config = {
            'user': 'root',
            'password': '',
            'database': 'test',
            'host': '127.0.0.1'
        }
        connection = MySQLConnection(**config)
        cur = connection.cursor()
        kayit = {
            'ad': self.txtAd.text(),
            'soyad': self.txtSoyad.text(),
            'telefon': self.txtTelefon.text(),
            'id': self.secili
        }
        sql = 'UPDATE adres_defteri SET ad="{ad}", soyad="{soyad}", telefon="{telefon}" WHERE id="{id}"'.format(**kayit)
        cur.execute(sql)
        connection.commit()
        model = self.get_model()
        self.tv.setModel(model)
        
        

    def secildiginde(self, index: QModelIndex):
        row = index.row()
        column = index.column()
        id = index.sibling(row, 0).data()
        self.secili = id

        ad = index.sibling(row, 1).data()
        soyad = index.sibling(row, 2).data()
        telefon = index.sibling(row, 3).data()
        self.secili_degerleri_getir(ad, soyad, telefon)
    
    def secili_degerleri_getir(self, ad, soyad, telefon):
        
        self.txtAd.setText(ad)
        self.txtSoyad.setText(soyad)
        self.txtTelefon.setText(telefon)

    def sil(self):
        if self.secili is not None:
            sql = 'DELETE FROM adres_defteri WHERE id = {id}'.format(id=self.secili)
            config = {
                'user': 'root',
                'password': '',
                'database': 'test',
                'host': '127.0.0.1'
            }
            connection = MySQLConnection(**config)
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
            model = self.get_model()
            self.tv.setModel(model)
            self.secili = None

    def database_olustur(self):
        config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1'
        }
        connection = MySQLConnection(**config)
        cur = connection.cursor()

        try:
            cur.execute('CREATE DATABASE test;')
        except DatabaseError as ex:
            print(ex.msg)

    def tablo_olustur(self):
        config = {
            'user': 'root',
            'password': '',
            'database': 'test',
            'host': '127.0.0.1'
        }
        connection = MySQLConnection(**config)
        cur = connection.cursor()
        try:
            cur.execute('CREATE TABLE adres_defteri (id INT PRIMARY KEY AUTO_INCREMENT,ad VARCHAR(50),soyad VARCHAR(50),telefon VARCHAR(20));')
        except ProgrammingError as ex:
            print(ex.msg)

    def kayit_ekle(self, ad,soyad,telefon):
        config = {
            'user': 'root',
            'password': '',
            'database': 'test',
            'host': '127.0.0.1'
        }
        connection = MySQLConnection(**config)
        cur = connection.cursor()
        kayit = {
            'ad': ad,
            'soyad': soyad,
            'telefon': telefon
        }
        cur.execute('INSERT INTO adres_defteri(ad,soyad,telefon) VALUES("{ad}", "{soyad}", "{telefon}");'.format(**kayit))

        connection.commit()

    def get_model(self):
        temp = QStandardItemModel()
        config = {
            'user': 'root',
            'password': '',
            'database': 'test',
            'host': '127.0.0.1'
        }
        connection = MySQLConnection(**config)
        cur = connection.cursor(dictionary=True)
        cur.execute('SELECT id, ad, soyad, telefon FROM adres_defteri;')


        for kayit in cur.fetchall():
            id = QStandardItem(str(kayit['id']))
            ad = QStandardItem(kayit['ad'])
            soyad = QStandardItem(kayit['soyad'])
            telefon = QStandardItem(kayit['telefon'])
            temp.appendRow([id, ad, soyad, telefon])

        return temp



app = QApplication(sys.argv)

pencere = AdresDefteri()
pencere.show()

sys.exit(app.exec_())
